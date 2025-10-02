import time
from funtions import scrape
from funtions import add_temp
from funtions import extract

URL="http://programmer100.pythonanywhere.com/"
timern=time.strftime("%Y-%m-%d-%H-%M-%S")


#st.title("Average Temperatures")

source=(scrape(URL))
extracted=extract(source)
add_temp(extracted)



