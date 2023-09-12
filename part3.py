import pathlib
import sys
import parse

# data_path = "day8_folder/day8_example.txt"
# data_path = "day8_folder/day8.txt"
data_path = "day8_folder/single_line.txt"

digit_total = 0
fin = open(data_path)
for line in fin:
    signals, digits = map(str.split, line.split('|'))
    # signals = tuple(map(lambda p: (frozenset(p), len(p)), signals))
    # digits   = tuple(map(lambda p: (frozenset(p), len(p)), digits))
    # exclude len in tuple
    signals = tuple(map(lambda p: (frozenset(p)), signals))
    digits   = tuple(map(lambda p: (frozenset(p)), digits))

    print(f"signals = ", signals)
    print(f"digits = ", digits)

    # s2d = decode_patterns(signals)
# print(s2d)

    # digit_total += s2d[digits[0][0]] * 1000
    # digit_total += s2d[digits[1][0]] * 100
    # digit_total += s2d[digits[2][0]] * 10
    # digit_total += s2d[digits[3][0]] 

print("Part 2 =", digit_total)
