from pprint import pprint

# plain script
item = '\n12345'     #immutable
clean_item =item.replace("n", "")   # returns expected result
print(clean_item)    

clean_item = item.strip('n')       #returns expected result
print(clean_item) 

item = '123'
item_int = int(item)
print(item_int)

# simple iteration
my_list = ['\n123', '\n456', '\n7890']
clean_list = []
for item in my_list:
    clean_list.append(item.replace("\n", ""))  # returns expected results
print(clean_list)

my_list = ['123', '456', '7890']
int_list = []
for item in my_list:
    int_list.append(int(item))   # returns expected results
print(int_list)

''' combine both into one'''
my_list = ['\n123', '\n456', '\n7890']
clean_list = []
int_list = []
for item in my_list:
    clean_list.append(item.replace("\n", ""))  
for item in clean_list:
    int_list.append(int(item))   # returns expected results
print(int_list)

'''     now a function  '''
def int_list(any_list):
    int_list =[]
    clean_list = []
    for item in my_list:
        clean_list.append(item.replace("\n", ""))  
    for item in clean_list:
        int_list.append(int(item))  
    return int_list

print("int_list = " ,int_list(my_list))

'''   need to import day1 data'''

''' convert to a dictionary
# combine the lists into a new dictionary
for num in my_list:
    day1_depths = {}
    key = -1
# for item in range(0,2000):
    key += 1
    # key =  day1_keys[item]
    value = my_list[num]
    day1_depths[key] = value
#print(day1_depths)  # output is the desired dictionary      
# ''' 



# gamma = str(10110)  TypeError
# gamma = str(0b10110)  ValueError
gamma = bin(0b10110)  #returns 22
gamma_rate = int(gamma, 2)
print(gamma_rate)
