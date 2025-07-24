import subprocess
import sys
import requests
import os

GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent"
API_KEY = os.getenv("GEMINI_API_KEY")  # Set your Gemini API key in the environment

def get_staged_diff():
    """Return the staged git diff as a string."""
    result = subprocess.run(["git", "diff", "--cached"], capture_output=True, text=True)
    return result.stdout

def generate_commit_message(diff_text):
    """Call Gemini Developer API to generate a commit message."""
    if not API_KEY:
        raise EnvironmentError("GEMINI_API_KEY environment variable not set.")
    
    headers = {"Content-Type": "application/json"}
    prompt = (
        "You are an assistant that writes concise, clear git commit messages. "
        "Generate a commit message for the following code changes:\n\n"
        f"{diff_text}"
    )
    data = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": prompt}]
            }
        ]
    }
    response = requests.post(f"{GEMINI_API_URL}?key={API_KEY}", headers=headers, json=data)
    response.raise_for_status()
    result = response.json()
    try:
        # Gemini's response structure
        return result['candidates'][0]['content']['parts'][0]['text'].strip()
    except Exception:
        print("Gemini API response parsing error. Raw response:")
        print(result)
        raise

def main():
    diff_text = get_staged_diff()
    if not diff_text.strip():
        print("No staged changes detected. Please stage changes with 'git add'.")
        sys.exit(1)
    commit_msg = generate_commit_message(diff_text)
    with open('commit_message.txt', 'w') as f:
        f.write(commit_msg)
    print("Commit message generated and saved to commit_message.txt")
    print(f"\nSuggested commit message:\n{commit_msg}")

if __name__ == "__main__":
    main()