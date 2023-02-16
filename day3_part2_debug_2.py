class AOC2021: 
    def __init__(self, data_path):
        self.first_illegal_character = None
        self.data_path = data_path
        self.sort_by_index = data_path
        self.index = 0
        self.bit_position = 0

    # write a method to print a column of binary strings without losing the leading zeros  
    def open_binary_list(self):
        data_list = []
        f = open(self.data_path)
        for  line in f:
            data_list.append(line.strip())
            # print(data_file)
        return data_list

    # write a method to sort a liat of binary numbers
    def sort_binary_list(self, my_list, bit_position):
        column_counter = 0
        for k in range(5):  # 5 for example data, 12 for actual data
            column_counter = 0
            # most_commons = [] # not working = can only get str
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
                # most_commons += (str(most_common))   # cannot iterate with int
            print("for bit_position ",bit_position, "column_counter = ", column_counter, "most_common = ",most_common, " least_common = ", least_common)
        return bit_position, most_common, least_common

    """    part 2     """

   
    

    # write a method to split the sorted list
    # def ox_or_co(self, my_list, sort_binary_list):
    def ox_or_co(self, my_list, most_common, bit_position):
        column_counter = 0
        for k in range(len(my_list)):
            ox = []
            co = []
            for bp in range (5): # 5 for example data - 12 for day3_data
                if int(my_list[k][bp]) >= most_common:
                    ox_or_co = "ox"
                    ox.append(my_list[k])
                else:
                    ox_or_co = "co"
                    co.append(my_list[k])
                print("ox_or_co = ", most_common)
                print(ox)
                print(co)
        return  ox_or_co, ox, co
        # return ox,co 


    def bp_winner(self, my_list, bit_position):
        # (most_common, least_common) = self.sort_binary_list(my_list, bit_position)
        # (most_common, least_common) = self.sort_binary_list(bit_position=0)
        (most_common, least_common) = self.sort_binary_list(my_list, bit_position=0)
        bp_winner = self.co_or_ox(my_list, most_common, bit_position)
        return (bp_winner, most_common, least_common)





    # write a method to shrink the two lists using recursion
    def o2_gen_and_co2_scrub(self, my_list, bit_position, ox_or_co, ox, co):
        if len(my_list) == 1:  # single list remaining
            # if ox_or_co == "ox":
            if most_common == "ox":
                self.o2_gen = f"0b{my_list[0]}"
            else:
                most_common == "co"
                self.co2_scrub = f"0b{my_list[0]}"
            print("recursion is complete")
            return
        most_common, co, ox = self.bp_winner(my_list, bit_position)
        
        if ox_or_co  == "ox" :
            self.ox += most_common
            data_pack = ox
            o2_gen = most_common(my_list, bit_position)
        else:
            data_pack = co
            if most_common == "1":
                self.co += "0"
            else:
                self.co += "1"         
        co2_scrub = most_common(my_list, bit_position)
        return my_list, co2_scrub, o2_gen
        bit_position += 1
        if bit_position == 12:
            #12 = one data item
            print("Something is worng - stopped for runawat recursion")
            return
    
        self.most_common(sort_binary_list(bit_position))
        self.sort_binary_list(my_list, bit_position=0, most_commmon ="ox")
        self.sort_binary_list(my_list, bit_position=0, least_common = "co")
         
        self.ox_or_co(my_list, bit_position = 0, ox_or_co = "ox")
        self.ox_or_co(my_list, bit_position = 0, ox_or_co = "co")

        self.o2_gen_and_co2_scrub(my_list, bit_position, ox_or_co)

        ox_rating = int(self.ox)
        co_rating = int(self.co)

    
    
    def life_support_rating(self, o2_gen, co2_scrub ):
        life_support_rating = o2_gen * co2_scrub
        print(o2_gen, co2_scrub)
        print("life_support_rating = ", life_support_rating)
        
 
my_data_path = "/Users/rsq2/Code_projects/2021-Challenge/input_data/day3_example.txt"
# call the class
aoc = AOC2021(data_path = my_data_path)   
# call the method
my_list = (aoc.open_binary_list())
print(my_list)
bit_position = len(my_list)
print(aoc.sort_binary_list(my_list, bit_position))


# my_list = (aoc.open_binary_list())
# bit_position = len(my_list)
# bit_position = len(item.my_list)
# most_common, least_common = aoc.sort_binary_list(my_list, bit_position)
most_common = aoc.sort_binary_list(my_list, bit_position)
least_common = aoc.sort_binary_list(my_list, bit_position)

#call the method
print(aoc.ox_or_co(my_list, bit_position, most_common))


# call the method
print(aoc.bp_winner(my_list, bit_position))

print(aoc.o2_gen_and_co2_scrub())

print(aoc.life_support_rating())

# if len(my_list) == 1:
        #   if ox_or_co == "ox":
        #       self.ox = f"0b{my_list[0]}"
        #   else:
        #       self.co = f"0b{my_list[0]}"
        # return  # we are done     """
