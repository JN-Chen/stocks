import time
import datetime
import os
import pandas as pd
class Data():
    def __init__(self):
        self.__TIME_FMT = "%Y%m%d"
        self.__root_path = "sotck_data"
        self.__mk_dir(os.path.join(os.getcwd(), self.__root_path))
    def __mk_dir(self, dir):
        exists = os.path.exists(dir)
        if not exists:
            os.makedirs(dir)
    def today(self):
        return time.strftime(self.__TIME_FMT, time.localtime())
    def prevday(self, str_date):
        time_datetime = datetime.datetime.strptime(str_date, self.__TIME_FMT)
        time_prevday = time_datetime - datetime.timedelta(days = 1)
        return time_prevday.strftime(self.__TIME_FMT)