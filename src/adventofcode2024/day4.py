import re
from pathlib import Path

import numpy as np


if __name__ == "__main__":
    datafile = Path(__file__).parent / "data" / "day4_input.txt"
    with open(datafile, 'r', encoding='utf-8') as f:
        data = f.read().splitlines()