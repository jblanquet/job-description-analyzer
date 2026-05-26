import subprocess
import sys
import pytest
from pathlib import Path
from analyzer import (
    normalize_text,
    find_relevant_job_skills,
    compare_to_user_skills,
    calculate_match_score,
    get_match_label,
    load_job_description,
)

MOCK_SKILLS = [
    {"name": "Python", "keywords": ["python"]},
    {"name": "SQL", "keywords": ["sql", "mysql", "postgresql"]},
    {"name": "Docker", "keywords": ["docker"]},
]


# normalize_text

def test_normalize_text_lowercases():
    assert normalize_text("Python") == "python"

def test_normalize_text_already_lower():
    assert normalize_text("python") == "python"

def test_normalize_text_empty():
    assert normalize_text("") == ""


# find_relevant_job_skills

def test_find_relevant_job_skills_matches():
    result = find_relevant_job_skills("we need python and sql experience", MOCK_SKILLS)
    assert result == ["Python", "SQL"]

def test_find_relevant_job_skills_no_match():
    result = find_relevant_job_skills("java and kotlin experience", MOCK_SKILLS)
    assert result == []

def test_find_relevant_job_skills_partial_word_no_match():
    result = find_relevant_job_skills("pythonic code style preferred", MOCK_SKILLS)
    assert result == []

def test_find_relevant_job_skills_synonym():
    result = find_relevant_job_skills("experience with mysql databases", MOCK_SKILLS)
    assert result == ["SQL"]


# compare_to_user_skills

def test_compare_to_user_skills_matched_and_missing():
    matched, missing = compare_to_user_skills(["Python", "SQL", "Docker"], {"Python", "Docker"})
    assert matched == ["Python", "Docker"]
    assert missing == ["SQL"]

def test_compare_to_user_skills_all_matched():
    matched, missing = compare_to_user_skills(["Python"], {"Python", "SQL"})
    assert matched == ["Python"]
    assert missing == []

def test_compare_to_user_skills_none_matched():
    matched, missing = compare_to_user_skills(["Python", "SQL"], {"Docker"})
    assert matched == []
    assert missing == ["Python", "SQL"]

def test_compare_to_user_skills_empty_relevant():
    matched, missing = compare_to_user_skills([], {"Python"})
    assert matched == []
    assert missing == []


# calculate_match_score

def test_calculate_match_score_full():
    assert calculate_match_score(["Python", "SQL"], ["Python", "SQL"]) == 100.0

def test_calculate_match_score_half():
    assert calculate_match_score(["Python"], ["Python", "SQL"]) == 50.0

def test_calculate_match_score_zero():
    assert calculate_match_score([], ["Python", "SQL"]) == 0.0

def test_calculate_match_score_empty_relevant():
    assert calculate_match_score([], []) == 0.0


# get_match_label

def test_get_match_label_strong():
    assert get_match_label(70.0, ["a"]) == "Strong match"

def test_get_match_label_moderate():
    assert get_match_label(40.0, ["a"]) == "Moderate match"

def test_get_match_label_weak():
    assert get_match_label(39.9, ["a"]) == "Weak match"

def test_get_match_label_no_skills():
    assert get_match_label(0.0, []) == "No tracked skills found"


# load_job_description

def test_load_job_description(tmp_path):
    job_file = tmp_path / "job.txt"
    job_file.write_text("We need a Python developer.", encoding="utf-8")
    assert load_job_description(job_file) == "We need a Python developer."

def test_load_job_description_not_found(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_job_description(tmp_path / "nonexistent.txt")


# CLI tests

def run_cli(*args):
    return subprocess.run(
        [sys.executable, "analyzer.py", *args],
        capture_output=True,
        text=True
    )


def test_cli_specific_file():
    result = run_cli("sample_jobs/software_dev_sample.txt")
    assert result.returncode == 0
    assert "Analyzing: software_dev_sample.txt" in result.stdout
    assert "Match Score:" in result.stdout

def test_cli_directory():
    result = run_cli("sample_jobs")
    assert result.returncode == 0
    assert result.stdout.count("Analyzing:") == 3

def test_cli_default_no_args():
    result = run_cli()
    assert result.returncode == 0
    assert "Analyzing:" in result.stdout

def test_cli_invalid_path():
    result = run_cli("nonexistent/path.txt")
    assert result.returncode == 0
    assert "Error:" in result.stdout

def test_cli_empty_directory(tmp_path):
    result = run_cli(str(tmp_path))
    assert result.returncode == 0
    assert "No .txt files found" in result.stdout
