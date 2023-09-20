import pathlib
import sys
import parse

"""
input is a text file with 10 signal patterns, a pipe delimiter
and 4 display patterns the represent a 4 digit number - the puzzle
solotion is to decode the 4 digit number

part 1 - only 4 of the digits 0 - 9 have a unique display
    1 use  c and f only
    7 uses a, c, and f
    4 uses b, c, d, and f
    8 uses all 7 (a,b,c,d,e,f,g)
        so, unique_display_digits = [2, 3, 4, 7,]
"""
# data_path = "day8_folder/day8_example.txt"
# data_path = "day8_folder/day8.txt"
data_path = "day8_folder/single_line.txt"

# Parse the data
fin = open(data_path)
for line in fin:
    raw_signals, raw_digits = map(str.split, line.split('|'))
    signals, digits = [], []
 

    for signal in raw_signals:
        signals.append(signal)
    
    for digit in raw_digits:
        digits.append(digit)

    print(f"signals =", signals)
    print(f"digits =", digits)
    
# create  s2d dictionary



d2s =   {0: ['a', 'b', 'c', 'e', 'f', 'g'],
            1: ['c', 'f'],
            2: ['a', 'c', 'd', 'e', 'g'],
            3: ['a', 'c', 'd', 'f', 'g'],
            4: ['b', 'c', 'd', 'f'],
            5: ['a', 'b', 'd', 'f', 'g'],
            6: ['a', 'b', 'd', 'e', 'f', 'g'],
            7: ['a', 'c', 'f'],
            8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
            9: ['a', 'b', 'c', 'd', 'f', 'g']
         }

# this is the reverse {} s2d,  k = disply:v = signals
# d2s = {v: k for k, v in s2d.items()}

s2d = {}
for s in signals:
        slen = len(s)
        # print(s, len(s))
        if slen == 2:
            s2d[s] = 1
        elif slen == 3:
            s2d[s] = 7
        elif slen == 4:
            s2d[s] = 4
        elif slen == 7:
            s2d[s] = 8
        elif slen == 5:
            s2d[s]= [2, 3, 5]
        elif slen == 6:
            s2d[s] = [0, 6, 9]






for s in signals:
    slen = len(s)
    # print(f"\n" , s, slen)
    if slen == 2:
        s2d[s] = 1
    elif slen == 3:
        s2d[s] = 7
    elif slen == 4:
        s2d[s] = 4
    elif slen == 7:
        s2d[s] = 8
    elif slen == 5: # 2, 3, or 5
        

        if '3' in d2s == True:
            s2d[s] = 3
            # print("f s2d[s] = ", s2d[s])
            # print('3' in d2s)

        elif 5 in d2s:
            s2d[s] = 5
        else:
            s2d[s] = 2
            # print("f s2d[s] = ", s2d[s])  

    elif slen == 6: # 0, 6, or 9
        
        if 4 in d2s:
            s2d[s] = 9
        if 2 in d2s:
            s2d[s] = 6
        else:
            s2d[s] = 0

print(s2d)
print(d2s)




