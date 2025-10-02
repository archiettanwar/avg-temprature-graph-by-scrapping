import streamlit as st
import plotly.express as px
import time
import requests
import selectorlib

URL="http://programmer100.pythonanywhere.com/"

def scrape(url):
    response=requests.get(url)
    source=response.text
    return source

def extract(source):
    extractor=selectorlib.Extractor.from_yaml_file("extract.yaml")
    value=extractor.extract(source)["temp"]
    return value

def add_temp

if __name__=="__main__":
    while True:
        source=(scrape(URL))
        extracted=extract(source)
        print(extracted)
    time.sleep(2)