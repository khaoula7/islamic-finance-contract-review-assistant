from pathlib import Path

from document_loader import process_contract


CONTRACT_PATH = Path(
    "sample_contracts/murabaha_complete.txt"
)


def main():
    contract = process_contract(CONTRACT_PATH)

    print(f"Document ID: {contract['document_id']}")
    print(f"Source: {contract['source']}")
    print(f"Number of clauses: {len(contract['clauses'])}")

    for clause in contract["clauses"]:
        print("\n" + "-" * 50)
        print(
            f"Clause {clause['clause_id']} — "
            f"{clause['title']}"
        )
        print(clause["text"])
    
    assert contract["document_id"] == "MUR-COMPLETE-001"
    assert len(contract["clauses"]) == 7
    assert contract["clauses"][0]["clause_id"] == "1"
    assert contract["clauses"][0]["title"] == "Parties"
    assert "Amanah Finance Ltd." in contract["clauses"][0]["text"]

    print("\nAll document-loader checks passed.")


if __name__ == "__main__":
    main()