# TESTING.md — Quick-Calc Testing Strategy

## Testing Strategy Overview
This project applies a layered testing approach:
- Unit tests target the pure calculation logic in quick_calc/core.py.
- Integration tests verify the interaction between the input layer (QuickCalcApp) and the core calculator logic.

The goal is to maximize fast feedback with unit tests and validate real usage scenarios with a smaller number of integration tests.

---

## What Is Tested

### Unit Tests (Calculator Core)
Covered operations:
- Addition
- Subtraction
- Multiplication
- Division

Edge cases:
- Division by zero (raises ZeroDivisionError in core)
- Negative numbers
- Decimal numbers
- Very large numbers

These tests ensure correctness of individual methods in isolation.

### Integration Tests (App + Core Interaction)
Covered scenarios:
- Simulated user flow: 5 + 3 = returns 8
- Clear behavior: pressing C resets the display to 0

These tests validate that components work correctly together.

---

## What Is Not Tested (and Why)

- No graphical UI testing (GUI is not required in this assignment).
- No non-functional testing such as performance, security, or usability.
- No concurrency or stress testing (application is simple and single-user).

The project focuses on functional correctness.

---

## Relation to Lecture Concepts

### 1) Testing Pyramid
The test suite follows the Testing Pyramid principle:
- Majority are unit tests (fast, isolated).
- A smaller number are integration tests (validate component interaction).

This balance improves maintainability and fast execution.

### 2) Black-box vs White-box Testing
- Unit tests are mostly white-box: methods are tested directly with known internal behavior.
- Integration tests are closer to black-box: simulate external input (key presses) and verify output without checking internal variables.

### 3) Functional vs Non-Functional Testing
This project focuses on functional testing:
- Correct arithmetic results
- Correct state transitions
- Correct error handling

Non-functional requirements are intentionally out of scope.

### 4) Regression Testing
The current test suite acts as regression protection.  
If the code is refactored or extended (e.g., adding new operations), running pytest will reveal if existing functionality is broken.

---

## Test Results Summary

| Test Name                    | Type        | Status |
|-----------------------------|------------|--------|
| test_addition               | Unit        | Pass   |
| test_subtraction            | Unit        | Pass   |
| test_multiplication         | Unit        | Pass   |
| test_division               | Unit        | Pass   |
| test_division_by_zero       | Unit        | Pass   |
| test_negative_numbers       | Unit        | Pass   |
| test_decimal_numbers        | Unit        | Pass   |
| test_large_numbers          | Unit        | Pass   |
| test_full_addition_flow     | Integration | Pass   |
| test_clear_resets_display   | Integration | Pass   |