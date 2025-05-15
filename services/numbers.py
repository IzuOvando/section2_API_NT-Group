from typing import Optional


class NumbersService:
    def __init__(self):
        self.numbers = list(range(1, 101))
        self.extracted_number: Optional[int] = None

    def extract(self, number: int):
        if number < 1 or number > 100:
            raise ValueError("El número debe estar entre 1 y 100.")
        if number not in self.numbers:
            raise ValueError(
                "El número ya ha sido extraído o no existe en el conjunto."
            )
        self.numbers.remove(number)
        self.extracted_number = number

    def find_missing_number(self) -> int:
        original_set = set(range(1, 101))
        current_set = set(self.numbers)
        extracted = list(original_set - current_set)
        extracted.sort()
        return extracted
