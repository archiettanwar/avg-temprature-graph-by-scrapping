import requests
import selectorlib
import time

timern=time.strftime("%Y-%m-%d-%H-%M-%S")


def scrape(url):
    response=requests.get(url)
    source=response.text
    return source


def extract(source):
    extractor=selectorlib.Extractor.from_yaml_file("extract.yaml")
    value=extractor.extract(source)["temp"]
    return value


def add_temp(extracted):
    with open("time_temp.txt","a") as file:
        file.write(timern+","+extracted+"\n")