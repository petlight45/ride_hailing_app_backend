import base64

from django.conf import settings


class Strings:
    @staticmethod
    def get_complete_url(suffix: str) -> str:
        return f"{settings.BACKEND_API_BASE_URL}{suffix}"

    @staticmethod
    def convert_camel_case_to_python_method_convention(str_: str) -> str:
        action_name = ""
        for id_, letter in enumerate(str_):
            if letter.isupper() and id_:
                action_name += "_"
            action_name += letter.lower()
        return action_name

    @staticmethod
    def convert_camel_case_to_words(str_: str) -> str:
        words = ""
        for id_, letter in enumerate(str_):
            if letter.isupper():
                if id_:
                    words += " "
                words += letter.lower()
            else:
                words += letter
        return words

    @staticmethod
    def convert_snake_case_to_words(str_: str) -> str:
        words = ""
        for letter in str_.strip("_"):
            if letter == "_":
                words += " "
            else:
                words += letter.lower()
        return words

    @staticmethod
    def convert_snake_case_to_title_case(str_: str) -> str:
        return Strings.convert_snake_case_to_words(str_).title()

    @staticmethod
    def convert_words_to_snake_case(str_: str) -> str:
        return Strings.join("_", *[item.lower() for item in str_.strip(" ").split(" ")])

    @staticmethod
    def join(sep="", *args):
        return sep.join(args)

    @staticmethod
    def convert_to_base_64_string(str_: str):
        return base64.b64encode(str_.encode("utf-8")).decode("utf-8")
