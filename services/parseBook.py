from io import BytesIO
import requests
from pdfminer.high_level import extract_text


def fetch_parse_book(url):
    response = requests.get(url)
    response.raise_for_status()

    pdf_data = BytesIO(response.content)
    text = extract_text(pdf_data)


    print(text)
