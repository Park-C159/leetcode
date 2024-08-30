test = [" 42", "  -042", "1337c0d3", "0-1", "words and 987", "99999999999999999"]


def my_atoi(s: str) -> int:
    result = 0
    isStart = True
    isNegative = 1
    for i in s:
        if isStart and (i == " " or i == "-" or i == "+"):
            if i == "-":
                isNegative = -1
                isStart = False
                continue
            elif i == "+":
                isNegative = 1
                isStart = False
                continue
            if i not in "0123456789 ":
                return 0
            continue
        else:
            if i not in "0123456789":
                break
            else:
                isStart = False
        # print(i)
        result = result * 10 + ord(i) - ord('0')
    result = result * isNegative

    if -2 ** 31 > result:
        return -2 ** 31
    elif 2 ** 31 - 1 < result:
        return 2 ** 31 - 1
    else:
        return result


for t in test:
    res = my_atoi(t)
    print(res)
