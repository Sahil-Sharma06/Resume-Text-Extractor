import fitz  # PyMuPDF
import re
import pdfplumber
import nltk

nltk.download('punkt')

# Define common resume section headings
RESUME_HEADINGS = [
    "Name", "Contact", "Summary", "Education", "Experience",
    "Projects", "Skills", "Certifications", "Languages"
]

def extract_text_from_pdf(pdf_path):
    """Extracts text from a given PDF file."""
    text = ""

    # Use pdfplumber for better text extraction
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"

    return text if text else "No text found"

def extract_sections(text):
    """Extracts sections from resume text based on keywords (headings)."""
    structured_resume = {}
    lines = text.split("\n")

    current_section = None

    for line in lines:
        line = line.strip()

        # Match if the line is a known heading (case-insensitive)
        if any(re.match(rf"^{heading}", line, re.IGNORECASE) for heading in RESUME_HEADINGS):
            current_section = line.strip(":")  # Normalize heading
            structured_resume[current_section] = []
        elif current_section:
            structured_resume[current_section].append(line)

    # Convert lists to strings
    for key in structured_resume:
        structured_resume[key] = "\n".join(structured_resume[key])

    return structured_resume

def extract_structured_resume(pdf_path):
    """Extracts structured resume data from a PDF."""
    raw_text = extract_text_from_pdf(pdf_path)
    return extract_sections(raw_text)
