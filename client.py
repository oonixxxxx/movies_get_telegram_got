import telebot
from bs4 import BeautifulSoup
import requests

# API token of the bot obtained from the BotFather
API_TOKEN = 'your api token'

# URL of the IMDb Top 100 movies list
IMDB_URL = 'https://www.imdb.com/chart/top/'

# Initialize the bot with the API token
bot = telebot.TeleBot(API_TOKEN)


def get_url(movie_name):
    # The name of the movie you want to find
    movie_name = movie_name

    # Search URL of IMDb website for movie using the name of the movie
    search_url = f'https://www.imdb.com/find?q={movie_name}&ref_=nv_sr_sm'
    return search_url


# Function to get the top 100 movies from IMDb
def get_top_100_movies():
    # Send a GET request to the IMDb URL
    response = requests.get(IMDB_URL)

    # Parse the HTML content of the response using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the movie titles in the list
    movie_titles = [title.text.rstrip() for title in soup.select('td.titleColumn a')]

    # Return the list of movie titles
    return movie_titles


# Get the top 100 movies from IMDb
top_100_movies = get_top_100_movies()


@bot.message_handler(commands=['start'])
def send_movies(message):
    number_of_rating = 1
    if number_of_rating < 101:
        # Send the top 100 movies to the user via the bot API
        for movie in top_100_movies:
            # Send a message containing the movie title to the user
            bot.send_message(message.chat.id, f'{number_of_rating}\n{movie} \n{get_url(movie)}')
            number_of_rating += 1


if __name__ == '__main__':
    bot.infinity_polling()
