from stocks.stock_ts import *
from data.data import *
if __name__ == "__main__":
    stock = Stock()
    data = Data()
    str_day = data.today()
    while True:
        if stock.is_trade_date(str_day):
            print(str_day, " is trade day")
            if data.check_data_dir(str_day):
                print(str_day, " exists quit")
                break
            data.mk_data_dir(str_day)
            df = stock.daily(str_day)
            data.store_data(str_day, df)
            print(str_day, " write daily csv")
        else:
            print(str_day, " is not trade day")
        str_day = data.prevday(str_day)
    