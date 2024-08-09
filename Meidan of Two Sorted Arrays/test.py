from median_2_sorted_arrays import *
test1 = {
    "nums1": [1, 3],
    "nums2": [2]
}

test2 = {
    "nums1": [1, 2],
    "nums2": [3, 4]
}

test = (test1, test2)

for t in test:
    median = find_median_sorted_arrays(t.get("nums1"), t.get("nums2"))

    print(median)
