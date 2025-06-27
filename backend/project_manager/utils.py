from PyPDF2 import PdfReader


def extract_pdf_text(document):
    pdf_text=''
    
    if document:
        reader = PdfReader(document)
        for page in reader.pages:
            pdf_text += page.extract_text()
        return pdf_text
    else:
        return False