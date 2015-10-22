#!/usr/bin/env python

"""
Project Goal: scrape a website, use the Alchemy API to perform keyword
sentiment analysis.

Website Scraped: King James Bibile from Project Gutenberg

Project Gutenberg note:
This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Project Gutenberg License included
with this eBook or online at www.gutenberg.org

"""

from bs4 import BeautifulSoup
import requests
# from threading import Thread
from alchemyapi import AlchemyAPI
import json

# Fixes some encoding problems with Beautiful Soup
import sys
reload(sys)
sys.setdefaultencoding("utf8")


# Create the AlchemyAPI Object
alchemyapi = AlchemyAPI()


def ScrapePage(URL):
    page = requests.get(URL)
    page_HTML = page.content
    return(page_HTML)


def ExtractSoup(pageHTML):
    soup = BeautifulSoup(pageHTML)
    text = soup.get_text()
    return(text)


def CheckSize(text):
    print(sys.getsizeof(text))
    if sys.getsizeof(text) > 50000:
        print("The selected text is larger than the Alchemy API allows.The entire text will not be analyzed.")


def RankedKeywordCall(text):
    response = alchemyapi.keywords('text', text, {'sentiment': 1, 'maxRetrieve': 10})
    if response['status'] == 'OK':
        print('## Keywords ##')
        for keyword in response['keywords']:
            print('text: ', keyword['text'].encode('utf-8'))
            print('relevance: ', keyword['relevance'])
            print('sentiment: ', keyword['sentiment']['type'])
            if 'score' in keyword['sentiment']:
                print('sentiment score: ' + keyword['sentiment']['score'])
            print('')
    else:
        print('Error in keyword extaction call: ', response['statusInfo'])
    return(response)

def TextCategorization(text):
    response = alchemyapi.category('text', text)

    if response['status'] == 'OK':
        print('## Response Object ##')
        print(json.dumps(response, indent=4))

        print('')
        print('## Category ##')
        print('text: ', response['category'])
        print('score: ', response['score'])
        print('')
    else:
        print('Error in text categorization call: ', response['statusInfo'])

if __name__ == "__main__":
    page = ScrapePage("http://www.gutenberg.org/files/10/10-h/10-h.htm")
    text = ExtractSoup(page)
    CheckSize(text)
    keywords = RankedKeywordCall(text)
    TextCategorization(text)
