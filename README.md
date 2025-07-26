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
---

