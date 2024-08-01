import math


def perf_num_simple(num):
    if num == 1: return False
    s = 1

    for i in range(2, int(math.sqrt(num)) + 2):
        if num % i == 0:
            s = s + i + num // i
    return s == num

def perf_num(num):
    if num == 1: return False
    if num == 2: return False
