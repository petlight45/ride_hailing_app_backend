import os


class URLS:
    @staticmethod
    def extract_scheme_from_url(url: str):
        scheme, *_ = url.split("://")
        return scheme.lower()

    @staticmethod
    def extract_filename_from_file_url(url: str):
        return os.path.basename(url)
