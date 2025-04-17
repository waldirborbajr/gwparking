import re

class PlateValidator:
    def __init__(self):
        # Mercosul format: AAANANN (3 letters, 1 number, 1 letter, 2 numbers)
        self.pattern = re.compile(r'^[A-Z]{3}\d[A-Z]\d{2}$')

    def is_valid(self, plate_text):
        if not plate_text:
            return False
        return bool(self.pattern.match(plate_text))