:::writing{variant="document" id="73519"}
# Python Mutation Testing Lab

A practical Python project demonstrating automated testing, mutation testing, and test quality evaluation using **pytest**.

## Overview

This project implements a simple discount calculation function and a custom mutation testing script to evaluate whether automated tests can detect intentional code changes.

The goal is to demonstrate how mutation testing can reveal weaknesses in a test suite that ordinary test execution may not identify.

## Technologies

- Python
- Pytest
- Git
- GitHub

## Project Structure

```text
python-mutation-testing-lab/
│
├── desconto.py
├── test_desconto.py
├── mutar.py
├── README.md
└── .gitignore
```

## Features

- Discount calculation with input validation.
- Automated unit tests using pytest.
- Custom mutation testing script.
- Isolated execution of mutated code using temporary directories.
- Detection of surviving and killed mutants.
- Automatic mutation testing report.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/inteligenciaia1021-ai/python-mutation-testing-lab.git
cd python-mutation-testing-lab
```

Replace `https://github.com/inteligenciaia1021-ai/python-mutation-testing-lab.git` with your repository URL.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install pytest
```

### 4. Run the unit tests

```bash
python -m pytest -q
```

### 5. Run the mutation testing script

```bash
python mutar.py
```

## Mutation Testing Results

The project currently includes four intentional mutations:

| Mutation | Expected behavior |
|---|---|
| Change `>` to `>=` | Detected |
| Change `<` to `<=` | Detected |
| Add 1 to the calculation result | Detected |
| Change the exception message | Detected |

### Experimental Result

- Mutants tested: 4
- Mutants killed: 4
- Mutants survived: 0
- Execution errors: 0
- Mutation score: **100%**

The mutation score is calculated as:

```text
Mutation Score = Killed Mutants / (Killed Mutants + Survived Mutants) × 100
```

This result applies to the four mutations implemented in this educational experiment. It does not guarantee that the application is free of defects.

## Learning Objectives

This project demonstrates practical knowledge of:

- Python fundamentals.
- Unit testing.
- Test assertions and exception handling.
- Mutation testing concepts.
- Automated test execution.
- Basic test quality analysis.
- Git and GitHub workflows.

## Future Improvements

- Generate reports in JSON or HTML.
- Add more mutation operators.
- Improve mutation execution error classification.
- Expand test coverage.
- Add continuous integration with GitHub Actions.

## Author

Developed as a practical software testing and Python learning project.

**Python | Automated Testing | Mutation Testing | Pytest**
:::