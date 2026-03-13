import logging

def logger():
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger(__name__)