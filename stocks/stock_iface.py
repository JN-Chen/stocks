import abc
class Stock_Iface():
    __metaclass__ = abc.ABCMeta
    def __init__(self):
        pass
    @abc.abstractmethod
    def get_stocks(self):
        pass
    @abc.abstractmethod
    def daily(self, date):
        pass
    @abc.abstractmethod
    def daily_detail(self, date, code):
        pass
    pass