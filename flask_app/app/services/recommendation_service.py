from typing import Union

import pandas as pd

from .data_service import DataService
from ..po.recommendation_po import RecommendationPo
from ..utils.movies import Movies


class RecommendationService:
    """
    Recommendation related methods
    """

    def __init__(self, title: str, year: Union[int, str], recommendation_po: RecommendationPo):
        self.title = title
        self.year = year
        self.recommendation_po = recommendation_po
        self.movies = DataService(dataset_file_name="movies").get_dataframe()
        self.ratings = DataService(dataset_file_name="ratings").get_dataframe()

    def get_recommendations(self):
        """
        This method is used to process the dataset and get recommendations based on input title and year values
        :return: dataframe with recommendations
        """

        self.movies["genres"] = self.movies["genres"].apply(lambda text: Movies.clean_text(text=text,
                                                                                           replace_string=" "))

        year_re_pattern = r'\((\d{4})\)'

        self.movies["year"] = self.movies["title"].apply(lambda text: Movies.find_match(text=text,
                                                                                        re_pattern=year_re_pattern))

        self.movies["title"] = self.movies["title"].apply(lambda text: Movies.clean_title(text=text,
                                                                                          re_pattern=year_re_pattern))

        self.movies.head()

        recommendations = self.collaborative_filtering()
        return recommendations

    def collaborative_filtering(self) -> pd.DataFrame:
        """
        This method is used to perform collaborative filtering on the movies and ratings dataset
        to find 10 movies that are similar to the given movie
        :return: dataframe with 10 recommended movies
        """
        movie_record = Movies.find_movie(movies_df=self.movies, title=self.title, year=self.year)
        movie_id = movie_record["movieId"].iloc[0]

        # Find the other users who liked the given movie. Call them similar_users
        similar_users = self.ratings[
            (self.ratings["movieId"] == movie_id) &
            (self.ratings['rating'] > self.recommendation_po.rating_filter)
            ]["userId"].unique()

        # Find the other movies liked by similar_users - call them similar_users_records
        similar_users_records = self.ratings[
            (self.ratings["userId"].isin(similar_users)) &
            (self.ratings["rating"] > self.recommendation_po.rating_filter)
            ]["movieId"]

        # Calculate the percentage of how many users in similar_users liked each movie
        # Get the number of users liked each movie.
        # Divide the number by the number of users.
        similar_users_records = similar_users_records.value_counts() / len(similar_users)

        # Find the movies liked by more than 10 percentage of the similar users
        similar_users_records = similar_users_records[
            similar_users_records > self.recommendation_po.popularity_threshold]

        # Find the other users who liked the movies that are liked by similar_users - call them all_users
        all_users = self.ratings[
            (self.ratings["movieId"].isin(similar_users_records.index)) &
            (self.ratings["rating"] > self.recommendation_po.rating_filter)
            ]

        # Calculate the percentage of how many users in the whole dataset liked each movie
        all_users_records = all_users["movieId"].value_counts() / len(all_users["userId"].unique())

        records_percentages = pd.concat([similar_users_records, all_users_records], axis=1)

        records_percentages.columns = ["similar", "all"]

        records_percentages["score"] = records_percentages["similar"] / records_percentages["all"]

        records_percentages = records_percentages.sort_values("score", ascending=False)

        recommendations = records_percentages. \
            head(self.recommendation_po.recommendations_count).merge(self.movies, left_index=True, right_on="movieId")

        recommendations = recommendations.loc[:, ["title", "year", "genres"]]

        return recommendations
