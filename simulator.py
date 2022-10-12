import price_estimator
import eltoque
from random import uniform
from statistics import NormalDist

class tools:
    # Generador de personas
    @staticmethod
    def persons_generator(count : int) -> list:
        persons = []
        x = NormalDist(0, 5).samples(count)
        while count != 0:
            persons.append(price_estimator.person(round(x[count - 1], 1)))
            count -= 1
        return persons
    # Dada una lista de anuncios y una moneda, genera su lista de precios
    @staticmethod
    def prices_list_generator(announcements_list : list, currency : str) -> list:
        prices_list=[]
        for a in announcements_list:
            if a.currency == currency:
                prices_list.append(a.price)
        return prices_list
            
            
    
class simulation:
    
    def __init__(self, announcements_count : int, analized_prices : int, publication_frec : int, statistical_method : str, init_values : dict, supply_demand : dict) -> None:
        self.announcements_count = announcements_count
        self.analized_prices = analized_prices
        self.publication_frec = publication_frec
        self.statistical_method = statistical_method
        self.supply_demand = supply_demand
        self.init_values = init_values
        
    def run_simulation(self, steps) -> None:
        round : int = 0
        
        # Generar eltoque
        et = eltoque.eltoque(self.publication_frec, self.analized_prices, self.statistical_method, self.init_values, self.supply_demand)
        price_estimator.et = et
        while round < steps:
            round += 1
            # Generar personas
            persons = tools.persons_generator(self.announcements_count)
            
            # Generar anuncios
            announcements = []
            for p in persons:
                announcements.append(p.post_announcement())
                
            # Calcular nuevos precios
            prices_list = tools.prices_list_generator(announcements,"usd")
            prices_list1 = tools.prices_list_generator(announcements, "euro")
            et.calc_new_price(prices_list, "usd")
            et.calc_new_price(prices_list1, "euro")
     
            # Publicamos los precios si toca
            if round % self.publication_frec == 0:
                et.publish_prices()
            
            # Imprimir valores
            print(f"Round {round}: usd = {et.usd.value}, euro = {et.euro.value}")    
            print("------------------------------------------------------------")
            


s = simulation(300, 100, 1, "median", {"usd" : 100, "euro" : 110}, {"usd" : (0.4, 0.8), "euro" : (0.4, 0.8)})
s.run_simulation(100)

