# Islamic Finance Contract Review Assistant

An evidence-aware prototype that reviews synthetic Murabaha contracts
against a defined checklist and produces structured, traceable findings.

The system is designed to support preliminary review. It does not issue
a final Shariah ruling.

## Current Scope

The current prototype supports:

- English Murabaha contracts
- Plain-text and text-based PDF documents
- Five educational review requirements
- Clause-level document parsing
- Page-by-page PDF text extraction
- Keyword-based evidence retrieval
- Structured expected results for evaluation

The project currently uses synthetic contracts and an educational
checklist. The checklist should not be represented as an official
Shariah compliance standard.

## Review Statuses

The planned review output uses three statuses:

- `evidence_found`: sufficient supporting information was identified
- `evidence_missing`: required information is absent or insufficient
- `requires_review`: relevant information exists, but professional or
  external verification is required

## Test Contracts

The project includes three controlled Murabaha scenarios:

| Contract | Purpose |
|---|---|
| Complete | Required information is stated clearly |
| Incomplete | Some required information is absent |
| Ambiguous | Related wording exists, but it is insufficient for a confident result |

Each contract has manually defined expected results that will be used
to evaluate the review system.

## Processing Pipeline

1. Load a text or text-based PDF contract.
2. Extract text while preserving page information.
3. Parse the contract into structured clauses.
4. Load the Murabaha review checklist.
5. Retrieve clauses relevant to each requirement.
6. Evaluate the retrieved evidence.
7. Return structured findings with reasons and citations.
8. Compare the findings with expected results.


## Project Structure

```text
islamic-finance-contract-review-assistant/
├── data/
│   └── murabaha_checklist.json
├── sample_contracts/
│   ├── murabaha_complete.txt
│   ├── murabaha_complete.pdf
│   ├── murabaha_complete_expected.json
│   ├── murabaha_incomplete.txt
│   ├── murabaha_incomplete_expected.json
│   ├── murabaha_ambiguous.txt
│   └── murabaha_ambiguous_expected.json
├── schemas/
│   └── review_result_example.json
├── ARCHITECTURE.md
├── PROJECT_BRIEF.md
├── checklist_loader.py
├── document_loader.py
├── evidence_retriever.py
├── pdf_loader.py
├── test_document_loader.py
├── test_evidence_retriever.py
├── test_pdf_loader.py
├── requirements.txt
└── README.md
For detailed module responsibilities and design decisions, see ARCHITECTURE.md