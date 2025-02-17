import random


class Numbers:
    @staticmethod
    def generate_random_positive_integer(max_: int = None):
        return random.randint(0, max_ or 99999)

    @staticmethod
    def convert_number_to_base_36_string(num: int = None):
        chars = "0123456789abcdefghijklmnopqrstuvwxyz"
        base36 = ""
        while num > 0:
            num, i = divmod(num, 36)
            base36 = chars[i] + base36
        return base36
