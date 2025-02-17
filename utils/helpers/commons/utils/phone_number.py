import re


class PhoneNumber:
    @staticmethod
    def check_if_is_a_us_or_canada_phone_number(phone_number: str):
        return phone_number.startswith("+1")

    @staticmethod
    def check_if_a_text_contains_phone_number(text_: str):
        regex_phone_no = re.compile(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}")
        return regex_phone_no.search(string=text_) is not None
