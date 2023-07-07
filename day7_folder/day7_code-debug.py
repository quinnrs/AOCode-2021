import string

# +_+_+_+_+_+_+_  part 1 +_+_+_+_+_+__

# copy directly into a list
posits = [16,1,2,0,4,2,7,1,2,14]


"""   
list item posit is an int that denotes a start position

make a homogram for start poositions in posit
    keys = str(posit) since posit is int
    values = fuel required where
        fuel_req = distance * fuel_rate - a constant int
        distance = abs (end - start)
        end  i int posit 
"""

def histogram(list):   # k is a list of int
    """ 
    input:  a list of int
    returns d - dictionary
    """
    d = dict()  # a function to create an empty dictionary
    for x in list:     # loops through each num in the list
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
    return d

# print(f"\npositions = ",histogram(posits))

"""  --- error because travel does not include the vlaues of {positions} -- 
for k in histogram(posits): 
    # n = int("k")
    n = int(k)
    # print(k, n)
    fuel_rate = 1
    fuel_req = 0
    start = n
    print(f"\nstart at position", start)
    # meet_point = posits[k]
    # print(n,meet_point)

    
    for k in histogram(posits):  #  this is using k, not v
    # fuel_req = 0
    # meet_point = v
    # print(meet_point)
        end = int(k)
        travel = abs(start-end)       # results not as expected
        # print(travel)
        # print(f"travel = ", travel)
        fuel_req += travel * fuel_rate
    print(f"for meet point at", k, "fuel_req =", fuel_req)
"""   


"""
    define fuel optimum dict, where
        input: a list of int
        return dict wih keys = horizontal position str and values = int
            of start positions
"""

# def fuel_optimum(d):
def fuel_optimum(t):
    fuel_req_dict = {}
    # positions = len("input_data/day7ex.data" + 1)
    # print((len(posits) + 1))
    for k in posits:
    # for n in posits:
    # for position in range(max(posits) + 1): # max position value
        fuel_req = 0
        end = k
        # for k in posits:
        # for k in posits
        for n in posits:
        # for k in range(max(posits) + 1):
            # start = int(k)
            start = int(n)
            # end = int(k)
            fuel_req += abs(end - start)
            # print(fuel_req)  # debugging
        fuel_req_dict[k] = fuel_req
        # fuel_req_dict(n) = fuel_req
        # fuel_req_dict[position] = fuel_req
        # fuel_req_dict += str(fuel_req)  # Typeerror here for str or int
        # fuel_req_dict[int(k)] += (fuel_req)    #KeyError here
        print(fuel_req_dict)    # OK
    return min(fuel_req_dict.values())

# positions = histogram(posits) #dictionary # not using histogram
print(fuel_optimum(posits))

"""    Jerry's function   ---------
def fuel_optimization(self, filename):  
    data = self.get_data_for_day6(filename)
    fuel_usage_dict = {}
    horizontal_positions = len(data)
    for horizontal_position in range(max(data) + 1):
        fuel_cost = 0
        for ii in data:
            #  the first step costs 1, the second step costs 2, the third step costs 3, and so on.
            distance = abs(ii - horizontal_position)
            for dd in range(distance + 1):
                fuel_cost += dd
        fuel_usage_dict[horizontal_position] = fuel_cost
        # print("Calculating", horizontal_position, "out of", max(data) + 1)
    return min(fuel_usage_dict.values())
"""



