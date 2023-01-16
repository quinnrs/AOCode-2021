# AOC script combining previous deparate files for each day
import pandas as pd

""" 25 challenges (day1 to day25) """

#  +-+-+-+-+-  day 1 +-+-+-+-+- 

class AOC2021: 
        pass
# additional methods to be added later 

"""  write a method to open a txt.file with one data point on each line and convert to int and return a list """
def open_data_file(self, data_path):
    data_file = []
    f = open(data_path)
    for line in f:
        data_file.append(int(line))
    return data_file
   
self = "where is the data located"  # define befoe __init ??
def __init__(self):
     self.first_illegal_character = None
def __init__(self, data_path):
     self.data_path = data_path
    
# call the method
# data_path = "/Users/rsq2/Code_projects/2021-Challenge/input_data/day1_example.txt"
# day1_example_data = self.data_path
# day1_example_data = data_path("/Users/rsq2/Code_projects/2021-Challenge/input_data/day1_example.txt")


"""  the method will not run as currently written
error message   "NameError: name 'self' is not defined" 
error message for line 29 " TypeError: 'str' object is not callable"
error message for line 28 AttributeError: 'str' object has no attribute 'data_path'

"""
 

""" very klutzy function to open a txt.file with one data point on each line and convert to int and return a list """
# def open_data_list(self, data_path):
def open_data_file(data_path):
    clean_list=[]
    data_list = []
    string_list = []
    f = open(data_path)
    for line in f:
        # new_line = line.strip()
        # new_data = int(new_line)
        string_list.append(line)
        # data_list.append(int(line))  - gives error message
        # print(string_list)
    for sub in string_list:
        clean_list.append(sub.replace("\n", ""))
    # print(clean_list)
    for item in clean_list:
        data_list.append(int(item)) 
    
    # print("data file = " ,data_list)
    return data_list

''' read and inspect the data file list     '''
# data_path = "/Users/rsq2/Code_projects/2021-Challenge/input_data/day1_example.txt"
# day1_example_data = open_data_file("/Users/rsq2/Code_projects/2021-Challenge/input_data/day1_example.txt")
# print(day1_example_data)
# print(len(day1_example_data))

data_path = "/Users/rsq2/Code_projects/2021-Challenge/input_data/day1.txt"
day1_data = open_data_file("/Users/rsq2/Code_projects/2021-Challenge/input_data/day1.txt")
print(len(day1_data))


''' convert the list to a dictionary '''
keys =[]

# for k in range(len(day1_example_data)):
    # keys += (str(k))   # fix int to str here
for k in range(0,len(day1_data)):
    keys += (str(k))   # fix int to str here
# print("keys = ", keys)

"""  try zip function  """
# day1_depth_readings = dict(zip(keys, day1_example_data))
day1_depth_readings = dict(zip(keys, day1_data))
# print("day1_depths = ", day1_depth_readings)

"""     solve the puzzle using the example data   
def count_depth_increases (dictionary):
    counter = 0 
    for i in range (0,len(dictionary)-1): # for part 1
    # for i in range (0,len(dictionary)-3): # for part 2
        change = day1_depth_readings[(i)+1] - day1_depth_readings[(i)]    # for part 1
        # change = day1_depth_readings[(i)+ 3] - day1_depth_readings[(i)]     # for part 2
        if change > 0:
            counter +=1
        # print("counter = ", counter)
    print("The number of depth increases =" , counter)

count_depth_increases(day1_depth_readings)

 returned 7 which is correct for example data """

"""   now solve using day1.txt  
# manually comment out calls to day1_example data
# and replace with calls to day1.txt immediately below that line 

returned 1167 which is correct for day1_data  """

""" part 2   - change the depth increase definition to 3 steps   note that (day2+day3+day4) -(day1+day2+day3) is equal to day4 - day1 """

"""  returned 1130 which is correct for part 2  """

# +_+_+_+_+_+_ day 3 _+_+_+_+_+_+_
day3_data_path = ("input_data/day3.txt")
day3_example_data_path = ("input_data/day3_example.txt")

def data_str_list(data_path):
     data_list = []  # a list of binary strings
     f = open(data_path)
     for  line in f:
          data_list.append(line.strip())
          # print(data_file)
     return data_list

# example_data_list = data_str_list(day3_example_data_path)
# print(example_data_list)
day3_data_list = data_str_list(day3_data_path)
print(day3_data_list)


 
def binary_strings (my_list, bit_position):
    gamma = ""   # not "0b"
    epsilon = ""     # not "0b"
    for k in range(12):  # 5 for example data, 12 for actual data
        column_counter = 0

        for item in my_list:
            bit_position = k
            # column_counter += item([bit_position])  # TypeError: 'str' object is not callable
            column_counter += (int(item [bit_position]))
            #the line above returnred "ValueError: invalid literal for int() with base 10: 'i' "
            # although it did not return an error using day3_example data
            # print("column_counter = ",column_counter)
            if column_counter >= (len(my_list)/2):
                gam_add  = str(1)
                eps_add = str(0)
            else:
                gam_add = str(0)
                eps_add = str(1)

        gamma += gam_add 
        epsilon += eps_add
            
        # print (" bit_position = ", int(bit_position), "column_counter = ", column_counter,  "gam_add = ", (gam_add), " eps_add = ", (eps_add))
       
    print("gamma = ", gamma, "epsilon = " ,epsilon)
    
    gamma_rate = int(gamma, 2)
    print("gamma_rate = ", gamma_rate)
    epsilon_rate = int(epsilon, 2)
    print("epsilon_rate = ", epsilon_rate)
    power_consumption = gamma_rate * epsilon_rate
    print("power consumption = ", power_consumption)
    return (gamma, epsilon)
 
# my_list = example_data_list
my_list = day3_data_list
binary_strings(my_list,0)


"""   using example data returned
gamma =  10110 epsilon =  01001
gamma_rate =  22
epsilon_rate =  9
power consumption =  198
which is correct

""" 

""" using day3.txt returned
gamma =  010100111001 epsilon =  101011000110
gamma_rate =  1337
epsilon_rate =  2758
power consumption =  3687446
which is correct
"""

"""     open data file as str
filename = day3_example_data_path
file = open(filename, mode ="r")
text = file.read()
print(file.close)
print(text)
  this prints a column of strings without losing the leading zeros   """ 






















