import os
from pathlib import Path
from openai import OpenAI

DATA_PATH = Path("data/sample_meeting_notes.txt")
PROMPT_PATH = Path("prompts")
OUTPUT_PATH = Path("outputs/ba_output.txt")

# Create OpenAI client using YOUR env variable
client = OpenAI(api_key=os.getenv("ba_aiauto"))


def load_text(file_path: Path) -> str:
    with open(file_path, "r") as f:
        return f.read()


def load_prompt(prompt_name: str, text: str) -> str:
    template = load_text(PROMPT_PATH / prompt_name)
    return template.replace("{{TEXT}}", text)


def call_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a senior Business Analyst working in a regulated industry.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,
        max_tokens=600,
    )
    return response.choices[0].message.content


def main():
    stakeholder_notes = load_text(DATA_PATH)

    outputs = {}

    prompt_files = {
        "USER STORIES": "user_story_prompt.txt",
        "ACCEPTANCE CRITERIA": "acceptance_criteria_prompt.txt",
        "REQUIREMENT CLASSIFICATION": "classification_prompt.txt",
        "RISKS & GAPS": "risk_flag_prompt.txt",
    }

    for section, prompt_file in prompt_files.items():
        prompt = load_prompt(prompt_file, stakeholder_notes)
        outputs[section] = call_llm(prompt)

    with open(OUTPUT_PATH, "w") as f:
        f.write("AI-Assisted Business Analysis Output\n")
        f.write("=" * 40 + "\n\n")

        for section, content in outputs.items():
            f.write(section + "\n")
            f.write("-" * len(section) + "\n")
            f.write(content.strip() + "\n\n")

    print("BA automation output generated successfully.")


if __name__ == "__main__":
    main()
