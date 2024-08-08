# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 18:37:46 2024

@author: izqui
"""

import certifi
import json
from urllib.request import urlopen
from dotenv import load_dotenv


load_dotenv()

def get_jsonparsed_data(url):
    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    return json.loads(data)

url = ("https://financialmodelingprep.com/api/v3/search-ticker?query=AA&limit=10&exchange=NASDAQ&apikey=YOUR_API_KEY")
print(get_jsonparsed_data(url))