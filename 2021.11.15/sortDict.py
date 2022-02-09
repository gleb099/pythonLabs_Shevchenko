dictLines = {"as": 5, "as1": 6, "as2": 3, "as3": 1}
sorted_dict = {}
sorted_keys = sorted(dictLines, key=dictLines.get)
print(sorted_keys)
for key in sorted_keys:
    sorted_dict[key] = dictLines[key]

print(sorted_dict)