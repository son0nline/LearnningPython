#Using a Step in a Slice
strData = "1,234,567;890:123"
seperators = strData[1::4]
print(seperators)
values = "".join(char if char not in seperators else " " for char in strData).split()
# [for char in strData] -- split strData to array of char
# [char if char not in seperators else " "] return char. if char in seperators return " "
# "".join join all char to string result => "1 234 567 890 123"
# .split() => split result string to array. without parameter default is ' '
print(values)
lsInt = [int(val) for val in values]
print(lsInt)
