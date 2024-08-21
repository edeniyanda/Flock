num = 289

help = {
    1000: "thousand",
    100: "one hundred",
    90: "ninety",
    80: "eighty",
    70: "seventy",
    60: "sixty",
    50: "fifty",
    40: "forty",
    30: "thirty",
    20: "twenty",
    10: "ten",
    9: "nine",
    8: "eight",
    7: "seven",
    6: "six",
    5: "five",
    4: "four",
    3: "three",
    2: "two",
    1: "one"
}
ans = ""
while num >= 0:
    for i in help.keys():
        if num == i:
            ans += help.get(i) + " "
            break
        elif num > i:
            print(i)
            break
    if len(str(num)) == 1:
        break
    ans += help.get(i) + " "
    # print(ans)
    num = num - i
    print(f"MU remaining, {num}")

ans = ans.strip()

thousand_count = ans.split(" ")
print(thousand_count)
print(ans)
