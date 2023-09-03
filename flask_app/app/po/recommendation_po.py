from dataclasses import dataclass


@dataclass
class RecommendationPo:
    title: str
    year: int
    recommendations_count: int = 10
    rating_filter: float = 3.5
    popularity_threshold: float = 0.1
