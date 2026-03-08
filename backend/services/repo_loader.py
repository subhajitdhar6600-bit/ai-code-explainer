import os
import shutil
from git import Repo
from utils.logger import logger  # if you have a logger, else use print()

TEMP_REPO_DIR = "temp_repos"

def clone_repo(repo_url):
    # Convert HttpUrl to string (FastAPI gives HttpUrl type)
    if not isinstance(repo_url, str):
        repo_url = str(repo_url)

    # Get repo name
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    repo_path = os.path.join(TEMP_REPO_DIR, repo_name)

    # If folder exists, delete it safely
    if os.path.exists(repo_path):
        def remove_readonly(func, path, excinfo):
            import stat
            os.chmod(path, stat.S_IWRITE)  # make file writable
            func(path)
        
        shutil.rmtree(repo_path, onerror=remove_readonly)
        logger.info(f"Deleted old repo folder: {repo_path}")

    # Clone the repository
    logger.info(f"Cloning repository: {repo_url}")
    Repo.clone_from(repo_url, repo_path)
    logger.info(f"Repository cloned at: {repo_path}")

    return repo_path