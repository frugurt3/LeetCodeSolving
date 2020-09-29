words_test_case = ["ef", "fq", "ao", "at", "lx"]
pattern_test_case = "ya"
words_test_case = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
pattern_test_case = "abb"


def find_n_replace_pattern(words: list, pattern: str):
    """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        Note: brute-force solution, not best logic
    """
    result = []

    for word in words:
        # Mapping with pattern for every word.
        checker = dict()
        # Length of correct symbols in every checking word.
        res_len = 0
        for word_letter, pattern_letter in zip(word, pattern):
            check_value = checker.get(pattern_letter, '')
            if check_value:
                if check_value == word_letter:
                    res_len += 1
                else:
                    break
            # Letter from word must be not in values of checker dictionary.
            elif word_letter in checker.values():
                break
            else:
                res_len += 1
                checker[pattern_letter] = word_letter

        if res_len == len(pattern):
            result.append(word)
    return result


def find_n_replace_pattern_filter(words: list, pattern: str):
    """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        Note: solutions with filter. Fast, but time complexity still O(n**2).
        For except situation, when one letter matching with many letters, we checking count of unique combination.
        When match - we grab that word to result. Filter works faster, then for-loop.
        List converting added, because in task description was "return list".
    """
    return list(filter(lambda word: len(set(word)) == len(set(pattern)) == len(set(zip(word, pattern))), words))

