# AI Engineer Roadmap (~21 həftə, həftədə 5-10 saat)

> "Gün" = bir iş sessiyası (~1.5-2 saat). Həftədə təxminən 3-5 gün.
> Hər mərhələ bir **lab** ilə bitir. Hər lab portfolio-ya düşür.
> **Git:** hər sessiyanın sonunda ən azı bir mənalı commit.

---

## Mərhələ 1 — LLM əsasları + API (həftə 1-2) ✅
**Lab 1: CLI chatbot** — `labs/lab-01-cli-chatbot/`
- [x] anthropic SDK, `.env` ilə API açarı
- [x] Streaming, system prompt
- [x] Söhbət tarixçəsi, token sayğacı, `/reset`
- [x] Sliding window (`history[-11:]`)

**Əsas dərslər:** API stateless-dir; tarixçə hər sorğuda yenidən ödənilir (xərc kvadratik artır).
Həll yolları: sliding window, summarization, prompt caching, RAG.

---

## Mərhələ 2 — Embeddings + RAG (həftə 3-6) ⏳ İNDİ BURADAYIQ
**Lab 2: PDF üzərində sual-cavab** — `labs/lab-02-rag/`
> Generasiya modeli: Lab 2-dən etibarən `claude-haiku-5-5` (Lab 1-də `claude-haiku-4-5` idi).

### Həftə 3 — Embeddings
- [x] PDF seçimi → `data/araz_bulud_emekdas_beledcisi.pdf` (Araz Bulud MMC Əməkdaş Bələdçisi)
- [x] Embedding nədir? Vektor, ölçü (dimension), semantik oxşarlıq
- [x] Cosine similarity — əllə (numpy) hesabla
- [x] Embedding modeli ilə ilk vektorlar (`gemini-embedding-001`, 768 ölçü, RETRIEVAL_QUERY/DOCUMENT)
- [ ] Mini axtarış: 10-20 cümlə arasında sorğuya ən yaxınını tap *(2 cümlə ilə edilib, genişləndirmək olar)*

### Həftə 4 — Chunking + Vector DB
- [x] PDF-dən mətn çıxarmaq (pypdf), footer təmizləmə
- [x] Chunking strategiyası: bənd (section) üzrə → 94 parça
- [x] Metadata: bənd nömrəsi, başlıq, bölmə *(səhifə nömrəsi yoxdur)*
- [ ] Chunking strategiyalarını müqayisə: sabit ölçü + overlap vs bənd üzrə (niyə bənd üzrə seçdin?)
- [ ] Chroma: kolleksiya yarat, chunk-ları yaz, sorğula

### Həftə 5 — Retrieval + Cavab + Mənbə
- [ ] Top-k retrieval → prompt-a kontekst kimi qoymaq
- [ ] Claude ilə cavab generasiyası (yalnız kontekstə əsaslan)
- [ ] Mənbə göstərmə (bənd nömrəsi ilə: `(Mənbə: 4.1, 10.2)`) *(system prompt hazırdır: `day-01-embeddings/prompts.py`)*
- [ ] "Bilmirəm" davranışı (kontekstdə yoxdursa) *(prompt-da var, test edilməyib)*
- [ ] CLI interfeys (Lab 1-dən təkrar istifadə)
- [ ] **Mini golden set:** 10-15 sual + gözlənilən cavab + gözlənilən bənd (`eval/golden.json`)

### Həftə 6 — Keyfiyyəti yaxşılaşdırmaq (rəqəmlərlə)
- [ ] Golden set üzərində baseline: neçə sualda düzgün bənd top-k-dadır?
- [ ] Uğursuz sualları analiz et (retrieval xətası, yoxsa generasiya xətası?)
- [ ] Chunk ölçüsü / overlap / k ilə eksperiment → nəticəni golden set ilə ölç
- [ ] Hybrid search (BM25 + vektor) və ya reranking
- [ ] Query rewriting
- [ ] README + nəticə cədvəli (baseline vs yaxşılaşdırılmış)

---

## Mərhələ 3 — Evals (həftə 7-8)
**Lab 3: Lab 2 üçün evaluation sistemi** — `labs/lab-03-evals/`
- [ ] Golden set-i 25-30 suala genişləndir (asan / çətin / cavabı olmayan suallar)
- [ ] Retrieval metrikləri: hit@k, MRR
- [ ] Cavab metrikləri: düzgünlük, faithfulness (LLM-as-judge)
- [ ] LLM-as-judge-ı yoxla: 10 cavabı əllə qiymətləndir, judge ilə nə qədər üst-üstə düşür?
- [ ] Eval runner skripti → nəticələr cədvəli (CSV/Markdown)
- [ ] Bir dəyişiklik et (məs. chunk ölçüsü) və eval ilə yaxşılaşmanı **sübut et**

---

## Mərhələ 4 — Structured output + Tool use + Agentlər + MCP (həftə 9-13)
**Lab 4: Alətlərdən istifadə edən agent** — `labs/lab-04-agents/`

### Structured output (2-3 gün)
- [ ] LLM-dən etibarlı JSON almaq (schema, validasiya — Pydantic)
- [ ] Extraction: sərbəst mətndən strukturlu məlumat çıxarmaq
- [ ] Xətalı JSON-u idarə etmək (retry, validasiya xətası)

### Tool use + Agentlər
- [ ] Tool use əsasları: tool tərifi (JSON schema), tool_use / tool_result dövrü
- [ ] Əl ilə agent loop yaz (framework-süz)
- [ ] RAG-ı tool kimi agentə qoş (Lab 2-dən)
- [ ] Çox addımlı tapşırıqlar, xəta idarəsi, max iterasiya
- [ ] Agent eval-ları (tapşırıq uğur faizi)

### MCP
- [ ] MCP nədir? Öz MCP server-ini yaz (məs. sənəd axtarışı)
- [ ] MCP server-i Claude Code / Claude Desktop-a qoş

### Framework müqayisəsi (2-3 gün)
- [ ] Öz agentini bir framework ilə yenidən yaz (LangGraph / LlamaIndex / Claude Agent SDK — birini seç)
- [ ] Müqayisə qeydi: nə qazandın, nə itirdin, framework nəyi gizlədir?

---

## Mərhələ 5 — Production (həftə 14-17)
**Lab 5: RAG/agent-i servisə çevirmək** — `labs/lab-05-production/`
- [ ] FastAPI endpoint-lər (`/ask`, `/ingest`), streaming cavab
- [ ] Prompt caching + cavab keşi
- [ ] **Tracing/observability:** Langfuse (və ya analoqu) — hər sorğu üçün retrieval → prompt → cavab → token → xərc
- [ ] Logging, latency ölçümü
- [ ] Xərc hesabatı və limitlər
- [ ] Təhlükəsizlik: prompt injection, input validasiya, PII
- [ ] Docker

---

## Mərhələ 6 — Capstone + İşə hazırlıq (həftə 18-21)
**Capstone layihə** — `capstone/`
- [ ] Mövzu seçimi (real problem, Lab 2-5-in birləşməsi)
- [ ] Arxitektura sənədi
- [ ] Implementasiya + eval-lar
- [ ] GitHub: təmiz README, arxitektura diaqramı, eval nəticələri
- [ ] Demo (video və ya canlı link)

**İşə hazırlıq**
- [ ] 1-2 texniki blog yazısı (məs. "Azərbaycanca RAG: nə öyrəndim")
- [ ] LLM system design sualları (məs. "RAG-ı 1M sənədə necə miqyaslayardın?")
- [ ] Layihəni 5 dəqiqəyə izah etmə məşqi
- [ ] CV / LinkedIn üçün qısa təsvir

---

## Bilərəkdən daxil edilməyənlər
- **Fine-tuning** — junior LLM mühəndis rolları üçün vacib deyil, vaxt aparır.
- **Dərin ML nəzəriyyəsi** (transformer riyaziyyatı, backprop) — maraq üçün oxumaq olar, hədəfin yolu deyil.
