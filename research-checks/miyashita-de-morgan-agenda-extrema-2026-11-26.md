# Exact extrema for formula-based multivalued judgment aggregation with De Morgan negation

Date: 2026-11-26
Status: Candidate theorem in an explicitly defined extension; not a verified resolution of the full original research direction. AI-assisted draft; independent review and novelty verification pending.

## Source and target

Masaki Miyashita, "Agenda manipulation under doctrinal paradox", Social Choice and Welfare 67 (2026), 799–820, DOI https://doi.org/10.1007/s00355-026-01659-5 . Section 5.3 explicitly leaves mixed positive and negative occurrences for future research, including complications from non-neutral voting rules. The original positive-language framework uses a monotone common voting rule, individual valuations respecting entailment, and min–max collective deduction. Definition 3 requires a unique extension from voted premises.

## Precisely specified extension

Fix m >= 1 atoms. Let L be the free (unbounded) distributive lattice on the 2m signed literals p_i and not p_i, with involution N_L defined by swapping signed generators and interchanging meet and join. Equivalence here is distributive lattice equivalence plus De Morgan and double-negation laws, NOT classical Boolean equivalence or all identities of a particular finite truth chain. This is essential. Let T be a chain with an order-reversing involution N. Each individual v_i:L -> T is isotone, not necessarily a lattice homomorphism. Negation compatibility may additionally be required of individuals without affecting the proof. Let f:T^n -> T be isotone.

A formula-based procedure chooses an equivalent expression for a target a in L and a cut of its syntax tree, covering all leaves, with voted premise subtrees evaluated by g(b)=f(v_1(b),...,v_n(b)). All remaining connectives are evaluated by min, max and N in T. This definition is operational: voted subtrees are treated as input values rather than simultaneously imposing global consistency equations on all formulas. The same f is used for every vote. If desired, selected premise representatives can be padded by idempotent repetition to have equal syntactic height and hence avoid proper syntactic containment among distinct selected representatives.

Define h(b)=N(g(N_L b)), ell(b)=min(g(b),h(b)), u(b)=max(g(b),h(b)). Each of these maps is isotone: both N and N_L reverse order, while g preserves it.

Let J_a be the canonical join-prime monomials in the irredundant DNF of a, and M_a the canonical meet-prime clauses in its irredundant CNF, taken in the free distributive lattice on signed literals. Thus a=join J_a=meet M_a.

## Theorem

For every fixed profile and every formula-based procedure F,

    max_{j in J_a} ell(j) <= F <= min_{q in M_a} u(q).

Both extrema are attained by fixed procedures independent of the profile, in the operational model above.

## Proof

Replace each voted subtree by a placeholder and push all negations in the remaining deduction into the placeholders using De Morgan and involution. Upon substituting the associated propositions, the resulting expression is still equal to a in L. A positive occurrence of a voted premise b has score g(b); a negative occurrence represents proposition N_L b and has score N(g(b)) = h(N_L b). Hence every resulting signed input representing c has numerical value between ell(c) and u(c).

Distribute this remaining min/max expression into DNF. Its lattice interpretation is a join of meets of the corresponding signed input propositions c. For each j in J_a, join-primality and j <= a imply j <= one of these meets, hence j <= every input proposition c of that meet. Isotonicity implies ell(j) <= every corresponding numerical input value, hence ell(j) <= F. Maximize over j. Dually, use CNF and meet-primality: for each q in M_a, some disjunctive clause is <= q, so each constituent input c <= q and its numerical value <= u(q). This gives F <= u(q). Minimize over q.

For attainment, represent a as the join over j in J_a of (j meet N_L N_L j). Vote on j and N_L j, and negate the latter output in the formula. Each such term evaluates to ell(j); the whole expression gives the lower bound. Similarly represent a as the meet over q in M_a of (q join N_L N_L q); votes on q and N_L q give u(q) and attain the upper bound. These fixed expressions are logically equivalent in L by idempotence and involution. QED for the specified operational model.

If v_i(N_L b)=N(v_i(b)) and f is neutral, g=h and the formulas reduce to the canonical DNF/CNF extrema on signed literals. In the positive-language restriction with no negative votes or connectives, the standard DNF/CNF bounds likewise follow directly by taking g as the score of each input.

## Crucial compatibility caveat

The original paper requires a unique extension from the voted premises. The operational model above deliberately does not impose global consistency of these votes. For example, on [0,1] with N(t)=1-t, two voters assign p values 0.2 and 0.8, and f=min. Direct aggregation assigns both p and not p value 0.2, incompatible with a globally negation-preserving extension. The extremizing procedures may therefore be inadmissible in a negation-inclusive model that retains this global requirement. Syntactic padding does not repair semantic inconsistency. Moreover, the free De Morgan lattice equivalence is not classical equivalence: min/max with N(t)=1-t does not validate Boolean excluded middle at intermediate values.

Accordingly this note proves an exact theorem for a stated formula-based extension, not an unconditional resolution of Miyashita's original open direction. A further investigation must define admissibility under negation, check existence and uniqueness of deduction in the original sense, and determine extremal rules when votes must be globally coherent. A targeted literature search located the 2026 paper and related earlier work, but does not establish worldwide novelty or priority. The repository's solved count should not be increased on the basis of this draft.

## Review checklist

- Confirm the intended negation semantics and equivalence relation with the original author.
- Compare the operational cut model to Definition 3, especially the unique-extension condition.
- Examine restricted admissibility and neutral vs non-neutral aggregation.
- Review free distributive lattice normal form argument and prior work.
- Obtain independent expert verification before a confirmed solved entry or journal submission.
