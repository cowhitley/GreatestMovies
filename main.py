# import the required libraries
from bs4 import BeautifulSoup
import requests

# retrieve the website
response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
great_movies_web_page = response.text
soup = BeautifulSoup(great_movies_web_page, 'html.parser')

# select the movies
movies = soup.select(selector='.listicle_listicle__item__CJna4 h3')
movie_titles = [movie.getText() for movie in movies]

# fix formatting of first movie in list which is missing )
movie_titles[0] = f'{movie_titles[0].split()[0]}) {movie_titles[0].split()[1]}'

# reverse the list
movie_titles.reverse()

# write the movies to a file
with open('movies.txt', mode='w') as file:
    for movie in movie_titles:
        file.write(f'{movie}\n')