from pathlib import Path

from pypdf import PdfReader

from document_loader import (
    extract_clauses,
    extract_document_id,
)


def extract_pdf_pages(file_path: Path) -> list[dict]:
    """
    Extract text from a text-based PDF page by page.
    """
    if not file_path.exists():
        raise FileNotFoundError(
            f"PDF file not found: {file_path.resolve()}"
        )

    if file_path.suffix.lower() != ".pdf":
        raise ValueError("The supplied file must be a PDF.")

    reader = PdfReader(file_path)
    pages = []

    for page_number, page in enumerate(
        reader.pages,
        start=1,
    ):
        page_text = page.extract_text(extraction_mode="layout")

        if page_text:
            page_text = page_text.strip()
        else:
            page_text = ""

        pages.append(
            {
                "page_number": page_number,
                "text": page_text,
            }
        )

    if not any(page["text"] for page in pages):
        raise ValueError(
            "No text was extracted from the PDF. "
            "The document may be scanned and require OCR."
        )

    return pages

def combine_page_text(pages: list[dict]) -> str:
    """
    Combine extracted PDF pages into one text string.
    """
    page_texts = []

    for page in pages:
        if page["text"]:
            page_texts.append(page["text"])

    return "\n\n".join(page_texts)

def process_pdf_contract(file_path: Path) -> dict:
    """
    Extract and structure a text-based PDF contract.
    """
    pages = extract_pdf_pages(file_path)
    contract_text = combine_page_text(pages)

    document_id = extract_document_id(contract_text)
    clauses = extract_clauses(contract_text)

    return {
        "document_id": document_id,
        "source": file_path.name,
        "file_type": "pdf",
        "page_count": len(pages),
        "pages": pages,
        "clauses": clauses,
    }