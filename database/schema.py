class Schema:
    def __init__(self,env):
        self.env = env
        self.SALES_SCHEMA= f"sales_schema_{self.env}"
        self.ORDERS_SCHEMA= f"sales_schema_{self.env}"
    
    