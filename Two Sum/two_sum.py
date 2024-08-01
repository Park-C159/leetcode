def twoSumSimple(nums, target):
    for i in range(len(nums)):
        num1 = nums[i]
        for j in range(i + 1, len(nums)):
            num2 = nums[j]
            if num1 + num2 == target:
                return [i, j]
            else:
                continue

def twoSum(nums, target):
