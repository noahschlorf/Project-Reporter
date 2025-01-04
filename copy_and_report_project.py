import os
import sys
from pathlib import Path

def generate_project_report(directory, report_file):
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(f"# Project Report: {directory}\n\n")

        f.write("## Project Layout\n\n")
        layout = []
        generate_layout_recursive(directory, layout)
        f.write("```\n")
        f.write("\n".join(layout))
        f.write("\n```\n\n")

        f.write("## Project Layout and File Contents\n\n")
        generate_content_recursive(directory, f)

    print(f"Project report generated at '{report_file}'.")

def generate_layout_recursive(current_path, layout, prefix=""):
    items = sorted(os.listdir(current_path))
    for index, item in enumerate(items):
        path = os.path.join(current_path, item)
        # Skip virtualenv, __pycache__, or hidden directories
        if item in ['venv', '__pycache__'] or item.startswith('.'):
            continue

        connector = "└── " if index == len(items) - 1 else "├── "
        layout.append(prefix + connector + item)

        if os.path.isdir(path):
            extension = "    " if index == len(items) - 1 else "│   "
            generate_layout_recursive(path, layout, prefix + extension)

def generate_content_recursive(current_path, file_handle, prefix=""):
    items = sorted(os.listdir(current_path))
    for item in items:
        # Skip virtualenv, __pycache__, or hidden directories
        if item in ['venv', '__pycache__'] or item.startswith('.'):
            continue

        path = os.path.join(current_path, item)

        if os.path.isdir(path):
            # Write directory name, then recurse further
            file_handle.write(f"**Directory: {item}**\n\n")
            generate_content_recursive(path, file_handle, prefix + "    ")
        else:
            # Write file contents if it's a recognized text/code file
            file_handle.write(f"**{item}**\n")
            try:
                with open(path, 'r', encoding='utf-8') as content_file:
                    content = content_file.read()

                file_ext = Path(item).suffix.replace('.', '')
                # Adjust the list below if you need more file types
                if file_ext in ['py', 'js', 'java', 'c', 'cpp', 'html', 'css', 'md', 'swift']:
                    code_block = f"```{file_ext}\n{content}\n```\n"
                else:
                    code_block = f"```\n{content}\n```\n"
                file_handle.write(code_block + "\n")
            except Exception as e:
                file_handle.write(f"```\nError reading file: {e}\n```\n\n")

def main():
    print("Enter project directory")
    print("Ex. /Users/noahschlorf/Desktop/....")
    source_dir = input().strip()
    source_dir = os.path.expanduser(source_dir)

    if not os.path.isdir(source_dir):
        print(f"The provided path '{source_dir}' is not a valid directory.")
        sys.exit(1)

    report_file = os.path.join(os.getcwd(), "project_report.txt")

    print("\nGenerating project report...")
    generate_project_report(source_dir, report_file)

if __name__ == "__main__":
    main()
