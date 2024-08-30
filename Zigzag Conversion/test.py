from zig_conversion import *

s1 = "PAYPALISHIRING"
num1 = 3
s2 = "PAYPALISHIRING"
num2 = 4
s3 = "ABCDE"
num3 = 4

test = [(s1, num1), (s2, num2), (s3, num3)]

for t in test:
    res = convert(t[0], t[1])

    print(res)



