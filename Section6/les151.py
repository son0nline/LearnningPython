def banner_text(text:str = "*", screen_width:int = 80):
    """
    ****************************

    ** Show text like a baner **  

    ****************************
    """
    
    if len(text) > screen_width - 4:
        raise ValueError("The text input is longer than 80.")

    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centred_text)
        print(output_string)


banner_text("*",90)
banner_text("Always look on the bright side of life...")
banner_text("If life seems jolly rotten,")
banner_text("There's something you've forgotten!")
banner_text("And that's to laugh and smile and dance and sing,")
banner_text(" ")
banner_text("When you're feeling in the dumps,")
banner_text("Don't be silly chumps,")
banner_text("Just purse your lips and whistle - that's the thing!")
banner_text("And... always look on the bright side of life...")
banner_text("*",90)


def mycenter(input, width):
    lip = len(input)
    if lip >= width:
        return input
    sp = (width - lip)
    return "{0}{1}{0}{2}".format( " " * (sp // 2) , input, " " * (sp % 2))

input = "12345"
a = input.center(10)
b = mycenter(input,10)

print("[{}]".format( input.center(10)))
print("[{}]".format( mycenter(input,10)))

print(a==b)

#banner_text("_"*81)