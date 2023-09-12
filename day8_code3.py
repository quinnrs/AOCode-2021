import pathlib
import sys
import parse

"""
THIS CODE INCLUDES A CONSOLIDATED DECODE SIGNALS FUNCTION 
WITHOUT USING THE LIST 235 and LIST 069 FUNCTIONS - CORRECT!

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

def decode_patterns(signals):
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
    # print(f"\ns2d = ", s2d)

    # this is the reverse {} s2d,  k = disply:v = signals
    d2s = {v: k for k, v in s2d.items()}

    for str in signals:
        slen = len(str)   
        if str in s2d:
            continue    
    
        if slen == 5:
            # s2d[str]= [2, 3, 5]
            # sort_list235(list = [signals])

            if 'a' in str and 'b' in str:
                s2d[str] = 3
                # print("solved for digit 3  -- s2d[s] = 3")
                
            elif 'e' in str and 'f' in str and 'b' in str:
                s2d[str] = 5
                # print("solved for digit 5  -- s2d[s] = 5")

            else:
                s2d[str] = 2
                # print("solved for digit 2  -- s2d[s] = 2")

            # print(f"s2d[str] = ", s2d[str])

        
        elif slen == 6:
            # s2d[str] = [0, 6, 9]
            # sort_list069(list = [signals]) 
            if 'a' in str and 'f' in str:
                s2d[str] = 6
                # print("solved for digit 6  -- s2d[s] = 6")
            elif 'b' in str and 'c' in str and 'd' in str and 'f' in str:
                s2d[str] = 9
                # print("solved for digit 9  -- s2d[s] = 9")
            # elif 'a' in str and 'f' in str:
            #     s2d[str] = 6
            #     print("solved for digit 6  -- s2d[s] = 6")
            else:
                s2d[str] = 0
                # print("solved for digit 0  -- s2d[s] = 0")
    
    print(f"\ns2d = ", s2d)

    # this is the reverse {} s2d,  k = disply:v = signals
    d2s = {v: k for k, v in s2d.items()}
    print(f"\nd2s = ", d2s)


    return s2d, d2s
    

    # this is the reverse {} s2d,  k = disply:v = signals
# d2s = {v: k for k, v in s2d.items()}
# print(f"\nd2s = ", d2s)


# call the function
decode_patterns(signals)  

# this is the reverse {} s2d,  k = disply:v = signals
# d2s = {v: k for k, v in s2d.items()}
# print(f"\nd2s = ", d2s)


#  Solve part 2
# print(f"\ndigits = ", digits)
# sort [digits] for consitent strings
# dig_sort = sorted([''.join(sorted(d)) for d in digits])
# print(f"dig_sort = ", dig_sort)
"""  - sorted digits will not work because it changes the puzzle input
     - the s2d dicionary get method will decode the signal, but it requires
        that the signal str exactly match the s2d key
     - use frozen set
     reparse the data
"""
fin = open(data_path)
for line in fin:
    signals, digits = map(str.split, line.split('|'))
    # signals = tuple(map(lambda p: (frozenset(p), len(p)), signals))
    signals = tuple(map(lambda s: (frozenset(s)), signals))
    digits   = tuple(map(lambda p: (frozenset(p)), digits))
    # signals = tuple(map(lambda s: (frozenset(s), len(s)), signals))
    
    # print(f"signals = ", signals)
    # print(f"digits = ", digits)

    s2d = decode_patterns(signals)
   
    d2s = decode_patterns(signals)

"""
    outout is
        s2d =  CORRECT
        d2s=  CORRECT
        None
    """

digit_total = 0
for lin in fin:
    digits = tuple(map(lambda p: (frozenset(p)), digits))
    for frozenset in digits:
        print(f"digit in digits= ", frozenset)
    print(f"\nstarting a new solution loop")
    s2d = decode_patterns(signals)
    # for digit in digits:
        # print(f"digit in digits= ", digit)
print(f"digits in d2s = ", digits)

# print(s2d[digits[0][0]])

"""
 - 9/11 at 1845 results for  digits is CORRECT but 
    I am not getting any print outut from either digit or frozensets in digits

"""





# digit1 = d2s.digit[0]
# digit1 = s2d[digits[0][0]] # TypeError'frozenset' object is not subscriptable
    
# for key, value in d2s(): # TypeError: 'tuple' object is not callable

""""    
# for digit in d2s:
#     print(f"\ndigits in d2s = ", digit)
output is
digits in d2s =  {frozenset({'d', 'c', 'f', 'b', 'e', 'g', 'a'}): 8, 
                frozenset({'d', 'b', 'a'}): 7, 
                frozenset({'e', 'f', 'a', 'b'}): 4, 
                frozenset({'b', 'a'}): 1, 
                frozenset({'d', 'c', 'f', 'b', 'e'}): 5, 
                frozenset({'d', 'c', 'f', 'g', 'a'}): 2, 
                frozenset({'d', 'c', 'f', 'b', 'a'}): 3, 
                frozenset({'d', 'c', 'f', 'b', 'e', 'a'}): 6, 
                frozenset({'d', 'c', 'f', 'b', 'e', 'g'}): 9, 
                frozenset({'d', 'c', 'b', 'e', 'g', 'a'}): 0}

digits in d2s =  {8: frozenset({'d', 'c', 'f', 'b', 'e', 'g', 'a'}),
                    7: frozenset({'d', 'b', 'a'}),
                    4: frozenset({'e', 'f', 'a', 'b'}), 
                    1: frozenset({'b', 'a'}), 
                    5: frozenset({'d', 'c', 'f', 'b', 'e'}), 
                    2: frozenset({'d', 'c', 'f', 'g', 'a'}), 
                    3: frozenset({'d', 'c', 'f', 'b', 'a'}), 
                    6: frozenset({'d', 'c', 'f', 'b', 'e', 'a'}), 
                    9: frozenset({'d', 'c', 'f', 'b', 'e', 'g'}), 
                    0: frozenset({'d', 'c', 'b', 'e', 'g', 'a'})}

"""

# for frozenset in d2s:
    # if frozenset not in digits:
        # print(f"\nfrozenset not in digits = ", frozenset)
    # if frozenset in digits:
        # print(f"\nfrozenset in digits = ", frozenset)
"""   there are no (zero) frozensets in d2s ??? """









"""   working with tuple digits -----   
for digit in digits:
    print(digit, type(digit))

dlen = len(digits)
print(f"dlen = ", dlen)

# for k in range(0,4): #last idex is not included
    # print(digit in s2d)  # all False for both s2d and d2s
    # print(k, digit(k)) # frozenset item is not callable
    # print(k, digit[k])  #  'frozenset' object is not subscriptable
          
    # digit1 = digit["antecedents"].apply(lambda x: ', '.join(list(x))).astype("unicode")
        # returns TypeError: 'frozenset' object is not subscriptable
    # digits["antecedents"] = digits["antecedents"].apply(lambda x: ', '.join(list(x))).astype("unicode")
        # returns TypeError: tuple indices must be integers or slices, not str
    # sub_digit = digit.apply(lambda x: ', '.join(list(x)))
    # sub_digit = digit.join(', ')
        # AttributeError: 'frozenset' object has no attribute 'join'

for frozenset in digits:
    print(frozenset in d2s, frozenset in s2d) # all False for both s2d and d2s
    print(f"\nfrozenset =", frozenset) 

    # sub_digit = frozenset.apply(lambda x: ', '.join(list(x)))
        # AttributeError: 'frozenset' object has no attribute 'apply'
    
----- working with tuple digits ------"""













