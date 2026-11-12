def calculate_keyword_score( clause: dict, search_terms: list[str]) -> int:
    """
    Count how many search terms occur in a clause.
    """
    searchable_text = (
        clause["title"] + " " + clause["text"]
    ).lower()

    score = 0

    for term in search_terms:
        if term.lower() in searchable_text:
            score += 1

    return score

def retrieve_top_clauses(requirement: dict, clauses: list[dict], top_k: int = 2) -> list[dict]:
    """
    Retrieve the highest-scoring clauses for one requirement.

    Clauses with no keyword matches are excluded.
    """
    if top_k < 1:
        raise ValueError("top_k must be at least 1.")

    ranked_results = []

    for clause in clauses:
        score = calculate_keyword_score(clause=clause, search_terms=requirement["search_terms"])

        if score > 0:
            ranked_results.append(
                {
                    "clause": clause,
                    "score": score,
                }
            )

    ranked_results.sort(
        key=lambda result: result["score"],
        reverse=True,
    )

    return ranked_results[:top_k]

def retrieve_best_clause(requirement: dict, clauses: list[dict]) -> dict | None:
    """
    Retrieve the single highest-scoring clause.
    Kept as a convenience function for code that needs one result.
    This is a compatibility wrapper.
    It prevents existing code from breaking while allowing new code to use top-k retrieval.
    That is a safer refactoring approach than immediately removing an existing function.
    """
    results = retrieve_top_clauses(
        requirement=requirement,
        clauses=clauses,
        top_k=1,
    )

    if not results:
        return None

    return results[0]