import pathlib
import sys
import parse

data_path = "day8_folder/day8_example.txt"
# data_path = "day8_folder/day8.txt"

fin = open(data_path)
for line in fin:
    raw_signals, raw_digits = map(str.split, line.split('|'))
    signals, digits = [], []

    for signal in raw_signals:
        # signals.append((frozenset(p), len(p)))
        signals.append(signal)
        print(signals)   # CORRECT
        for s in signals:
            sig_sort = []
            sort_s = sorted(s)
            '  '.join(sort_s)
        print(f"sort_s = ",sort_s)  # CORRECT
            # sig_sorted = str(sort_s)
        print(f"sig_sorted = ", str(sort_s))
    
    # for digit in raw_digits:
    #     # digits.append((frozenset(d), len(d)))
    #     digits.append(digit)
    # print(digits)      # CORRECT

    # for d in digits:
    #     sort_dig = sorted(d)
    #     '  '.join(sort_dig)
    # print(f"sort_dig = ",sort_dig) # CORRECT


    
      
    