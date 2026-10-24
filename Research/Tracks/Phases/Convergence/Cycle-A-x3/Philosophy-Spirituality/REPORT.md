# Convergence in the Philosophy Spirituality — Cycle-A-x3 (CVA)

Phase report: Convergence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x3: Peirce's primary text (P75) sourced; a toy shows convergence on the truth needs every method's errors, including shared ones, to shrink.

## Claims (ledger: `claims/claims.csv`)
- **CVA-PHI-01** [PS] Peirce characterised truth as the opinion that inquiry would converge on: 'the opinion which is fated to be ultimately agreed to by all who investigate' (1878), later the 'ideal limit towards which endless investigation would tend' (1901); P72 reports the long-standing objection that such epistemic accounts cannot handle 'buried secrets', statements true or false that no inquiry could settle, and Misak's point that we are then never in a position to judge whether a belief is true. *Operationalization:* PHI Convergence = Peircean convergence of inquiry. *Sources:* P72. *Limits:* Interpretive; pragmatic theories differ widely (James, Dewey, Rorty, Price, Misak) and P72 says there is no consensus response to the fundamental objection. Slip: 'monor functions'.
- **CVA-PHI-03** [PS] Peirce's own statement of convergence: investigators of the velocity of light by different methods 'may at first obtain different results, but, as each perfects his method and his processes, the results will move steadily together toward a destined centre'; truth is the opinion 'fated to be ultimately agreed to by all who investigate'; he answers the 'buried secrets' worry by holding that any question with a clear meaning would be settled if investigation went far enough, and contrasts science with methods where 'the idea of loyalty replaced that of truth-seeking'. *Operationalization:* PHI Convergence = Peirce's convergence of inquiry (primary text). *Sources:* P75. *Limits:* 1878 essay; Peirce's footnote says 'fate' means only what is sure to come true. Transcription slip or period spelling: 'curves of Lissajoux'.
- **CVA-PHI-02** [H] Bayesian inquirers sharing 5000 Bernoulli(0.6) observations converged but not within 0.02: disagreement shrank 0.61, 0.40, 0.20, 0.07 at 10, 100, 1000, 5000 observations (H1 not supported) because a confident wrong prior Beta(200, 800) was still at 0.53; a dogmatic inquirer whose prior excluded the truth settled on its nearest support (0.4); for observationally equivalent hypotheses ('buried secrets') posterior odds stayed at the prior odds, so disagreement never shrank. *Operationalization:* PHI Convergence = merging of opinions. *Sources:* SIM-CV-PHI-0/iter-1#V1;SIM-CV-PHI-0/iter-1#H1;SIM-CV-PHI-0/iter-1#H2;SIM-CV-PHI-0/iter-1#H3;SIM-CV-PHI-0/iter-1#H4. *Limits:* A toy of a philosophical thesis; priors and truth are the agent's choices; convergence of opinion is not Peirce's truth.
- **CVA-PHI-04** [H] In a toy of Peirce's passage, nine investigators whose biases (-3% to +3%) and noise shrink by 0.9 per round converged (spread 0.082 -> 0.000002) on the truth; one never-improving method kept the spread at 0.030 and the mean 0.003 off; and a 1% bias shared by all methods let them converge just as tightly on a value 1% from the truth: agreement alone does not show truth unless shared errors are removed. *Operationalization:* PHI Convergence = agreement of methods vs truth. *Sources:* SIM-CV-PHI-A/iter-1#V1;SIM-CV-PHI-A/iter-1#H1;SIM-CV-PHI-A/iter-1#H2;SIM-CV-PHI-A/iter-2#V1;SIM-CV-PHI-A/iter-2#H1;SIM-CV-PHI-A/iter-2#H2;SIM-CV-PHI-A/iter-3#V1;SIM-CV-PHI-A/iter-3#H1;SIM-CV-PHI-A/iter-3#H2. *Limits:* Toy; rates arbitrary; the shared-bias case is by construction.

## Simulations (SIM-CV-PHI-A; 3 iteration(s), spec-first; validation 3/3, hypotheses supported 6/6)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `a6e9419f` | Peirce's velocity-of-light passage (P75) as a toy: nine investigators with biases -3% to +3% perfect their methods (bias and noise x 0.9 per round): does their spread fall below 1% of the initial spread by round 100 and their mean come within 1e-4 of the truth? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |
| 2 | `37b36289` | Same toy with one method that never improves: does the spread stay >= 0.027 and the mean >= 0.003 from the truth? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |
| 3 | `ed14985a` | Same toy with a bias of 1% shared by every method: do the investigators still converge (spread < 1% of initial) - but on a value 1% from the truth? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (3; details `research/PASSES.md`)
- Pass 1: Peirce's primary text sourced (CVA-PHI-03, PS); convergence toy (CVA-PHI-04).
- Pass 2: CVA-PHI-04 (iter-2): a never-improving method blocks convergence.
- Pass 3: CVA-PHI-04 (iter-3): a shared bias gives convergence without truth.

## Unresolved
- No source on religious or perennialist 'convergence of traditions' read.
- Shared-bias case is a construction; no source on systematic error in science history read.
