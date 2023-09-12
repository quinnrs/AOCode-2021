import pathlib
import sys
import parse

"""
THIS CODE INCLUDES A CONSOLIDATED DECODE SIGNALS FUNCTION USING
NESTED FUNCTIONS for LIST 235 and LIST 069
BUT THE LIST235 LOOP IS NOT RUNNING - INCORRECT !!
input is a str file with 10 signal patterns, a pipe delimiter
and 4 display patterns
- the 10 signal patterns are combinations of on/off wire connections 
to the digital dislays
- the 4 digit output values are the on connection for the 10 bulb 
locations on each digila displays

the challenge is to decode the scrambled signal to display
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
    print(f"digits = ", digits)

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
# create the signal to digit dictionary
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
    # elif slen == 5:
    #     s2d[str]= [2, 3, 5]
    # elif slen == 6:
    #     s2d[str] = [0, 6, 9]


def sort_list235(list):
    for str in signals:
        print(str)
        slen = len(str)
    print(slen)
    if slen == 5: # 2, 3, or 5 
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

def sort_list069(list):
    """
    all three choices have 6 six displays out of a total 7 possible
    
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
            #     s2d[str] = 6
            #     print("solved for digit 6  -- s2d[s] = 6")
            else:
                s2d[str] = 0
                print("solved for digit 0  -- s2d[s] = 0")

    #  return s2d[6], s2d[9], s2d[0]
    # return s2d


def decode_patterns(signals):
    
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
        # elif slen == 5:
        #     s2d[str]= [2, 3, 5]
        # elif slen == 6:
        #     s2d[str] = [0, 6, 9]
    print(f"\ns2d = ", s2d)

    for str in signals:
        slen = len(str)   
        if str in s2d:
            continue    
    
        elif slen == 5:
            # s2d[str]= [2, 3, 5]
            sort_list235(list = [signals])

        elif slen == 6:
            # s2d[str] = [0, 6, 9]
            sort_list069(list = [signals]) 
    
    print(f"\ns2d = ", s2d)
    return s2d
    

# this is the reverse {} s2d,  k = disply:v = signals
# d2s = {v: k for k, v in s2d.items()}
# print(f"\nd2s = ", d2s)


# # call the function
decode_patterns(signals)  

# this is the reverse {} s2d,  k = disply:v = signals
# d2s = {v: k for k, v in s2d.items()}
# print(f"\nd2s = ", d2s)


#  Solve part 2
print(f"digits = ", digits)
# sort [digits] for consitent strings
# dig_sort = sorted([''.join(sorted(d)) for d in digits])
# print(f"dig_sort = ", dig_sort)
"""  - sorted digits will not work because it changes the puzzle input
     - the s2d dicionary get method will decode the signal, but it requires
        that the signal str exactly match the s2d key
     - use frozen set
     reparse the data
"""






# # for value in d2s:  # values are keys
# for digit in digits:
#     test = digit
#     # test2 = str(test) # TypeError str object not callsble
#     test1 = 'cdfbe'
#     # test2 = s2d['cdfbe']  
#     # digit_value = s2d.get[digit] #TypeError: '...  object is not subscriptable
#     digit_value = s2d.get('cdfbe')
#     print(test, test1, digit_value)
#     print(test in s2d)  # all are False
#     # print(test1 in s2d) # predict True - CORRECT
















