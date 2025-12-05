# Course-Marks-Tracker

## Instructions

- Setup python virutal environment to install dependencies 
```bash
./setup.sh
```

- Activate the environment
```bash 
source .venv/bin/activate
```

- Run
```bash
python main.py
```

## Features

- **Persistent & Editable:** Load an existing `grades.xlsx` file to pick up where you left off. You don't have to re-enter all your course data in one session.

- **Flexible Grade Components:** Define course structures with a mix of standard components (Mid/End Sem), auto-calculated weights for repeated items (like quizzes and assignments), and fully custom components.

- **Dynamic Excel Generation:** The output is a "living" spreadsheet. It automatically calculates component scores and your overall SPI using built-in Excel formulas. Just enter your marks and grades, and the sheet does the rest.

- **User-Friendly CLI:** A robust, menu-driven interface guides you through the process. You can type `exit` at almost any prompt to safely cancel the current action and return to the main menu without losing your progress.
