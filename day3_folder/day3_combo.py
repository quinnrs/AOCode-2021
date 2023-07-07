my_data_path = "/Users/rsq2/Code_projects/2021-Challenge/day3_folder /day3.txt"
day3_example_data =["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

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
# my_list = day3_example_data

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
# call
# print("test_ox_slicer = ", str(most_common(my_list, bit_position=0)))

def gamma(my_list, bit_position):
    # gamma = []
    for item in my_list:
        # gamma = ("0b")
        gamma = ("")
        for bp in range(0,12): # 12 for day3, 5 for example data
            bit_position = bp
            most = (most_common(my_list, bit_position))
            gamma += str(most)
        # print(gamma)
        return gamma
        
print(gamma)
# call 
test1 = print("gamma = ", gamma(my_list, bit_position=0)) 




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
    for bp in range (0,12): #12 for day3, 5 for example data
        bit_position = bp
        slicer = str(most_common(my_list, bit_position))  # use for keepers
        # print("ox_keeper_slicer =" ,slicer)
        keepers = []
        for item in my_list:
            if item[bit_position] == slicer:
                keepers += [item]
        my_list = keepers
        # print("keepers = ", keepers)
        if len(my_list) == 1:
            print("ox_data recursion is complete")
            # need to convert to decimal
            print(keepers)
            return my_list
    
#calls
print("")
test1 = print("ox_data = ", ox_data(my_list, bit_position=0))

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

def epsilon(my_list, bit_position):
    for item in my_list:
        epsilon = ("")
        for bp in range(0,12):  #12 for day3, 5 for example data
            bit_position = bp
            least = (least_common(my_list, bit_position))
            epsilon += str(least)
        # print(least)
        return epsilon
        
print(epsilon)
# call 
test1 = print("epsilon = ", epsilon(my_list, bit_position=0)) 

day3_example_data =["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]  
my_list = day3_example_data
def co_data(my_list, bit_position):
    for bp in range (0,12): #12 for day3, 5 for example data
        bit_position = bp
        # my_list =
        slicer = str(least_common(my_list, bit_position))  # use for keepers    
        # print("co_keeper_slicer =" ,slicer)
        keepers = []    
        for item in my_list:
            # print(item)    
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
print("")


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

# gamma = ("10110")
gamma =  ("010100111001")
gamma_item = gamma[0]
# print("gamma_item = ", gamma[0])
gamma_rate = binaryToDecimal(gamma)
print("gamma_rate =", gamma_rate)
print("")

# epsilon =  ("01001")
epsilon =  ("101011000110")
epsilon_item = epsilon[0]
# print("epsilon_item = ", epsilon_item)
epsilon_rate = binaryToDecimal(epsilon)
print("epsilon_rate = ", epsilon_rate)
print("")

power_consumption = gamma_rate * epsilon_rate
print("power consumption = ", power_consumption)
print(" expected value is 3687446") 

# ox_data =  ['10111']
# ox_data =  ['111100011111'] i don't know where this came from
ox_data = ['011000111111']

o2_item = ox_data[0]
print(o2_item)
o2_gen = binaryToDecimal(o2_item)
print("o2_gen =", o2_gen)
print("")

# co_data =  ['01010']
# co_data =  ['001001100101'] i don't know where this came from
co_data =  ['101011000100']
co2_item = co_data[0]
print(co2_item)
co2_scrub = binaryToDecimal(co2_item)
print("co2_scrub =", co2_scrub)
print("")

life_support_rating = o2_gen * co2_scrub
print("life_support_rating = " ,life_support_rating)
print("espected value is  4406844")



