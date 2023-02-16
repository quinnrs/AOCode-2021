# AOC script combining previous separate files for each day
import pandas as pd
""" 25 challenges (day1 to day25) """

class AOC2021:   
    # additional methods to be added later 

    def __init__(self, data_path):
        self.first_illegal_character = None
        self.data_path = data_path
        self.sort_by_index = data_path
        
    # data_path is now defined and can be used  anywhere in the class by calling self.data_path    

    # write a method to open a txt.file with one data point on each line and convert to int and return a list   
    # def open_data_file(self, data_path):
    def open_data_file(self):
        data_file = []
        # f = open(data_path)
        f = open(self.data_path)
        for line in f:
            data_file.append(int(line))
        return data_file

    # write a method to convert a list to a dictionary
    # def list_to_dictionary(self, open_data_file):
    def list_to_dictionary(self, data_file):
        keys = []
        for k in range(len(data_file)):
            # keys += k  # int not interable
            keys += str(k)
        print ("keys = ", keys)
        
        list_to_dictionary = dict(zip(keys, data_file))
        print(list_to_dictionary)
        return(list_to_dictionary)

# write a method to print a column of binary strings without losing the leading zeros  
    def open_binary_list(self):
        data_list = []
        f = open(self.data_path)
        for  line in f:
            data_list.append(line.strip())
            # print(data_file)
        return data_list

# write a method to sort a list of binary numbers
    def sort_binary_list(self, my_list, bit_position):
        column_counter = 0
        for k in range(5):  # 5 for example data, 12 for actual data
            column_counter = 0
            for item in my_list:
                # print("current item = " , [item])
                bit_position = k
                column_counter += (int(item [bit_position]))
                # print("column_counter = ",column_counter)
                if column_counter >= (len(my_list)/2):
                    most_common = 1
                    least_common = 0
                else:
                    least_common = 1
                    most_common = 0
            print("for bit_position ",bit_position," most_common = ",most_common, " least_common = ", least_common)
        return most_common, least_common 

# call the class
my_data_path = "/Users/rsq2/Code_projects/2021-Challenge/input_data/day3_example.txt"
# call the class
aoc = AOC2021(data_path = my_data_path)   
#call the method
my_list = (aoc.open_binary_list())
print(my_list)
bit_position = len(my_list)
sort_binary_list = (aoc.sort_binary_list(my_list, bit_position))

#    =-=-=-=-  day 1 =-=-=-       
# my_data_path = "/Users/rsq2/Code_projects/2021-Challenge/input_data/day1_example.txt"
# my_data_path = "/Users/rsq2/Code_projects/2021-Challenge/input_data/day1.txt"
# call the class
# aoc = AOC2021(data_path = my_data_path)
# call the method
# day1_example_data = aoc.open_data_file()
day1_data = aoc.open_data_file()

 
# day1_example_data = self.data_path
# day1_example_data = data_path("/Users/rsq2/Code_projects/2021-Challenge/input_data/day1_example.txt")

def count_depth_increases(my_list):
    counter = 0
    my_list = day1_data
    # my_list = day1_data
    print("len =", len)
    # for i in range (0,len(my_list)-1): # for part 1
    # for i in range (0, len(day1_depth_readings)-1): # for part1
    for i in range (0,len(my_list)-3): # for part 2  
        # change = day1_data[(i)+1] - day1_data[(i)]    # for part 1
        change = day1_data[(i)+ 3] - day1_data[(i)]     # for part 2
        # print("change = ", change)
        if change > 0:
            counter +=1
        # print("counter = ", counter)
    print("The number of depth increases =" , counter)

count_depth_increases(day1_data)
 #returned 7 which is correct for example data 


# now solve using day1.txt  
# manually comment out calls to day1_example data
# and replace with calls to day1.txt immediately below that line 

# returned 1451 which is correct for day1_data


# part 2   - change the depth increase definition to 3 steps   note that (day2+day3+day4) -(day1+day2+day3) is equal to day4 - day1 


# returned 1395 which is correct for part 2  
  
# +_+_+_+_+_+_ day 2 _+_+_+_+_+_+_
# my_data_path = "/Users/rsq2/Code_projects/2021-Challenge/input_data/day2_example.txt"
my_data_path = "/Users/rsq2/Code_projects/2021-Challenge/input_data/day2.txt"

day2_data = pd.read_csv(my_data_path, header=None)
print ("This is the day2 input data for the challenge <br> ",day2_data.head)
# get description of data
print (day2_data.dtypes)

# convert to list using tolist() function
# ls = df.day2_data.tolist()   values is required
ls = day2_data.values.tolist()   #.valuesis required

# combine list of lists into a single list aka "flatten the list" via list comprehension
flat_ls = []
for i in ls:
   for j in i:
        flat_ls.append(j)

# combine list of lists into a single list aka "flatten the list" via list comprehension
flat_ls = []
for i in ls:
    for j in i:
        flat_ls.append(j)
# print("this is the flat list of example data strings ",(flat_ls)) # output is a single list of strings

depth = 0
horizontal = 0
for items in flat_ls:
    #split the string
    direction = items[0]
    step_string = items[-1]
    step = int(step_string)

    if direction == "f":
        horizontal += step
    if direction == "d":
        depth  += step
    if direction == "u":
        depth  += -step
print ("horizontal = ", horizontal)
print("depth = ", depth)

solution = depth * horizontal
print("part 1 solution = depth x horizontzal = ", solution)
  
# +_+_+_+_+_+_+_  part 2 +_+_+_+_+_+__
# position = horizontal * depth
aim = 0
depth = 0
horizontal = 0
for items in flat_ls:
    #split the string
    direction = items[0]
    step_string = items[-1]
    step = int(step_string)
    
    if direction == "f" and aim == 0:   # this does not work
        horizontal += step
        depth = aim * step
    if direction == "f" and aim != 0 :
        horizontal += step 
        depth += aim * step
        
    elif direction == "d":
        aim += step
    elif direction == "u":
        aim -=step
   
solution = depth * horizontal
print("part 2 solution = depth x horizontzal = ", solution)
  


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

example_data_list = data_str_list(day3_example_data_path)
# print(example_data_list)
# day3_data_list = data_str_list(day3_data_path)
# print(day3_data_list)

 
# ----------  part1 
def binary_strings (my_list, bit_position):
    gamma = ""   # not "0b"
    epsilon = ""     # not "0b"
    for k in range(5):  # 5 for example data, 12 for actual data
        column_counter = 0

        for item in my_list:
            bit_position = k
            # column_counter += item([bit_position])  # TypeError: 'str' object is not callable
            column_counter += (int(item [bit_position]))
            # the line above returnred "ValueError: invalid literal for int() with base 10: 'i' "
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

# =-=-=-=-=- part 2
my_data_path = "/Users/rsq2/Code_projects/2021-Challenge/input_data/day3_example.txt"
"""  entered earlier  - redundant 
# call the class
aoc = AOC2021(data_path = my_data_path) 
# write a method to print a column of binary strings without losing the leading zeros  
    def open_binary_list(self):
        data_list = []
        f = open(self.data_path)
        for  line in f:
            data_list.append(line.strip())
            # print(data_file)
        return data_list
  entered earlier  - redundant """



# call the method
my_list = (aoc.open_binary_list())
print(my_list)
bit_position = len(my_list)
sort_binary_list = (aoc.sort_binary_list(my_list, bit_position))



"""   using example data returned
gamma =  10110 epsilon =  01001
gamma_rate =  22
epsilon_rate =  9
power consumption =  198
which is correct for part 1

# using day3.txt returned
gamma =  010100111001 epsilon =  101011000110
gamma_rate =  3903
epsilon_rate =  192
power consumption =  749376
which is correct for part 1 

#=-=-  expected result for part 2 is
gamma_rate = 23
epsilon_rate = 10
life_support =230

""" 


