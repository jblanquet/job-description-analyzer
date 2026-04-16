from pathlib import Path

from skills import JOB_SKILLS, USER_SKILLS


def load_job_description(file_path: Path) -> str:
    """Read and return the contents of a job description text file."""
    return file_path.read_text(encoding="utf-8")


def normalize_text(text: str) -> str:
    """Convert text to lowercase for simple matching."""
    return text.lower()


def find_relevant_job_skills(job_text: str, job_skills: list[dict]) -> list[str]:
    """Return tracked skills that appear in the job description."""
    relevant_skills = []

    for skill in job_skills:
        skill_name = skill["name"]
        keywords = skill["keywords"]

        if any(keyword in job_text for keyword in keywords):
            relevant_skills.append(skill_name)

    return relevant_skills


def compare_to_user_skills(
    relevant_skills: list[str], user_skills: set[str]
) -> tuple[list[str], list[str]]:
    """Return matched and missing skills based on the user's skill set."""
    matched_skills = []
    missing_skills = []

    for skill in relevant_skills:
        if skill in user_skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    return matched_skills, missing_skills


def calculate_match_score(matched_skills: list[str], relevant_skills: list[str]) -> float:
    """Return match percentage based only on relevant job skills."""
    if not relevant_skills:
        return 0.0

    return (len(matched_skills) / len(relevant_skills)) * 100


def get_match_label(score: float, relevant_skills: list[str]) -> str:
    """Return a simple label based on the score."""
    if not relevant_skills:
        return "No tracked skills found"

    if score >= 70:
        return "Strong match"
    if score >= 40:
        return "Moderate match"
    return "Weak match"


def print_results(
    relevant_skills: list[str],
    matched_skills: list[str],
    missing_skills: list[str],
    score: float,
    label: str,
) -> None:
    """Print formatted analysis results."""
    print("\nRelevant Job Skills:")
    if relevant_skills:
        for skill in relevant_skills:
            print(f"- {skill}")
    else:
        print("- None")

    print("\nMatched Skills:")
    if matched_skills:
        for skill in matched_skills:
            print(f"- {skill}")
    else:
        print("- None")

    print("\nMissing Skills:")
    if missing_skills:
        for skill in missing_skills:
            print(f"- {skill}")
    else:
        print("- None")

    print(f"\nMatch Score: {score:.1f}%")
    print(f"Summary: {label}")


def analyze_file(file_path: Path) -> None:
    """Analyze a single job description file."""
    print(f"\n=== Analyzing: {file_path.name} ===")

    try:
        raw_text = load_job_description(file_path)
    except Exception as error:
        print(f"Error reading file: {error}")
        return

    normalized_text = normalize_text(raw_text)
    relevant_skills = find_relevant_job_skills(normalized_text, JOB_SKILLS)
    matched_skills, missing_skills = compare_to_user_skills(relevant_skills, USER_SKILLS)
    score = calculate_match_score(matched_skills, relevant_skills)
    label = get_match_label(score, relevant_skills)

    print_results(relevant_skills, matched_skills, missing_skills, score, label)
    print("\n" + "-" * 40)


def main() -> None:
    sample_folder = Path("sample_jobs")

    if not sample_folder.exists():
        print("Error: 'sample_jobs' folder not found.")
        return

    text_files = sorted(sample_folder.glob("*.txt"))

    if not text_files:
        print("Error: No .txt files found in 'sample_jobs'.")
        return

    for file_path in text_files:
        analyze_file(file_path)


if __name__ == "__main__":
    main()
