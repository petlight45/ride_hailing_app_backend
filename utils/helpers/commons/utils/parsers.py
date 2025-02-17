import dateutil.parser
import pytz


class Parsers:
    @staticmethod
    def parse_int(_data: any) -> int:
        if isinstance(_data, int):
            return _data
        try:
            return int(_data)
        except ValueError:
            return 0

    @staticmethod
    def parse_float(_data: any) -> float:
        if isinstance(_data, float):
            return _data
        try:
            return float(_data)
        except ValueError:
            return 0

    @staticmethod
    def parse_bool(boolean: str):
        if not isinstance(boolean, bool):
            if isinstance(boolean, str):
                if boolean.lower() == "true":
                    return True
            return False
        return boolean

    @staticmethod
    def parse_date_string(date_string: str, tzinfo=None):
        return dateutil.parser.parse(date_string).replace(tzinfo=tzinfo or pytz.UTC)
