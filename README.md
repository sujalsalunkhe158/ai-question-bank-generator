# Pattern-Based Question Bank Generator

A React prototype for organizing questions, analyzing a sample previous-paper pattern, generating a draft paper, and printing/saving it as PDF.

## Features
- Add and delete questions with unit, marks, type, and difficulty metadata
- Search and filter questions
- View sample unit-wise pattern analysis
- Generate a draft paper with a target mark total and avoid questions flagged as previously asked
- Replace a question with a compatible unused question
- Print or save the generated paper as PDF
- Store question edits in browser localStorage

## Run locally
1. Install Node.js.
2. Run `npm install`.
3. Run `npm run dev`.
4. Open the URL printed by Vite.

## Limitations
This prototype uses structured sample data and deterministic rules. It does not parse uploaded PDFs or use a trained NLP model. Generated papers require faculty review.
