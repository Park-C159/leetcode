def intToRoman(num: int) -> str:
    roman_numerals = [
        ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
        ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
        ('X', 10), ('IX', 9), ('V', 5), ('IV', 4),
        ('I', 1)
    ]

    res = ""

    for symbol, value in roman_numerals:
        while num >= value:
            res += symbol
            num -= value

    return res


test = (3749, 58, 1994)

for i in test:
    res = intToRoman(i)
    print(res)
