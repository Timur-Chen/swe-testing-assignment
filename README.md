# Quick-Calc (Python)

Quick-Calc is a simple calculator application developed for a Software Testing and Version Control assignment. 
The project demonstrates clean code structure, unit testing, integration testing, and proper Git/GitHub workflow.

The calculator supports:
- Addition
- Subtraction
- Multiplication
- Division (with safe handling of division by zero)
- Clear (C) operation


## Project Structure

- quick_calc/core.py – Core arithmetic logic (unit tested)
- quick_calc/app.py – Application layer simulating key presses (integration tested)
- tests/ – Unit and integration test files
- TESTING.md – Detailed explanation of testing strategy


## Setup Instructions (Windows)

1. Create virtual environment:

python -m venv .venv

2. Activate it:

.venv\Scripts\activate

3. Install dependencies:

pip install pytest


## How to Run Tests

Run all tests using:

pytest

If everything works correctly, you should see:

10 passed


## Example Usage

from quick_calc.app import QuickCalcApp

app = QuickCalcApp()

print(app.press("5"))
print(app.press("+"))
print(app.press("3"))
print(app.press("="))  # Output: 8


## Testing Framework Research: Pytest vs Unittest

Python provides a built-in testing framework called unittest. It uses a class-based structure and predefined assertion methods. Because it is included in Python’s standard library, it does not require installation and is reliable for basic test cases. However, the syntax can be more verbose and less readable for small projects.

pytest is a modern and widely used third-party testing framework. It allows writing shorter and more readable test functions using simple assert statements. It also provides powerful features such as fixtures, parameterization, and detailed error reporting, which make debugging easier.

For this project, pytest was chosen because it produces cleaner test code, better readability, and faster development when writing both unit and integration tests.