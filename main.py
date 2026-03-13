from utils.logging.logger import logger
from utils.enviroment.enviroment import Enviroment
from database.schema import Schema
from database.unity_catalog import UnityCatalog
from utils.tables.tables import Tables

"""
This app fetch an enviroment variable 
and
define some untiy_catalog's, schema's and table's
"""

log = logger()

env = Enviroment().fetch_enviroment_variable

if env not in ["dev","stg", "prd"]:
    log.error("Invalid Environment name")

table_name = UnityCatalog(env).SALES_CATALOG + "." + Schema(env).SALES_SCHEMA + "." + Tables(env).SALES_TABLE

log.info(f"The table name is {table_name}")