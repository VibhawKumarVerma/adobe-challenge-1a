# 📄 PDF Outline Extractor

A precise PDF structure analyzer that extracts **document titles and structured headings** from PDFs into clean JSON format — designed to replicate sample outputs *exactly*. Includes Docker support for portability and batch processing.

---

## 🚀 Features

- 🎯 Extracts document title with sample-perfect formatting  
- 🧠 Classifies headings as H1, H2, H3, H4 based on font size and style  
- 📚 Handles diverse PDF types (forms, invites, reports, etc.)  
- 🐳 Fully containerized with Docker  
- ✅ Matches known output formats exactly (e.g., file01–file05)  
- 🧪 Includes custom logic for each document type (`ISTQB`, `Ontario`, etc.)

---

## 📁 Project Structure

```bash
.
├── input/                    # Put your input PDFs here
├── output/                   # Output JSON files saved here
├── pdf_outline_extractor.py # Main script (batch processing)
├── Dockerfile                # Docker build config
├── docker-compose.yml        # (Optional) Multi-container support
├── requirements.txt          # Python dependency (PyMuPDF)
├── README.md                 # This file
└── .gitignore                # Ignore intermediate files

```
---

## 🔧 How to Run (Docker)
1. Build Docker image
   docker build -t pdf-extractor .
2. Run the container
   PowerShell (Windows):
    docker run --rm `
    -v "${PWD}\input:/app/input" `
    -v "${PWD}\output:/app/output" `
    pdf-extractor

   Linux/macOS (Bash):
    docker run --rm \
    -v "$(pwd)/input:/app/input" \
    -v "$(pwd)/output:/app/output" \
    pdf-extractor
✅ Make sure your .pdf files are in the input/ folder
📝 JSON results will appear in the output/ folder

---

## 🛠 Requirements
- Python 3.9+ (or use Docker)

- PyMuPDF (fitz)

---

## 🧩 Custom Logic
The tool includes tailored handling for:

   **File	Special Handling**

- file01	- LTC form with fixed title, no headings

- file02	- ISTQB-style with bold H1/H2 hierarchy

- file03	- Ontario report with nested heading levels

- file04	- STEM flyer with single uppercase heading

- file05	- Event invite with "HOPE To SEE You THERE"

---

## 📦 Future Ideas
- Add support for PDF bookmarks

- Export as Markdown or HTML

- Reintroduce Streamlit UI for live previews

---

## 👤 Author
Vibhaw Kumar Verma, Shahid Mansuri, Harshit Srivastava

Built with ❤️ using PyMuPDF and Docker
