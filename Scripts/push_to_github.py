# push_to_github.py

import os
from github import Github

# GitHub token stored as an environment variable for security
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Ensure you have set the GITHUB_TOKEN env variable

# Repository details
REPO_NAME = "jeswanth27/github_vs_db"
BRANCH_NAME = "main"

def push_to_github(file_path, commit_message):
    try:
        # Initialize GitHub instance
        g = Github(GITHUB_TOKEN)
        repo = g.get_repo(REPO_NAME)

        # Read file content
        with open(file_path, 'r') as file:
            content = file.read()

        # Commit to GitHub (create or update file)
        repo.create_file(file_path, commit_message, content, branch=BRANCH_NAME)
        print(f"Successfully pushed {file_path} to GitHub.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
push_to_github('notebooks/GitHubIntegrationNotebook.dbc', 'Initial commit of GitHub integration notebook')
