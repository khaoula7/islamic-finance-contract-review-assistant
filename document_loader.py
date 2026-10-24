from pathlib import Path
import re


def load_contract(file_path: Path) -> str:
    """
    Load a plain-text contract.

    Args:
        file_path: Path to the contract file.

    Returns:
        The complete contract text.
    """
    if not file_path.exists():
        raise FileNotFoundError(
            f"Contract file not found: {file_path.resolve()}"
        )

    if file_path.suffix.lower() != ".txt":
        raise ValueError("Only .txt contracts are supported currently.")

    contract_text = file_path.read_text(encoding="utf-8").strip()

    if not contract_text:
        raise ValueError("The contract file is empty.")

    return contract_text


def extract_document_id(contract_text: str) -> str | None:
    """
    Extract the document ID from the contract text.
    """
    match = re.search(
        r"Document ID:\s*(.+)",
        contract_text,
        flags=re.IGNORECASE,
    )

    if match:
        return match.group(1).strip()

    return None


def extract_clauses(contract_text: str) -> list[dict]:
    """
    Split a contract into structured clauses.

    Expected heading format:
    Clause 1 — Parties
    """
    clause_pattern = re.compile(
        r"^Clause\s+(\d+)\s*[—-]\s*(.+)$",
        flags=re.MULTILINE | re.IGNORECASE,
    )

    matches = list(clause_pattern.finditer(contract_text))
    clauses = []

    for index, match in enumerate(matches):
        clause_id = match.group(1)
        title = match.group(2).strip()

        text_start = match.end()

        if index + 1 < len(matches):
            text_end = matches[index + 1].start()
        else:
            text_end = len(contract_text)

        clause_text = contract_text[text_start:text_end].strip()

        clauses.append(
            {
                "clause_id": clause_id,
                "title": title,
                "text": clause_text,
            }
        )

    return clauses


def process_contract(file_path: Path) -> dict:
    """
    Load a contract and return its structured representation.
    """
    contract_text = load_contract(file_path)
    document_id = extract_document_id(contract_text)
    clauses = extract_clauses(contract_text)

    return {
        "document_id": document_id,
        "source": file_path.name,
        "clauses": clauses,
    }