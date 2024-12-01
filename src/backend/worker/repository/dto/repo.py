from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class SuccessDTO(Generic[T]):
    data: T | None = None
    url: str | None = None

    def __init__(self, data: T):
        self.data = data

    def set_url(self, url):
        self.url = url


@dataclass
class ErrorDTO(Generic[T]):
    detail: T | None = None
    status_code: int | None = None

    def __init__(self, detail: T, status_code: int):
        self.detail = detail
        self.status_code = status_code
