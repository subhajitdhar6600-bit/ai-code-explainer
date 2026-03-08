from services.repo_loader import clone_repo
from services.code_parser import parse_code_files
from services.ai_chunker import chunk_code
from utils.logger import logger
import os

def explain_repository(repo_url: str):
    logger.info(f"Processing repo for explanation: {repo_url}")

    # Step 1: Clone repository
    repo_path = clone_repo(repo_url)

    # Step 2: Parse code files (code_parser skips .git automatically)
    code_files = parse_code_files(repo_path)

    explanations = []

    # Step 3: Process each file
    for file in code_files:
        chunks = chunk_code(file["content"])
        for chunk in chunks:
            explanation = f"Explanation for part of {file['file_name']}:\n{chunk[:200]}..."
            explanations.append(explanation)

    logger.info(f"Completed explanation for repo: {repo_url}")
    return explanations

def summarize_repository(repo_url: str):
    logger.info(f"Processing repo for summary: {repo_url}")

    # Step 1: Clone repository
    repo_path = clone_repo(repo_url)

    # Step 2: Parse code files (ignores .git)
    code_files = parse_code_files(repo_path)

    all_chunks = []

    # Step 3: Chunk all files
    for file in code_files:
        try:
            chunks = chunk_code(file["content"])
            all_chunks.extend(chunks)
        except Exception:
            # Skip any file that causes errors (permissions, encoding)
            continue

    # Step 4: Create a safe summary
    summary = f"Repository has {len(code_files)} files and {len(all_chunks)} chunks. Sample code:\n"
    summary += "".join([chunk[:200] + "...\n" for chunk in all_chunks[:5]])

    logger.info(f"Completed summary for repo: {repo_url}")
    return summary