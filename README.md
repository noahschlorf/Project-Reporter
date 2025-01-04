# Project Report Generator

This Python project generates a structured report for a given directory, including the project layout and file contents. It outputs a report file containing a tree view and file contents of the specified directory.

## Features
- Recursively scans a directory
- Generates a tree-like structure of the directory layout
- Displays the contents of text and code files
- Skips virtual environments, cache directories, and hidden files

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/noahschlorf/Project-Reporter
   cd Project-Reporter
   ```

2. Run the script:
   ```bash
   python3 main.py
   ```

3. Enter the project directory path when prompted.

4. The report will be generated as `project_report.txt` in the current working directory.

## Project Structure

- `main.py`: Entry point for the script
- `project_report.txt`: Generated report containing directory layout and file contents

## Example Output
```plaintext
# Project Report: /example/path

## Project Layout
.
├── main.py
├── utils
│   └── helper.py

## Project Layout and File Contents
**main.py**
```python
print('Hello World')
```
```
