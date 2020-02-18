import requests
import config
from bs4 import BeautifulSoup
from Robinhood import Robinhood

FEAR_AND_GREED_URL = "https://money.cnn.com/data/fear-and-greed/"
FEAR_AND_GREED_PHRASE = "Fear &amp; Greed Now: "
FEAR_THRESOLD = 20
GREED_THRESOLD = 80
INTSTRUMENT_TO_BUY = "SPY"

r = requests.get(FEAR_AND_GREED_URL)
html = r.content

soup = BeautifulSoup(html)

div = soup.find_all(id="needleChart")
div = str(div[0])

print(div)

position = div.find(FEAR_AND_GREED_PHRASE)
position = position + len(FEAR_AND_GREED_PHRASE)

current_fear_and_greed_index = int(div[position:position+3].strip())

print(current_fear_and_greed_index)
print(type(current_fear_and_greed_index))

others_are_greedy = current_fear_and_greed_index >= GREED_THRESOLD
others_are_fearful = current_fear_and_greed_index <= FEAR_THRESOLD

# robinhood setup
robinhood = Robinhood()
logged_in = robinhood.login(username=config.username, password=config.password)
instrument = robinhood.instruments(INTSTRUMENT_TO_BUY)[0]

print("Printing stock instrument info")
print(stock)

quote = robinhood.quote_data(INTSTRUMENT_TO_BUY)

print("Printing quote data for {}".format(INTSTRUMENT_TO_BUY))
print(quote)

if others_are_greedy:
    # sell
    sell_order = robinhood.place_sell_order(instrument, 1)

if others_are_fearful:
    # buy
    buy_order = robinhood.place_buy_order(instrument, 1)