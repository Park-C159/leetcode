from reverse_integer import *

x1 = 123
x2 = -901000
x3 = 1201232341423123
x4 = 0

X = (x1, x2, x3, x4)

for x in X:
    res = reverse(x)
    res_bits = reverse_bits(x)
    print(res_bits)
