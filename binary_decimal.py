# these files from geeksfor geeks  --will nt tun beause of local host issue
# wht are the semicolons ; at the end of each line ??
# for a binary numder coversion
def binaryToDecimal(n):
    num = n;
    dec_value = 0;
    base = 1;
    temp = num;

    while(temp):
        last_digit = temp % 10
        temp = int(temp / 10)
        dec_value += last_digit * base
        base = base * 2
    return dec_value;

num = 10101001;

print(binaryToDecimal(num));

# for strimg
def binaryToDecimal(n):
    num = n;
    dec_value = 0;
    base1 = 1;
    len1 = len(num);

    for i in range(len1 - 1, -1, -1):
        if (num[i] == '1'):    
            dec_value += base1;
        base1 = base1 * 2;
    return dec_value;

num = "10101001";
print("num = ", binaryToDecimal(num));

# this code is from scaler.com
# Function to convert decimal to binary
# using built-in python function
def decimalToBinary(n):
    # converting decimal to binary
    # and removing the prefix(0b)
    return bin(n).replace("0b", "")
   
# Driver code
if __name__ == '__main__':
    # calling function
    # with decimal argument
    print(decimalToBinary(77))


# this code is from geekstogeeks
# Function to convert decimal number
# to binary using recursion
def DecimalToBinary(num):
     
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')
 
# Driver Code
if __name__ == '__main__':
     
    # decimal value
    dec_val = 24
     
    # Calling function
    DecimalToBinary(dec_val)

# using builtin function
# Python program to convert decimal to binary
   
# Function to convert Decimal number
# to Binary number
def decimalToBinary(n):
    return bin(n).replace("0b", "")
   
# Driver code
if __name__ == '__main__':
    print(decimalToBinary(8))
    print(decimalToBinary(18))
    print(decimalToBinary(7))

