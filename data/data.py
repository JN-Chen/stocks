import time
import datetime
import os
import pandas as pd
import numpy as np
class Data():
    def __init__(self):
        self.__TIME_FMT = "%Y%m%d"
        self.__root_path = "stock_data"
        self.__mk_dir(os.path.join(os.getcwd(), self.__root_path))

    def __mk_dir(self, dir):
        exists = os.path.exists(dir)
        if not exists:
            os.makedirs(dir)

    def check_data_dir(self, dir):
        path = os.path.join(os.path.join(os.getcwd(), self.__root_path), dir)
        return os.path.exists(path)

    def mk_data_dir(self, dir):
        path = os.path.join(os.path.join(os.getcwd(), self.__root_path), dir)
        if os.path.exists(path) == False :
            os.makedirs(path)

    def check_data(self, dir, name):
        path = os.path.join(os.path.join(os.path.join(os.getcwd(), self.__root_path), dir), name)
        return os.path.exists(path)

    def store_data(self, dir, name, df):
        path = os.path.join(os.path.join(os.path.join(os.getcwd(), self.__root_path), dir), name)
        df.to_csv(path)
    
    def load_data(self, dir, name):
        path = os.path.join(os.path.join(os.path.join(os.getcwd(), self.__root_path), dir), name)
        return pd.read_csv(path, dtype = {'code': np.str_})

    def today(self):
        return time.strftime(self.__TIME_FMT, time.localtime())

    def prevday(self, str_date):
        time_datetime = datetime.datetime.strptime(str_date, self.__TIME_FMT)
        time_prevday = time_datetime - datetime.timedelta(days = 1)
        return time_prevday.strftime(self.__TIME_FMT)

    def compare_time(self, time1, time2):
        #dtime1 = datetime.datetime.strptime(time1, self.__TIME_FMT)
        #dtime2 = datetime.datetime.strptime(time2, self.__TIME_FMT)
        #print("cmp", time1, time2, "date time", dtime1, dtime2)
        return time1 == time2