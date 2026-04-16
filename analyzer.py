from pathlib import Path

from skills import SKILLS


def normalize_text(text: str) -> str:
    """Convert text to lowercase for simple matching."""
    return text.lower()


def find_skill_matches(job_text: str, skills: list[dict]) -> tuple[list[str], list[str]]:
    """Return matched and missing skills based on keyword checks."""
    matched_skills = []
    missing_skills = []

    for skill in skills:
        skill_name = skill["name"]
        keywords = skill["keywords"]

        if any(keyword in job_text for keyword in keywords):
            matched_skills.append(skill_name)
        else:
            missing_skills.append(skill_name)

    return matched_skills, missing_skills


def calculate_match_score(matched_skills: list[str], total_skills: int) -> float:
    """Return match percentage based on the total tracked skills."""
    if total_skills == 0:
        return 0.0
    return (len(matched_skills) / total_skills) * 100


def get_match_label(score: float) -> str:
    """Return a simple label based on the score."""
    if score >= 70:
        return "Strong match"
    if score >= 40:
        return "Moderate match"
    return "Weak match"


def print_results(
    matched_skills: list[str],
    missing_skills: list[str],
    score: float,
    label: str,
) -> None:
    """Print formatted analysis results."""
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


def main() -> None:
    sample_folder = Path("sample_jobs")

    for file_path in sorted(sample_folder.glob("*.txt")):
        print(f"\n=== Analyzing: {file_path.name} ===")

        try:
            raw_text = file_path.read_text(encoding="utf-8")
        except Exception as e:
            print(f"Error reading file: {e}")
            continue

        normalized_text = normalize_text(raw_text)
        matched_skills, missing_skills = find_skill_matches(normalized_text, SKILLS)
        score = calculate_match_score(matched_skills, len(SKILLS))
        label = get_match_label(score)

        print_results(matched_skills, missing_skills, score, label)
        print("\n" + "-" * 40)


if __name__ == "__main__":
    main()
