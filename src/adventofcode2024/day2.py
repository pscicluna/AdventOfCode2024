from pathlib import Path
import numpy as np


if __name__ == "__main__":
    datafile = Path(__file__).parent / "data" / "day2_input.txt"
    data = []
    max_levels = 0
    levels = []
    with open(datafile, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            # print(line)
            data.append(np.array(line.strip().split(" "), dtype=int))
            level = len(data[-1])
            levels.append(level)
            if level > max_levels:
                max_levels = level

    levels = np.array(levels)

    data_array = np.zeros((len(data), max_levels), dtype=int)
    for i, d in enumerate(data):
        data_array[i, :len(d)] = d
    diffs = data_array[:, 1:] - data_array[:, :-1]
    # print(diffs)
    # fix the diffs for the elements that are out of range for each row
    # diffs[:, levels[levels<=diffs.shape[1]]-1] = 0
    for i, level in enumerate(levels):
        if level <= diffs.shape[1]:
            diffs[i, level-1:] = 0
    signs = np.array([np.sign(d) for d in diffs])
    max_diffs = np.abs(diffs).max(axis=1)
    safe = []
    for i, d in enumerate(diffs):
        # print(d) # .shape)
        # print(levels[i])
        # print(d[:levels[i]-1]) #.shape)
        s = np.sign(d[:levels[i]-1])
        # print(s)
        m = np.max(np.abs(d[:levels[i]-1]))
        # print(m)
        if np.any(s == 0):
            # some zeros, so not safe
            safe.append(False)
        elif np.all(s == 1) or np.all(s == -1):
            # all the same sign, so safe as long as the max is less than 3
            safe.append(m <= 3)
        else:
            # different signs, so unsafe
            safe.append(False)
    safe = np.array(safe)
    print(safe.sum())

    #  ############# PART 2 ################
    print("Part 2")
    # the problem dampener can remove up to one unsafe element to make a
    # report safe!
    # so we can remove one element from the unsafe list and see if the report
    # is safe
    for i, d in enumerate(data): 
        if not safe[i]:  # only check the unsafe ones!
            # n_unsafe = 0
            row = d[:levels[i]].copy()
            for j in range(levels[i]):
                # delete an entry
                row_new = np.delete(row[:levels[i]], j)
                # print(i, row[:levels[i]], row_new, j)
                # recompute teh diffs
                d_new = np.diff(row_new)
                # print(d_new)
                s2 = np.sign(d_new)
                m2 = np.max(np.abs(d_new))
                if np.any(s2 == 0):
                    # still unsafe!
                    continue
                if (np.all(s2 == 1) or np.all(s2 == -1)) and m2 <= 3:
                    safe[i] = True
                    break

            # # THis had the wrong logic - you actually have to re-calculate the differences!
            # for j, dl in enumerate(d[:levels[i]-1]):
            #     d2 = np.delete(d[:levels[i]-1].copy(), j)
            #     # print(len(d2), len(d[:levels[i]-1]))
            #     s2 = np.sign(d2)
            #     m2 = np.max(np.abs(d2))
            #     if np.any(s2 == 0):
            #         continue  # still unsafe
            #     if (np.all(s2 == 1) or np.all(s2 == -1)):
            #         if m2 <= 3:
            #             safe[i] = True
            #             break
            #         continue
            # if not safe[i]:
            #     print(i, d[:levels[i]-1])
            #     # print(safe[i])
            # # exit()

    print(safe.sum())
