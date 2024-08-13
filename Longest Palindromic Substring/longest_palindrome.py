def expandAroundCenter(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return s[left + 1:right]


def longest_palindrome(s: str) -> str:
    temp_str = ""
    for i in range(len(s)):
        str1 = expandAroundCenter(s, i, i)
        str2 = expandAroundCenter(s, i, i + 1)
        if len(str1) > len(str2):
            if len(str1) > len(temp_str):
                temp_str = str1
        else:
            if len(str2) > len(temp_str):
                temp_str = str2

    return temp_str
