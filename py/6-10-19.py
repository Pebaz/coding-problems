"""
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

def subber(s, k):
    if k == 0:
        return ''
    elif k == 1:
        return s[0]
    p1 = 0
    p2 = 1
    prv = ''
    while p2 <= len(s):
        string = s[p1:p2]
        l = len(set(string))
        if l <= k:
            if len(string) > len(prv):
                prv = string
            p2 += 1
        if l > k:
            p1 += 1
    return prv

print(subber('abcba', 2))
print(subber('abcccccccccbbbbbbaaaaaaaaaaaaaaaaaaaaaa', 2))
