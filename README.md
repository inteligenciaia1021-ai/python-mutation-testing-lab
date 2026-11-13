# Python Mutation Testing Lab

A practical Python project demonstrating automated testing, mutation testing, code coverage analysis, and continuous integration using **pytest**, **pytest-cov**, and **GitHub Actions**.

## Overview

This project implements a discount calculation function and a custom mutation testing script to evaluate whether automated tests can detect intentional code changes.

The goal is to demonstrate how mutation testing can reveal weaknesses in a test suite that ordinary test execution may not identify.

The project also integrates code coverage analysis and an automated CI pipeline to validate code quality whenever changes are pushed to GitHub.

## Technologies

- Python 3.13
- Pytest
- Pytest-cov
- Coverage.py
- Git
- GitHub
- GitHub Actions (CI)

## Project Structure

```text
python-mutation-testing-lab/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── desconto.py
├── test_desconto.py
├── mutar.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Features

- Discount calculation with input validation.
- Automated unit tests using pytest.
- Custom mutation testing script.
- Isolated execution of mutated code using temporary directories.
- Detection of killed and surviving mutants.
- Automatic mutation testing report.
- Code coverage measurement using pytest-cov.
- Minimum coverage enforcement (100%).
- Continuous integration with GitHub Actions.
- Automated test execution on pushes and pull requests targeting the main branch.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/inteligenciaia1021-ai/python-mutation-testing-lab.git

cd python-mutation-testing-lab
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run unit tests

```bash
python -m pytest -q
```

### 6. Run tests with coverage

```bash
python -m pytest --cov=desconto --cov-report=term-missing --cov-fail-under=100 -q
```

### 7. Run mutation testing

```bash
python mutar.py
```

## Test Results

Current project results:

| Metric | Result |
|---|---:|
| Unit tests passed | 6 |
| Code coverage | 100% |
| Executable statements | 4 |
| Uncovered statements | 0 |
| Mutants tested | 4 |
| Mutants killed | 4 |
| Mutants survived | 0 |
| Mutation execution errors | 0 |
| Mutation score | **100%** |

## Mutation Testing

The project currently includes four intentional mutations:

| Mutation | Expected behavior |
|---|---|
| Change `>` to `>=` | Detected |
| Change `<` to `<=` | Detected |
| Add 1 to the calculation result | Detected |
| Change the exception message | Detected |

### Mutation Score

The mutation score is calculated as:

```text
Mutation Score =
Killed Mutants / (Killed Mutants + Survived Mutants) × 100
```

The experiment achieved a mutation score of **100%**, with all four implemented mutations detected by the test suite.

This result applies only to the mutations included in this educational experiment. It does not guarantee that the application is free of defects.

## Code Coverage

Code coverage is measured using pytest-cov.

The current test suite achieves **100% statement coverage** for `desconto.py`.

A minimum coverage threshold of 100% is enforced in the automated CI pipeline.

Coverage measures which executable statements were exercised during testing. It does not independently guarantee that all possible behaviors are correct.

## Continuous Integration

This project uses GitHub Actions to automatically validate changes.

The workflow is triggered by:

- Pushes to the `main` branch.
- Pull requests targeting the `main` branch.

The CI pipeline performs the following steps:

1. Checks out the repository.
2. Sets up Python 3.13.
3. Installs project dependencies from `requirements.txt`.
4. Runs unit tests and checks code coverage.
5. Enforces the minimum coverage threshold.
6. Executes the custom mutation testing script.

The workflow fails if a required test or coverage check fails.

## Learning Objectives

This project demonstrates practical knowledge of:

- Python fundamentals.
- Unit testing.
- Test assertions and exception handling.
- Mutation testing concepts.
- Code coverage analysis.
- Automated test execution.
- Continuous integration.
- Git and GitHub workflows.
- Test quality evaluation.

## Future Improvements

- Generate HTML and JSON test reports.
- Add more mutation operators.
- Improve mutation execution error classification.
- Expand the test suite with additional scenarios.
- Introduce branch coverage analysis.
- Improve CI reporting and test visualization.

## Author

Developed as a practical software testing and Python learning project.

**Python | Automated Testing | Mutation Testing | Code Coverage | CI/CD**