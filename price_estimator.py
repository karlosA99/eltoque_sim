# Estimador del precio de compra-venta que utilizarían las personas, basándose en el precio de eltoque,
# la velocidad con que quieran vender la divisa, la relacion oferta-demanda actual. (tal vez posibles 
# noticias que afecten el precio)

from random import randint, random
import eltoque

et = eltoque.eltoque(1, 1, "mode", {"usd" : 1, "euro" : 1 }, {"usd" : (1,1), "euro" : (1,1)})

class announcement:
    def __init__(self, type, price, currency : str):
        self.type = type
        self.price = price
        self.currency = currency

class person:
    
    def __init__(self, need_to_sell : float):
        self.need_to_sell = need_to_sell
    
    # 0-compra, 1-venta
    def type_ann_gen() -> int:  
        return randint(0, 1)
    
    def calc_price(self, curr : str) -> float:
        usd_price = et.usd.value + et.usd.supply_demand_rate + self.need_to_sell
        euro_price = et.euro.value + et.euro.supply_demand_rate + self.need_to_sell
        return usd_price if curr == "usd" else euro_price
    
    def currency_gen(self):
        r = randint(0,1)
        return "usd" if r == 0 else "euro"
    
    def post_announcement(self) -> announcement:
        # 0-compra, 1-venta
        tp = randint(0,1)
        curr = self.currency_gen()
        pr = self.calc_price(curr)
        return announcement(tp, pr, curr)