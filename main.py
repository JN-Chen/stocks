from stocks.stock_ts import *
from data.data import *
import sys

def check_write(dir, name, cover):
    write = False
    if data.check_data(dir ,name):
        if cover:
            write = True
    else:
        write = True
    return write

def get_all_and_store(data, stock, str_day, df, cover):
    code_list = stock.get_code_list(df)
    store_cnt = 0
    for code in code_list:
        write = check_write(str_day ,code+".csv", cover)
        print('check', code, "write=", write)
        if write == False:
            continue
        df_code = stock.daily_detail(str_day, code)
        data.store_data(str_day, code+".csv", df_code)
        store_cnt = store_cnt + 1
    return code_list, store_cnt

def get_daily_and_store(data, stock, str_day, cover):
    df = 0
    write = check_write(str_day ,"daily.csv", cover)
    if write :
        df = stock.daily(str_day)
        data.mk_data_dir(str_day)
        data.store_data(str_day ,"daily.csv", df)
    else :
        df = data.load_data(str_day ,"daily.csv")
    return df

if __name__ == "__main__":
    stock = Stock()
    data = Data()
    str_day = data.today()
    cover = False
    all_detail = False
    code_list = []
    store_cnt = 0
    if sys.argv[4] == "1" :
        all_detail = True
    if sys.argv[3] == "1" :
        cover = True
    if sys.argv[1] != "-" :
        str_day = sys.argv[1]
    end_day = sys.argv[2]
    print("run begin day:", str_day, " to day:", end_day, " cover:", cover, " detail:", all_detail)
    while True:
        if data.compare_time(str_day, end_day) == True:
            break
        if stock.is_trade_date(str_day):
            df = get_daily_and_store(data, stock, str_day, cover)
            if all_detail:
                code_list, store_cnt = get_all_and_store(data, stock, str_day, df, cover)
            print(str_day, " write csv all ", len(code_list), " codes store count:", store_cnt)
        else:
            print(str_day, " is not trade day")
        str_day = data.prevday(str_day)
    