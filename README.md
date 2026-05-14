# Job Description Analyzer

A tool that analyzes job descriptions to identify key skills and compare them against a predefined skill set.

## Overview

Job descriptions are often long and inconsistent. This tool helps quickly identify relevant skills and evaluate how well they match a known skill set.

## Features

- Parses job description text from a file
- Identifies matching skills based on keyword detection
- Highlights missing skills
- Calculates a match score based on relevant skills found in the job description
- Provides a simple match summary (Strong / Moderate / Weak)

## How to Run

### Requirements

- Python 3.11+

### Run

Analyze all files in the `sample_jobs` folder:

```bash
python analyzer.py
```

Analyze a specific file:

```bash
python analyzer.py path/to/job.txt
```

## Setup

Copy the example skills file and update it with your own skills:

```bash
cp user_skills.example.py user_skills.py
```

`user_skills.py` is gitignored and will never be committed.

## Customization

### Add or update your skills

Edit `USER_SKILLS` in `user_skills.py` to reflect your own skill set.

### Expand the skill catalog

Edit `JOB_SKILLS` in `job_skills.py` to add new skills or keyword synonyms.

## Example Output

> Output reflects partial skill set

```
=== Analyzing: embedded_software_eng_sample.txt ===

Relevant Job Skills:
- Python
- C++
- Debugging
- Root Cause Analysis
- Test Automation

Matched Skills:
- Debugging
- Root Cause Analysis
- Test Automation

Missing Skills:
- Python
- C++

Match Score: 60.0%
Summary: Moderate match

----------------------------------------

=== Analyzing: senior_software_engineer_sample.txt ===

Relevant Job Skills:
- Python
- C++
- JavaScript
- Debugging

Matched Skills:
- Debugging

Missing Skills:
- Python
- C++
- JavaScript

Match Score: 25.0%
Summary: Weak match

----------------------------------------

=== Analyzing: software_dev_sample.txt ===

Relevant Job Skills:
- C++
- SQL
- Debugging
- Object-Oriented Programming

Matched Skills:
- Debugging
- Object-Oriented Programming

Missing Skills:
- C++
- SQL

Match Score: 50.0%
Summary: Moderate match

----------------------------------------
```
