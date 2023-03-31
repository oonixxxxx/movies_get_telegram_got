# In this code, replace `your_api_token_here` with the API token obtained from the BotFather. You can obtain the chat ID by starting a chat with the bot and sending the `/start` command to it, and then looking for the `chat` object in the JSON response returned by the bot API.
# This code initializes a Telegram bot that sends the top 100 movies from IMDb to the user who sends the command "/start" to the bot.

First, the necessary libraries (telebot, BeautifulSoup, requests) are imported. The API token and URL of the IMDb Top 100 movies list are defined, and the bot is initialized with the API token.

Two functions are defined - one to get the search URL for a given movie name on IMDb, and one to get the top 100 movie titles from IMDb.

The top 100 movies titles are retrieved and stored in a variable. 

A message handler is defined for the "/start" command. When a user sends this command to the bot, the bot sends a message containing each movie title and its corresponding search URL to the user.

The main function is set to continuously poll for updates from the Telegram API.

Overall, the code appears to function as intended, but it could be improved with better error handling and more robust functionality (such as allowing users to search for specific movies or filtering the top 100 list).
