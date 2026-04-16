# Job Description Analyzer

A tool that analyzes job descriptions to identify key skills and compare them against a predefined skill set.

## Overview

Job descriptions are often long and inconsistent. This tool helps quickly identify relevant skills and evaluate how well they match a known skill set.

## Features

- Parses job description text from a file
- Identifies matching skills based on keyword detection
- Highlights missing skills
- Calculates a basic match score
- Provides a simple match summary (Strong / Moderate / Weak)

## Example Output

```
Matched Skills:
- Python
- C++
- Debugging
- Root Cause Analysis
- Test Automation

Missing Skills:
- JavaScript
- SQL
- HTML
- CSS
- Git
- System Validation
- Object-Oriented Programming

Match Score: 41.7%
Summary: Moderate match
```

## How to Run

### Requirements

- Python 3.11+

### Run

```bash
python analyzer.py
```
