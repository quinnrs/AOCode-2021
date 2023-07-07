# binary conversion


def BinaryToDecimal(binary):
     decimal = 0
     for digit in binary:
        decimal = decimal*2 + int(digit)
     return decimal
     print("The decimal value is:", decimal)

binary = [0b01001]
decimal = BinaryToDecimal(binary)
# print(decimal)
print("the decimal value = ", decimal)

test_list = ["01001"]
gamma = ["0b"]
for item in test_list:
    gamma +=[str(item)]
print(gamma)

