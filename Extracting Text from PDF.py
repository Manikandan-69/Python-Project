"""
Install a Python library known as PyPDF2.
"""

import PyPDF2

def extract_text_pdf(pdf_path):
    text=" "
    with open (pdf_path,"rb") as file:
        pdf_reader=PyPDF2.PdfReader(file) #Open pdf file
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

path="C:/Users/ManiKandan/Desktop/SQL_Scenarios.pdf"
final=extract_text_pdf(pdf_path=path)
print(final)