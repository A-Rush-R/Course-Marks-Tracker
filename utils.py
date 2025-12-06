# utils.py
COURSE_COLORS = [
    '#FF6666',  # red row
    '#00FF00',  # bright green row
    '#FF9900',  # orange row
    '#FFFF33',  # yellow row
    '#0000FF',  # blue row
]

class ExitToMenu(Exception):
    """Raised when user wants to abort the current operation and return to main menu."""
    pass

def get_input(prompt, type_func=str, condition=lambda x: True,
              error_msg="Invalid input. Please try again."):
    """
    Prompt user for input, validate type/condition, and support 'exit'.
    """
    while True:
        raw = input(prompt).strip()
        if raw.lower() == 'exit':
            raise ExitToMenu()
        
        # Allow empty strings if strictly asking for string and condition passes
        if not raw and type_func is str:
            if condition(raw):
                return raw

        try:
            val = type_func(raw)
            if condition(val):
                return val
            else:
                print(f"  Error: {error_msg}")
        except ValueError:
            print(f"  Error: Expected {type_func.__name__}, got '{raw}'.")

