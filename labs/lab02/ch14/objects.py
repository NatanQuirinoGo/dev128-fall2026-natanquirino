from dataclasses import dataclass

@dataclass
class Movie:
    name: str = ""
    year: int = 1990

    def getStr(self):
        return f"{self.name} ({self.year})"

    