from pathlib import Path
from checklist_loader import load_checklist
from document_loader import process_contract
from evidence_retriever import (
    retrieve_best_clause,
    retrieve_top_clauses,
)


CONTRACT_PATH = Path(
    "sample_contracts/murabaha_complete.txt"
)

CHECKLIST_PATH = Path(
    "data/murabaha_checklist.json"
)

def find_requirement(checklist: list[dict], requirement_id: str) -> dict:
    """
    Find one requirement by its ID.
    """
    for requirement in checklist:
        if requirement["id"] == requirement_id:
            return requirement

    raise ValueError(
        f"Requirement not found: {requirement_id}"
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

    #Multi-clause requirement
    mur_05 = find_requirement(checklist=checklist, requirement_id="MUR-05")

    results = retrieve_top_clauses(requirement=mur_05, clauses=contract["clauses"], top_k=2)
    
    retrieved_clause_ids = {
        result["clause"]["clause_id"]
        for result in results
    }

    print("\nMUR-05 TOP RESULTS")

    for rank, result in enumerate(results, start=1):
        clause = result["clause"]

        print(
            f"Rank {rank}: "
            f"Clause {clause['clause_id']} — "
            f"{clause['title']} "
            f"(score: {result['score']})"
        )

    assert "5" in retrieved_clause_ids
    assert "6" in retrieved_clause_ids

    print("MUR-05 multi-clause retrieval passed.")

    unsupported_requirement = {
        "search_terms": [
            "takaful certificate number",
            "insurance policy reference",
        ]
    }
    # No evidence test
    results = retrieve_top_clauses(
        requirement=unsupported_requirement,
        clauses=contract["clauses"],
        top_k=2,
    )

    assert results == []

    print("No-evidence retrieval check passed.")

    


if __name__ == "__main__":
    main()