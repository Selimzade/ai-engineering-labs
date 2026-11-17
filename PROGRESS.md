# Progress Jurnalı

> Ən yeni qeyd yuxarıda. Hər sessiyanın sonunda yenilənir.

---

## 2026-11-18 — Claude Code-a keçid
**Nə etdik:**
- `CLAUDE.md`, `ROADMAP.md`, `PROGRESS.md` yaradıldı.
- Köhnə kod `D:\Projects\Python\ai-engineer-lab`-dan **kopyalandı** (orijinal yerində qalıb):
  - `lab1-chatbot` → `labs/lab-01-cli-chatbot/`
  - `embedding-lab` → `labs/lab-02-rag/day-01-embeddings/`
  - `chunking` → `labs/lab-02-rag/day-02-chunking/` (PDF yolu `../data/...` olaraq düzəldildi)
  - PDF → `labs/lab-02-rag/data/`
- Bir ümumi `.env` (ANTHROPIC_API_KEY, GEMINI_API_KEY), `.gitignore`, `requirements.txt`, kökdə `.venv` (Python 3.13).
- `chunk.py` yeni yerdə yoxlanıldı → 94 parça.
- Roadmap yeniləndi (~21 həftə): Git indidən; mini golden set Həftə 5-də; structured output və framework müqayisəsi Mərhələ 4-də; tracing (Langfuse) Mərhələ 5-də; işə hazırlıq Mərhələ 6-da; Lab 2-dən `claude-haiku-5-5`.
- Git repo quruldu (`main`), ilk commit edildi, `README.md` əlavə olundu. GitHub-a hələ push edilməyib.

**Harada qaldıq:** Lab 2, Həftə 4 — chunking hazırdır, növbəti addım **Chroma**.

**Növbəti addım:**
1. Day-01 və Day-02 üçün qısa `NOTES.md` (öz sözlərinlə nə öyrəndin)
2. `day-03-chroma/`: chunks.json → Gemini embedding → Chroma kolleksiyası → sorğu

**Açıq suallar:**
- Chunking: niyə bənd üzrə? Ən uzun/ən qısa bəndlər nə qədərdir, problem yaradırmı?
- Embedding üçün Gemini, generasiya üçün Claude — bu seçim düşünülmüşdürmü? (Anthropic-in öz embedding modeli yoxdur, Voyage AI tövsiyə edir)

---

## Əvvəlki iş (Claude AI-da)

**Lab 2 / Day-02 — Chunking** (`day-02-chunking/chunk.py`)
- pypdf ilə mətn, ilk 2 səhifə (üz qabığı + mündəricat) atılır, footer regex ilə silinir
- Bənd (`4.1 ...`) üzrə bölmə, hər chunk-a `bölmə > bənd başlıq` prefiksi əlavə olunur
- Nəticə: `chunks.json` (number, title, chapter, text)

**Lab 2 / Day-01 — Embeddings** (`day-01-embeddings/`)
- `gemini-embedding-001`, 768 ölçü, sual üçün RETRIEVAL_QUERY, sənəd üçün RETRIEVAL_DOCUMENT
- Cosine similarity numpy ilə əllə
- RAG system prompt: yalnız kontekst, "Məndə bu haqda məlumat yoxdur", `(Mənbə: 4.1)` formatı

**Lab 1 — CLI chatbot ✅**
- anthropic SDK, `.env`, `claude-haiku-4-5`
- Streaming, system prompt, tarixçə, token sayğacı, `/reset`
- Öyrəndiklərim: API stateless-dir; tarixçə hər sorğuda yenidən ödənilir (xərc kvadratik artır); sliding window `history[-11:]` (tək rəqəm ki, ilk mesaj həmişə user olsun)
- Həll yolları: sliding window, summarization, prompt caching, RAG
