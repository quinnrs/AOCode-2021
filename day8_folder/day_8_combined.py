import pathlib
import sys
import parse
from collections import OrderedDict


K_PATTERNS = "p"
K_DIGITS = "d"
P_WITH_UNIQUE_LENGTH = {2:1,3:7,4:4,7:8}

# data_path = "day8_folder/day8_example.txt"
data_path = "day8_folder/day8.txt"
# data_path = "day8_folder/single_line.txt"

# fin = open(data_path)
fin = open(data_path, 'r')
# unique_counter = 0
lines = fin.read().splitlines() # single line here

entry_list = []
count = 0

for line in lines:
    # print(line) # returns single line as exoected

    signals_and_digits = line.split(" | ")
    # print(signals_and_digits) # debug

    code_dict = { K_PATTERNS:signals_and_digits[0].split(" "), \
                 K_DIGITS:signals_and_digits[1].split(" ")}
    entry_list.append(code_dict)
    for d in code_dict[K_DIGITS]:
        if len(d) in P_WITH_UNIQUE_LENGTH.keys(): count+= 1

    # print(code_dict) # for each line, retuns two {} unsorted
        # {'p' ['str '. .]} and {'pd' ['str '. .]}

print("count of 1,4,7,8: %d"%count)
print(f"\nPart 1 = %d"%count )
# returned 26 for example data CORRECT
# returned 344 for data CORRECT

# Part 2

"""
Make ordered dicionaries to solve puzzle
Part 2 instructions includes a unique signal pattern
    so manually input this data as input_p2d where
    {original_p2d} keys are sorted patterns : values are didits
"""
original_p2d = {"abcefg":0,"cf":1,"acdeg":2,"acdfg":3,"bcdf":4,"abdfg":5,\
              "abdefg":6,"acf":7,"abcdefg":8,"abcdfg":9}
# convert to original_d2p
# ORIGIN_K_N = dict([(value, key) for key, value in ORIGIN_K_P.items()])
original_d2p = dict([(value, key) for key, value in original_p2d.items()])


# sort keys and list
def keys_sorted(list, is_sort_list):
    ret = []
    for key in list:
        ret.append("".join(sorted(key)))
    return ret if not is_sort_list else sorted(ret)

def find_unique_pattern_by_length(patterns, length):
    for p in patterns:
        if len(p) != length: continue
        if length in P_WITH_UNIQUE_LENGTH.keys(): return p # return unique pattern
    return None

# parse the basic matching item of connections
def find_matched_item(matched_dict, new, origin): 
    new_matched = matched_dict.copy()
    for m in matched_dict:
        set_m = set(m)
        set_new = set(new)
        if not set_m.issubset(set_new): continue

        new_shorted = "".join(sorted(set_new.difference(set_m))) 
        origin_shorted = "".join(sorted(set(origin).difference(set(matched_dict[m]))))
        return find_matched_item(matched_dict, new_shorted, origin_shorted)
    new_matched[new] = origin
    return new_matched 


# try to find the matching pattern by replace matching items in pattern
def find_matched_pattern(pattern,matched_dict):
    leftover = pattern
    origin = ""
    for m in matched_dict:
        if len(m) > len(leftover): continue
        if not set(m).issubset(set(leftover)): continue
        shortened = "".join(sorted(set(leftover).difference(set(m))))
        origin += matched_dict[m]
        leftover = shortened
        if len(shortened) == 0: break

    item_found = []
    sorted_key = "".join(sorted(origin))
    for op in original_p2d:
        if len(pattern) != len(op): continue
        if not set(sorted_key).issubset(set(op)): continue
        if op == sorted_key: return op
        item_found.append(op)

    if len(item_found) != 1: return None
    matched_dict[shortened] = "".join(set(item_found[0]).difference(set(sorted_key)))
    return item_found[0]


def get_number(digits, entry_map):
    new_digits = digits.copy()
    new_digits.reverse()
    number = 0
    mutiple = 1
    for d in new_digits:
        number += entry_map[d] * mutiple
        mutiple *= 10
    return number 

def decode_number(patterns, digits):
    patterns = keys_sorted(patterns, True)
    digits = keys_sorted(digits, False)

    entry_map = {}
    matched_dict = {} 

    # unique patterns: 1,4,7,8
    for l in P_WITH_UNIQUE_LENGTH.keys():
        p = find_unique_pattern_by_length(patterns, l)
        digit =  P_WITH_UNIQUE_LENGTH[l]
        entry_map[p] = digit 
        matched_dict = find_matched_item(matched_dict, p, original_d2p[digit])

    # try if patterns is combination of matched items 
    for p in patterns:
        if len(p) in P_WITH_UNIQUE_LENGTH: continue
        origin = find_matched_pattern(p, matched_dict)
        if origin is not None:
            entry_map[p] = original_p2d[origin]

    if len(entry_map) != len(original_p2d):
        print("FAILED to decode the patterns")
        return 0

    number = get_number(digits, entry_map)
    return number

patterns = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb\
    ab".split(" ")
digits = "cdfeb fcadb cdfeb cdbaf".split(" ")
decode_number(patterns, digits)

number_list = []
for entry in entry_list:
    number = decode_number(entry[K_PATTERNS], entry[K_DIGITS])
    number_list.append(number)
print("final sum: ", sum(number_list))
print("Part 2 = ",sum(number_list))
# returned 61299 for example data CORRECT
# returned 1048410 for data CORRECT



