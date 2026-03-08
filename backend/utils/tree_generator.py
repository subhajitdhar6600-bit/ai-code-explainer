import os

def generate_tree(repo_path: str):
    tree = []

    for root, dirs, files in os.walk(repo_path):
        level = root.replace(repo_path, "").count(os.sep)
        indent = " " * 4 * level
        tree.append(f"{indent}{os.path.basename(root)}/")

        sub_indent = " " * 4 * (level + 1)
        for file in files:
            tree.append(f"{sub_indent}{file}")

    return tree