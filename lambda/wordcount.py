"""
On the whiteboard, please write a version of the unix utility "wc" in the
language of your choice.

This is a rudimentary programming question, but it tests many things:

Working under stress. It requires the candidate to actually get up to the
whiteboard and write some code under observation. This tests how well they work
under pressure, and how well they can "think on their feet", literally. :-) I
make sure to not speak at all while they're writing code, unless they ask me a
question. It's best to let them sweat it out in total silence.
Basic programming abilities. Any competent programmer should be able to bang
this out with very little difficulty. if they can't do this, then you have to
wonder how well they know these languages that they say they know. If they try
to write pseudo-code, you can press them to actually write real syntax. However,
if they forget the exact name of a specific java method call in a specific
class, that's no big deal.
Understanding requirements and following instructions. See how well they can
reverse-engineer the feature set of wc. If they aren't familiar with wc, then
you can describe it to them. See how easily they pick up on your instructions.
Once they've written it one way, I usually ask them how they can implement it a
different way. This forces them to "think outside the box" and be creative.

Another variation: once they've solved it, you can add a requirement that the
program should report the number of distinct words in the file. In addition to
introducing a different data structure, this will also test their ability to
refactor their code, even if it is just a little.

WC Description:
    wc -l  print line count
    wc -c  print character count
    wc -w  print word count

f(text, l=False, w=False, c=False)

"""

import sys

def word_count(text, l=False, w=False, c=False):
    l, w, c = 0, 0, 0
    for line in text.splitlines():
        line = line.strip()
        l += 1
        words = line.split()
        w += len(words)
        for word in words:
            c += len([
                char for char in word if bool(char.strip())
            ])
    return l, w, c

def word_count(text, l=False, w=False, c=False):
    l, w, c = 0, 0, 0
    unique = set()
    for line in text.splitlines():
        line = line.strip()
        l += 1
        words = line.split()
        w += len(words)
        for word in words:
            word = word.strip()
            c += len([char for char in word if bool(char.strip())])
            unique.add(word)
    return l, w, c, len(unique)

def wc_cli():
    assert len(sys.argv) > 1
    flags = sys.argv[1]
    assert flags.startswith('-')
    lc = 'l' in flags
    wc = 'w' in flags
    cc = 'c' in flags
    text = sys.stdin.read()
    l, w, c, u = word_count(text, lc, wc, cc)
    if lc: print('Lines  :', l)
    if wc: print('Words  :', w)
    if cc: print('Chars  :', c)
    print('Unique :', u)

if __name__ == '__main__':
    l, w, c, u = word_count('hello world!\nhow are you?', True, True, True)
    assert l == 2
    assert w == 5
    assert c == 21
    assert u == 5

    wc_cli()
