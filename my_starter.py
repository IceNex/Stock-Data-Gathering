# Create a program that takes one argument (stock ticker) and retrieve some data points.

# I want to pull stock information from amazon (AMZN) and plot on graph over 20 years.
import yfinance as yf

start_date = "2005-01-01"

end_date = "2025-04-08"

ticker_amazon = "AMZN"

ticker_apple = "AAPL"

ticker_google = "GOOG"

data_amazon = yf.download(ticker_amazon, start_date, end_date)

data_apple = yf.download(ticker_apple, start_date, end_date)

data_google = yf.download(ticker_google, start_date, end_date)

# print(data_amazon)

# print(data_apple)

# print(data_google)
# two array

# ticker_list
ticker_list = ["AMZN, AAPL, GOOG"]
# print(ticker_list)

# result_tuple
result_tuple = (data_amazon, data_apple, data_google)
# print(result_tuple)

# for loop
for stocks in ticker_list:
    #    print(stocks)

    for data in result_tuple:
        #    print(data)

        # put it all in a function

        def stocks(name):
            return result_tuple


print(stocks("AMZN"))
