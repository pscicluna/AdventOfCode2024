import re
from pathlib import Path

import numpy as np


if __name__ == "__main__":
    datafile = Path(__file__).parent / "data" / "day3_input.txt"
    with open(datafile, 'r', encoding='utf-8') as f:
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
        if m := re.findall(expr, d):
            # print(m)
            muls.extend(m)
        else:
            print("No match")

    # print(muls)
    muls = np.array(muls, dtype=int)
    # print(muls)
    prods = muls[:, 0] * muls[:, 1]
    print(f"Part 1 result: {prods.sum()}")

    #  ############# PART 2 ################
    # We have to account for the presence of don't() calls at the end of lines
    # in the input,
    # so we merge all the lines into one string first and split it by the
    # presence of do() calls
    data_2 = ["".join(data)]
    # first split the input by the presence of do() calls
    dos = []
    do_expr = r"do\(\)"
    dont_expr = r"don\'t\(\)"
    for d in data_2:
        dos.extend(re.split(do_expr, d))
    donts = [re.split(dont_expr, d) for d in dos]
    muls2 = []
    for d in donts:
        muls2.extend(re.findall(expr, d[0]))
    muls2 = np.array(muls2, dtype=int)
    # print(muls2)
    prods2 = muls2[:, 0] * muls2[:, 1]
    print(f"Part 2 result: {prods2.sum()}")
