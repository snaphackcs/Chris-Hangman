

# from functools import map, filter
import re

fp = open("托福词汇表", "r", encoding="utf-8")
_iter = fp.readlines()


def foo(pattern):
    def bar(s):
        if re.match(pattern, s):
            return True
        return False
    return bar


while True:
    pattern = input("pattern? ").lower().replace('_', '.')
    dic = [[pattern[0], 1]]
    if pattern[0] == "0":
        break
    idx = 0

    for i in range(1, len(pattern)):
        if pattern[i] == pattern[i-1]:
            print(pattern[i], pattern[i-1])
            dic[-1][1] += 1
        else:
            dic.append([pattern[i], 1])

    pat = ""
    for p in dic:
        pat += '{p[0]}{{{p[1]}}}'.format(p=p)
    pat += r'\s'

    print(pat)
    for i in filter(foo(pat), _iter):
        print(i)
