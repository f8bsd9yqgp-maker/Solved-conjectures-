"""Reproduce the shear-wave predictions in Aluminum_steel_ultrasound.pdf.

Run with Python 3, NumPy, SciPy and mpmath. Material impedances are in MRayl.
All outputs are theoretical predictions, unless labelled as literature data.
"""

import json
import math
from itertools import product

from mpmath import iv
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.stats import qmc


MATERIAL = {'Al': (2700., 26.), 'St': (8000., 80.), 'Ti': (4430., 42.2)}
Z = {key: math.sqrt(rho * mod * 1e9) / 1e6 for key, (rho, mod) in MATERIAL.items()}
SPEED = {key: math.sqrt(mod * 1e9 / rho) for key, (rho, mod) in MATERIAL.items()}


def field_matrix(impedances, phases):
    """Matrix in displacement / scaled shear-traction coordinates."""
    a, b, c, d = 1., 0., 0., 1.
    for z, phase in zip(impedances, phases, strict=True):
        cs, sn = np.cos(phase), np.sin(phase)
        a, b, c, d = (a * cs - b * z * sn, a * sn / z + b * cs,
                      c * cs - d * z * sn, c * sn / z + d * cs)
    return a, b, c, d


def conditional_gaps(impedances, free_phases):
    """Average over the first transit phase analytically."""
    z0 = impedances[0]
    a, b, c, d = field_matrix(impedances[1:], free_phases)
    radius = np.hypot((a + d) / 2., (c / z0 - z0 * b) / 2.)
    return (2. / np.pi) * np.arccos(1. / np.maximum(1., radius))


def gap_density(impedances, exponent=16, repetitions=8):
    if len(impedances) == 2:
        value, error = quad(lambda t: conditional_gaps(impedances, [t]), 0., np.pi,
                            epsabs=2e-13, epsrel=2e-13)
        return {'fraction': value / np.pi, 'integration_error_estimate': error / np.pi}
    estimates = []
    for seed in range(repetitions):
        sampler = qmc.Sobol(len(impedances) - 1, scramble=True, seed=7901 + seed)
        phases = sampler.random_base2(exponent).T * np.pi
        estimates.append(float(np.mean(conditional_gaps(impedances, phases))))
    return {'fraction': float(np.mean(estimates)), 'replicate_standard_error':
            float(np.std(estimates, ddof=1) / np.sqrt(repetitions))}


def wave_half_trace(impedances, phases):
    """Independent traveling-wave calculation with normalized interface matrices."""
    alpha, beta = 1., 0.
    for j, zp in enumerate(impedances):
        zn = impedances[(j + 1) % len(impedances)]
        rapidity = 0.5 * np.log(zn / zp)
        ch, sh = np.cosh(rapidity), np.sinh(rapidity)
        e = np.exp(1j * phases[j])
        alpha, beta = (alpha * e * ch + beta / e * sh,
                       alpha * e * sh + beta / e * ch)
    return np.real(alpha)


def transmitted_power(impedances, delays, frequencies, exterior, periods=5):
    phases = [2. * np.pi * delay * frequencies for delay in delays]
    a, b, c, d = field_matrix(impedances, phases)
    aa, bb, cc, dd = 1., 0., 0., 1.
    for _ in range(periods):
        aa, bb, cc, dd = (aa * a + bb * c, aa * b + bb * d,
                          cc * a + dd * c, cc * b + dd * d)
    return 4. / ((aa + dd)**2 + (cc / exterior - exterior * bb)**2)


def midpoint_quadrature(impedances, size=128):
    """Deterministic cross-check of the two-, three-, and four-layer values."""
    axes = [(np.arange(size) + .5) * np.pi / size] * (len(impedances) - 1)
    return float(np.mean(conditional_gaps(impedances, np.meshgrid(*axes, indexing='ij', sparse=True))))


def thickness_tolerance(materials, widths, divisions=5):
    """Enclose the result for every choice of +/-1% in each repeated thickness.

    Inputs are exact nominal properties / widths evaluated with interval arithmetic.
    All five periods share the same chosen thickness vector.
    """
    iv.dps = 35
    density = {'Al': 2700, 'St': 8000}
    modulus = {'Al': 26_000_000_000, 'St': 80_000_000_000}
    exterior = iv.sqrt(density['Al'] * modulus['Al'])
    normalized_z = [iv.sqrt(density[m] * modulus[m]) / exterior for m in materials]
    phases = [2 * iv.pi * 500000 * width / 1000
              / iv.sqrt(iv.mpf(modulus[m]) / density[m]) for m, width in zip(materials, widths)]
    bands, powers = [], []
    for box in product(range(divisions), repeat=len(materials)):
        a, b, c, d = 1, 0, 0, 1
        for phase, z, i in zip(phases, normalized_z, box):
            # Rational endpoints 0.99 + 0.02 i/divisions, rounded outwards.
            error_factor = iv.mpf([99 * divisions + 2 * i, 99 * divisions + 2 * (i+1)]) / (100 * divisions)
            cs, sn = iv.cos(phase * error_factor), iv.sin(phase * error_factor)
            a, b, c, d = (a * cs - b * z * sn, a * sn / z + b * cs,
                          c * cs - d * z * sn, c * sn / z + d * cs)
        h = (a + d) / 2
        # For five identical cells, the off-diagonal traveling-wave entry is
        # multiplied by the Chebyshev polynomial U_4(h).
        u4 = (16 * h**2 - 12) * h**2 + 1
        excess = ((a - d)**2 + (b + c)**2) / 4
        power = 1 / (1 + u4**2 * excess)
        bands.append((float(h.a), float(h.b)))
        powers.append((float(power.a), float(power.b)))
    return {'half_trace_enclosure': [min(x[0] for x in bands), max(x[1] for x in bands)],
            'power_enclosure': [min(x[0] for x in powers), max(x[1] for x in powers)]}


def frequency_gaps(impedances, delays, upper=2e6, samples=80001):
    """Locate band edges from crossings of the half-trace magnitude through one."""
    def criterion(f):
        phases = [2. * np.pi * delay * f for delay in delays]
        a, _, _, d = field_matrix(impedances, phases)
        return np.abs((a + d) / 2.) - 1.

    frequencies = np.linspace(0., upper, samples)
    in_gap = criterion(frequencies) > 0.
    turns = np.flatnonzero(in_gap[:-1] != in_gap[1:])
    edges = [brentq(criterion, frequencies[i], frequencies[i + 1]) for i in turns]
    cutoffs = [0., *edges, upper]
    gaps = [(lo, hi) for lo, hi in zip(cutoffs, cutoffs[1:]) if criterion((lo + hi) / 2.) > 0.]
    return {'first_gap_kHz': [x / 1000. for x in gaps[0]],
            'finite_fraction': sum(hi - lo for lo, hi in gaps) / upper,
            'intervals_kHz': [[lo / 1000., hi / 1000.] for lo, hi in gaps]}


def main():
    al, st, ti = (Z[k] for k in ('Al', 'St', 'Ti'))
    ideal = math.sqrt(al * st)
    named = {'Al / steel': [al, st], 'Al / Ti / steel': [al, ti, st],
             'Al / ideal match / steel': [al, ideal, st],
             '2018 three-material example': [al, st, math.sqrt(5000.*70e9)/1e6],
             'Al / steel / Al / steel': [al, st] * 2,
             '6 alternating': [al, st] * 3, '8 alternating': [al, st] * 4}
    results = {'impedances_MRayl': Z, 'target_MRayl': ideal, 'speeds_m_s': SPEED,
               'broadband': {name: gap_density(z) for name, z in named.items()}}
    for name, z in named.items():
        if len(z) <= 4:
            value = midpoint_quadrature(z)
            results['broadband'][name]['128_point_per_axis_midpoint_check'] = value
            assert abs(value - results['broadband'][name]['fraction']) < .0002
    rng = np.random.default_rng(74032)
    worst = 0.
    for z in named.values():
        phases = rng.uniform(0., 2.*np.pi, (len(z), 2048))
        a, _, _, d = field_matrix(z, phases)
        worst = max(worst, float(np.max(np.abs((a + d) / 2. - wave_half_trace(z, phases)))))
    assert worst < 5e-13
    results['maximum_half_trace_cross_check_error'] = worst
    # Same 5 mm period and same amounts of Al and steel in both two-metal cells.
    split_al, split_st = 3./math.sqrt(2.), 2./math.sqrt(3.)
    examples = {'Al / steel': (['Al', 'St'], [3., 2.]),
                'Al / Ti / steel': (['Al', 'Ti', 'St'], [2.4, .6, 2.]),
                'Al / steel / Al / steel': (['Al', 'St', 'Al', 'St'],
                                            [split_al, split_st, 3.-split_al, 2.-split_st])}
    results['frequency_examples'] = {}
    for name, (metals, mm) in examples.items():
        delays = [d * .001 / SPEED[m] for m, d in zip(metals, mm)]
        z = [Z[k] for k in metals]
        band = frequency_gaps(z, delays)
        finer = frequency_gaps(z, delays, samples=160001)
        assert np.allclose(band['intervals_kHz'], finer['intervals_kHz'], rtol=0, atol=1.e-6)
        power = float(transmitted_power(z, delays, 5.e5, al))
        results['frequency_examples'][name] = {'thickness_mm': mm, **band,
              'five_period_transmitted_power_at_500kHz': power,
              'five_period_transmission_dB_at_500kHz': 10.*math.log10(power)}
    iv.dps = 35
    xa, xs = 3/iv.sqrt(2), 2/iv.sqrt(3)
    results['one_percent_thickness_enclosures'] = {
        'two-layer': thickness_tolerance(['Al','St'], [iv.mpf(3), iv.mpf(2)]),
        'four-layer': thickness_tolerance(['Al','St','Al','St'], [xa, xs, 3-xa, 2-xs])}
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()
