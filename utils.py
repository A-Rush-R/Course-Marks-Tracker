# utils.py
COURSE_COLORS = [
    '#E8F4F8', '#F0E8F8', '#F8F0E8', '#E8F8E8',
    '#F8E8E8', '#F8F8E8', '#E8F8F0', '#F8E8F0',
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

