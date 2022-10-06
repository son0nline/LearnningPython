strString = """Udemy Learn Python Programming Masterclass
line 2
line 3
"""

for char in strString:
    print(char)

strData = "1,234,567;890:123"
separators = ""
for char in strData:
    if not char.isnumeric():
        separators = separators + char
print(separators)

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
print(quote.upper())