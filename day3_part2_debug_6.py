my_data_path = "/Users/rsq2/Code_projects/2021-Challenge/input_data/day3_example.txt"

# write a function to open a file of binary stings without losing the lading zeros
def open_data_file(data_path):
    data_file = []
    f = open(data_path)
    for line in f:
        data_file.append(line.strip())
    return data_file

# call the function
data_file = open_data_file(my_data_path)
print("data_file = ", data_file)

# write a function to sort a list of binary numbers
def sort_binary_list(my_list, bit_position):
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

# call the function
my_list = data_file
bit_position = len(my_list)
sort_binary_list(my_list, bit_position)
print(sort_binary_list)


"""  - - - part 2 - - - """    

def ones_or_zeros(my_list, bit_position, most_common="1"):
    print("starting part2")
    ones = []
    zeros = []
    for item in my_list:
        # if item[bit_position] == "1":
        if item[bit_position] == str(most_common):
            ones += [item]
        else:
            zeros += [item]
    print("ones = ", ones)
    print("zeros = ", zeros)
    return  ones_or_zeros, ones, zeros
    # return (ones, zeros) 

# call the function 
print("function call for ones_or_zeros at line 59")
print(ones_or_zeros(my_list, most_common=1, bit_position=0))
# print("ox = ",ones_or_zeros(my_list, most_common=1, bit_position=0))
# print("co = ",ones_or_zeros(my_list, most_common=1, bit_position=0))
# print(co)
# write a function to shrink the lists using recursion
# def o2_gen_and_co2_scrub(my_list, bit_position):


""" - - - this is list 1st then bp version  - - - """
def shrink_my_list(my_list):
    print(my_list)
    print("starting recursion")
    print("list has ", len(my_list), "items")

    # call ones_or_zeros for co(which is zeros) at bit_position 1
    print("iteration 1 using bit_position 1")
    ones = (ones_or_zeros(zeros, bit_position = 1))
    print("ones = ",ones)
    split_bp1 = ones_or_zeros(zeros, bit_position = 1)
    keepers = zeros
    print (split_bp1)

    # this is for zeros now
    ones_or_zeros = zeros
    keepers = []
    bit_position = 1

    if len(my_list) == 1:  # single list remaining
        if ones_or_zeros == "ones":
        # if most_common == "ones":
            o2_gen = f"0b{my_list[0]}"
        else:
            # most_common == "zeros"
            co2_scrub = f"0b{my_list[0]}"
            print("recursion is complete")
            return
    
    # begin recursion
    # bit-position = 1

    for item in my_list:
        print(item)
        bp = bit_position
        for bp in range(1,5):
            column_counter = 0
            if item[bit_position] == 0:
                column_counter += 1
            print(bit_position, column_counter)
        if column_counter < (len(my_list)/2):
            most_common = 0
            keepers += [item]
        else:
            most_common = 1
        print(" for bp ", bit_position, "most_common = ", most_common, "keepers = ", keepers)
    bit_position += 1

    if bit_position == 5:   #12 = one data item
        print("Something is worng - stopped for runaway recursion")
    return bit_position

# call the function
zeros =  ['00100', '01111', '00111', '00010', '01010']
bit_position = len(zeros)
print(sort_binary_list(zeros, bit_position))
print("first_split = ",shrink_my_list(zeros))



"""        
#call the function
print("o2_gen = ", o2_gen_and_co2_scrub(ox, bit_position=1))
print("co2_scrub = ", o2_gen_and_co2_scrub(co, bit_position=0))
"""





    


    

        

        



       
"""   
        

    # return  ox_or_co, ox, co

        # for k in range (5): #5 for example data
            # bit_position = my_list.index()

# bp_winner = (bp_winner(my_list, bit_position))  
# print(ox_or_co(my_list, bit_position))
# print(ox_or_co(my_list, int(bp_winner), int(bit_position)))     

   

    
    
def life_support_rating(o2_gen, co2_scrub):
        life_support_rating = o2_gen * co2_scrub
        print(o2_gen, co2_scrub)
        print("life_support_rating = ", life_support_rating)

"""     
 



# if len(my_list) == 1:
        #   if ox_or_co == "ox":
        #       self.ox = f"0b{my_list[0]}"
        #   else:
        #       self.co = f"0b{my_list[0]}"
        # return  # we are done   

"""   this is the bp 1st then list version ---
def shrink_my_list(my_list, bit_position):
    # my_list = [co]
    # for item in my_list:
        # print("current item = " , [item])
    for k in range(1,5):
        column_counter = 0
        bit_position = k
        keepers = []
        for item in my_list:
            print("current item = " , [item])

            if item[bit_position] == 0:
                column_counter += 1
            print(bit_position, column_counter)
            
            if column_counter >= (len(my_list)/2):
                most_common = 0
                keepers += [item]
            else:
                most_common = 1
            print(" for bp ", bit_position, "most_common = ", most_common, "keepers = ", keepers)

            if bit_position == 5:   #12 = one data item
                print("Something is worng - stopped for runaway recursion")
    return bit_position


    - - - this is the bp 1st then list version """
def shrink_my_list(my_list, bit_position):
    # my_list = [co]
    # for item in my_list:
        # print("current item = " , [item])
    for k in range(1,5):
        column_counter = 0
        bit_position = k
        keepers = []
        for item in my_list:
            print("current item = " , [item])

            if item[bit_position] == 0:
                column_counter += 1
            print(bit_position, column_counter)
            
            if column_counter >= (len(my_list)/2):
                most_common = 0
                keepers += [item]
            else:
                most_common = 1
            print(" for bp ", bit_position, "most_common = ", most_common, "keepers = ", keepers)

            if bit_position == 5:   #12 = one data item
                print("Something is worng - stopped for runaway recursion")
    return bit_position


