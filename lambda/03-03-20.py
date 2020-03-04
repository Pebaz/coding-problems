"""
7:47 - 8:33
Shortest Common Supersequence

Given two strings str1 and str2, find the length of the smallest string which
has both, str1 and str2 as its sub-sequences.
Note: str1 and str2 can have both uppercase and lowercase letters.

Input:
The first line of input contains an integer T denoting the number of test cases.
Each test case contains two space separated strings.

Example:
Input:
3
abcd xycd
efgh jghi
vtri trip
Output:
6
6
5

Strategy:
    1. Sort each string
    2. Compare each element from str1 with str2 to see if there are any similar
    3. Return count of each similar char.
"""

def scs(a, b):
    """
    Time: O(a + b)
    Space: O(min(a, b))
    """

    # NOTE: In practice, hashing the longer string will take more time
    if len(a) < len(b):
        a, b = b, a

    chars_by_count = {}
    for i in b:
        chars_by_count[i] = chars_by_count.get(i, 0) + 1
    
    count = 0

    for i in a:
        if i in chars_by_count and chars_by_count[i]:
            count += 1
            chars_by_count[i] -= 1

    return len(b) + len(a) - count


tests = []

def test(func):
    global tests
    tests.append(func)
    return func

def run_tests(trace=False):
    for test in tests:
        try:
            test()
        except AssertionError as e:
            if trace:
                raise e from e
            else:
                print('Test', test.__name__, 'failed.')
                continue
        print('Test', test.__name__, 'succeeded.')

@test
def test_expected():
    assert scs('abcd', 'xycd') == 6
    assert scs('efgh', 'jghi') == 6
    assert scs('triv', 'trip') == 5

@test
def test_upper_lower_cases():
    assert scs('abcd', 'ABCD') == 8
    assert scs('efgh', 'jghI') == 6
    assert scs('tivR', 'trip') == 6

@test
def test_special_characters():
    assert scs('abc!', 'xy!z') == 7
    assert scs('&&$%', '^%*!') == 7
    assert scs('....', '.!.!') == 6

@test
def test_repeated_characters():
    assert scs('aaa', 'baa') == 4

@test
def test_both_empty():
    assert scs('', '') == 0

@test
def test_one_empty():
    assert scs('', 'foo') == 3

@test
def test_one_longer():
    assert scs('abc', 'bcdefghijklmnop') == 16

if __name__ == '__main__':
    run_tests(True)
