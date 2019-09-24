from stocks.stock_ts import *
if __name__ == "__main__":
    stock = Stock()
    data_l = stock.get_stocks()
    print(stock.daily('20180816'))