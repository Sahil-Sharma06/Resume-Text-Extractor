import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a given PDF file.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        str: Extracted text from the PDF.
    """
    text = ""  # Initialize an empty string for storing extracted text

    # Open the PDF file
    doc = fitz.open(pdf_path)

    # Iterate through each page in the document
    for page in doc:
        text += page.get_text("text") + "\n"  # Extract text from each page

    return text  # Return the extracted text
