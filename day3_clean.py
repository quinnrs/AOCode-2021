my_data_path = "day3_folder /day3_combo.py"
day3_example_data =["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

 
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
print(gamma_rate = binary_analysis(my_list))
print(epsilon_rate =  binary_analysis(my_list))
print(power_consumption =  binary_analysis(my_list))



