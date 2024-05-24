# Import Statement
import smtplib, ssl
import os
import requests
from send_email import send_email

# Storing the news API key
api_key = "82d97b1654a94571b989e207c0362d52"

# Storing the url, the query to pass to the news API
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-04-23&\
       sortBy=publishedAt&apiKey=82d97b1654a94571b989e207c0362d52"

# Making a request to the news API
request = requests.get(url)

# Storing the response in content as a JSON
content = request.json()

# Creating the message string
body = "Subject: Today's News\n"

# Retrieving only the titles and descriptions of each articles stored in the 
# JSON response
for i in content["articles"]:
       # If the article title is NOT None (article exists)..
       if i["title"] is not None:
              # appending the article title, description, and link to the message str
              body = body + "Title: " + i["title"] + "\n" + "Description: " + \
                     i["description"] + "\n" + "Link: " + i["url"] + 2*"\n"

# Encoding the body with the utf-8 format in case of potential encoding errors
body = body.encode("utf-8")

# Sending the message to the user
send_email(body)
