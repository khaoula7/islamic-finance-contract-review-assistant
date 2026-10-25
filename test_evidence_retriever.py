from pathlib import Path
from checklist_loader import load_checklist
from document_loader import process_contract
from evidence_retriever import retrieve_best_clause


CONTRACT_PATH = Path(
    "sample_contracts/murabaha_complete.txt"
)

CHECKLIST_PATH = Path(
    "data/murabaha_checklist.json"
)


def main():
    contract = process_contract(CONTRACT_PATH)
    checklist = load_checklist(CHECKLIST_PATH)

    for requirement in checklist:
        result = retrieve_best_clause(
            requirement=requirement,
            clauses=contract["clauses"],
        )

        print("\n" + "=" * 60)
        print(
            f"{requirement['id']}: "
            f"{requirement['title']}"
        )

        if result is None:
            print("No evidence candidate found.")
            continue

        clause = result["clause"]

        print(f"Best clause: Clause {clause['clause_id']}")
        print(f"Clause title: {clause['title']}")
        print(f"Keyword score: {result['score']}")
        print(f"Evidence: {clause['text']}")


if __name__ == "__main__":
    main()