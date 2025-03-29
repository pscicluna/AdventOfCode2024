import re
from pathlib import Path

import numpy as np


# 1D sequence-finder from https://stackoverflow.com/a/36535397
def search_sequence_numpy(arr,seq):
    """ Find sequence in an array using NumPy only.

    Parameters
    ----------    
    arr    : input 1D array
    seq    : input 1D array

    Output
    ------    
    Output : 1D Array of indices in the input array that satisfy the 
    matching of input sequence in the input array.
    In case of no match, an empty list is returned.
    """

    # Store sizes of input array and sequence
    Na, Nseq = arr.size, seq.size

    # Range of sequence
    r_seq = np.arange(Nseq)

    # Create a 2D array of sliding indices across the entire length of input array.
    # Match up with the input sequence & get the matching starting indices.
    M = (arr[np.arange(Na-Nseq+1)[:, None] + r_seq] == seq).all(1)

    # Get the range of those indices as final output
    if M.any() > 0:
        return np.where(np.convolve(M, np.ones((Nseq), dtype=int)) > 0)[0]
    else:
        return []       # No match found  

      
def get_diagonals(a):
    # Then a list comprehension is used to collect all the diagonals.  The range
    # is -x+1 to y (exclusive of y), so for a matrix like the example above
    # (x,y) = (4,5) = -3 to 4.
    diags = [a[::-1,:].diagonal(i) for i in range(-a.shape[0]+1,a.shape[1])]

    # Now back to the original array to get the upper-left-to-lower-right diagonals,
    # starting from the right, so the range needed for shape (x,y) was y-1 to -x+1 descending.
    diags.extend(a.diagonal(i) for i in range(a.shape[1]-1,-a.shape[0],-1))

    return diags


if __name__ == "__main__":
    datafile = Path(__file__).parent / "data" / "day4_input.txt"
    with open(datafile, 'r', encoding='utf-8') as f:
        data = f.read().splitlines()

    data = np.array(data)

    # convert the characters to numbers for easier processing
    data = np.array([list(map(
        int, re.sub(r"[X]", "0",
                    re.sub(r"[M]", "1",
                            re.sub(r"[A]", "2",
                                   re.sub(r"[S]", "3", x)
                                   )
                           )
                    )
                    )) for x in data
        ])

    print(data)

    # Find sequence 0123 forwards, backwards, up and down usings search_sequence_numpy
    # This will give us the indices of the start of each sequence
    count=0
    for row in data:
        # forwards
        count += len(search_sequence_numpy(row, np.array([0, 1, 2, 3])))//4
        # backwards
        count += len(search_sequence_numpy(row, np.array([3, 2, 1, 0])))//4

    for row in data.T:  # transpose to search up and down
        # up
        count += len(search_sequence_numpy(row, np.array([0, 1, 2, 3])))//4
        # print(search_sequence_numpy(row, np.array([0, 1, 2, 3])))
        # down
        count += len(search_sequence_numpy(row, np.array([3, 2, 1, 0])))//4
        # print(search_sequence_numpy(row, np.array([3, 2, 1, 0])))

    # Now we have to do the diagonals. This is more irritating because we have to
    # find the diagonals first. We can't just extract the diagonals to a new array
    # because the diagonals are not the same length.

    diags = get_diagonals(data)
    for diag in diags:
        # forwards
        count += len(search_sequence_numpy(diag, np.array([0, 1, 2, 3])))//4
        # backwards
        count += len(search_sequence_numpy(diag, np.array([3, 2, 1, 0])))//4
        # print(diag)
        # print(search_sequence_numpy(diag, np.array([0, 1, 2, 3])))
        # print(search_sequence_numpy(diag, np.array([3, 2, 1, 0])))
        # exit()

    diags = get_diagonals(data.T)
    for diag in diags:
        # up
        count += len(search_sequence_numpy(diag, np.array([0, 1, 2, 3])))//4
        # down
        count += len(search_sequence_numpy(diag, np.array([3, 2, 1, 0])))//4

    print(count)
