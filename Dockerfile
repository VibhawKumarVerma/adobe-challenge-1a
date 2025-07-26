FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY pdf_outline_extractor.py .

ENTRYPOINT ["python", "pdf_outline_extractor.py"]
