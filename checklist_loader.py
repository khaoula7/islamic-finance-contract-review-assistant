from pathlib import Path
import json


def load_checklist(file_path: Path) -> list[dict]:
    """
    Load and validate a contract-review checklist.
    """
    if not file_path.exists():
        raise FileNotFoundError(
            f"Checklist not found: {file_path.resolve()}"
        )

    with file_path.open("r", encoding="utf-8") as file:
        checklist = json.load(file)

    if not isinstance(checklist, list):
        raise ValueError("The checklist must contain a JSON list.")

    if not checklist:
        raise ValueError("The checklist is empty.")

    required_fields = {
        "id",
        "title",
        "review_question",
        "evidence_expected",
        "evidence_scope",
        "search_terms",
    }

    for requirement in checklist:
        missing_fields = required_fields - requirement.keys()

        if missing_fields:
            raise ValueError(
                f"Requirement {requirement.get('id', 'unknown')} "
                f"is missing fields: {sorted(missing_fields)}"
            )

    return checklist