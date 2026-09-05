# Research Translation

Use this for papers, notebooks, arXiv/SSRN ideas, model-guided research, JAX demos, PyTorch ports, and productionization.

## Translation Pipeline

1. Extract the claim.
2. Identify assumptions.
3. Map to a minimal reproducible experiment.
4. Implement the dumb baseline.
5. Implement the paper/model idea.
6. Run ablations and stress tests.
7. Compare to benchmark.
8. Decide: reject, archive, iterate, or promote.

## Model-Guided Research Pattern

For speculative math/AI ideas, separate:

- exploratory demo
- production implementation
- benchmark matrix
- failure cases
- computational cost
- domain use cases

Keep exotic ideas under controlled experiments until they beat simple baselines.

## Source Triage

- Prefer primary papers, repos, and official docs.
- Record exact URL/path and retrieval date.
- Distinguish peer-reviewed, preprint, blog, benchmark, and marketing claims.
- Do not import unverified claims into production logic.

## Output Pattern

- Paper/repo/source.
- Core idea.
- Why it may matter.
- Assumptions.
- Minimal experiment.
- Baselines.
- Risks.
- Implementation sketch.
- Promotion criteria.

