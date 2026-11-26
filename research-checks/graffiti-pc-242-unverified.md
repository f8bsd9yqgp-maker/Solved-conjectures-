# Graffiti.pc #242 — total domination and degree-two neighborhoods

**Status (26 November 2026): research note only — NOT an independently verified new solution.**

## Claim discussed in ChatGPT

For a nontrivial tree (T), the candidate stronger inequality is

```text
gamma_t(T) >= (c(T) + diam(T))/2
```

where `gamma_t(T)` is the total domination number, and `c(T)` is the number of components of the graph induced by the union of the closed neighborhoods of degree-two vertices (the precise convention must be checked against the source conjecture). Because average eccentricity is no more than diameter, this claimed stronger inequality would imply the stated conjecture #242, provided the definitions coincide.

## Verification limitations

- The preceding chat **asserted** a complete proof, but did not supply its proof steps. **No independently checkable proof is archived here.**
- The preceding chat reported 986 trees tested up to order 12, 48 equality cases and zero counterexamples. No reproducible code, graph listing, or output accompanies those numbers, so they remain **unverified reports**, not certified computations.
- An originality review in the preceding chat identified a potentially prior, stronger result associated with Graffiti.pc #350 (posed in 2009 and reportedly previously proved in a 2026 account). This overlap **must be examined against the original theorem and conventions** before claiming novelty.
- Neither external peer review nor formal verification has been performed for this note.

## Next steps before promoting into the solved catalogue

1. Retrieve and quote exact definitions and quantifiers in #242 and #350.
2. Locate the earlier proof, check whether it really implies #242, and cite it.
3. Write a complete, line-by-line proof of the proposed diameter inequality or withdraw it.
4. Provide executable exhaustive-verification code and independently reproduce its reported counts.
5. Mark as a rediscovery or an existing result if the earlier proof applies.

**Counting policy:** This item does **not** increase the number of novel solved conjectures in the repository.
