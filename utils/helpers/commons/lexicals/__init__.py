class LexicalHelpers:
    @staticmethod
    def get_proper_determiner_of_a_word(word: str):
        vowels = "aeiou"
        word = word.strip().lower()
        if word == "user":
            return "a"
        word_first_letter = word[0]
        word_sec_letter = len(word) > 1 and word[1]
        if word_first_letter in vowels or (
            word_first_letter == "h" and word_sec_letter in vowels
        ):
            return "an"
        else:
            return "a"

    @staticmethod
    def get_readable_file_size_unit(size_value: int):
        units = ["B", "KB", "MB", "GB"]
        no_of_units = len(units)
        for level, unit in enumerate(units):
            if size_value < 1024 ** (level + 1) or (level + 1) == no_of_units:
                return f"{round(size_value / (1024 ** level), 2)}{unit}"
