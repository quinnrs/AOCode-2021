import pathlib
import sys
import parse
from collections import OrderedDict

"""
This approcah returns the correct solition but it is not efficient

as of 9/15/2023, it runs for part 1 conly
"""


# data_path = "day8_folder/day8_example.txt"
data_path = "day8_folder/day8.txt"
# data_path = "day8_folder/single_line.txt"

fin = open(data_path)
unique_counter = 0
for line in fin:
    print(line) # returns single line as exoected
    raw_signals, raw_digits = map(str.split, line.split('|'))
    signals, digits = [], [] 

    for signal in raw_signals:
        signals.append(signal)
    print(f"signals = ", signals)
    
    for digit in raw_digits:
        digits.append(digit)
    print(f"digits = ", digits)

    # not using dictionary here to avoid tuple restrictions
# def decode_digit(list):
#     """  solution works for one specifc list of digits only"""
#     dlen = len(list)
#     # print(f"\nitem = ", str, type(str), dlen, type(dlen))
#     if dlen == 2:
#         decoded_digit = 1      # unique dlen
#     elif dlen == 3:
#         decoded_digit = 7      # unique slen
#     elif dlen == 4:
#         decoded_digit = 4      # unique slen
#     elif dlen == 7:
#         decoded_digit = 8      # unique slen

#     elif dlen == 5:
#         # [2, 3, 5]
#         if 'g' not in str and 'a' not in str:
#             decoded_digit = 5
                
#         elif 'e' not in str and 'b' not in str:
#             decoded_digit = 2
               
#         elif 'e' not in str and 'g' not in str:
#             decoded_digit = 3

#     elif dlen ==  6:
#          # [0, 6, 9]
        
#         if 'g' not in str:
#             decoded_digit = 6
                
#         elif 'a' not in str: 
#             decoded_digit = 9
                
#         elif 'f' not in str:
#             decoded_digit = 0
           
#     else:
#         decoded_digit = None

#     # print(f"decode digit = ", decode_digit(str))
#     print("decode_digit = ", decode_digit)

#     return(decoded_digit)

# # call the function
# list = ['fdgacbe']
# decode_digit(list)
# print("decode fdgacbe  =", decode_digit(list))


# # solve Part 2
# def solve_puzzle(data_path):
#     for line in fin:
#         print(line)
#     # raw_signals, raw_digits = map(str.split, line.split('|'))
#     # signals, digits = [], []
    
#     # for digit in raw_digits:
#     #     digits.append(digit)
#         print(f"\ndigits = ", digits) 

#         value_list = []
#         for str in digits:
#             print("\n lin digits = ", digits)
#             str_digit_value = []
#         # print(str)
#             digit_value = decode_digit(str)
#             # print(f"digit_value = ", digit_value)
#             # str_digit_value.append(digit_value)
#         print(f"str_digit_value = ", str_digit_value.append(digit_value))

# # call the function
# solve_puzzle(data_path = "day8_folder/single_line.txt")


"""
This approcah returns the correct solition but it is not efficient
"""
