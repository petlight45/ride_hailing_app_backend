from typing import Any

from rest_framework import status


class CustomException(Exception):
    __slots__ = ["_data", "status_code"]

    def __init__(
        self,
        data: Any,
        status_code: int = status.HTTP_400_BAD_REQUEST,
    ):
        self.status_code = status_code or status.HTTP_400_BAD_REQUEST
        self._data = data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
