import argparse
import os
class Enviroment:
    @property
    def fetch_enviroment(self) -> str:
        parser = argparse.ArgumentParser()
        parser.add_argument("environment")

        args = parser.parse_args()
        env = args.environment
        
        return env

    @property
    def fetch_enviroment_variable(self):
        return os.getenv('MODE')
