# Satisfiability complexity of cautious and bold distributed belief

Date: 2026-11-26. AI-assisted proof draft, pending independent verification and priority confirmation. No journal submission; not counted as an independently confirmed solved conjecture.

Source: J. I. Lindqvist, F. R. Velázquez-Quesada and T. Ågotnes, "Variations on distributed belief", Journal of Logic, Language and Information 35 (2026), 233–268, published online 12 November 2025, https://doi.org/10.1007/s10849-025-09446-8. Section 5 explicitly raises the complexity profile of the two languages. Preprint: https://arxiv.org/abs/2408.10637.

## Claimed classification and scope

For unrestricted Kripke models, explicitly listed nonempty groups, and formula-tree input:
- Fixed nonempty finite agent set: cautious, bold and combined satisfiability are PSPACE-complete.
- Variable finite agent set: bold satisfiability is PSPACE-complete; cautious and combined satisfiability are EXPTIME-complete.

Only agents occurring in the input need be considered. No frame conditions (KD45, S5, etc.) are imposed. The variable-agent theorem is an extension of the fixed-agent setting of the source.

## 1. Local signature semantics

At a world w, a successor v has signature S(v)={i : w R_i v}. Ignore empty signatures. For a nonempty group G, let P_G be the family of realized nonempty projections S(v) intersect G. Its inclusion-maximal elements are exactly the maximally consistent subgroups of G. Every world in the conjecture set of such a maximal subgroup H has projection exactly H. Thus C_G phi (cautious) is true iff every successor with a maximal nonempty projection satisfies phi. E_G phi (bold) is true iff some maximal nonempty projection has all its successors satisfying phi. When P_G is empty, C_G phi is vacuously true and E_G phi is false. This is precisely the source's nonempty-subgroup convention.

A useful equivalent local constraint is:
- C_G phi true iff each realized nonempty projection at a phi-false successor has a strict extension among realized projections.
- E_G phi false iff every realized nonempty projection has an extension (possibly equal) at a phi-false successor.
The latter follows by taking a maximal extension, or by applying the condition to a maximal projection. Both equivalences use finiteness of the agent set, not of the original world set.

## 2. Fixed-agent PSPACE upper bound and finite model property

Let n be formula length and a be agent count. At each node of a satisfying model retain one successor of each realized nonempty signature (at most 2^a); for each false cautious subformula retain one false witness with maximal projection; for each false bold subformula retain a false witness at each maximal nonempty projection (at most 2^a). All maximal projection families are preserved, as are the required counterexamples and true modalities. Empty-signature worlds need not be retained as successors.

Repeat on retained copies with decreasing modal depth, preserving the truth of the operands required at each stage. Unrestricted accessibility permits tree unfolding; no property of edges other than their signatures is required. This yields a finite tree of depth at most n and branching at most 2^a+n+n*2^a. For fixed a, guess each local list of successor signatures and Boolean-consistent subformula types, verify each modal requirement by direct projection enumeration, and recursively verify successor types with reduced depth. Polynomial space suffices by depth-first nondeterministic traversal; NPSPACE=PSPACE.

## 3. Combined variable-agent EXPTIME upper bound

Use subformula types restricted to modal depth at most d and compute their realizability bottom-up in d. Boolean consistency is checked within each type. Given a root type at depth d, let U be the universe of pairs (S,t) where S is a nonempty subset of the occurring agents and t is a realizable depth-(d-1) type. Its size is at most 2^(a+n).

For each false C_G phi choose a nonempty designated projection H subseteq G, intending a maximal phi-false witness. For each true E_G phi choose a nonempty designated projection H subseteq G, intending a maximal all-phi fiber. Enumerate these choices (at most 2^(an)). Remove every candidate whose G-projection strictly contains any corresponding designated H. For true E additionally remove candidates whose projection equals H but whose type falsifies phi.

From the surviving universe delete repeatedly:
1. For every true C_G phi, a candidate with nonempty G-projection and false phi if no remaining candidate has a strictly larger G-projection.
2. For every false E_G phi, a candidate with nonempty G-projection if no remaining candidate has a G-projection containing it and a type falsifying phi.

Take the greatest fixed point of these deletions. Accept the root type for this choice iff each false C has a surviving candidate with projection exactly its designated H and false phi, and each true E has at least one surviving candidate with its designated H. A satisfying local family survives because each deletion is justified by absence of a required witness and the family is closed under the required existential witnesses. Conversely the final fixed point itself is a satisfying family by the local equivalences in section 1 and the designated witnesses. Attach independent realizing models for its successor types. This gives induction on modal depth including the depth-zero propositional base case.

There are at most n depth levels and 2^n types per level, and each enumeration, fixed-point scan and projection check costs at most a single exponential in n+a (with a<=n under explicit encoding). Hence deterministic EXPTIME suffices.

## 4. Variable-agent bold-only PSPACE upper bound

Fix a Boolean-consistent type at a node. Guess a nonempty designated projection H_i subseteq G_i for each positive E_(G_i) phi_i. Each signature S is admissible if S intersect G_i never strictly contains H_i. Its local positive obligations are all phi_i for which S intersect G_i equals H_i. A type satisfying these obligations is permitted for S.

Shrinking a permitted signature S to a nonempty subset S' cannot create a strict superset of any H_i. Nor can it create a new equality with H_i: if S' intersect G_i=H_i then S intersect G_i contains H_i, and admissibility forces equality already. Thus shrinking preserves permission for the same truth type.

Every positive modality requires a witness at H_i, and by shrinking one may choose its full signature to equal H_i. Each negative modality not E_(G_j) psi_j requires, for each realized S with S intersect G_j nonempty, some psi_j-false successor with projection containing S intersect G_j. Shrinking allows choosing its signature exactly S intersect G_j. Start the signature family from all H_i and close under nonempty intersections with negative groups G_j. All signatures are subsets of some H_i, and the family is generated by at most 2^n intersection choices per seed. For each seed require a successor satisfying its positive obligations. For every signature S in the closure and every negative group G_j with nonempty H=S intersect G_j, require a successor of signature H satisfying its positive obligations together with not psi_j. Disallow any inadmissible signature. No mutual exclusion exists between successors satisfying different operand requirements, so choose a separate successor for each obligation. These requirements are necessary by shrinking in an actual model and sufficient by building the indicated family; every chosen successor is in the closure and every negative witness exists. When there are no positives the empty family works.

A polynomial-space procedure enumerates closure elements by a seed and a subset of negative-group indices, computes their bit-vector intersections, and recursively checks each required operand conjunction. The positive designated subgroups are guessed once per node and held fixed across all checks. Each recursive test concerns only lower-depth subformulas from the input; keep them as references with signs, not recursively expanded syntax. Depth-first storage is polynomial, even though the number of successor checks can be exponential. NPSPACE=PSPACE proves membership.

## 5. PSPACE lower bounds

Modal K satisfiability is PSPACE-complete (R. E. Ladner, 1977, "The computational complexity of provability in systems of modal propositional logic", SIAM Journal on Computing 6, 467–480). With any one agent i, replace the ordinary box by C_{i} phi for cautious logic, or by (not E_{i} top) or E_{i} phi for bold logic. These are exactly the ordinary box, including at empty accessibility sets, and contain only one occurrence of the translated operand. Translation size is linear. Thus all stated PSPACE lower bounds hold, including the variable-agent bold case.

## 6. Variable-agent cautious EXPTIME hardness

Reduction from acceptance of a fixed alternating polynomial-space machine M on input x (APSPACE=EXPTIME, Chandra–Kozen–Stockmeyer). Normalize M to two labelled transitions per nonterminal configuration, with duplicated deterministic moves where needed, polynomial-length configuration encodings, and halting on all branches. A polynomial-space clock can enforce halting if needed, using a polynomial number of additional bits. Use polynomial-size propositional formulas for well-formed configurations, accept/reject/existential/universal status, the initial configuration, and legal labelled transitions between two copies of the configuration bit vector. For the standard fixed machine and tape-cell encoding these are polynomial-size Boolean formulas by local transition rules, without requiring circuit-to-formula expansion.

All modal constraints below are evaluated at a single root. Write C for cautious belief. Let X,Y be two registers of configuration bits. For every bit b in either register introduce base agents b^0,b^1. Impose C_{b^0}(not b) and C_{b^1}(b). Let the role agents be I (initial X configuration), Q_X,Q_Y (configuration), and T_XY^0,T_XY^1,T_YX^0,T_YX^1 (labelled transition). Let A0 contain all bit and role agents. Use distinct role propositions rho_r and singleton C_{r}(rho_r and all not rho_s for s different from r), so no signature can contain two distinct role agents. Additional singleton C_{r} constraints impose:
- I: initial configuration in X.
- Q_X/Q_Y: valid nonrejecting configuration in X/Y.
- I also valid nonrejecting in X.
- T_XY^t: X a valid nonterminal configuration, Y its legal t-successor; similarly T_YX^t. Destination must be nonrejecting (or equivalently this follows from mandatory transfer into a nonrejecting configuration role).
Require not C_{I} bottom, ensuring I is realized.

### Completeness gadget

For every bit b let G_b=A0 minus {b^0,b^1}. Introduce two fresh auxiliary agents u_b,v_b and fresh propositions p_b,q_b. Add five constraints:
    C_{u_b}(p_b and q_b)
    C_{v_b}(p_b and not q_b)
    C_{G_b union {u_b}} q_b
    C_{G_b union {v_b}} not q_b
    C_{A0} not p_b.

Claim: every maximal realized A0-projection containing a role agent contains exactly one bit agent per bit. At most one follows from singleton bit constraints. Suppose such a maximal projection S lacks both agents for b. At a world with projection S, choose the u_b constraint if q_b is false, otherwise the v_b constraint. Its projection to that auxiliary group is S, since the chosen auxiliary agent cannot occur there by the corresponding singleton constraint. S is nonempty due to its role. The violated cautious condition forces a strictly larger projection; maximality in A0 means this extension can only add the chosen auxiliary agent. The witness therefore has base projection exactly S and p_b true, violating C_{A0} not p_b. Contradiction.

### Computation constraints

Let B_X and B_Y be the sets of all bit agents in the respective registers. Define source marker Xsrc=rho_I or rho_Q_X, Ysrc=rho_Q_Y. For register X add
    C_{B_X union {T_XY^0,T_XY^1}} not (Xsrc and Exist(X))
    C_{B_X union {T_XY^t}} not (Xsrc and Univ(X))   for t=0,1.
For Y add the analogous constraints with Ysrc and T_YX^t. Here Exist and Univ designate nonterminal configurations, not accepting halts.

Transfer from transition roles to destination configuration roles is forced by
    C_{B_Y union {Q_Y}} not (rho_T_XY^0 or rho_T_XY^1)
    C_{B_X union {Q_X}} not (rho_T_YX^0 or rho_T_YX^1).

Conjoin all constraints. The number of agents and the total written group sizes and formula sizes are polynomial.

### Soundness

Start at an I-world and extend its nonempty base projection to a maximal realized base projection, keeping I. By the gadget its registers are complete and its X configuration is the initial one. Consider any maximal base world with a configuration role and a nonterminal configuration. Its projection to the appropriate transition group consists of the complete source register signature and no transition agent, by role exclusivity. Its marker falsifies the cautious operand in each required constraint. Hence there must be a strict extension of this nonempty projection. No further source bit agent is compatible, so an indicated transition role must be added. At existential configurations this supplies one legal labelled child; at universal configurations both labelled children are required. Extend each resulting base signature to a maximal one, retaining the transition role and the complete source register; the gadget makes the destination register complete, and singleton transition constraints certify legality.

Now the transition-role world falsifies the corresponding transfer operand. Its projection to the transfer group consists of the complete destination register, without the target configuration role. A strict extension necessarily adds that role and preserves the destination register. Extend to a maximal base signature again; this yields a valid nonrejecting configuration in the other register. Recursively follow these steps. The machine halts on all branches, and reject states cannot occur in configuration roles; all leaves accept. Hence M accepts x.

### Completeness

Given a finite accepting computation tree, create one root successor for each configuration and chosen transition occurrence. Alternate the active register by tree depth. The initial occurrence has role I, subsequent occurrences Q_X or Q_Y as appropriate. Each transition occurrence has its labelled transition role and encodes both endpoints in the appropriate registers. Assign unused register bits arbitrarily at configuration occurrences. Give every successor exactly its one role and exactly one bit agent per bit in both registers. Its propositional valuation matches those bits and its role marker, and all p_b are false. Choose q_b arbitrarily for these base worlds.

For each base world and each bit b add two copies, remove its b-bit agent, and add u_b or v_b respectively. Keep its role marker and register valuations, set p_b true and q_b to true or false according to the auxiliary agent; other p and q values may be copied. Copies do not gain other auxiliary agents. Define root accessibility by these signatures; no further edges are necessary.

Verify singleton constraints: copied worlds preserve the parent role and bit valuations, and the new auxiliary valuations satisfy their singleton constraints. A copy's base projection is strictly contained in its parent's complete projection; complete base projections all have equal cardinality and are maximal, so C_{A0} not p_b holds. For auxiliary group G_b union {u_b}, any successor falsifying q_b lacks u_b. Its projection is contained in its underlying parent's G_b projection. The u_b copy of that parent realizes this parent projection plus u_b, a strict extension. Thus all maximal projections satisfy q_b. The v_b group is dual. This verifies all five completeness constraints, including copies belonging to other bits.

For computation and transfer constraints every violating successor has the same register valuation and role marker as its parent base world. Its relevant group projection is a subset of that parent's projection (auxiliary agents do not belong to these groups). At a violating parent, the accepting tree provides a strict extension by a required transition role or destination configuration role, while preserving all active register bits. This extension also strictly extends the copy's projection. Consequently no violating successor has a maximal nonempty projection in the corresponding group. All cautious constraints hold, and the initial I-world exists.

This proves satisfiability iff M accepts. Hence cautious satisfiability is EXPTIME-hard, already for modal-depth-one formulas, and combined logic inherits hardness. Section 3 supplies matching membership.

## 7. Novelty and audit record

Renewed public search on 2026-11-26 located the source article, its arXiv preprint and the earlier cautious-distributed-belief conference paper, but no directly matching complexity classification. Searches included the paper title with complexity/satisfiability, cautious distributed belief with EXPTIME, and bold distributed belief with PSPACE. No claim that all literature or all unpublished manuscripts were inspected.

Recursive default-branch GitHub path checks, all untruncated:
- f8bsd9yqgp-maker/Solved-conjectures-: 424 entries
- 1337isnot1337/solved-conjectures: 19,113 entries
- f8bsd9yqgp-maker/Math: 296 entries
No path matched author names or distributed/cautious/bold belief keywords. These are filename/tree checks, not full-content checks.

The proof above expands the previous chat's hardness sketch and spells out closure, witness, and auxiliary-copy correctness. In particular, the polynomial-space bold argument depends on shrinking not introducing a new equality to a designated maximal projection, which is justified by the prohibition on strict supersets. These results have not been peer reviewed, formally verified in a proof assistant, or independently certified. The original paper also asks for axiomatizations; this note addresses satisfiability complexity only. Do not increase the confirmed solved count pending independent review and priority confirmation.
