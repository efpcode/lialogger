from src.entry_logger import WeeklyEntry
from src.config import WEEKLY_LOG_QUESTIONS
from src.entry_prompter import question_to_answer

def main():
    markdown_header = ("header", "rating")
    user_input = [input(f">>> What is this week's {i}: ") for i in markdown_header]

    alltext = [ question_to_answer(q) for q in WEEKLY_LOG_QUESTIONS]

    entry = WeeklyEntry(body_text=alltext, header=user_input[0], rating=user_input[1])
    entry.save_log()
    print("Daily log saved successfully!")


if __name__ == "__main__":
    main()
