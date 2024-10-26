import os
import PyPDF2
import docx

def reader(file_path):
    """
    Reads and extracts text from PDF or DOCX files.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The extracted text or an error message.
    """
    _, file_extension = os.path.splitext(file_path)
    text = ""

    try:
        if file_extension.lower() == '.pdf':
            text = read_pdf(file_path)
        elif file_extension.lower() == '.docx':
            text = read_docx(file_path)
        else:
            return "Unsupported file format. Please provide a .pdf or .docx file."

        return text.strip() if text else "No text found"

    except Exception as e:
        return f"An error occurred: {str(e)}"

def read_pdf(file_path):
    """Extracts text from a PDF file."""
    text = ""
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() or ''
    except Exception as e:
        return f"Failed to read PDF file: {str(e)}"
    return text

def read_docx(file_path):
    """Extracts text from a DOCX file."""
    text = ""
    try:
        doc = docx.Document(file_path)
        for paragraph in doc.paragraphs:
            text += paragraph.text + '\n'
    except Exception as e:
        return f"Failed to read DOCX file: {str(e)}"
    return text