import sys, os
sys.path.append('/media/hdd1/stocks')
print(sys.path)
from stocks.stock_ts import *
from data.data import *

def check_a_day(data, stock, str_day):
    ret = 0
    if data.check_data(str_day ,"daily.csv"):
        df = data.load_data(str_day ,"daily.csv")
        code_list = stock.get_code_list(df)
        for code in code_list:
            if data.check_data(str_day ,code+".csv") != True :
                df_code = stock.daily_detail(str_day, code)
                print(str_day, " code:", code, " is not exits, download and store")
                if df_code is not None:
                    data.store_data(str_day, code+".csv", df_code)
                    ret = ret +  1
    return ret

if __name__ == "__main__":
    check_count = 20
    data = Data()
    stock = Stock()
    str_day = data.today()
    count = 0
    if sys.argv[1] != "-" :
        str_day = sys.argv[1]
    while check_count:
        if data.compare_time(str_day, "20000101") == True:
            break
        count = check_a_day(data, stock, str_day)
        if count > 0 :
            check_count = check_count - 1
        print(str_day, " is checked, fix ", count, " code")
        str_day = data.prevday(str_day)
    print("fix done day ", str_day);
