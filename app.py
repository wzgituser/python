from dotenv import load_dotenv
import requests
import json
from pprint import pprint
import os
import pandas as pd

load_dotenv()
print(os.getenv("key"))


def getCryptoList(id):

    url_list = "https://api.coincap.io/v2/rates/{id}}"
    url_market = "https://api.coincap.io/v2/markets"
    get_market = requests.get(url_list).json()
    get_list = requests.get(url_list).json()


if __name__ == "__main__":

    print("type curency name")

    inpt = input("curency name:")

    data = getCryptoList(inpt)

    pprint(data)
