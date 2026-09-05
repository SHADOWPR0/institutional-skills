#!/usr/bin/env python3
"""Route AI/ML/RL tasks to the right lab references and output contract."""

from __future__ import annotations

import argparse
import json


ROUTES = {
    "RL_EXPERIMENT": {
        "keywords": ["reinforcement", "rl", "policy", "reward", "simulator", "simulation", "bandit", "environment", "abides"],
        "references": ["references/rl-simulation.md", "references/experiment-design.md", "references/model-risk-governance.md"],
        "agents": ["Experiment Designer", "Model Builder", "Evaluation Lead", "Model Risk Officer"],
        "outputs": ["environment contract", "reward specification", "baseline policies", "risk limits", "promotion gate"],
    },
    "LLM_AGENT_EVAL": {
        "keywords": ["llm", "agent", "agents", "tool use", "memory", "benchmark", "hallucination", "eval", "evaluation"],
        "references": ["references/llm-agent-evals.md", "references/model-risk-governance.md", "references/experiment-design.md"],
        "agents": ["Research Scout", "Evaluation Lead", "Model Risk Officer", "Production Integrator"],
        "outputs": ["benchmark task set", "rubric", "tool policy", "memory policy", "failure examples"],
    },
    "MODEL_RISK": {
        "keywords": ["model risk", "governance", "drift", "monitor", "calibration", "challenger", "rollback", "kill switch"],
        "references": ["references/model-risk-governance.md", "references/experiment-design.md"],
        "agents": ["Model Risk Officer", "Data Auditor", "Evaluation Lead"],
        "outputs": ["model card", "monitoring plan", "drift metrics", "rollback plan", "approval gate"],
    },
    "RESEARCH_TRANSLATION": {
        "keywords": ["paper", "arxiv", "ssrn", "research", "jax", "pytorch", "notebook", "implementation", "ablation"],
        "references": ["references/research-translation.md", "references/experiment-design.md"],
        "agents": ["Research Scout", "Experiment Designer", "Model Builder", "Evaluation Lead"],
        "outputs": ["claim extraction", "minimal experiment", "baseline", "ablation plan", "promotion criteria"],
    },
    "ML_EXPERIMENT": {
        "keywords": ["ml", "machine learning", "model", "forecast", "classifier", "ranking", "features", "dataset", "training"],
        "references": ["references/experiment-design.md", "references/model-risk-governance.md"],
        "agents": ["Data Auditor", "Experiment Designer", "Model Builder", "Evaluation Lead"],
        "outputs": ["data contract", "split policy", "baseline", "metrics", "leakage checklist"],
    },
}


def route(text: str) -> dict:
    hay = text.lower()
    scored = []
    for name, spec in ROUTES.items():
        score = sum(1 for kw in spec["keywords"] if kw in hay)
        if score:
            scored.append((score, name, spec))
    if not scored:
        scored.append((1, "ML_EXPERIMENT", ROUTES["ML_EXPERIMENT"]))
    scored.sort(reverse=True, key=lambda x: x[0])
    primary = scored[0]
    refs: list[str] = []
    agents: list[str] = []
    outputs: list[str] = []
    for _score, _name, spec in scored[:3]:
        for key, target in [("references", refs), ("agents", agents), ("outputs", outputs)]:
            for item in spec[key]:
                if item not in target:
                    target.append(item)
    return {
        "classification": primary[1],
        "secondary": [name for _score, name, _spec in scored[1:3]],
        "references": refs,
        "agents": agents,
        "required_outputs": outputs,
        "universal_gates": [
            "baseline defined",
            "split policy defined",
            "leakage checklist completed",
            "success metric defined",
            "kill switch defined",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("text", nargs="+")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = route(" ".join(args.text))
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"classification: {result['classification']}")
        print("references:")
        for item in result["references"]:
            print(f"- {item}")
        print("required outputs:")
        for item in result["required_outputs"]:
            print(f"- {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

