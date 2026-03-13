from database.unity_catalog import UnityCatalog

class Tables:
    def __init__(self, env):
        self.env = env
        self.SALES_TABLE= f"sales_table_{self.env}"
        self.ORDERS_TABLE= f"order_table_{self.env}"

    