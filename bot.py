#Import the dependencies
from bs4 import BeautifulSoup

import requests
import urllib.request
import time



def send_message_telgram(message):
    apiToken = '<apitoken>'
    chatID = "<chat_id>"
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)


#Create lists to store the scraped data
authors = []
quotes = []


#Create a function to scrape the site
def scrape_website(page_number):
    page_num = str(page_number)
  #Convert the page number to a string
    URL = 'https://www.goodreads.com/quotes/tag/inspirational?page='+page_num
  #append the page number to complete the URL
    webpage = requests.get(URL)
  #Make a request to the website
    soup = BeautifulSoup(webpage.text, "html.parser")
#Parse the text from the website
    quoteText = soup.find_all('div', attrs={'class':'quoteText'})
#Get the tag and it's class
    for i in quoteText:
        quote = i.text.strip().split('\n')[0]
    #Get the text of the current quote, but only the sentence before a new line
        author = i.find('span', attrs={'class':'authorOrTitle'}).text.strip()
    #print(quote)
        quotes.append(quote)
    #print(author)
        authors.append(author)

n = 10
for num in range(0,n):
  scrape_website(num)


combined_list = []
for i in range(len(quotes)):
    combined_list.append(quotes[i]+'-'+authors[i])

print(combined_list)

send_message_telgram('hey')

send_message_telgram(combined_list[0])