
import re
from typing import Union

import pandas as pd


class Movies:
    """
    Movies related utility methods
    """

    @staticmethod
    def clean_text(text: str, re_pattern: str = "[^a-zA-Z0-9 ]", replace_string="") -> str:
        """
        This method is used to replace the given regular expression pattern with the replace_string
        :param text: the input text
        :param re_pattern: regular expression pattern
        :param replace_string: string to be used for replacement
        :return: text after replacement
        """
        text = re.sub(re_pattern, replace_string, text)
        return text

    @staticmethod
    def find_match(text: str, re_pattern: str) -> Union[str, None]:
        """
        This method is used to find the substring that matches the given regular expression pattern
        :param text: input text
        :param re_pattern: regular expression pattern
        :return: The substring or None
        """
        match = re.search(re_pattern, text)
        if match:
            return match.group(1)
        else:
            return None

    @staticmethod
    def concatenate_columns(df: pd.DataFrame, cols_list: list) -> pd.Series:
        """
        This method is used to concatenate the values in multiple columns into a new column
        :param df: input dataframe
        :param cols_list: list of columns to be concatenated
        :return: the new column with concatenated values (pandas series)
        """
        return df[cols_list].apply(lambda row: ' '.join(row.values.astype(str)), axis=1)

    @staticmethod
    def clean_title(text: str, re_pattern: str) -> str:
        """
        This method is used to clean the input text by replacing the regular expression with empty string
        and removing unnecessary spaces
        :param text: input text
        :param re_pattern: regular expression
        :return: cleaned text
        """
        text = Movies.clean_text(text=text, re_pattern=re_pattern)
        text = text.strip()
        return text

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
        year = str(year)
        movies_copy = movies_df.copy()
        movies_copy["title"] = movies_copy["title"].apply(lambda text: text.lower())
        movie_record = movies_copy[
            (movies_copy['title'] == title) &
            (movies_copy['year'] == year)
            ]
        return movie_record
