# main.py
import sys
import os
from utils import get_input, ExitToMenu
from course_ops import collect_course_details, print_summary
from excel_io import load_courses_from_excel, create_excel

def main_menu(initial_courses, default_path):
    courses = initial_courses[:]
    while True:
        try:
            print_summary(courses)
            print("\nOptions:")
            print("  [A] Add a course")
            if courses:
                print("  [E] Edit a course")
                print("  [D] Delete a course")
                print("  [G] Generate Excel File")
            print("  [Q] Quit (without overwriting)")

            choice = get_input("\nSelect Option (type 'exit' anytime to reset current action): ", str).upper()

            if choice == 'A':
                try:
                    courses.append(collect_course_details())
                except ExitToMenu:
                    print("\n[!] Add cancelled. Returning to menu.")
                    continue

            elif choice == 'E' and courses:
                try:
                    idx = get_input("Enter number of course to edit: ", int,
                                    lambda x: 1 <= x <= len(courses),
                                    "Invalid number")
                    print(f"Editing Course #{idx}...")
                    courses[idx-1] = collect_course_details(courses[idx-1])
                except ExitToMenu:
                    print("\n[!] Edit cancelled. Returning to menu.")
                    continue

            elif choice == 'D' and courses:
                try:
                    idx = get_input("Enter number of course to delete: ", int,
                                    lambda x: 1 <= x <= len(courses),
                                    "Invalid number")
                    confirm = get_input(
                        f"Delete {courses[idx-1]['code']}? (y/n): ", str).lower()
                    if confirm == 'y':
                        del courses[idx-1]
                except ExitToMenu:
                    print("\n[!] Delete cancelled. Returning to menu.")
                    continue

            elif choice == 'G' and courses:
                try:
                    filename = get_input(
                        f"Enter filename (default: {default_path}): ", str)
                    if not filename:
                        filename = default_path
                    if not filename.endswith(".xlsx"):
                        filename += ".xlsx"
                    create_excel(courses, filename)
                    break
                except ExitToMenu:
                    print("\n[!] Generation cancelled. Returning to menu.")
                    continue

            elif choice == 'Q':
                print("Exiting without generating.")
                break

            else:
                print("Invalid option.")

        except ExitToMenu:
            print("\n(Already at main menu)")
            continue

if __name__ == "__main__":
    try:
        path = "grades.xlsx"
        if len(sys.argv) > 1:
            path = sys.argv[1]

        initial_courses = []
        if os.path.exists(path):
            try:
                initial_courses = load_courses_from_excel(path)
            except Exception as e:
                print(f"Warning: could not load '{path}', starting fresh. ({e})")

        main_menu(initial_courses, path)

    except KeyboardInterrupt:
        print("\nCancelled by user.")
