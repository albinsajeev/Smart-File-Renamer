# Smart-File-Renamer
"Windows GUI tool for automated batch renaming. Features regex-based string cleaning, conflict detection, and smart sequential numbering."

python batch-rename file-management automation regex tkinter windows-tool cleaner

\# Smart File Renamer



!\[Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=flat-square\&logo=windows)

!\[Language](https://img.shields.io/badge/Language-Python-3776AB?style=flat-square\&logo=python)

!\[License](https://img.shields.io/badge/License-MIT-green?style=flat-square)



\*\*Created by \[Albin Sajeev](https://github.com/albinsajeev)\*\*



> \*\*Clean messy filenames and organize them into a perfect sequence (001, 002...) automatically.\*\*



---



\## 🧐 The Problem

Files often come with inconsistent naming conventions, leading to sorting issues:

\* `1. Intro.mp4`

\* `10. Conclusion.mp4` (Gets sorted before 2)

\* `001\_001\_Chapter1.mp4` (Redundant numbers)



\## 💡 The Solution

\*\*Smart File Renamer\*\* scans a folder, identifies the "Real Name" of the file using Regex, strips away the junk prefixes, and applies a clean, zero-padded numbering system (`001\_Name.ext`).



---



\## 🚀 Features

\* \*\*Regex Cleaning:\*\* Automatically removes messy prefixes like `001\_001\_`, `1. `, or `1 - `.

\* \*\*Smart Sequencing:\*\* Renumbers files as `001`, `002`, `003`... ensuring correct sorting in Windows Explorer.

\* \*\*Safe Rename:\*\* Checks for file conflicts before renaming to prevent data loss.

\* \*\*Long Path Support:\*\* Handles Windows file paths longer than 260 characters.



---



\## 📥 Download

\[\*\*Download the latest App (v1.0)\*\*](https://github.com/albinsajeev/Smart-File-Renamer/releases)



---



\## 🛠 Build from Source

```bash

pip install pyinstaller

python -m PyInstaller --onefile --noconsole --name "Smart File Renamer" smart\_renamer.py

