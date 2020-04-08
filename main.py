import sys, os
sys.path.append('/media/cjn/hdd1/stocks')
print(sys.path)
from stocks.stock_ts import *
from data.data import *

def check_write(dir, name, cover):
    write = False
    if data.check_data(dir ,name):
        if cover:
            write = True
    else:
        write = True
    if write == False and name == "daily.csv":
        df = data.load_data(dir ,name)
        code_list = stock.get_code_list(df)
        if len(code_list) <= 10 :
            print(dir, name, "wrong code list len rewrite")
            write = True
    return write

def get_all_and_store(data, stock, str_day, df, cover):
    code_list = stock.get_code_list(df)
    store_cnt = 0
    none_cnt = 0
    for code in code_list:
        write = check_write(str_day ,code+".csv", cover)
        if write == False:
            continue
        df_code = stock.daily_detail(str_day, code)
        if df_code is not None:
            data.store_data(str_day, code+".csv", df_code)
            store_cnt = store_cnt + 1
        else:
            none_cnt = none_cnt + 1
    return code_list, store_cnt, none_cnt

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
    end_day = data.prevNday(str_day, 5)
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
    if sys.argv[2] != "-" :
        end_day = sys.argv[2]
    print("run begin day:", str_day, " to day:", end_day, " cover:", cover, " detail:", all_detail)
    while True:
        if data.compare_time(str_day, end_day) == True:
            break
        if stock.is_trade_date(str_day):
            df = get_daily_and_store(data, stock, str_day, cover)
            if all_detail:
                code_list, store_cnt, none_cnt = get_all_and_store(data, stock, str_day, df, cover)
            print(str_day, " write csv all ", len(code_list), " codes store count:", store_cnt, " none count:", none_cnt)
        else:
            print(str_day, " is not trade day")
        str_day = data.prevday(str_day)
    
