import os
from pypdf import PdfReader


def get_document_paths():

    folders = [
        "knowledge/rbi_reports",
        "knowledge/npci_reports",
        "knowledge/phonepe_docs",
        "knowledge/fintech_reports"
    ]

    documents = []

    for folder in folders:

        if os.path.exists(folder):

            for file in os.listdir(folder):

                documents.append(
                    os.path.join(folder, file)
                )

    return documents


def load_pdf_text(file_path):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:

        text += page.extract_text()

    return text