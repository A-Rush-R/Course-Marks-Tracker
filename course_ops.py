# course_ops.py
from utils import get_input, ExitToMenu

def collect_course_details(existing_data=None):
    """Interactively collect one course's configuration."""
    print(f"\n--- {'Editing' if existing_data else 'Adding New'} Course (Type 'exit' to cancel) ---")
    code = get_input("Course Number (e.g., CS360): ",
                     str, lambda x: len(x) > 0, "Cannot be empty")
    title = get_input("Course Title: ",
                      str, lambda x: len(x) > 0, "Cannot be empty").upper()
    credits = get_input("Credits: ", int,
                        lambda x: x > 0, "Credits must be positive")

    components = []

    std_fields = ["Attendance", "Project", "Mid Semester", "End Semester"]
    print("\n--- Component Weightages (Enter 0 to skip) ---")
    for field in std_fields:
        w = get_input(f"Weightage for {field}: ", float,
                      lambda x: x >= 0, "Must be non-negative")
        if w > 0:
            components.append({"name": field, "weight": w})

    iter_fields = [["Quiz", "Quizzes"], ["Assignment", "Assignments"]]
    for field, field_mul in iter_fields:
        w = get_input(f"Total Weightage for all {field_mul}: ", float,
                      lambda x: x >= 0, "Must be non-negative")
        if w > 0:
            count = get_input(f"  -> How many {field_mul}?: ", int,
                              lambda x: x > 0, "Count must be at least 1")
            per_item_weight = w / count
            for i in range(1, count + 1):
                components.append({"name": f"{field} {i}",
                                   "weight": per_item_weight})

    print("\n--- Custom Components (Enter 0 weight to finish) ---")
    while True:
        try:
            w = get_input("Weightage for Other/Custom Component: ", float,
                          lambda x: x >= 0, "Must be non-negative")
        except ExitToMenu:
            raise
        if w == 0:
            break
        name = get_input("  -> Name of this component (e.g., 'Lab Exam'): ",
                         str, lambda x: len(x) > 0, "Name cannot be empty")
        components.append({"name": name, "weight": w})
        print(f"     (Added '{name}' with weight {w})")

    return {"code": code, "title": title, "credits": credits,
            "components": components}

def print_summary(courses):
    print("\n" + "="*40)
    print(f"Current List ({len(courses)} courses)")
    print("="*40)
    if not courses:
        print("  (No courses added yet)")
    for idx, c in enumerate(courses):
        comps = ", ".join([x['name'] for x in c['components']])
        print(f"  [{idx+1}] {c['code']} - {c['title']} ({c['credits']} cr)")
        print(f"      Components: {comps}")
    print("="*40)

