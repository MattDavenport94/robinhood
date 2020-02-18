import config
from Robinhood import Robinhood

robinhood = Robinhood()

logged_in = robinhood.login(username=config.username, password=config.password)

stock = robinhood.instruments("SBUX")[0]

print("Printing stock instrument info")
print(stock)

quote = robinhood.quote_data("SBUX")

print("Printing quote data for Starbucks")
print(quote)
