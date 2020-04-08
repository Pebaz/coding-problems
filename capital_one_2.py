def findSmallestDivisor(s, t):
    if len(s) % len(t) != 0: return -1
    if s[:len(t)] != t: return -1
    
    for j in range(len(s) // len(t)):
        if t * j not in s:
            return -1
    
    for i in range(len(t)):
        word = t[:i + 1]
        if word * (len(t) // len(word)) == t:
            return len(word)

    return len(t * i)







def findSmallestDivisor(s, t):
    ls, lt = len(s), len(t)
    
    # Handle edge cases including:
    #  * `s` not being divisible by `t`
    #  * `t` not being the start of `s`
    #  * `t` repeated not being `s`
    if any((ls % lt != 0, s[:lt] != t, t * (ls // lt) != s)):
        return -1

    # Find the smallest set of characters in `t` that can be used to build both
    for i in range(len(t)):
        word = t[:i + 1]

        # Return the smallest word that can be used to build both strings
        if word * (len(t) // len(word)) == t:
            return len(word)
            
    return len(t * i)