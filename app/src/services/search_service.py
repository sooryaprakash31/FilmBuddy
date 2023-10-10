from .data_service import DatasetService
from ..config import MOVIES_DATASET_FILE_PATH, RATINGS_DATASET_FILE_PATH
from ..po.search_po import SearchPo


class SearchService:

    def __init__(self, search_po: SearchPo):
        self.search_po = search_po
        dataset_service = DatasetService(movies_dataset_file_path=MOVIES_DATASET_FILE_PATH,
                                         ratings_dataset_file_path=RATINGS_DATASET_FILE_PATH)

        movies = dataset_service.get_movies_dataset()
        self.movies = movies.copy()

    def get_results(self):

        title_condition = self.movies['title'].str.contains(self.search_po.title, case=False)

        if self.search_po.year is not None:
            year_condition = self.movies['year'] == str(self.search_po.year)
        else:
            year_condition = True

        filtered_df = self.movies[title_condition & year_condition]

        del self.movies

        filtered_df = filtered_df.loc[:, ['title', 'year', 'genres']]

        return filtered_df.head(self.search_po.count)




