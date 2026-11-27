# Project Rhinology — Differential nasal impedance and wall-motion assessment

Date: 2026-11-26 (US Central)
Status: UNVALIDATED RESEARCH PROPOSAL — not a solved clinical problem or verified novel conjecture.

## Clinical question
Can frequency-dependent pressure/flow measurements combined with controlled lateral wall support and direct motion observation improve assessment of dynamic nasal valve collapse relative to four-phase rhinomanometry?

## 1. Single-relaxation model
Let Z(w)=R+iwL+G/(1+iw tau), with G,tau>0. For 0<w1<w2 define A_j=Re Z(w_j), B_j=Im Z(w_j)/w_j, D=A1-A2, E=B2-B1. Direct algebra gives
D=G tau^2 (w2^2-w1^2)/[(1+w1^2 tau^2)(1+w2^2 tau^2)]>0 and E=tau D.
Thus tau=E/D, G=D(1+w1^2 tau^2)(1+w2^2 tau^2)/(tau^2(w2^2-w1^2)), R=A1-G/(1+w1^2 tau^2), L=B1+G tau/(1+w1^2 tau^2).
This is a special case of established rational transfer-function identification and the extended RIC circuit model, not an original model. For a third frequency, B=L+tau R-tau A provides a necessary collinearity check, not sufficient proof of the full model.
If each measured real and imaginary part has absolute error <=epsilon, then |tau_hat-tau| <= epsilon(1/w1+1/w2+2tau)/(D-2epsilon) when D>2epsilon.
For fixed ratio r=w2/w1>1, the resistance contrast D is maximized at w1*w2=1/tau^2, with D_max=G(r-1)/(r+1). This follows by differentiating D/G=(r^2-1)x/[(1+x)(1+r^2 x)], x=(w1 tau)^2. It is not a general optimum under arbitrary measurement noise or for estimating every parameter.

## 2. Differential multifrequency identifiability
Model the unsupported-minus-supported impedance as
Delta Z(s)=Delta R+s Delta L+sum_{j=1}^k g_j/(1+s tau_j),
where k<=m, s=iw, tau_j distinct positive, g_j real and nonzero.
Claim: m+1 distinct positive frequencies uniquely identify the reduced rational function in noiseless data.
Proof: for two candidate functions P1/Q1 and P2/Q2, deg P<=m+1 and deg Q<=m. Equality at m+1 positive imaginary points implies equality at their complex conjugates by real coefficients. The polynomial P1Q2-P2Q1 has degree <=2m+1 and at least 2m+2 distinct zeros, so vanishes identically. Distinct nonzero residues and positive relaxation times follow from the unique partial fraction decomposition. Poles cannot be recovered for zero or exactly cancelling residues. Necessity: on the open full-dimensional parameter family with exactly m ordered distinct relaxation times and nonzero residues, a continuous injective measurement map requires at least 2m+2 real dimensions by invariance of domain. This yields m+1 complex measurements. The argument uses classical rational interpolation and does not establish novelty.
A separate statistical test can project complex measurements onto the complement of the two-dimensional real span of 1 and iw. If errors are independent Gaussian with common known real-component variance sigma^2, the squared residual divided by sigma^2 has chi-square distribution with 2M-2 degrees of freedom under the affine null. This detects departures from the affine model, not disease.

## 3. Motion coupling and confounding
At a fixed frequency, write Z_j=B+H M_j+e_j, where M_j is measured complex wall displacement per unit flow, B is a shared complex background, H is complex coupling, and e_j is residual error.
If M1!=M2 and M is exact, H_hat=(Z1-Z2)/(M1-M2) satisfies |H_hat-H|<=2 epsilon/|M1-M2| when |e_j|<=epsilon, by the triangle inequality. A third condition permits checking the assumed affine relationship. If displacement is noisy the bound must be modified; if the background changes without a known bound, causal coupling is not identifiable. Indeed for arbitrary a, H'=H+a and e'_j=e_j-a M_j produce exactly the same measurements. Additional support conditions alone do not resolve proportional confounding.
The single-relaxation impedance can also be produced by a passive parallel resistance/compliance element in series with R and L, with compliance C=tau/G. Thus even the full frequency response cannot uniquely attribute the mechanism to anatomical valve collapse.

## 4. Proposed clinical study
This is a research design for review by qualified clinicians, not instructions for unsupervised experimentation.
- Establish equipment safety and calibration, repeatability and signal feasibility first, using benchtop phantoms and appropriate oversight.
- Prospectively enroll consecutive adults with nasal obstruction and suitable negative controls, including fixed and inflammatory obstruction, subject to ethics approval and consent.
- Obtain independently assessed clinical reference labels, blinded to the investigational test; use dynamic imaging as appropriate. Explicitly document possible reference-standard error.
- Collect paired four-phase rhinomanometry and investigational impedance/motion measurements under randomized or counterbalanced support and sham conditions, with standardized operating points.
- Predefine features and diagnostic thresholds using development data only; evaluate on an independent cohort. Account for within-person correlation between nostrils. Report uninterpretable measurements and missing data.
- Compare paired sensitivity and specificity, with patient-clustered confidence intervals, ROC-AUC and prespecified criteria for improvement. Power the study using paired discordance rates rather than assuming an arbitrary sample count establishes superiority.
- A 2022 study reported sensitivity 88.3% and specificity 89.9% at a study-selected loop-area cutoff; this is a contextual benchmark, not our accuracy or a head-to-head result.

## 5. Prior art and limitations
- Gagnieur et al., 2022, objective diagnosis of internal nasal valve collapse by four-phase rhinomanometry: https://doi.org/10.1002/lio2.784
- Synchronous pressure-flow and nasal wall movement investigation (2005): https://pubmed.ncbi.nlm.nih.gov/16222191/
- Englhard et al., dynamic nasal valve optical coherence tomography (2018): https://doi.org/10.1002/lary.26962
- Bauer et al., electro-optical nasal valve elastography (2024): https://pubmed.ncbi.nlm.nih.gov/39305858/
- Lateral support maneuver (2025): https://pubmed.ncbi.nlm.nih.gov/40951987/
The proposed combined protocol overlaps substantially with published research. Independent novelty is not established. No patient-level validation or clinical superiority has been demonstrated. Earlier synthetic demonstrations are not patient evidence; numerical claims are not included here without verified reproducible execution records.

## 6. Research outreach
Seven individually addressed research-feedback messages were sent on 2026-11-26 US Central to relevant rhinology researchers, requesting prior-art pointers, feasibility feedback and appropriately governed data access. No endorsement, collaboration or response is implied.

Do not count this proposal as a solved medical conjecture or a clinical breakthrough.
