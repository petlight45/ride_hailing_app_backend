from . import CustomException


class CustomExceptionHelper:
    @classmethod
    def assert_(cls, condition, message, errors, status_code=None):
        if not condition:
            raise CustomException(
                {"message": message, "errors": errors}, status_code=status_code
            )
