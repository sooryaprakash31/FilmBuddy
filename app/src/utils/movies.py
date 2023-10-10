from typing import Union

import pandas as pd


class Movies:
    """
    Movies related utility methods
    """

    @staticmethod
    def find_movie(movies_df: pd.DataFrame, title: str, year: Union[str, int]) -> pd.DataFrame:
        """
        This method is used to find a movie record in the movies dataset based on the given movie title and year values
        :param movies_df: Movies dataframe
        :param title: movie title
        :param year: year
        :return: the identified movie record
        """
        title = title.lower()
        movies_copy = movies_df.copy()
        movies_copy["title"] = movies_copy["title"].apply(lambda text: text.lower())
        movie_record = movies_copy[
            (movies_copy['title'] == title) &
            (movies_copy['year'] == year)
            ]
        return movie_record
