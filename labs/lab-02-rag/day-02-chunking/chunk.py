import json
import re
from pypdf import PdfReader

PDF = "../data/araz_bulud_emekdas_beledcisi.pdf"

# 1) Üz qabığı və mündəricatı (ilk 2 səhifə) atırıq, qalan səhifələri birləşdiririk
reader = PdfReader(PDF)
text = "\n".join(page.extract_text() for page in reader.pages[2:])

# 2) Hər səhifədə təkrarlanan footer-i silirik
text = re.sub(r"^Araz Bulud MMC — Əməkdaş Bələdçisi · Versiya .*\nSəhifə \d+\n", "", text, flags=re.MULTILINE)

# 3) Sətir-sətir gəzib bəndlərə bölürük
chunks = []
chapter_no, chapter_title, current = None, "", None

for line in text.split("\n"):
    line = line.strip()
    chapter = re.match(r"^(\d+)\. (.+)$", line)          # məs: "4. Əmək haqqı və bonuslar"
    section = re.match(r"^(\d+)\.(\d+) (.+)$", line)     # məs: "4.1 Ödəniş tarixləri"

    if chapter and int(chapter[1]) == (chapter_no or 0) + 1:
        chapter_no, chapter_title, current = int(chapter[1]), chapter[2], None
    elif section and int(section[1]) == chapter_no:
        current = {"number": f"{section[1]}.{section[2]}", "title": section[3],
                   "chapter": f"{chapter_no}. {chapter_title}", "lines": []}
        chunks.append(current)
    elif current is None:
        chapter_title += " " + line      # bölmə başlığı iki sətrə sığmayıbsa
    elif line:
        current["lines"].append(line)

# 4) Sətir qırılmalarını düzəldib yekun mətni yığırıq: bölmə başlığı + bənd başlığı + məzmun
for c in chunks:
    body = " ".join(c.pop("lines"))
    c["text"] = f'{c["chapter"]} > {c["number"]} {c["title"]}\n{body}'

with open("chunks.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f, ensure_ascii=False, indent=2)

print(len(chunks), "parça")
for c in chunks:
    print(c["number"], "|", c["title"], "|", len(c["text"]))
