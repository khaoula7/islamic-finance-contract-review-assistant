from pathlib import Path

from pdf_loader import process_pdf_contract


PDF_PATH = Path(
    "sample_contracts/murabaha_complete.pdf"
)


def main():
    contract = process_pdf_contract(PDF_PATH)

    print(f"Document ID: {contract['document_id']}")
    print(f"Source: {contract['source']}")
    print(f"File type: {contract['file_type']}")
    print(f"Page count: {contract['page_count']}")
    print(f"Clauses detected: {len(contract['clauses'])}")

    for page in contract["pages"]:
        print("\n" + "=" * 60)
        print(f"PAGE {page['page_number']}")
        print(page["text"])

    assert contract["document_id"] == "MUR-COMPLETE-001"
    assert len(contract["clauses"]) == 7
    assert contract["clauses"][0]["title"] == "Parties"

    print("\nAll PDF extraction checks passed.")


if __name__ == "__main__":
    main()