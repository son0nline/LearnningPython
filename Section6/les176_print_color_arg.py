class bcolors:
    ## \u or \x meaning the number after that is hexa
    # \u format \u0000 4 bytes UTF‑8
    ENDC = '\033[0m'

    BOLD = '\u001b[1m'
    UNDERLINE = '\x1b[4m'
    REVERSE = '\033[7m'

    GRAY = '\u001b[30m'
    RED = '\u001b[31m'
    GREEN = '\x1b[32m'
    YELLOW = '\x1b[33m'    
    BLUE = '\u001b[34m'
    MAGENTA = '\u001b[35m'
    CYAN = '\u001b[36m'
    WHITE = '\u001b[37m'

def print_color(input:str, *effection):
    effectionStr = "".join(effection)
    print(effectionStr, input , bcolors.ENDC)

print_color("NONE")
print_color("GRAY", bcolors.GRAY)
print_color("RED", bcolors.RED)
print_color("GREEN", bcolors.GREEN)
print_color("YELLOW", bcolors.YELLOW)
print_color("BLUE", bcolors.BLUE)
print_color("MAGENTA", bcolors.MAGENTA)
print_color("CYAN", bcolors.CYAN)
print_color("WHITE", bcolors.WHITE)
print_color("REVERSE", bcolors.REVERSE)
print_color("REVERSE", bcolors.RED, bcolors.REVERSE)
print_color("REVERSE", bcolors.GREEN, bcolors.REVERSE)
print_color("REVERSE", bcolors.BLUE, bcolors.REVERSE, bcolors.BOLD, bcolors.UNDERLINE )

