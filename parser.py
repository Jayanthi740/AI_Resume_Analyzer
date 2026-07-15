# parser.py

import PyPDF2


def extract_text_from_pdf(file_path):
    """
    Extract text from PDF resume
    """

    text = ""

    try:
        with open(file_path, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)

            for page in pdf_reader.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text

        return text

    except Exception as e:
        print("Error reading PDF:", e)
        return ""