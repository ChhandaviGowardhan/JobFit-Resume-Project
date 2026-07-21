import PyPDF2

def extract_text_from_pdf(pdf_file):
    text = ""

    pdf_reader = PyPDF2.PdfReader(pdf_file)

    for page in pdf_reader.pages:
        extracted_text = page.extract_text()
        
        if extracted_text:
            text += extracted_text + "\n"

    return text