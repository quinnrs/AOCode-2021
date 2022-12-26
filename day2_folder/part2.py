import pandas as pd
day2_data = pd.read_csv("day2.ini", header=None)
# day2_data = pd.read_csv("day2_example.txt", header=None)
day2_data.head
print (day2_data.dtypes)

# convert to list using tolist() function
# ls = df.day2_data.input.tolist()
ls = day2_data.values.tolist()

# combine list of lists into a single list aka "flatten the list" via list comprehension
flat_ls = []
for i in ls:
   for j in i:
        flat_ls.append(j)
        # print("this is the flat list of the input data",(flat_ls)) # output is a single list of strings

# the following code was for the example data
# example_data = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']  #manually pasted into file
# print("")
# position = horizontal * depth
aim = 0
depth = 0
horizontal = 0
# for items in example_data:
for items in flat_ls:
    #split the string
    direction = items[0]
    # print("direction = ", direction)
    step_string = items[-1]
    # print("step_string = ", step_string)
    step = int(step_string)
    # print("step = ", step_string)
    
    if direction == "f" and aim == 0:   # this does not work
        horizontal += step
        depth = aim * step
    if direction == "f" and aim != 0 :
        # aim += step        #forward does not change depth
        horizontal += step 
        depth += aim * step
        
    elif direction == "d":
        aim += step
    elif direction == "u":
        aim -=step
   
    print("aim = ", aim)
    print("horizontal = ", horizontal)
    print("depth = ", depth)
    # print("")
solution = 1006983 * 1993
print("solution = depth x horizontzal = ", solution)