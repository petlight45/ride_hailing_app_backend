from pathlib import Path


class OS:
    @staticmethod
    def create_folder_recursively(path):
        path = Path(path)
        path.mkdir(parents=True, exist_ok=True)
