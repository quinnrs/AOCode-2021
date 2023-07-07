my_data_path = "/Users/rsq2/Code_projects/2021-Challenge/day3_folder /day3.txt"

# write a function to open a file of binary stings without losing the lading zeros
def open_data_file(data_path):
    data_file = []
    f = open(data_path)
    for line in f:
        data_file.append(line.strip())
    return data_file

# call the function
data_file = open_data_file(my_data_path)
# print("data_file = ", data_file)
my_list = data_file

#identity most common for each item in a binary list
def most_common(my_list, bit_position):
    column_counter = 0
    for item in my_list:
        column_counter += (int(item [bit_position]))
        if column_counter < (len(my_list)/2):
            most_common = 0
        else:
            most_common = 1
    # print("for bit_position ",bit_position, "column_counter = ", column_counter, " most_common = ",most_common)
    return most_common 
# calls
print("test_ox_slicer = ", str(most_common(my_list, bit_position=0)))

#binary conversion for string
def binaryToDecimal(n):
    num = n;
    dec_value = 0;
    base1 = 1;
    len1 = len(num);

    for i in range(len1 - 1, -1, -1):
        if (num[i] == '1'):    
            dec_value += base1;
        base1 = base1 * 2;
    return dec_value;


def ox_data(my_list, bit_position):
    for bp in range (0,12):
        bit_position = bp
        slicer = str(most_common(my_list, bit_position))  # use for keepers
        # print ("ox_keeper_slicer =" ,slicer)
        keepers = []
        for item in my_list:
            if item[bit_position] == slicer:
                keepers += [item]
        my_list = keepers
        # print("keepers = ", keepers)
        if len(my_list) == 1:
            print("ox_data recursion is complete")
            print(keepers)
            ox_data = keepers
            # need to convert to decimal
            return my_list
    
#calls
print("")
print("ox_gen = ",ox_data(my_list, bit_position=0 ))
   
def least_common(my_list, bit_position):
    column_counter = 0
    for item in my_list:
        # bit_position = k
        column_counter += (int(item [bit_position]))
        if column_counter < (len(my_list)/2):
            least_common = 1
        else:
            least_common = 0
    # print("for bit_position ",bit_position, "column_counter = ", column_counter, " least_common = ",least_common)
    return least_common

# call
print("")
least_common_0 = least_common(my_list, bit_position = 0)
print("least common for bp[0] is ", least_common_0) 
   

def co_data(my_list, bit_position):
    for bp in range (0,12):
        bit_position = bp
        # my_list =
        slicer = str(least_common(my_list, bit_position))  # use for keepers    
        # print("co_keeper_slicer =" ,slicer)
        keepers = []    
        for item in my_list:    
            if item[bit_position] == slicer:
                keepers += [item]   
        my_list = keepers   
        # print("keepers = ", keepers)
        if len(my_list) == 1:
            print("co_data recursion is complete")
            print(keepers)
            # need to convert to decimal
            return my_list
        
    print ("co_data = ", co_data(my_list, bit_position))
# calls
test1 = print("co_data = ", co_data(my_list, bit_position=0))

#binary conversion for string
def binaryToDecimal(n):
    num = n;
    dec_value = 0;
    base1 = 1;
    len1 = len(num);

    for i in range(len1 - 1, -1, -1):
        if (num[i] == '1'):    
            dec_value += base1;
        base1 = base1 * 2;
    return dec_value;

#ox_data =  ['10111']
ox_data =  ['011000111111']
o2_item = ox_data[0]
print(o2_item)
o2_gen = binaryToDecimal(o2_item)
print("o2_gen =", o2_gen)

#co_data =  ['01010']
co_data =  ['101011000100']
co2_item = co_data[0]
print(co2_item)
co2_scrub = binaryToDecimal(co2_item)
print("co2_scrub =", co2_scrub)

life_support_rating = o2_gen * co2_scrub
print("life_support_rating = " ,life_support_rating)






