# AI Engineering Labs

A hands-on, ~21-week path to becoming an LLM / GenAI engineer: RAG, evals, agents, MCP, and production.
Each phase ends with a working lab. Progress is logged session by session.

| Lab | Topic | Status |
|---|---|---|
| [Lab 1](labs/lab-01-cli-chatbot/) | CLI chatbot — streaming, history, token counting | ✅ Done |
| [Lab 2](labs/lab-02-rag/) | RAG over a PDF (Azerbaijani employee handbook) — embeddings, chunking, Chroma, citations | ⏳ In progress |
| Lab 3 | Evals — golden set, hit@k, MRR, LLM-as-judge | ⬜ |
| Lab 4 | Structured output, tool use, agents, MCP server | ⬜ |
| Lab 5 | Production — FastAPI, caching, tracing, cost, security | ⬜ |
| Capstone | End-to-end project | ⬜ |

**Stack:** Python 3.13 · Anthropic Claude · Gemini embeddings · Chroma

- [ROADMAP.md](ROADMAP.md) — full plan with checkboxes
- [PROGRESS.md](PROGRESS.md) — session log

## Setup
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
# create .env with ANTHROPIC_API_KEY and GEMINI_API_KEY
```
