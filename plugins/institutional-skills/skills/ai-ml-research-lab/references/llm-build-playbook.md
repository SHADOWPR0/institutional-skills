# LLM Build Playbook

## Purpose

This is the canonical local reference for learning how large language models are built, from first principles to production. It starts from the beginner mental model in the user's pasted primer, then upgrades it into an engineering roadmap for building, fine-tuning, evaluating, serving, and compounding LLM systems alongside trading and research models.

The practical goal is not to jump straight to a frontier-scale model. The goal is to build the full loop:

1. Understand the math and code.
2. Train tiny models from scratch.
3. Fine-tune and evaluate open models.
4. Build domain datasets and evals.
5. Connect LLM agents to research, trading, and portfolio workflows.
6. Let model errors and trading outcomes improve the next data and eval cycle.

## The Core Idea

An autoregressive LLM learns a probability distribution over the next token:

```text
p_theta(x_t | x_1, x_2, ..., x_{t-1})
```

Training minimizes next-token prediction loss:

```text
loss = -mean(log p_theta(true_next_token | prior_tokens))
```

Generation repeats the same operation:

1. Convert prompt text into tokens.
2. Predict logits for the next token.
3. Convert logits into probabilities.
4. Sample or choose a token.
5. Append it to the context.
6. Repeat until a stop condition.

Everything else is engineering around this loop: better data, larger models, better architecture, better training stability, better post-training, better evals, better serving, and better governance.

## What Is Actually Inside An LLM

Most modern text LLMs are decoder-only Transformers.

Core components:

- Tokenizer: maps text to integer token ids.
- Embedding table: maps token ids to vectors.
- Positional information: tells the model token order.
- Transformer blocks: repeated attention plus feed-forward layers.
- Residual connections: preserve signal across deep networks.
- Normalization: stabilizes training.
- Output head: maps hidden vectors back to token logits.
- Softmax and loss: converts logits into probabilities and trains against next-token labels.

## Tokenization

LLMs do not directly read words. They read token ids.

Common tokenizer families:

- BPE: byte-pair encoding.
- Unigram / SentencePiece-style tokenization.
- Byte-level tokenizers.

Tokenizer design affects:

- context efficiency
- multilingual performance
- code performance
- number handling
- rare names/entities
- training and inference speed
- domain vocabulary coverage

For finance and trading work, tokenization matters for tickers, option symbols, CUSIPs, ISINs, filings, formulas, dates, tables, code, and weird market shorthand.

Practical rule: before training a domain model, measure tokenization quality on your own corpus. If common internal terms explode into many tokens, consider a domain tokenizer or a better base model tokenizer.

## Transformer Mechanics

Each Transformer block learns which prior tokens matter for the current token.

For input matrix `X`, attention creates:

```text
Q = X W_q
K = X W_k
V = X W_v

attention(Q, K, V) = softmax((Q K^T) / sqrt(d_k) + causal_mask) V
```

The causal mask prevents the model from seeing future tokens during training. The model can only learn to predict token `t` from tokens before `t`.

Multi-head attention runs several attention maps in parallel, letting the model track different relationships: syntax, entities, references, code structure, table relationships, ticker mentions, and more.

The feed-forward or MLP layer applies nonlinear transformations token by token. In many LLMs, the MLP contains a large share of the parameters.

## The LLM Build Stack

An LLM system has several layers:

```text
data -> tokenizer -> architecture -> pretraining -> checkpointing -> evaluation
     -> post-training -> safety/governance -> serving -> product/agent loop
     -> telemetry -> data flywheel
```

Do not skip the eval layer. Without evals, model improvement is just vibes.

## Data Is The Main Asset

Model quality is heavily downstream of data quality.

Pretraining data pipeline:

1. Source selection.
   - web text
   - books
   - code
   - papers
   - docs
   - filings
   - transcripts
   - internal research, if legally and ethically usable

2. Cleaning.
   - remove boilerplate
   - fix encoding
   - normalize whitespace
   - remove broken pages
   - remove spam
   - strip dangerous or private material when required

3. Deduplication.
   - exact dedupe
   - near-dedupe
   - train/validation/test contamination control

4. Quality filtering.
   - language detection
   - perplexity filters
   - classifier filters
   - source trust rules
   - domain-specific quality checks

5. Mixture design.
   - general language
   - code
   - math
   - domain data
   - instruction data
   - safety data

6. Splits.
   - train
   - validation
   - test
   - adversarial holdout
   - private golden eval set

For a finance LLM, the dangerous failure mode is data leakage. A model that saw future filings, future prices, or evaluation answers in training is useless for research claims.

## Pretraining

Pretraining teaches broad language, facts, reasoning patterns, code patterns, and domain priors through next-token prediction.

Key design choices:

- parameter count
- context length
- tokenizer vocabulary size
- number of layers
- hidden dimension
- attention heads
- MLP expansion
- activation function
- normalization
- optimizer
- batch size in tokens
- learning-rate schedule
- weight decay
- gradient clipping
- precision
- checkpoint cadence
- validation cadence

Rules of thumb:

- Train tiny first. Bugs scale faster than models.
- Track validation loss, not just train loss.
- Use held-out data from the same domain and from harder adjacent domains.
- Watch gradient norm, loss spikes, learning rate, throughput, GPU utilization, and data loader health.
- Save checkpoints often enough to recover from bad runs.
- Run ablations on small models before burning large compute.

Compute-optimal training depends on data quality and objective. A common starting heuristic from Chinchilla-style thinking is roughly 20 training tokens per model parameter for dense decoder-only pretraining, then adjust based on empirical loss curves, domain mix, and budget.

## Post-Training

Raw pretrained models complete text. Assistant models follow instructions.

Main post-training stages:

1. Supervised fine-tuning.
   - Train on high-quality prompt/response examples.
   - Teaches format, tone, instruction following, and domain behavior.

2. Preference optimization.
   - Train from pairwise preferences or rankings.
   - RLHF uses a reward model and policy optimization.
   - DPO-style methods optimize preference data more directly and are often simpler to run.

3. Tool and agent training.
   - Teach the model when to call tools.
   - Teach source hierarchy, citation, file inspection, database use, and refusal boundaries.

4. Domain adaptation.
   - Continued pretraining on domain corpus.
   - SFT on domain tasks.
   - Preference tuning on expert choices.
   - Eval-driven regression protection.

For your stack, the right order is usually:

```text
open base model -> continued pretraining on legal/clean domain corpus -> SFT on your task formats -> DPO/preference tuning -> agent evals -> deployment behind retrieval/tools
```

## Fine-Tuning Vs RAG Vs Training From Scratch

Use the cheapest method that changes the needed behavior.

| Need | Best first move |
| --- | --- |
| Current facts or private docs | RAG/tool retrieval |
| Writing style or output format | SFT or prompt templates |
| Domain vocabulary and recurring reasoning style | continued pretraining plus SFT |
| Strong task preference, ranking, or judgment | preference tuning |
| New architecture or full control | train from scratch |
| Fast local specialist | LoRA/QLoRA adapter |

Training from scratch is mostly for learning, full control, or serious proprietary data/architecture strategy. For most useful internal systems, adapt a strong open model and invest heavily in evals, retrieval, and data quality.

## Parameter-Efficient Fine-Tuning

LoRA freezes the base model and trains small low-rank adapter matrices. It is the practical on-ramp for local experimentation.

Use LoRA/QLoRA when:

- you have limited GPU memory
- you want multiple task adapters
- you need fast iteration
- you want to avoid modifying the full base model

Use full fine-tuning when:

- you have enough compute
- the task deeply changes model behavior
- adapters are not enough
- you can afford stronger regression testing

## Evaluation

Evaluation is the real product.

Minimum eval harness:

- base model baseline
- task dataset
- scoring method
- human review rubric where needed
- contamination check
- adversarial cases
- cost and latency
- failure taxonomy
- regression suite
- promotion and rollback gate

Core LLM evals:

- perplexity on held-out data
- instruction-following quality
- factuality
- citation correctness
- math and code performance
- tool-use accuracy
- long-context retrieval
- hallucination rate
- calibration
- refusal and safety behavior
- latency, throughput, and cost

Finance-specific evals:

- filing extraction accuracy
- table and footnote interpretation
- time-aware reasoning with as-of dates
- no-lookahead compliance
- portfolio/risk math checks
- investment memo quality
- factor and regime explanation accuracy
- hallucinated citation rate
- correct uncertainty language
- ability to say "insufficient evidence"

No benchmark, no claim. No leakage check, no production promotion.

## Serving And Inference

Serving is its own engineering discipline.

Inference concepts:

- KV cache: stores prior attention keys/values for faster generation.
- batching: groups requests for throughput.
- streaming: returns tokens as generated.
- quantization: reduces memory and sometimes increases speed.
- speculative decoding: uses a smaller draft model to accelerate generation.
- retrieval: brings fresh/private facts into context.
- tool calling: gives the model actions beyond text.

Serving stack options:

- local Python for experiments
- Hugging Face Transformers for flexible research
- vLLM or similar engines for production throughput
- quantized local runtimes for edge/private use
- API model routing when local serving is not worth the infrastructure

Track tokens/sec, time-to-first-token, total latency, GPU memory, batch size, cache hit rate, error rate, and cost per accepted answer.

## Governance And Safety

Production LLM systems need controls:

- dataset provenance
- license and privacy review
- PII handling
- secrets filtering
- reproducible training configs
- checkpoint registry
- eval registry
- red-team cases
- rollback plan
- usage logs
- prompt and tool-call audit trail
- kill switch

For finance and family-office workflows:

- no live trading solely from LLM output
- no client/private data in external systems without explicit approval
- no fabricated sources
- no future-data leakage in research evals
- separate model estimates from facts and actions
- route capital decisions through `investment-management`

## Practical Learning Roadmap

### Phase 0: Vocabulary And Mental Model

Learn:

- tokenization
- embeddings
- attention
- MLPs
- logits
- cross-entropy
- sampling
- train/validation/test split
- overfitting
- hallucination
- evals

Deliverable:

- explain a decoder-only Transformer in your own words
- trace one prompt through tokenization, attention, logits, and sampling

### Phase 1: Build A Tiny GPT From Scratch

Goal: understand the machinery.

Projects:

- implement a character-level tokenizer
- implement embeddings and positional embeddings
- implement causal attention
- implement a Transformer block
- train on a tiny text corpus
- generate samples
- plot train/validation loss

Good repo to study: `karpathy/nanoGPT`.

### Phase 2: Train A Small Token-Level Model

Goal: make the system real.

Projects:

- train or load a BPE tokenizer
- train a 10M to 100M parameter causal LM
- use a real validation set
- add checkpointing
- add loss curves
- add basic generation controls
- compare data mixes

Deliverable:

- a small model card with data, hyperparameters, loss curves, evals, limitations, and sample failures

### Phase 3: Fine-Tune An Open Model

Goal: produce useful behavior.

Projects:

- choose a small open base model
- create a clean instruction dataset
- run LoRA/QLoRA SFT
- evaluate against the base model
- add domain-specific failure cases
- track cost and latency

Deliverable:

- local specialist assistant that beats the base model on a narrow eval set

### Phase 4: Build The Finance/Research Flywheel

Goal: compound LLMs with trading and research models.

Pipeline:

```text
research notes + filings + transcripts + market data docs + model logs
  -> cleaning and source hierarchy
  -> task datasets
  -> eval harness
  -> domain SFT / preference data
  -> research assistant / coding agent / risk reviewer
  -> outputs reviewed by trading and portfolio systems
  -> realized outcomes and error labels
  -> better datasets and evals
```

LLM roles:

- research scout
- filing/table extractor
- hypothesis generator
- code assistant
- experiment planner
- risk memo reviewer
- citation auditor
- model-risk checker
- post-mortem summarizer

Trading-model roles:

- signal generation
- backtesting
- walk-forward validation
- portfolio construction
- execution simulation
- risk and sizing
- realized outcome labels

The LLM should accelerate research and QA. It should not replace deterministic backtests, risk limits, or capital-allocation governance.

### Phase 5: Continued Pretraining And Preference Tuning

Goal: adapt the model to your actual corpus.

Projects:

- build a legally clean corpus
- remove future leakage
- train continued-pretraining checkpoints
- compare validation loss and domain evals
- SFT on your task formats
- DPO on expert preference pairs
- red-team hallucination and overconfidence

Deliverable:

- a domain model that shows measurable improvement on private evals and does not regress on general capability beyond acceptable thresholds

### Phase 6: Serious Pretraining From Scratch

Goal: full ownership.

Only do this after the earlier phases.

Requirements:

- strong data pipeline
- tokenizer choice
- distributed training stack
- reproducible configs
- GPU budget
- monitoring
- eval harness
- checkpoint management
- incident response

Likely training stacks:

- PyTorch for first-principles learning
- Hugging Face Transformers/Accelerate for flexible research
- Megatron-LM or similar frameworks for large distributed training
- custom infrastructure only when existing stacks become the bottleneck

## Minimal First Build Plan

Do this first:

1. Create a local repo for `llm-lab`.
2. Implement a tiny decoder-only Transformer or adapt nanoGPT.
3. Train on a tiny corpus until loss decreases.
4. Add a tokenizer experiment.
5. Fine-tune a small open model with LoRA.
6. Build a private eval set for finance/research workflows.
7. Add a model card for every run.
8. Connect the eval results to `ai-ml-research-lab` and `investment-management`.

Acceptance criteria:

- you can explain each tensor shape
- you can reproduce the run
- you can show train and validation loss
- you can name the model's failure modes
- you can compare it against a baseline
- you know whether the model improved or merely sounded better

## Common Failure Modes

- Training on dirty data and blaming the architecture.
- Evaluating on contaminated examples.
- Mistaking low train loss for capability.
- Skipping baseline comparison.
- Fine-tuning style but expecting new factual knowledge.
- Using RAG when the model needs behavior change.
- Training when retrieval would solve the problem.
- Scaling before the tiny model works.
- Ignoring serving cost and latency.
- Letting LLM outputs leak into trading decisions without deterministic checks.

## How This Connects To The Existing Skill System

Use:

- `ai-ml-research-lab` for LLM experiments, training plans, evals, model risk, and reproducibility.
- `agent-ops-control-plane` for agent swarms, context budgets, benchmark harnesses, cost/runtime governance, and recursive ledgers.
- `investment-management` as decision owner for finance, trading, risk, and portfolio use cases.
- `ethical-supersuader` for writing quality and voice alignment after factual correctness is established.
- `growth-operating-system` when LLMs are used for campaigns, CRM, outreach, or sales agents.

## Source Trail

Primary and practical sources to study:

- Transformer architecture: https://arxiv.org/abs/1706.03762
- Scaling laws: https://arxiv.org/abs/2001.08361
- GPT-3 and few-shot behavior: https://arxiv.org/abs/2005.14165
- Compute-optimal training / Chinchilla: https://arxiv.org/abs/2203.15556
- InstructGPT / RLHF: https://arxiv.org/abs/2203.02155
- LoRA: https://arxiv.org/abs/2106.09685
- DPO: https://arxiv.org/abs/2305.18290
- The Pile dataset paper: https://arxiv.org/abs/2101.00027
- Llama 3 model-family paper: https://arxiv.org/abs/2407.21783
- OLMo open language model: https://arxiv.org/abs/2402.00838
- Hugging Face causal LM guide: https://huggingface.co/docs/transformers/tasks/language_modeling
- Hugging Face TRL: https://huggingface.co/docs/trl
- nanoGPT: https://github.com/karpathy/nanoGPT
- Megatron-LM: https://github.com/NVIDIA/Megatron-LM
- vLLM serving: https://blog.vllm.ai/2023/06/20/vllm.html
