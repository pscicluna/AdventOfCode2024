import numpy as np
from pathlib import Path


if __name__ == "__main__":
    datafile = Path(__file__).parent / "data" / "day1_input.txt"
    with open(datafile) as f:
        data = np.loadtxt(f, dtype=int)

    loc1 = np.sort(data[:, 0])
    loc2 = np.sort(data[:, 1])

    print(loc1.shape)

    dist = np.abs(loc1 -  loc2)
    print(dist.sum())



    ############# PART 2################

    loc1 = data[:, 0]
    loc2 = data[:, 1]

    # for each entry in loc1, count how many times it appears in loc2

    # First we're going to make a square array where each row is the same as loc2
    locrep = np.tile(loc2, (loc1.shape[0], 1))

    # Now we're going to subtract loc1 from locrep
    diff = locrep - loc1[:, np.newaxis]
    # print(diff, diff.shape)

    # Now we're going to count how many times each element in loc1 appears in loc2
    # by finding the number of zeros in each row
    counts = np.count_nonzero(diff == 0, axis=0)

    # print(counts)

    similarity = loc1 * counts
    # print(similarity)
    print(similarity.sum())

    # try it brute force...
    counts = np.zeros(loc1.shape[0])
    for i, l in enumerate(loc1):
        # how many times does l appear in loc2?
        count = np.count_nonzero(loc2 == l)
        # print(l, count)
        counts[i] = count

    # print(counts)
    similarity = loc1 * counts
    # print(similarity)
    print(similarity.sum())
