# Recursive Improvement Loop

Use this loop to continuously improve strategies and decision quality.

## Loop Stages

1. Observe
   - gather latest performance, risk, and implementation metrics
   - detect drift vs expected behavior

2. Diagnose
   - determine whether issue is signal, regime, execution, sizing, or governance
   - quantify confidence in diagnosis

3. Patch
   - design smallest effective change first
   - avoid multi-variable patching unless absolutely needed

4. Re-Test
   - run out-of-sample and stress checks
   - compare to pre-patch baseline
   - verify no metric gaming (for example, Sharpe improvement from hidden tail risk)

5. Redeploy
   - deploy with guarded sizing
   - define observation window and rollback trigger

## Evidence Standards

For every patch:

- include hypothesis
- include expected measurable effect
- include metrics used to validate/refute
- include explicit stop condition

## Minimum Experiment Register

Store and update:

- strategy id
- change id
- date/time
- hypothesis
- patch summary
- expected impact
- realized impact
- decision (keep/rollback/iterate)

## Meta-Learning Rules

- If two consecutive patches fail, reduce complexity and test simpler hypotheses.
- If performance improves but risk asymmetry worsens, treat as false improvement.
- If multiple sleeves degrade simultaneously, suspect regime or data pipeline first.
- If one sleeve degrades while peers hold, suspect sleeve-specific decay.

## Guardrails

- no overfitting to the last window
- no hidden leverage added to mask weak signal quality
- no narrative-only justification for redeployment

## Output Format for Each Loop

- `state`: what changed in market/system
- `diagnosis`: why the current approach degraded or improved
- `patch`: what is being changed
- `validation`: how the patch was tested
- `decision`: keep, rollback, or iterate
