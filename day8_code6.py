import pathlib
import sys
import parse

"""
THIS CODE INCLUDES A CONSOLIDATED DECODE SIGNALS FUNCTION 
WITHOUT USING THE LIST 235 and LIST 069 FUNCTIONS - CORRECT!

# # # RUNS CORRECTLY FOR SINGLE LINE TEXT ONLY # # #

input is a str file with 10 signal patterns, a pipe delimiter
and 4 display patterns
- the 10 signal patterns are combinations of on/off wire connections 
to the digital dislays
- the 4 digit output values are the on connection for the 10 bulb 
locations on each digila displays

the challenge is to decode the scrambled supply to display
connections to read the correct 4 digit number of the display

"""

# data_path = "day8_folder/day8_example.txt"
# data_path = "day8_folder/day8.txt"
data_path = "day8_folder/single_line.txt"

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

    # if len(digit) in [2, 3, 4, 7]:
        #unique_counter += 1

"""    new approach working on digits rather than signals"""
def decode_patterns(list):
    s2d = {}
    for str in digits:
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

    for str in digits:
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

# decode_patterns(list = digits)  
    
