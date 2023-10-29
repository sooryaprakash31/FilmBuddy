# Film Buddy

FilmBuddy enables you to get personalized film recommendations by choosing a film as a reference and applying filters to match your preferences.

## Endpoints

### 1. Recommendations

<b>Endpoint</b>: /recommend <br>
<b>Description</b>: This endpoint allows you to receive film recommendations based on configurable parameters, including the film title and the release year. <br>

### 2. Search

<b>Endpoint</b>: /search <br>
<b>Description</b>: This endpoint allows you to search for films based on a keyword in the film title. <br>



## QuickStart Guide

1. Clone the Repository: Clone the repository to your local machine.

```
git clone https://github.com/sooryaprakash31/FilmBuddy.git
```
2. Change the current directory to `app`
```
cd app
```
3. To start the application, execute
```
docker-compose up -d
```
4. To stop the application, execute
```
docker-compose down
```

Note: The endpoints can be accessed in the Swagger UI - [http://localhost:8000/apidocs/](http://localhost:8000/apidocs/)



## Datasets

- Retrieved from [MovieLens](https://grouplens.org/datasets/movielens/)

## License

- [MIT License](/LICENSE)

---

Leave a :star: if you find this useful! :)