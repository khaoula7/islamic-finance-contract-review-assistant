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


def retrieve_best_clause(requirement: dict, clauses: list[dict]) -> dict | None:
    """
    Return the clause with the highest keyword score.
    """
    ranked_clauses = []

    for clause in clauses:
        score = calculate_keyword_score(
            clause=clause,
            search_terms=requirement["search_terms"],
        )

        ranked_clauses.append(
            {
                "clause": clause,
                "score": score,
            }
        )

    ranked_clauses.sort(
        key=lambda result: result["score"],
        reverse=True,
    )

    best_result = ranked_clauses[0]

    if best_result["score"] == 0:
        return None

    return best_result