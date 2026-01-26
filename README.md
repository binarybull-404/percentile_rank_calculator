# Percentile Rank & Pass/Fail Calculator (Python)

A command-line Python program that calculates **student percentages, pass/fail status, rankings, and percentiles** based on marks entered for multiple subjects.

The program supports multiple students, validates input marks, ranks students by percentage, and computes percentiles using rank-based calculation.

---

## Features
- Supports **multiple students and multiple subjects**
- Calculates **overall percentage** for each student
- **Subject-wise fail check** (less than 33%)
- **Overall fail check** (percentage ≤ 40%)
- Stores and displays **all student percentages**
- Sorts students by percentage in **descending order**
- Identifies the **highest scorer**
- Calculates **percentile ranks** for all students
- Input validation for invalid marks

---


## How the Program Works
1. User inputs:
   - Number of students
   - Number of subjects
   - Total marks per subject
2. For each student:
   - Marks are entered subject-wise
   - Invalid marks (negative or above total marks) are rejected
   - Overall percentage is calculated
   - Subject-level and overall pass/fail status is checked
3. All student percentages are stored
4. Percentages are sorted in descending order
5. Highest scorer is identified
6. Percentile for each student is calculated using rank-based formula

---

## Percentile Calculation Formula

- Percentile = ((Number of students - Rank) / Number of students) × 100
---

## Concepts Used
- Dictionaries
- Lists
- Loops (for / while)
- Conditional statements
- Sorting with lambda functions
- Input validation
- Basic statistics

---

## How to Run
```bash
python 02_pass_or_fail.py
```
## Example Output
```
Student 1 overall percentage is: 72.5 %
Student 2 overall percentage is: 65.0 %

Overall percentage of all students in descending order:
{'Student 1': 72.5, 'Student 2': 65.0}

Student 1 has secured the highest percentage of 72.5 %

Percentile of all students respectively:
{'Student 1': 100.0, 'Student 2': 50.0}
```
## Pass / Fail Criteria

- Subject-wise fail:
  - Less than 33% in any subject

- Overall fail:
  - Overall percentage ≤ 40%

## Code Structure Overview

- #### Uses lists to store subject marks

- #### Uses dictionaries to store:

  - Student percentages

  - Sorted rankings

  - Percentiles

- #### Sorting is done using `lambda` on percentage values
