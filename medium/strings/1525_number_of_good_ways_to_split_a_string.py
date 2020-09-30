def num_splits(s):
    """
    :type s: str
    :rtype: int
    Note: Return number of "good" splits.
    "Good" split - on left and right side an equal count of unique letters.
    """

    good_splits = 0

    # Mapping for future checking.
    counter = dict()

    # Counters unique letters
    left_set = set()
    right_set = set()

    ln = len(s)

    # Double-counting loop.
    for index in range(ln - 1):
        left_set.add(s[index])
        right_set.add(s[ln - index - 1])

        counter[index + 1] = (len(left_set), len(right_set))

    # Counting matches.
    for key in counter.keys():
        if counter[key][0] == counter[ln - key][1]:
            good_splits += 1

    return good_splits
