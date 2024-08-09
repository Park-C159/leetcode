from typing import List

def quicksort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [ x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    nums = nums1 + nums2
    nums = quicksort(nums)

    median = len(nums) // 2

    if len(nums) % 2 == 0:
        return (nums[median - 1] + nums[median]) / 2.0
    else:
        return nums[median]
