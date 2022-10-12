# Calculadora de la tasa de cambio representativa actual de la divisa, basándose en datos de precios, 
# en anuncios de compra-venta publicados por las personas, y aplicandole
# formulas estadísticas para lograrlo
from statistics import mean, median_grouped, mode
from abc import ABC

class currency(ABC):
    
    def __init__(self, supply : float, demand : float) -> None:
        self.supply = supply
        self.demand = demand
        self.historical_values = [float]
        self.supply_demand_rate = self.demand - self.supply
        
    def add_to_histv(self, value : float):
        self.historical_values.append(value)

class usd(currency):
    
    def __init__(self, supply: float, demand: float, initial_price : float) -> None:
        self.value = initial_price
        super().__init__(supply, demand)
        
    def __str__(self) -> str:
        return "usd"

class euro(currency):

    def __init__(self, supply: float, demand: float, initial_price : float) -> None:
        self.value = initial_price
        super().__init__(supply, demand)
    
    def __str__(self) -> str:
        return "euro"

class eltoque:
    
    def __init__(self, publication_frec : int, announcement_count : int, statistical_method : str, initial_values : dict, supply_demand : dict):
        self.publication_frec = publication_frec
        self.announcement_count = announcement_count
        self.statistical_method = statistical_method
        self.usd = usd(supply_demand.get("usd")[0], supply_demand.get("usd")[1], initial_values.get("usd"))
        self.euro = euro(supply_demand.get("euro")[0], supply_demand.get("euro")[1], initial_values.get("euro"))
        self.not_published_values : dict = initial_values # Diccionario con las divisas y sus valores publicados
        
    
    def calc_new_price(self, prices_list : list, currency_name : str) -> None:
        
        short_prices_list = []
        new_value = 0
        for i in range (self.announcement_count):
            short_prices_list.append(prices_list[i])
        
        if self.statistical_method == "mode":
            new_value = mode(short_prices_list)
        
        if self.statistical_method == "median":
            new_value = median_grouped(short_prices_list)
        
        if self.statistical_method == "mean":
            new_value = mean(short_prices_list)
        
        if currency_name == "usd":
            self.not_published_values["usd"] = new_value
            self.usd.add_to_histv(new_value)
        else:
            self.not_published_values["euro"] = new_value
            self.euro.add_to_histv(new_value)
            
    def publish_prices(self) -> None:
        self.usd.value = self.not_published_values["usd"]
        self.euro.value = self.not_published_values["euro"]
        