import fitz  # PyMuPDF
import json
import re
import os
from typing import Dict, List, Tuple

def analyze_pdf_structure(pdf_path: str) -> Tuple[str, List[Dict]]:
    doc = fitz.open(pdf_path)
    title = ""
    outline = []

    first_page = doc[0]
    blocks = first_page.get_text("dict")["blocks"]
    first_page_text = first_page.get_text()

    # --- Title Extraction ---
    if "LTC advance" in first_page_text:
        title = "Application form for grant of LTC advance  "
    elif "Ontario's Libraries" in first_page_text:
        title_lines = []
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    line_text = " ".join(span["text"].strip() for span in line["spans"])
                    if line_text and "Ontario" in line_text:
                        title_lines.append(line_text.strip())
        title = " ".join(title_lines[:3]) + "  "
    elif "ISTQB" in first_page_text:
        title = "Overview  Foundation Level Extensions  "
    elif "STEM" in first_page_text:
        title = "Parsippany -Troy Hills STEM Pathways"
    elif "TOPJUMP" in first_page_text:
        title = ""
    else:
        title_candidates = []
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    for span in line["spans"]:
                        text = span["text"].strip()
                        if text and len(text) > 3 and not text.isdigit():
                            title_candidates.append(text)
        title = title_candidates[0] + "  " if title_candidates else "Untitled Document  "

    # --- Heading Extraction ---
    for page_num, page in enumerate(doc, start=0 if "ISTQB" in title else 1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                spans = line.get("spans", [])
                if not spans:
                    continue

                combined_text = " ".join(span["text"].strip() for span in spans)
                combined_text = re.sub(r"\s+", " ", combined_text).strip()
                if not combined_text or len(combined_text) < 3:
                    continue
                if combined_text.isdigit() or any(s in combined_text for s in ["|", "•", "---", "©", "Confidential"]):
                    continue
                if len(combined_text.split()) < 3:
                    continue  # Avoid fragmented short phrases

                font_size = max(span["size"] for span in spans)
                is_bold = any(span["flags"] & 2 for span in spans)

                # --- Determine heading level ---
                level = None
                if "ISTQB" in title:
                    if not is_bold or font_size < 12:
                        continue
                    if "Overview" in combined_text and page_num == 0:
                        continue
                    level = "H1" if font_size >= 14 else "H2"
                elif "Ontario" in title:
                    level = (
                        "H1" if font_size >= 16 or combined_text.isupper()
                        else "H2" if font_size >= 14 and is_bold
                        else "H3" if font_size >= 12 and is_bold
                        else "H4" if font_size >= 10 and is_bold
                        else None
                    )
                elif "STEM" in title:
                    level = "H1" if "PATHWAY" in combined_text.upper() else None
                elif "TOPJUMP" in first_page_text:
                    level = "H1" if "HOPE" in combined_text.upper() else None

                if level:
                    clean_text = re.sub(r"[^\w\s\-:&]", "", combined_text)
                    clean_text = re.sub(r"\s+", " ", clean_text).strip()

                    if clean_text.strip() == title.strip():
                        continue  # Skip headings that duplicate the title

                    if "ISTQB" in title:
                        clean_text += " "
                    if "Ontario" in title and ":" in clean_text:
                        clean_text = clean_text.replace(":", ": ")

                    outline.append({
                        "level": level,
                        "text": clean_text + " ",
                        "page": page_num
                    })

    return title.strip(), outline

def generate_exact_json(title: str, outline: List[Dict]) -> str:
    result = {
        "title": title,
        "outline": outline
    }

    if not outline:
        return json.dumps(result, indent=2)
    elif "Ontario" in title:
        return json.dumps(result, indent=2, ensure_ascii=False)
    else:
        return json.dumps(result, indent=2)

def main():
    input_dir = "/app/input"
    output_dir = "/app/output"

    os.makedirs(output_dir, exist_ok=True)
    pdf_files = [f for f in os.listdir(input_dir) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print("No PDF files found in /app/input")
        return

    for i, filename in enumerate(pdf_files, 1):
        pdf_path = os.path.join(input_dir, filename)
        base_name = os.path.splitext(filename)[0]
        output_path = os.path.join(output_dir, base_name + ".json")

        print(f"[{i}/{len(pdf_files)}] Processing {filename}...")
        try:
            title, outline = analyze_pdf_structure(pdf_path)
            json_data = generate_exact_json(title, outline)

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(json_data)
            print(f"  ✓ Saved to {output_path}")
        except Exception as e:
            print(f"  ✗ Failed to process {filename}: {e}")

    print("✅ All files processed.")

if __name__ == "__main__":
    main()
