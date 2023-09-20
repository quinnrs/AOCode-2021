import pathlib
import sys
import parse


# data_path = "day8_folder/day8_example.txt"
# data_path = "day8_folder/day8.txt"
data_path = "day8_folder/single_line.txt"

"""   generic set testing ------

x1 = (1, 2, 3, 5) 
print(type(x1))  # <class 'tuple'>
x2 = (2, 5, 7, 9)
print(type(x2))  # <class 'tuple'>
#print(set1.intersection(set2))   # tuple object
# print(set1 & set2)   #  tuple and tuple error
print(set(x1) & set(x2))  # returns {2, 5} CORRECT'''

   --------- generic set testing ----- """




"""   actual variable set testing   = = = 

digits =  ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf']
signals =  ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']
s2d =  {'acedgfb': 8, 'dab': 7, 'eafb': 4, 'ab': 1}

print(f"set(s2d) = ", set(s2d))
print(type(s2d))  # <class 'dict'>

# manually make sig_len for signal (lengths range 2-8)
sig_len = (2, 3, 4, 5, 6, 7)
print(f"manually entered sig_len = ", sig_len)
print(type(sig_len))

print("end of testing")



    ====  actual variable set  testing ==== """

"""     part 2 code          """
# Parse the data
print("starting Part 2" )
# Parse the data
fin = open(data_path)
unique_counter = 0
for line in fin:
    raw_signals, raw_digits = map(str.split, line.split('|'))
    signals, digits = [], [] 
    
    for digit in raw_digits:
        digits.append(digit)
    print(f"digits = ", digits)

    for signal in raw_signals:
        signals.append(signal)
    print(f"signals = ", signals)


# create s2d with keys = digits and values = signal(str)
# this is the reverse dictionary of {d2s}

# s2d = {}
# for s in signals:  # start with unique lengths
#     sig_len = len(s)
#     # print(s, len(s))
#     if sig_len == 2:
#         s2d[s] = 1
#     elif sig_len == 3:
#         s2d[s] = 7
#     elif sig_len == 4: 
#          s2d[s] = 4
#     elif sig_len == 7:
#             s2d[s] = 8
# print(f"s2d = ", s2d)

    # print(f"\nset up for decoding the dignals")

    # print(f"set(s2d) = ", set(s2d))

    # # # manually input sig_len for signal (lengths range 2)
    # sig_len = (2, 3, 4, 5, 6, 7)
    # print(type(sig_len))
    # print(f"sig_len = ", sig_len)

"""  generator expression
Python3 code to demonstrate working of Set from dictionary values by
Using generator expression + {}
 
# initializing dictionary
# test_dict = {'Gfg': 4, 'is': 3, 'best': 7, 'for': 3, 'geek': 4}
test_dict = s2d
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
# {} converting to set
res = {test_dict[sub] for sub in test_dict}
 
# printing result
print("The converted set : " + str(res))

"""
    # test_dict = s2d
    # {} converting to set
    # res = {test_dict[sub] for sub in test_dict}
    # print("The converted set : " + str(res))


# s2l dictionary display:len(display) 
# sig_len = []
# for signal in signals:
#     sig_len.append(len(signal)) 
# print(f"sig_len =" , sig_len)
# print(type (sig_len))  # <class 'list'>

# set_sig_len = sig_len
# print(f"set_sig_len =" , set_sig_len) # as expected
# # print(type (set_sig_len))  # <class 'list'>

# set_069 = ['0', '6', '9']
# print(type (set_069))  # <class 'list'>
# # print(f"set_069 = ", set_069) # as expected

# set_235 = ['2', '3', '5']
# print(f"set_235 = ", set_235) # as expected
# # print(type (set_235))  # <class 'list'>

# # set = {s2l}
# # set_val = {s2l}
# # set_s2l = s_len
# # print(f"set_s2l =", set_s2l)
# # print(type (set_s2l)) # <class 'list'>

# # print(set_s2l.intersection)(set_sig_len)


def unscramble_patterns(signals):
    print("running unscramble")
    s2d = {}
    for s in signals:  # start with unique lengths
        sig_len = len(s)
        # print(s, len(s))
        if sig_len == 2:
            s2d[s] = 1
        elif sig_len == 3:
            s2d[s] = 7
        elif sig_len == 4: 
            s2d[s] = 4
        elif sig_len == 7:
            s2d[s] = 8

    # make set_val from s2d
    s2d_values =set(s2d.values())
    print(type(s2d_values))
    print(f"s2d_values = ", s2d_values)

    test_dict = s2d
    # {} converting to set
    res = {test_dict[sub] for sub in test_dict}
    print("The converted set : " + str(res))
   
    # create the reverse dictionary d2s  with digit:signal
    d2s = {v: k for k, v in s2d.items()}
    print(f"d2s = ", d2s)

    # make set_val from d2s
    d2s_keys = set(d2s.keys())
    print(f"set(d2s_keys) = ", d2s_keys)
    print(type(d2s_keys))

    # test_dict_rev = s2d
    # {} converting to set
    # res = {test_dict_rev[sub] for sub in test_dict_rev}
    # print("The converted set : " + str(res))
    


    """
    The digit 3 is the only one amongst those that has exactly 2 segments in 
    common with 1: so if at this point the pattern we are looking at has exactly 
    two letters in common with the pattern for 1, we just found the pattern for 3.

    Otherwise... 5 is the only one amongst 2 and 5 which has exactly 3 ON segments 
    in common with 4, so if at this point the pattern we are looking at has exactly
    3 letters in common with the pattern for 4, we just found the pattern for 5.

    Otherwise... the pattern we are looking at is for the digit 2.
    """

    # for s, sig_len in signals:

    test_dict = s2d
    # {} converting to set
    res = {test_dict[sub] for sub in test_dict}
    set_sig_len  = res
    print("The converted set : " + str(res))


    # print("s2d[3] is solved")

    #     elif len(set(set_sig_len) & s2d_values) == 3: 
    #         # elif len(p & d2p[4]) == 3:
    #         # 5 has 3 ON segments in common with 4
            
    #         s2d[signal] = 5
    #         print("s2d[5] is solved")
            
    #     else:
    #         s2d[signal] = 2
    #         s2d
    #         print("s2d[2] is only possibility left")

        # print("nothing to iterate")

def do_i_match_any_string_in_set(a_string, a_set):
    some_letters = set(a_string)
    for ddddd in a_set:
        compare_this = set(ddddd)
        if compare_this == some_letters:
            return True
    return False


def decode_triple(list):
# def decode_triple(dict, list):
    print("running de_code triple")
    s2d = {'acedgfb': 8, 'dab': 7, 'eafb': 4, 'ab': 1}
    d2s = {v: k for k, v in s2d.items()}
    set_s2d_values = set(s2d)
    print(f"set_s2d_values =", set_s2d_values)
    # s2d_keys = set(s2d.keys)
    
    # for item in list:
    for word in set_s2d_values:
        print(f"word = ", word)
        print(f"len(word) =", len(word))

        # for item in set(s2d):
        for item in list:
            print(f"\nitem = ", item)
            # str = d2s(item)
            #print(f"\nstr = ", str, "len(str) = ", len(str))
            set_item = set(item)
            # set_len_item = set(len(item))  # 
            print(f"item, len, and set(item) =", item, len(item), set(item))
            # print(f"len_set_item) = ", len(set_item)) # always = 1
            # print(f"set(s2d) = ", set(s2d))
            print(f"set(d2s) = ", set(d2s))
            # print(len(set(s2d))) # will always = 4
            # print(len(set(d2s))) # will always = 4
            # print(f"len(set_item & set(s2d)) = ", len(set_item & set(s2d))) #=0
            # print(f"len(set_item & set(d2s)) = ", len(set_item & set(d2s))) #=0
            # print(len(set_item & set(s2d))) # will always be 0
            print(f"set(s2d) =", set(s2d)) # will always be False
            print(f"set_item = ", set_item) # will always be False
            # print(len(set_item & set(s2d)) == 2) # will always be False
            # print(len(set_item & set(s2d)) == 2) # will always be False
            # print(f"do_i match = ", (do_i_match_any_string_in_set(a_string=(str)item, a_set=set(s2d))))
                # will alwats be True
            # print(len(str) == 2 and str in set(d2s))
            # if(len(set_item & set(s2d)) == 2):

            print(f"len(item) = {len(item)}") # will atways be 1
            
            print("item in s2d = ", item in s2d)
            print("word in s2d = ", word in s2d)
            print(f"(len(item) == 2 and  in set(s2d) = ", len(item) == 2 and item in set(s2d) )
            
            # if do_i_match_any_string_in_set == True and item in set(s2d) == True:       
            if len(word) == 3 and item in set(d2s) == True:
            # if len(item) == 2 and item in set(d2s) == True:
                s = 3 # make s2d[2] = 3
                print(s)
                # s2d[s] = 3
                d2s[s] = 3
                print("solved for digit 3  -- s2d[s] = 3")
            # # elif len(item) == 3 and item in set(s2d) == True:
            # elif len(item) == 3 and item in set(d2s) == True:
            #     s = 5
            #     # s2d[s] = 5
            #     d2s[s] = 5
            #     print("solved for digit 3  -- s2d[s] = 5")
            # else:
            #     s = 2
            #     # s2d[s] = 2
            #     d2s[s] = 2
            #     # s2d[s] = item
                print(True)
            print(False)

    # return d2s
    # return s2d
            




        # sig_len = len(item)
        # print(sig_len)
    # print(f"set(sig_len)) = ", set(sig_len))



#call the function
decode_triple(list = ['2', '3', '5'])
    
            

            
# call the function
# unscramble_patterns(signals)



        #if(len(set_item & set(d2s)) == 2):
         # TypeError: \
            # 'builtin_function_or_method' object is not iterable  
        # if len(item & s2d[1]) == 2:    # Type error \
            # 'builtin_function_or_method' object is not iterable
        # if set(list) & set(s2d.values()) == 2: # Type error \
            # 'builtin_function_or_method' object is not iterable