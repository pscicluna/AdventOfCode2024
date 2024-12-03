import re
from pathlib import Path

import numpy as np


if __name__ == "__main__":
    datafile = Path(__file__).parent / "data" / "day3_input.txt"
    with open(datafile, 'r') as f:
        data = f.readlines()
    print(len(data))

    # We want to match patterns like:
    #  mul(111,222), with up to 3 digits in each number
    # *anything* else is noise

    # re.compile(r"mul\((\d+),(\d+)\)")
    # re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    expr = r"mul\((\d{1,3}),(\d{1,3})\)"

    # now we want to run this on the data
    # and sum the results
    muls = []
    for d in data:
        m = re.findall(expr, d)
        if m:
            # print(m)
            muls.extend(m)
        else:
            print("No match")
    
    # print(muls)
    muls = np.array(muls, dtype=int)
    print(muls)
    prods = muls[:, 0] * muls[:, 1]
    print(f"Part 1 result: {prods.sum()}")

    #  ############# PART 2 ################

    