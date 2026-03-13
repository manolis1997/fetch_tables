from utils.enviroment.enviroment import Enviroment
from database.schema import Schema
from database.unity_catalog import UnityCatalog
from utils.tables.tables import Tables
import pytest
import sys

@pytest.mark.parametrize("env_name", ["dev", "stg", "prd"])
def test_table_names(env_name):
    sys.argv = ["test_tables.py", env_name]
    env = Enviroment().fetch_enviroment_variable

    assert env in UnityCatalog(env).SALES_CATALOG
    assert env in Schema(env).SALES_SCHEMA
    assert env in Tables(env).SALES_TABLE