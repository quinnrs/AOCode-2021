# import pandas as pd
# import numpy as np
# from pprint import pprint


# +-+-+-+-+-+-+- day 3 -- *--*-*-*-*--*---*-*-*-*

"""
The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly, can tell you many useful things about the conditions of the submarine. The first parameter to check is the power consumption.

You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report.

"""
 
def import_day3_data():
     # f = open("input_data/day3.txt")
     f = open("input_data/day3_example.txt")
     day3_data = []
     counter = 0
     for line in f:
          counter += 1
          # day3_data.append(int(line)) # for a list of int
          day3_data.append(line.strip())   # for a list of str
         #  print(counter)  # debugging
     return day3_data
     
day3_data = import_day3_data()  # usingexample data
print(len(day3_data))
print(day3_data[0:5])

# convert string to binary
 
 
# def column_count(my_list, bit_position):
def binary_analysis(my_list):
     
     """  determine most common bit position for each position
               in the list of binary numbers
          divide the dist into two new lists
               gamma - which is most common bit position
               esilon - leastcommon bit position
     """
     gamma = ("0b")
     epsilon = ("0b")
     for k in range(5):  # 5 for example data, 12 for actual data
          column_counter = 0
          # gamma = ["0b"]
          # epsilon = ["0b"]
          # print("starting iteration by bit_position")

          for item in my_list:
               #column_counter = 0
               bit_position = k
               # column_counter += (item [bit_position])
               column_counter += (int(item[bit_position]))
          # print("column_counter = ",column_counter)
              
          if column_counter >= (len(my_list)/2):
               most_common_value = 1
               least_common_value = 0
          else:
               most_common_value = 0
               least_common_value = 1
        
          print (" bit_position = ", int(bit_position), "column_counter = ", column_counter,  "most_common_value = ", int(most_common_value), " least_common_value = ", int(least_common_value))

          gamma += str(least_common_value)
          print(f"gamma = ", gamma)
          epsilon += str(most_common_value)
          print(f"epsilon = ", epsilon)
          # return gamma, epsilon


     gamma_rate = int(gamma, 2)
     print("gamma_rate = ", gamma_rate)
     epsilon_rate = int(epsilon, 2)
     print("epsilon_rate = ", epsilon_rate)
     power_consumption = gamma_rate * epsilon_rate
     print("power consumption = ", power_consumption)
     return(gamma, gamma_rate, epsilon, epsilon_rate, power_consumption)



# call the function 
my_list = day3_data
# print(gamma_rate = binary_analysis(my_list))
# print(epsilon_rate =  binary_analysis(my_list))
# print(power_consumption =  binary_analysis(my_list))



          # good to here

""" -----    part2 ------   """

"""  determine most common bit position for each position
               in the list of binary numbers
          divide the dist into two new lists           
"""
# calculate most common value for each bit position in a binary list
def most_common_value(my_list, bit_position):
     column_counter = 0
     for item in my_list:
          column_counter += (int(item[bit_position]))
     # bit_position = item
     # column_counter += (int(item [bit_position]))
     # column_counter += (int(item))
     if column_counter < (len(my_list)/2):
          most_common_value = 0
     else:
            most_common_value = 1
     print("for bit_position ",bit_position, "column_counter = ", column_counter, " most_common _value= ",most_common_value)
     return most_common_value

# call the function

print("test_ox_slicer = ", str(most_common_value(my_list, bit_position =0)))
# print(type(str(most_common_value(my_list, bit_position=0))))
# print(type(test_ox_slicer))


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
        slicer = str(most_common_value(my_list, bit_position))  # use for keepers
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

def least_common_position(my_list, bit_position):
    column_counter = 0
    for item in my_list:
        # bit_position = k
        column_counter += (int(item [bit_position]))
        if column_counter < (len(my_list)/2):
            least_common_position = 1
        else:
            least_common_position = 0
    # print("for bit_position ",bit_position, "column_counter = ", column_counter, " least_common = ",least_common)
    return least_common_position

# call
print("")
least_common_position_0 = least_common_position(my_list, bit_position = 0)
print("least common positon for bp[0] is ", least_common_position_0)

def co_data(my_list, bit_position):
    for bp in range (0,12):
        bit_position = bp
        # my_list =
        slicer = str(least_common_position(my_list, bit_position))  # use for keepers    
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

"""   see file ListRecursion_2  for remainder of solution 
          I have to manually input values to complete the solution 


o2_item = ox_data[0]
print(o2_item)

o2_gen = binaryToDecimal(o2_item)
print("o2_gen =", o2_gen)

co2_item = co_data[0]
print(co2_item)
co2_scrub = binaryToDecimal(co2_item)
print("co2_scrub =", co2_scrub)

life_support_rating = o2_gen * co2_scrub
print("life_support_rating = " ,life_support_rating)
"""

# totally oboleste junk beow

"""
          print("trying epsilon")
          for line in my_list:
               epsilon += str(least_common_value)
               # epsilon += [str(least_common_value)]
          print(epsilon)

          gamma = ["0b"]
          epsilon = ["0b"]

          print("trying gamma")
          for line in my_list:
               # gamma += [str(most_common_value)]  # Error here
               gamma += (str(most_common_value))






# call the function
# print(column_count(day3_data))


"""
"""

    
          gamma_rate = int(gamma, 2)
          print("gamma_rate = ", gamma_rate)
          epsilon_rate = int(epsilon, 2)
          print("epsilon_rate = ", epsilon_rate)
          power_consumption = gamma_rate * epsilon_rate
          print("power consumption = ", power_consumption)
     return(gamma, gamma_rate, epsilon, epsilon_rate, power_consumption)
"""
# call the function



     
     
     
     
     
"""

f = open(day3_data)
for line in f:
     # data_list.append(int(line)) for a list of int
     gamma.append(line.strip())   # for a list of str
print(gamma)

          for bit_position in range(12):
          # gamma = gamma + ("most_common_value")
          # gamma += column_count(day3_data)
          #    gamma += str(most_common_value)
               gamma += "most_common_value"
               epsilon += "least_commom_value"
          # gamma.append[(most_common_value)]
          print("gamma = ", gamma)
          # epsilon = epsilon + ("least_common_value")
          # epsilon.append(str[least_common_value])
          print("epsilon = ", epsilon)       
    
     

          # combine list of lists into a single list aka "flatten the list" via list comprehension
          flat_ls = [gamma]
          for i in gamma:
               for j in i:
                    flat_ls.append(j)
          print(flat_ls) # output is a single list


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
     
"""
"""
def column_count(my_list, bit_position):
     print("the function has been called")
     gamma = ("0b")
     epsilon = ("0b")
     for k in range(5):  # 5 for example data, 12 for actual data
          column_counter = 0
          # gamma = ["0b"]
          # epsilon = ["0b"]
          # print("starting iteration by bit_position")

          for item in my_list:
               #column_counter = 0
               bit_position = k
               # column_counter += (item [bit_position])
               column_counter += (int(item [bit_position]))
          print("column_counter = ",column_counter)
              
          if column_counter >= (len(my_list)/2):
               most_common_value = 1
               least_common_value = 0
          else:
               most_common_value = 0
               least_common_value = 1
        
          print (" bit_position = ", int(bit_position), "column_counter = ", column_counter,  "most_common_value = ", int(most_common_value), " least_common_value = ", int(least_common_value))
           
# all results as expected to this point ---------
          
                   
""" 
"""  
          print("trying epsilon")
          for line in my_list:
               epsilon += str(least_common_value)
               # epsilon += [str(least_common_value)]
          print(epsilon)

          gamma = ["0b"]
          epsilon = ["0b"]
          print("trying gamma")
          for line in my_list:
               gamma += [str(most_common_value)]
            
          gamma_rate = int(gamma, 2)
          print("gamma_rate = ", gamma_rate)
          epsilon_rate = int(epsilon, 2)
          print("epsilon_rate = ", epsilon_rate)
          power_consumption = gamma_rate * epsilon_rate
          print("power consumption = ", power_consumption)
     # return(gamma, gamma_rate, epsilon, epsilon_rate, power_consumption)
"""

"""  this section is obsolete code
class AOC2021:
     pass

def __init__(self):
     self.first_illegal_character = None
def __init__(self, data_path):
     self.data_path = data_path
"""

    
""" alternate import approach for exampledata
# filename = "/Users/rsq2/Code_projects/2021-Challenge/input_data/day3_example.txt"   
file = open(filename, mode ="r")
text = file.read()
print(file.close)
print(text)
   this prints a column of strings without losing the leading zeros   


def day3_example_data(data_path):
     data_file = []  # a list of binary strings
     f = open(data_path)
     for  line in f:
          data_file.append(line.strip())
          print(data_file)
     return data_file

day3_example_data("input_data/day3_example.txt")
print(day3_example_data)
"""

""" import the day3_example_data  - 
path_to_input = "/Users/rsq2/Code_projects/2021-Challenge/input_data/day3_example.txt"
day3_example_data_column = pd.read_csv(path_to_input, header=None)
print ("This is the example data in the challenge  description<br> ",day3_example_data_column.head(10))
# convert data column to data_list
ls = day3_example_data_column.values.tolist()
# combine list of lists into a single list aka "flatten the list" via list comprehension
day3_example_data = []
for i in ls:
    for j in i:
        day3_example_data.append(str(j))   #need a list of str
print("day3_example_data = ", day3_example_data)
original """

""" import the day3_data 
path_to_input = "/Users/rsq2/Code_projects/2021-Challenge/input_data/day3.txt" 
day3_data_column = pd.read_csv(path_to_input, header=None)
print ("This is the actual data to be used in the challenge <br> ",day3_data_column.head(10))
#convert data column to data_list
ls = day3_data_column.values.tolist()
# combine list of lists into a single list aka "flatten the list" via list comprehension
day3_data = []
for i in ls:
    for j in i:
        day3_data.append(str(j))   # need a list of str
# print("day3_data = ", day3_data)   # returns a single list of strings


# manually input the  example data  as strings 

# my_list = day3_example_data
# column_count(day3_data, 0)
 # output as expected up to this point  

# gamma =["0b", "1", "0", "1", "1", "0"]
# gamma = [0b10110]
# epsilon =[0b01001]
"""

"""  
# copied this function from Djangocentral
def BinaryToDecimal(binary):
     decimal = 0
     for digit in binary:
        decimal = decimal*2 + int(digit)
     return decimal
     print("The decimal value is:", decimal)

binary = gamma
# Calling the function
gamma_rate = BinaryToDecimal(binary)
print("gamma_rate = ",gamma_rate)

# gamma_rate =  int(gamma, 2)
# print(gamma_rate)  error = int() can't convert non-string with explicit base

epsilon_rate = BinaryToDecimal([0b01001])
print("epsilon_rate = ", epsilon_rate)
"""

