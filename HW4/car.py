class Car:
    def __init__(self, model: str, mark: str, year: int):
        self.mark = mark
        self.model = model
        self.year = year

    def get_info(self):
        return f"Your model is {self.model}, your mark is {self.mark}, it was made in {self.year}"