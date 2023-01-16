gamma = str(10110)  # gamma rate returns 22 which is correct
# gamma = str(0b10110)  # gamma rate returns "ValueError: invalid literal for int() with base 2: '22'
# gamma = 0b10110   #rgamma rate r eturns "int() can't convert non-string with explicit base"
# gamma = bin(0b10110)  #returns 22
gamma_rate = int(gamma, 2)
print(gamma_rate)