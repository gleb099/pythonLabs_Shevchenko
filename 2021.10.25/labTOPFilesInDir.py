import operator
import os
import collections

dir = "C:\\Users\\gleb9\\source\\repos\\FindAndHighlightText\\FindAndHighlightText\\bin\\Debug\\net6.0"
files = []

class File:
    def __init__(self, name, end, size, namesize, endsize):
        self.name = name
        self.end = end
        self.size = size
        self.namesize = namesize
        self.endsize = endsize
    def __repr__(self):
        return repr((self.name, self.end, self.size, self.namesize, self.endsize))

os.chdir(dir)

for item in os.listdir():
    end = ""
    start = item.split('.')[0]
    if (len(item.split('.')) > 1):
        end = item.split('.')[-1]
    if os.path.isfile(item):
        files.append(File(start, end, os.path.getsize(item), len(start), len(end)))

print(files)
print()

print(1)
for i in sorted(files, key=lambda file: file.name, reverse=True)[:5]:
    print(f"{i.name}")
print()
print(2)
for i in sorted(files, key=lambda file: file.end, reverse=True)[:5]:
    print(f"{i.end}")
print()
print(3)
for i in sorted(files, key=lambda file: file.size, reverse=True)[:5]:
    print(f"{i.name}.{i.end} {i.size}")
print()
print(4)
for i in sorted(files, key=lambda file: file.size)[:5]:
    print(f"{i.name}.{i.end} {i.size}")
print()
print(5)
for i in sorted(files, key=lambda file: file.namesize, reverse=True)[:5]:
    print(f"{i.name}.{i.end} {i.namesize}")
print()
print(6)
for i in sorted(files, key=lambda file: file.endsize, reverse=True)[:5]:
    print(f"{i.name}.{i.end} {i.endsize}")
print()
print(7)
for i in sorted(files, key=lambda file: file.namesize)[:5]:
    print(f"{i.name}.{i.end} {i.namesize}")
print()
print(8)
for i in sorted(files, key=lambda file: file.endsize)[:5]:
    print(f"{i.name}.{i.end} {i.endsize}")
print()