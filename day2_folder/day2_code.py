import pandas as pd
# import the day2 exercise data into Python

# path_to_input = "day2_example.txt"
# day2_example = pd.read_csv(path_to_input, header=None)
# print ("This is the example data to verify the challenge answer <br> ",day2_example.head)
# get description of data
# print (day2_example.dtypes)

path_to_input = "day2.ini"
day2_data = pd.read_csv(path_to_input, header=None)
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

# sort the list for the three possible vectors

sorted_vectors = sorted(flat_ls)
# sorted_vectors = flat_ls.sort()
# print("this is the sorted flat list ", [sorted_vectors])  # output is sorted list BUT flat_ls is unchanged

# need to count the the number for each direction
#for1 = flat_ls.count("forward 1")
#print ("forward 1 = ",for1)

forwards = 0
for i in range (11):
    num = i
    numi = str(num)
    # print (numi)
    s1 ="forward "
    ctr = s1 +  numi
    # print(ctr)
    forwards += sorted_vectors.count(ctr)
print("forward vectors = ",forwards)

downs = 0
for i in range (11):
    num = i
    numi = str(num)
    # print (numi)
    s1 ="down "
    ctr = s1 +  numi
    # print(ctr)
    downs += flat_ls.count(ctr)
print("down vectors = ",downs)

ups = 0
for i in range (11):
    num = i
    numi = str(num)
    # print (numi)
    s1 ="up "
    ctr = s1 +  numi
    # print(ctr)
    ups += flat_ls.count(ctr)
print("up vectors = ",ups)

# slice sorted_vectors into three new lists
# downs = 1 to 391, slice 0 to 391
# ups = 801 to 1000, slice -200:
# forwards = 391 to 801
forward_vectors = sorted_vectors[391:800]
print(forward_vectors)

down_vectors = sorted_vectors [0:391]
print(down_vectors)

up_vectors = sorted_vectors [-200:]
print(up_vectors)




# split each of the sorted strings into two strings using list comprehension
# down_steps =[w[-1:] for w in down_list]
# print("down_steps = ", down_steps)
# print("down_steps = ", [w[-1:] for w in down_list]) #  got desired results!!

# convert vertical_steps "str" to int
#print("vertical_values = ", [w[int] for w in vertical_steps])
    #  error - vertical steps is not defined despite line 36??

#print("vertical_value = ", [n[int] for n in [vertical_steps]])
    #   same error as above

def vector_value(vector_list):  # tuple formant is ["direction"_"value"]  
    #split list into two strings
    vector_steps =[w[-1:] for w in vector_list]
    print(vector_steps)
    #convert "value" to int and add the steps
    vector_value = 0
    for item in vector_steps:
        int_item = int(item)
        vector_value += int(item)
    print(vector_value)

forward_values = vector_value(forward_vectors)
# print("forward values = ", forward_values)

up_values = vector_value(up_vectors)

down_values = vector_value(down_vectors)

course = 1993 *(1943-945)
# print(course)







# the following code was for the exaplie data
# flat_list = ['down 5', 'down 8', 'forward 2', 'forward 5', 'forward 8', 'up 3']  # manually pasted list ino this line
# print("down_list = ",flat_list[0:2])
# print("forward_list = ",flat_list[2:5])
# down_list = flat_list[0:2]
# print("down_list = ", down_list)
# up_list = flat_list[-1:]
# print("up_list =  ", up_list)


forward_list =  ['forward 2', 'forward 5', 'forward 8']
forward_value = vector_value(forward_list)
print("forward_value = ",forward_value)
horizontal_position = forward_value
print(horizontal_position)

down_list =  ['down 5', 'down 8']
down_value = vector_value(down_list)
print("down_value = ", down_value)

up_list =   ['up 3']
up_value =  vector_value(up_list)
print("up_value = ", up_value)

# calculate new value value aim
aim = [0]
for item in sorted_vectors:  # error = 'NoneType' object is not iterable
    print(item)
    # aim.append(item)
    # print(aim)





# depth_position = []
# for item i

# depth_position = vector_value(down_list) - vector_value(up_list)
# # print(depth_position)
# course = horizontal_position * depth_position
# print("course = ", course)









