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
    numMap = dict()
    for index, num in enumerate(nums):
        if target - num in numMap:
            return [numMap[target - num], index]
        numMap[nums[index]] = index
