from summarizer import summarize_text
from relevance import calculate_relevance
import os
import PyPDF2

def extract_text_from_pdfs(files):
    text = ""
    for file in files:
        with open(file.name, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text()
    return text

def search_engine(query, files):
    text = extract_text_from_pdfs(files)
    summary = summarize_text(text)
    relevance = calculate_relevance(query, text)
    return summary, relevance

if __name__ == "__main__":
    query = "Example search query"
    # Load example PDFs
    files = [open("pdf1/Heart Disease Prediction Using Binary Classification.pdf", "rb")]
    summary, relevance = search_engine(query, files)
    print("Summary:", summary)
    print("Relevance Score:", relevance)

