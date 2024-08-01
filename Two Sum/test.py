from two_sum import *

test_tuple = (([2, 7, 11, 15], 9), ([3, 2, 4], 6), ([3, 3], 6))

for nums, target in test_tuple:
    print(twoSumSimple(nums, target))
    print(twoSum(nums, target))