from typing import List

def longestCommonPrefix(strs: List)->str:
    if not strs:
        return ""

    # 以第一个为基准
    for i in range(len(strs[0])):
        char = strs[0][i]
        for st in strs:
            if i >= len(strs[0]) or i >= len(st) or st[i] != char:
                return strs[0][:i]

    return strs[0]


test = ([""], ["a"], ["flower","flow","flight"], ["dog","racecar","car"], ["ab", "a"])

for i in test:
    res = longestCommonPrefix(i)
    print(res)
