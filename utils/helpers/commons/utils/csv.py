import csv
import gc
import io

import requests


class CSV:
    @staticmethod
    def parse_by_url(csv_url):
        import chardet

        csv_res = requests.get(csv_url)
        csv_res.raise_for_status()
        encoding = chardet.detect(csv_res.content)["encoding"]
        with io.StringIO(csv_res.content.decode(encoding)) as csv_content:
            csv_reader = csv.DictReader(csv_content)
            for csv_data in csv_reader:
                yield csv_data
        del csv_content
        del csv_reader
        gc.collect()
