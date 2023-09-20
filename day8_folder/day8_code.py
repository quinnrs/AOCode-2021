import pathlib
import sys
import parse

"""
input is a str file with 10 signal patterns, a pipe delimiter
and 4 display patterns
- the 10 signal patterns are combinations of on/off wire connections 
to the digital dislays
- the 4 digit output values are the on connection for the 10 bulb 
locations on each digila displays

the challenge is to decode the scrambled supply to display
connections to decode the 4 digit number of the display

"""

# data_path = "day8_folder/day8_example.txt"
# data_path = "day8_folder/day8.txt"
data_path = "day8_folder/single_line.txt"


"""   Part 1 is only concerned with the 4 digit displays

 only 4 of the digits 0 - 9 have a unique display
    1 use  c and f only
    7 uses a, c, and f
    4 uses b, c, d, and f
    8 uses all 7 (a,b,c,d,e,f,g)
        so, unique_display_digits = [2, 3, 4, 7,]
"""


# Parse the data
fin = open(data_path)
unique_counter = 0
for line in fin:
    raw_signals, raw_digits = map(str.split, line.split('|'))
    signals, digits = [], [] 

    for signal in raw_signals:
        signals.append(signal)
    print(f"signals = ", signals)
    
    for digit in raw_digits:
        digits.append(digit)
        print(digits)

        if len(digit) in [2, 3, 4, 7]:
            unique_counter += 1



    # print(unique_counter)


# print(f"\nunique_counter = ", unique_counter)
# returns 4 for single line data. CORRECT
# returns 26 for example data CORRECT
# returns 344 for puzle input CORRECT

"""  
Part 2
    This is the answer for the single_line,txt example,
    which was given as part of the puzzle input
     
    I can half way understand it, my challenge is to write code to verify it

d2s =   {0: 'abcefg',
            1: 'cf',        # unique slen
            2: 'acdeg',
            3: 'acdfg',     # from diplays cf in 1
            4: 'bcdf',      # unique slen
            5: 'abdfg',
            6: 'abdefg',
            7: 'acf',       # unique slen
            8: 'abcdefg',   # unique slen
            9: 'abcdfg'

"""

s2d = {}
for str in signals:
    slen = len(str)
    # print(s, len(s))
    if slen == 2:
        s2d[str] = 1      # unique slen
    elif slen == 3:
        s2d[str] = 7      # unique slen
    elif slen == 4:
        s2d[str] = 4      # unique slen
    elif slen == 7:
        s2d[str] = 8      # unique slen
    elif slen == 5:
        s2d[str]= [2, 3, 5]
    elif slen == 6:
        s2d[str] = [0, 6, 9]
print(f"\ns2d = ", s2d)

def sort_list235(list):
    for str in signals:
        print(str)
        slen = len(str)
        print(slen)
        if slen == 5: # 2, 3, or 5 and 
            """ 3 has 2 ON segments in common with 1 which are 'c' and 'f'
                so if the pattern string cotains both c and f is digit 3
            """

            if 'a' in str and 'b' in str:
                s2d[str] = 3
                print("solved for digit 3  -- s2d[s] = 3")
                
            elif 'e' in str and 'f' in str and 'b' in str:
                s2d[str] = 5
                print("solved for digit 5  -- s2d[s] = 5")

            else:
                s2d[str] = 2
                print("solved for digit 2  -- s2d[s] = 2")

            print(f"s2d[str] = ", s2d[str])
    # return s2d[2], s2d[3], s2d[5]
    return s2d

# call the function
# sort_list235(list = [signals])


def sort_list069(list):
    """
    all three choices have 6 six displays out of a total 7 possible
    by inspection, digit zero does not require 'd', digit six does not 
    require 'c' and digit 9 does not require 'e'
    str2 = the lens signals of 10 displays
    """
    for str in signals:
        print(str)
        slen = len(str)
        print(slen)
        if slen == 6: # 0, 6, or 9
            if 'a' in str and 'f' in str:
                s2d[str] = 6
                print("solved for digit 6  -- s2d[s] = 6")
            elif 'b' in str and 'c' in str and 'd' in str and 'f' in str:
                s2d[str] = 9
                print("solved for digit 9  -- s2d[s] = 9")
            # elif 'a' in str and 'f' in str:
            #     s2d[s] = 6
            #     print("solved for digit 6  -- s2d[s] = 6")
            else:
                s2d[str] = 0
                print("solved for digit 0  -- s2d[s] = 0")

    #  return s2d[6], s2d[9], s2d[0]
    return s2d



# def decode_patterns(signals):
#     # signal to digit dictionary
#     s2d = {}

#     for str in signals:
#         slen = len(str)
#         if slen == 2:
#             s2d[str] = 1      # unique slen
#         elif slen == 3:
#             s2d[str] = 7      # unique slen
#         elif slen == 4:
#             s2d[str] = 4      # unique slen
#         elif slen == 7:
#             s2d[str] = 8      # unique slen

#     # print(f"\ns2d = ", s2d)

#     # digit to signal dictionary
#     d2s = {v: k for k, v in s2d.items()}
#     print (f"\nd2s = ", d2s)
    
#     for str in signals:
#         if str not in s2d:
#             print(str, len(str))
#             continue

#         elif len(str) == 5:
#             # s2d[s]= [2, 3, 5]
#             sort_list235(list = [signals])
#             # sort_list235(list = ['2', '3', '5'])

#         elif len(str) == 6:
#             # s2d[s] = [0, 6, 9]
#             sort_list069(list = [signals])

#     print(f"\ns2d = ", s2d)
    

# # call the function
# decode_patterns(signals)

s2d = {}
for s in signals:
    slen = len(s)
    # print(s, len(s))
    if slen == 2:
        s2d[s] = 1      # unique slen
    elif slen == 3:
        s2d[s] = 7      # unique slen
    elif slen == 4:
        s2d[s] = 4      # unique slen
    elif slen == 7:
        s2d[s] = 8      # unique slen
    elif slen == 5:
        # s2d[s]= [2, 3, 5]
        sort_list235(list = [signals])
    elif slen == 6:
        # s2d[s] = [0, 6, 9]
        sort_list069(list = [signals]) 
    print(f"\ns2d = ", s2d)

# this is the reverse {} s2d,  k = disply:v = signals
d2s = {v: k for k, v in s2d.items()}
print(f"\nd2s = ", d2s)

#  Solve part 2

# total = 0
# print(digits)
# digits = ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf']
# for digit in digits:
# # for k in range(0, len(digits) - 1): 
# # for value in d2s:  # values are keys
#     # test = digit
#     # test1 = digits[0]
#     # test2 = s2d['cdfbe']  
#     digit_value = s2d.get[digit]
#     # digit_value = s2d.get('cdfbe')
#     print(digit, digit_value)
# # print(s2d[k])
# # print(digit[k])
# # print(digits)
# # total = d2s[digits[0][0]] 


























