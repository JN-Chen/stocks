from stock_iface import *

class Stock(Stock_Iface):
    def __init__(self):
        Stock_Iface.__init__(self)
        self.__TOKEN  = "3b239c5c08e5e691a718fb15dd986555fe2f7b11f1b078af61692fe0"
        pass
    def get_token(self):
        return self.__TOKEN