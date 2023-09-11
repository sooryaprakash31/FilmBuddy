from dataclasses import dataclass


@dataclass
class SearchPo:
    title: str
    year: int = None
    count: int = 10
