import streamlit as st
import plotly.express as px
import time
from funtions import scrape
from funtions import add_temp
from funtions import extract

URL="http://programmer100.pythonanywhere.com/"
timern=time.strftime("%Y-%m-%d-%H-%M-%S")

if __name__=="__main__":
    while True:
        source=(scrape(URL))
        extracted=extract(source)
        add_temp(extracted)

        print(timern+","+extracted)
        time.sleep(2)