def reverse(x: int) -> int:
    x_list = ""
    sign = 1
    if x < 0:
        sign = -1
        x = -x

    while x > 0:
        x_list += str(x % 10)
        x = x // 10

    reverseX = sign * int(x_list if len(x_list) else 0)
    if reverseX < -2 ** 31 or reverseX > 2 ** 31 - 1:
        return 0

    return reverseX

