import os

def parse_code_files(repo_path: str):
    """
    Walk through repo_path, read code files, and skip hidden/system folders like .git.
    Returns a list of dicts: {"file_name": ..., "content": ...}
    """
    code_files = []

    for root, dirs, files in os.walk(repo_path):
        # Skip hidden/system folders completely
        dirs[:] = [d for d in dirs if not d.startswith(".")]

        for file_name in files:
            # Skip hidden/system files
            if file_name.startswith("."):
                continue

            # Only include code files (adjust extensions as needed)
            if file_name.endswith((".py", ".js", ".ts", ".java", ".cpp")):
                file_path = os.path.join(root, file_name)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    code_files.append({"file_name": file_name, "content": content})
                except Exception:
                    # Skip unreadable files (permission errors, locked files)
                    continue

    return code_files