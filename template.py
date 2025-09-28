import os
from pathlib import Path

# Get the folder where template.py is located
BASE_DIR = Path(__file__).parent.resolve()

print("✅ template.py started running...")
print(f"📂 Base directory: {BASE_DIR}")

project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

created_files = 0
skipped_files = 0

for filepath in list_of_files:
    full_path = BASE_DIR / filepath
    filedir = full_path.parent

    print(f"🔍 Checking: {full_path}")

    if not filedir.exists():
        filedir.mkdir(parents=True, exist_ok=True)
        print(f"📂 Created directory: {filedir}")

    if not full_path.exists():
        full_path.touch(exist_ok=True)
        print(f"📄 Created file: {full_path}")
        created_files += 1
    else:
        print(f"✅ Skipped (already exists): {full_path}")
        skipped_files += 1

print(f"🎯 Finished execution. Created {created_files} file(s), skipped {skipped_files}.")
