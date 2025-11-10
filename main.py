from src.logger import DailyEntry
from collections import namedtuple


def main():
    data_point = namedtuple("dailylog", ["header", "rating", "bodytext"])
    user_input = [
        input(f"what is today's {i}: ") for i in data_point._fields if i != "bodytext"
    ]

    bodytext_input = []

    print("\nEnter your log and to exit finish with empty line.\n")
    while True:
        line = input()

        if not line.strip():
            bodytext_input.append("\n--End--\n")
            break
        bodytext_input.append(line)

    bodytext = "\n".join(bodytext_input)
    entry = DailyEntry(body_text=bodytext, header=user_input[0], rating=user_input[1])
    entry.save_log()
    print("Daily log saved successfully!")


if __name__ == "__main__":
    main()
