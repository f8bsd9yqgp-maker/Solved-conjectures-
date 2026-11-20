# Shear-wave band-gap density maximization in periodic laminates

Public review version 1, 20 November 2026. [Read the five-page manuscript (PDF)](Aluminum_steel_ultrasound.pdf).

In §4.1 of their 2018 paper, Ben Lustig and Gal Shmuel suggested that, when the available impedances are bounded, adding alternating pairs of the extreme materials and varying their thicknesses increases the fraction of the spectrum in stop bands. Their Figure 7 gives numerical examples. This note presents a proof of the optimal ordering for each even layer count in the full phase-averaged model and characterizes the odd counts. [Original paper](https://doi.org/10.1016/j.jmps.2018.04.008) · [Earlier two-layer theory by Shmuel and Band](https://ramband.net.technion.ac.il/files/2016/10/Universality-of-the-frequency-spectrum-of-laminates.pdf)

## Precise claim

Consider normal-incidence shear waves in a one-dimensional periodic stack of lossless, isotropic, nondispersive layers with perfect interfaces. Let the transit times in a period be rationally independent, meaning that no nonzero integer linear combination vanishes. Let $M(\omega)$ be the one-period transfer matrix. The quantity being maximized is

$$
\Phi=\lim_{\Omega\to\infty}\frac{1}{\Omega}\int_0^\Omega
\mathbf{1}_{\{|\operatorname{tr} M(\omega)|>2\}}\,d\omega.
$$

* For every fixed even number of layers and any two distinct positive impedance bounds, the unique maximizing impedance sequence, up to the choice of starting layer, alternates the two endpoints. Adding another alternating pair strictly increases the optimum when the new transit times are rationally independent.
* For an odd count of at least three, the best density equals the preceding even-count optimum when adjacent equal impedances are allowed. If every interface must separate different impedances and values can vary continuously, the same value is the supremum.
* Inserting a layer between two fixed impedances minimizes the full-spectrum gap density at their geometric mean. This is also the strongest decrease obtainable by inserting an intermediate-impedance layer between those neighbors.

The argument integrates out a uniform propagation phase, then expresses the dependence on one interface as a circular mean of a strictly subharmonic function. The mean increases strictly with the interface reflection magnitude. Every interface attains its greatest possible magnitude at once in an even alternating stack. Pages 2–3 give the proof, the odd-count reduction and the hypotheses on the phases. Repeating an unchanged bilayer twice leaves its physical spectrum unchanged.

## Numerical example and reproduction

The model puts 41.99% of the full spectrum in stop bands for two aluminum/steel layers and 56.53% for four independently phased alternating layers. For the specific 25 mm specimens on page 4, using equal amounts of each metal and identical aluminum exteriors, the predicted transmitted powers at 500 kHz are 84.3% and 0.00183%, respectively. These are calculations for the listed designs. Experimental validation is open.

Run the following in the directory containing the [Python script](laminate_checks.py). The release was checked with Python 3.12, NumPy 2.3.5, SciPy 1.17.0 and mpmath 1.3.0.

```bash
python -m pip install numpy==2.3.5 scipy==1.17.0 mpmath==1.3.0
python laminate_checks.py > reproduced.json
```

The [reference JSON](laminate_results.json) includes the gap fractions, band edges, a comparison with an independent traveling-wave calculation, midpoint integration checks, and interval bounds under thickness variation. Two-layer phase integration uses adaptive quadrature. The higher-layer results use eight scrambled Sobol samples. The script contains deterministic seeds and numerical consistency checks.

Camdon initiated the investigation. OpenAI’s GPT-6.2 generated the derivation, numerical implementation and manuscript. Independent expert review and publication priority remain open. Comments identifying a gap in the argument or an earlier proof are welcome through [repository issues](https://github.com/f8bsd9yqgp-maker/Solved-conjectures-/issues).
