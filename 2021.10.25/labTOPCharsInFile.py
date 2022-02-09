import operator
import collections

file = "fileStat.txt"

with open(file) as f:
    c = collections.Counter(f.read())
    print(c)
    for key, value in c.items():
        print(repr(key), value)
    print()
    for key, value in sorted(c.items(), key=operator.itemgetter(1)):
        print(repr(key), value)
    print()
    for key, value in sorted(c.items(), key=operator.itemgetter(1)):
        if(key.isdigit()):
            print(repr(key), value)
    print()
    for key, value in sorted(c.items(), key=operator.itemgetter(1)):
        if(key.isalpha()):
            print(repr(key), value)