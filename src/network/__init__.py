import json
import os

import src.utils as utils
from .ops import *

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def get_urls():
    with open(f'{CURRENT_DIR}/urls.json', 'r') as f:
        return json.load(f)


def get_source(ticker: str) -> Optional[str]:
    return utils.get_ticker_source(ticker, get_urls())
