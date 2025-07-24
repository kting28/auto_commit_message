# auto_commit_message

## Overview

**auto_commit_message** is a Python tool that uses the Gemini Developer API to generate clear, AI-powered commit messages for your staged code changes in a Git repository.  
Simply stage your changes, run the script, and let Gemini do the rest!

---

## Features

- Automatically analyzes your staged changes (`git diff --cached`)
- Sends the diff to Gemini via its public Developer API
- Suggests a concise commit message, saved to `commit_message.txt`
- Easy integration into your workflow

---

## Requirements

- Python 3.8+
- `requests` Python package (`pip install requests`)
- Gemini Developer API key ([Get yours](https://ai.google.dev))
- Set your API key in your environment:
  ```bash
  export GEMINI_API_KEY="your-gemini-api-key"
  ```

---

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/kting28/auto_commit_message.git
    cd auto_commit_message
    ```

2. Install the required Python package:
    ```bash
    pip install requests
    ```

3. Set your Gemini API key as an environment variable:
    ```bash
    export GEMINI_API_KEY="your-gemini-api-key"
    ```

---

## Usage

1. Stage your changes:
    ```bash
    git add .
    ```

2. Run the script:
    ```bash
    python generate_commit_msg.py
    ```

3. The commit message will be saved to `commit_message.txt`. You can view and use it:
    ```bash
    cat commit_message.txt
    git commit -F commit_message.txt
    ```

---

## How it Works

- The script collects your staged diff
- It sends a prompt (including your diff) to the Gemini Developer API
- The API responds with a suggested commit message
- The message is saved to `commit_message.txt` and printed for review

---

## Troubleshooting & Notes

- If you see an error about the API key, ensure you have set `GEMINI_API_KEY` in your environment.
- If your staged diff is empty, the script will ask you to stage your changes.
- For API errors, the raw response will be printed to help you debug.
- Make sure your API key has access to the Gemini Developer API endpoints.

---

## Example

```bash
git add important_file.py
python generate_commit_msg.py
cat commit_message.txt
git commit -F commit_message.txt
```

---

## License

MIT
