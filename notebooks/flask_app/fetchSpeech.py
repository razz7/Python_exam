import requests
import pandas as pd
from bs4 import BeautifulSoup
import lxml
import re


def getspeech():
# URL to the main Wikipedia page
    main_url = "https://en.wikisource.org/wiki/Portal:State_of_the_Union_Speeches_by_United_States_Presidents"

    page = requests.get(main_url).text
    soup = BeautifulSoup(page, "lxml")

# Finds all speeches from 1900 to 2021:
    soup = soup.find_all('li')[144:268]

# Initialize empty list for speech URLs:
    speech_urls = []

# Initialize empty list for years - to be used for filenames:
    year_list = []

# Loads all speech URls into list:
    for li in soup:
    
    # Finds URL and appends to 'speech_urls' list
        url = "https://en.wikisource.org/" + li.a.get('href')
        speech_urls.append(url)
    
        # Finds text next to the second <a> tag, as this text contains the date infomation for the speech: 
        this_date = li.find_all('a')[1].next_sibling
    
    # We use regex to find the year from the date string:
        this_year = re.search(r"\b(19|20)\d{2}\b", this_date)
    
    # Year is appended to 'year_list'
        year_list.append(this_year.group(0))
    
# Creates a dictionary so we can iterate 'year_list' and 'speech_urls' at the same time:
    url_year_zip = zip(year_list, speech_urls)
    url_year_dict = dict(url_year_zip)

# Opens each URL, reads text and saves text:
    for year, url in url_year_dict.items():
        page = requests.get(url).content
        soup = BeautifulSoup(page, "lxml")
    
    # We remove the first and the last <p> tag to clean the data:
        text = soup.find_all('p')[1:-1]
    
    # Sets filename and increments year:
        filename = "./speeches_for_flask/" + year + ".txt" 
    
    # Creates file:
        f = open(filename ,"w+")
        for line in text:
        # .getText() method is added to extract content from each <p> tag, so the <p> tag is not included:
            f.write(line.getText())

    return "Speeches collected"