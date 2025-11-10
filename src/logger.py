from pathlib import Path
from datetime import datetime

FILE_NAME = "lia-logs.md"
DIR_NAME = "logs"
CWD = Path.cwd()

class DailyEntry:
    def __init__(self, body_text, header, rating):
        if not all([body_text, header, rating]):
            raise ValueError("Daily entry incomplete!")
        self.body_text = body_text
        self.header = header
        self.rating = rating


    def getDate(self):
        today = datetime.now()
        return today.strftime("%Y-%b-%d")

    def create_log_dir(self):
        dir_path = CWD.joinpath(DIR_NAME)
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"Created directory at: \n\n{dir_path}")
        else:
            print(f"Directory {DIR_NAME} exists already")
        return dir_path

    def save_log(self):
        log_dir = self.create_log_dir()
        file_path = log_dir.joinpath(FILE_NAME)
        
        with open(file_path, "a+", encoding="utf8") as f:
            f.write(self.markdownFormatter())
            f.write("\n------------\n\n")

    def markdownFormatter(self):
        return f"## {self.header} ({self.getDate()})\n\nToday rating: **{self.rating}**\n\n{self.body_text}\n"

