import re

import requests


class InternetHelpers:
    @staticmethod
    def get_title_and_description_of_a_web_page(url: str):
        from bs4 import BeautifulSoup

        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, "html.parser")
        # Find and return the title and description of the page
        title_tag = soup.find("title")
        description_tag = soup.find("meta", attrs={"name": "description"})
        title = title_tag.text.strip() if title_tag else None
        description = description_tag["content"].strip() if description_tag else None
        return {"title": title, "description": description}

    @staticmethod
    def check_if_string_is_a_url(str_: str):
        pattern = r"^(http[s]?:\/\/(www\.)?|ftp:\/\/(www\.)?|www\.){1}([0-9A-Za-z-\.@:%_\+~#=]+)+((\.[a-zA-Z]{2,3})+)(/(.)*)?(\?(.)*)?"
        return True if re.match(pattern, str_) else False

    @staticmethod
    def fetch_content_with_headers(url: str):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.content

    @staticmethod
    def _get_extension_from_content_type(content_type):
        content_type_map = {
            "image/jpeg": "jpg",
            "image/png": "png",
            "image/gif": "gif",
            "image/bmp": "bmp",
            "image/webp": "webp",
        }
        return content_type_map.get(content_type)

    @staticmethod
    def fetch_content_and_extension(url: str):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        content_type = response.headers.get("Content-Type")

        content_type_map = {
            "image/jpeg": "jpg",
            "image/png": "png",
            "image/gif": "gif",
            "image/bmp": "bmp",
            "image/webp": "webp",
        }
        extension = content_type_map.get(content_type)

        return response.content, extension
