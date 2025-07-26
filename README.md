# PDF Outline Extractor

Extracts structured outline (Title + H1, H2, H3 headings) from PDFs and outputs valid JSON files.

## 🔧 How it works

- Parses all PDFs in `/app/input`
- Uses font size to infer hierarchy:
  - Largest = H1
  - Next = H2
  - Next = H3
- Extracts title from largest text on page 1
- Outputs JSON to `/app/output`

## 🐳 Docker Build & Run

```bash
docker build --platform linux/amd64 -t mysolutionname:somerandomidentifier .

docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  mysolutionname:somerandomidentifier
