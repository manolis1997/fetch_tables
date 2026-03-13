class UnityCatalog:
    def __init__(self, env):
        self.env = env
        self.SALES_CATALOG= f"sales_catalog_{self.env}"
        self.ORDERS_CATALOG= f"order_catalog_{self.env}"
    
    