import re


class InternetValidatorHelpers:
    class Email:
        _non_company_domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
        _email_regex = re.compile(r"(.+?)@(.+)$")

        @classmethod
        def validate_email_as_company_email(cls, email):
            match = cls._email_regex.match(email)
            if match:
                if match.group(2) not in cls._non_company_domains:
                    return True, None
                return None, f"'{email}' is invalid. Company name required."
            return None, f"'{email}' is not a valid email address."
