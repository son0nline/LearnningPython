lsOptions = ["Learn python","Fix Ds bug","Learn Android"]
menus = f"""
Please choose your options
1. {lsOptions[0]}
2. {lsOptions[1]}
3. {lsOptions[2]}
0. Exit
My choose is:"""
choose = None
while True:
    choose = input(menus)
    if choose == '0':
        break
    if choose[0].isnumeric() and choose[0] in "123":
        print(f"{lsOptions[ int(choose[0])-1 ]}")
        break


#---------------------------------------
lsOptions = ["Learn python", "Learn Android", "Fix Ds bug", "update"
, "update15"
]

lsMenu = [i+1 for i in range(len(lsOptions))]

menus = "Please choose your options"
for idx, value in enumerate(lsOptions):
    menus += f"\r\n{idx+1}. {value}"
menus += "\n0. Exit"
menus += "\nMy choose is:"


choose = None
while True:
    choose = input(menus)
    if choose == '0':
        break

    if choose.isnumeric() and int(choose) in lsMenu:
        print(f"{lsOptions[ int(choose)-1 ]}")
        break
