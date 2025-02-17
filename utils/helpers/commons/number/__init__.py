class NumberHelpers:
    @staticmethod
    def get_ordinal_of_a_number(n: int):
        return f"{n:d}{'tsnrhtdd'[(n // 10 % 10 != 1) * (n % 10 < 4) * n % 10::4]}"
