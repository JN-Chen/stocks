from stocks.stock_ts import *
from data.data import *

def get_all_and_store(data, stock, str_day, df):
    code_list = stock.get_code_list(df)
    for code in code_list:
        df_code = stock.daily_detail(str_day, code)
        data.store_data(str_day, code+".csv", df_code)
    return code_list

def get_daily_and_store(data, stock, str_day):
    df = stock.daily(str_day)
    data.mk_data_dir(str_day)
    data.store_data(str_day ,"daily.csv", df)
    return df

if __name__ == "__main__":
    stock = Stock()
    data = Data()
    str_day = data.today()
    while True:
        if stock.is_trade_date(str_day):
            if data.check_data_dir(str_day):
                print(str_day, " exists quit")
                break
            df = get_daily_and_store(data, stock, str_day)
            code_list = get_all_and_store(data, stock, str_day, df)
            print(str_day, " write csv all ", len(code_list), " codes")
        else:
            print(str_day, " is not trade day")
        str_day = data.prevday(str_day)
    