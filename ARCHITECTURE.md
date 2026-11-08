# Project Architecture

## Purpose

The Islamic Finance Contract Review Assistant performs preliminary,
evidence-based review of Murabaha contracts against a defined checklist.

It does not issue a final Shariah ruling. It identifies evidence,
missing information, and cases requiring professional review.

## Processing Pipeline

1. A contract is loaded from a text file or text-based PDF.
2. PDF text is extracted page by page.
3. The contract is parsed into structured clauses.
4. Review requirements are loaded from a JSON checklist.
5. Relevant clauses are retrieved for each requirement.
6. A review engine evaluates the retrieved evidence.
7. Structured findings are returned with reasons and citations.
8. Results are compared with expected results during evaluation.

## Module Responsibilities

### `document_loader.py`

- Loads plain-text contracts.
- Extracts the document ID.
- Parses the contract into clauses.
- Validates that clauses were detected.

### `pdf_loader.py`

- Opens text-based PDF contracts.
- Extracts text page by page.
- Preserves page information.
- Passes extracted text to the clause parser.
- Detects PDFs that may require OCR.

### `checklist_loader.py`

- Loads review requirements from JSON.
- Validates required checklist fields.

### `evidence_retriever.py`

- Searches clauses for evidence relevant to each requirement.
- Currently provides a transparent keyword-based baseline.
- Does not make a compliance decision.

### Future `review_engine.py`

- Evaluates whether retrieved evidence satisfies a requirement.
- Produces evidence_found, evidence_missing, or requires_review.
- Does not issue a final Shariah ruling.

### Future `evaluation.py`

- Compares system output with manually defined expected results.
- Measures retrieval and classification performance separately.

### Future `app.py`

- Provides the user interface.
- Accepts uploaded contracts.
- Displays structured findings and supporting evidence.

## Current Scope

- Murabaha contracts only.
- English documents only.
- Text and text-based PDF files.
- Five educational prototype requirements.
- Synthetic contracts rather than confidential real-world documents.

## Known Limitations

- Scanned PDFs are not yet supported.
- Clause-heading formats are controlled.
- PDF clauses do not yet contain precise page citations.
- Keyword retrieval does not understand meaning or negation.
- Checklist requirements have not been presented as an official
  Shariah compliance standard.