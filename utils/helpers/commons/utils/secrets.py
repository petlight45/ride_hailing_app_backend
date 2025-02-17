import secrets


class Secrets:
    @staticmethod
    def generate_random_token(length=8):
        return secrets.token_hex(length).upper()
