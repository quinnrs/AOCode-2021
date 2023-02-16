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



