from pathlib import Path
from datetime import datetime
from typing import List

FILE_NAME = "lia-logs.md"
DIR_NAME = "logs"
CWD = Path.cwd()


class WeeklyEntry:
    def __init__(self, body_text: List[str], header: str, rating: str):
        if not all([body_text, header, rating]):
            raise ValueError("Daily entry incomplete!")
        self.body_text: List[str] = body_text
        self.header: str = header
        self.rating: str = rating

    def getDate(self) -> str:
        today = datetime.now()
        return today.strftime("%Y-%b-%d Week: %W")

    def create_log_dir(self) -> Path:
        dir_path = CWD.joinpath(DIR_NAME)
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"Created directory at: \n\n{dir_path}")
        else:
            print(f"Directory {DIR_NAME} exists already")
        return dir_path

    def save_log(self) -> None:
        log_dir = self.create_log_dir()
        file_path = log_dir.joinpath(FILE_NAME)

        with open(file_path, "a+", encoding="utf8") as f:
            f.write(self.markdownFormatter())
            f.write("\n------------\n\n")

    def markdownFormatter(self) -> str:
        all_text = "".join(self.body_text)
        return f"## {self.header} ({self.getDate()})\n\nToday rating: **{self.rating}**\n\n{all_text}\n"
