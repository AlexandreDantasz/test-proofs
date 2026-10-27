# AI Engineering Journey

My 2-year path from back-end developer to Applied AI Engineer.
Every concept I study becomes code in this repository, with tests.

###
Run tests as pytest module in virtual env.

## Weekly routine (~18 h)

| Day | 21h–00h | Focus |
| --- | --- | --- |
| Mon | Fundamentals | Math & ML — build it from scratch in pure Python |
| Tue | Code | 1 algorithm problem (no AI) + Python / testing module |
| Wed | Fundamentals | Math & ML — apply it with NumPy / real data |
| Thu | Code | Testing, Docker, open source reading |
| Fri | Project | Portfolio projects (separate repositories) |
| Sat (morning) | Writing & English | Weekly review, posts, spoken English |

## Structure

| Folder | Area |
| --- | --- |
| `01-math/` | Linear algebra, probability, statistics, calculus |
| `02-python/` | Idiomatic Python exercises |
| `03-algorithms/` | NeetCode 150, one folder per topic |
| `04-software-engineering/` | Testing, code review checklist |
| `05-infra/` | Docker, PostgreSQL |
| `06-frontend/` | TypeScript, React, Next.js |
| `07-applied-ai/` | Prompting, RAG, evals, agents |
| `08-classic-ml/` | scikit-learn, metrics |
| `09-deep-learning/` | micrograd, makemore, GPT from scratch |
| `10-post-training/` | Fine-tuning, LoRA, DPO, interpretability |
| `11-writing/` | Blog posts and English practice |
| `templates/` | Templates for weekly notes and problems |

## Progress

| Phase | Weeks | Gate | Status |
| --- | --- | --- | --- |
| 1 · Verify | 1–13 | Project 1 with tests + CI | 🟡 In progress |
| 2 · Applied LLM | 14–30 | ReqBot + published eval | ⬜ |
| 3 · ML internals | 31–52 | Mini-GPT + LoRA fine-tune | ⬜ |
| 4 · Public proof | 53–104 | Open source PRs, applications | ⬜ |

## Running

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
pytest
```

## Rules

1. Fundamentals and Code nights: AI may **explain** and **review**, never write the solution.
2. Every night ends with a commit and one line in [`diario.md`](diario.md).
3. A module is done only when its "how to prove it" exercise passes its tests.

## Portfolio projects

- `api-abuse-detector` — sliding-window rate detection over API logs
- `reqbot` — meeting transcript → requirements → email with human approval
- `rag-eval-lab` — measuring chunking strategies by recall@k
- `scheduling-mcp-server` — MCP server for a scheduling system
- `mini-gpt-pt` — a small GPT trained on Portuguese public-domain text
