from io import BytesIO
import requests
from pdfminer.high_level import extract_text


def fetch_parse_book(uri):
    """
    Fetches and parses pdf book.

    :param uri: URI to PDF book.
    :return: Parsed book content.
    """
    response = requests.get(uri)
    response.raise_for_status()

    pdf_data = BytesIO(response.content)
    text = extract_text(pdf_data)
    return text