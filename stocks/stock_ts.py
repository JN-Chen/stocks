from stock_iface import *
import tushare as ts
import time
class Stock(Stock_Iface):
    def __init__(self):
        Stock_Iface.__init__(self)
        self.__TIME_FMT = "%Y%m%d"
        self.__TOKEN  = "3b239c5c08e5e691a718fb15dd986555fe2f7b11f1b078af61692fe0"
        self.__ts = ts.pro_api(self.__TOKEN)
        self.__today = time.strftime(self.__TIME_FMT, time.localtime(time.time()))
        self.__trade_date = self.__ts.query('trade_cal', start_date='20000101', end_date=self.__today)
        self.__stocks, _, _ = self.__get_stocks()

    def __update_trade_date(self):
        self.__today = time.strftime(self.__TIME_FMT, time.localtime(time.time()))
        self.__trade_date = self.__ts.query('trade_cal', start_date='20000101', end_date=self.__today)

    def __get_stocks(self):
        data_l = self.__ts.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
        data_d = self.__ts.stock_basic(exchange='', list_status='D', fields='ts_code,symbol,name,area,industry,list_date')
        data_p = self.__ts.stock_basic(exchange='', list_status='P', fields='ts_code,symbol,name,area,industry,list_date')

        data_l.rename(columns={'symbol' : 'code', 'list_date' : 'date'}, inplace = True)
        data_l.drop('ts_code',axis=1, inplace=True)
        return data_l, data_d, data_p

    def get_stocks(self):
        return self.__stocks
    
    def is_trade_date(self, date):
        open_td = self.__trade_date[self.__trade_date['is_open'] == 1]
        return date in open_td['cal_date'].values
    
    def daily(self, date):
        df = self.__ts.daily(trade_date=date)
        df['ts_code'] = df['ts_code'].str[0:6]
        df.rename(columns={'ts_code' : 'code', 'trade_date' : 'date'}, inplace = True)
        return df
    
    def daily_detail(self, date, code):
        df = ts.get_tick_data(code, date=date, src='tt')
        return df
    
    def get_code_list(self, df):
        return df['code'].values