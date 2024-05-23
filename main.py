# Import Statement
import smtplib
import os
import requests

# Storing the news API key
api_key = "82d97b1654a94571b989e207c0362d52"

# Storing the url, the query to pass to the news API
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-04-23&\
       sortBy=publishedAt&apiKey=82d97b1654a94571b989e207c0362d52"

# Making a request to the news API
request = requests.get(url)

# Storing the response in content as a JSON
content = request.json()


# Retrieving only the titles and descriptions of each articles stored in the 
# JSON response
for i in content["articles"]:
       print(i["title"], ": ", i["description"])
