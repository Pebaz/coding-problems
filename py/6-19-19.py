"""
This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""

def findall(string, key):
    found = []
    start = 0
    end = len(key) - 1
    while end != len(string):
        sub = string[start:end + 1]
        if sub == key:
            found.append(start)
        start += 1; end += 1
    return found


def sent(the_words, string):
	words = dict()
	for word in the_words:
		if word in string:
			indexes = findall(string, word)
			for i in indexes:
				words[word] = (i, i + len(word))  # start, end
	new = words.copy()
	for word in words:
		for other in words:
			if word != other:
				if words[word][0] >= words[other][0] and words[word][1] <= words[other][1]:
					del new[word]
	return [i for i in sorted(new, key=lambda x: new[x][0])]



print(sent('bed bath bedbath and beyond'.split(), 'bedbathandbeyond'))
print(sent('quick brown the fox'.split(), 'thequickbrownfox'))
print(sent('thing throne one you and should'.split(), 'onethingyoushouldthroneandone'))
