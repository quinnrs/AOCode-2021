import pandas as pd
import numpy as np

# +-+-+-+-+-+-+- day 3 -- *--*-*-*-*--*---*-*-*-*

class AOC2021:
     """ 25 challenges (day1 to day25) """

def __init__(self):
     # self.my_list = my_list
     """ future init instance variables :  self.things = things  """

"""   import the example data   """

# day3_data = pd.read_csv("day3.txt", header=None)
# day3_example_data = pd.read_csv("day3_example.txt", header=None)
# day3_example_data = pd.read_csv("day3_example.txt")   this was not given i copied and pasted into a .txt file
# print(day3_data.head)
# print(day3_example_data.head)
# print (day3_example_data.dtypes)

"""     manually input the  example data  as strings """
day3_example_data =["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]


"""
The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly, can tell you many useful things about the conditions of the submarine. The first parameter to check is the power consumption.

You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report.

"""


def column_count(my_list):
     for k in range(5):
          bit_position = k
          for item in my_list:
               #print("list item = ", item)
               bit_position = k
               #print ("list item = ", item, " bit position = ", bit_position)
               key_counter = 0
               # key_counter += int(item[k][bit_position])
               key_counter += int(item [bit_position])
               print  ("key_counter = ",key_counter)
     
column_count(day3_example_data)

        