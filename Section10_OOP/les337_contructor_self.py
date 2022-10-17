class myPrinterColors:
    ## \u or \x meaning the number after that is hexa
    # \u format \u0000 4 bytes UTF‑8
    ENDC = '\033[0m'

    BOLD = '\u001b[1m'
    UNDERLINE = '\u001b[4m'
    REVERSE = '\u001b[7m'

    GRAY = '\u001b[30m'
    RED = '\u001b[31m'
    GREEN = '\x1b[32m'
    YELLOW = '\x1b[33m'    
    BLUE = '\u001b[34m'
    MAGENTA = '\u001b[35m'
    CYAN = '\u001b[36m'
    WHITE = '\u001b[37m'

class myPrinter:
    def __init__(self) -> None:
        pass

    @staticmethod
    def _print_color(input:str, color: myPrinterColors = myPrinterColors.ENDC):
        print(color, input, myPrinterColors.ENDC)

#colorPrinter = myPrinter()

myPrinter._print_color("NONE")
myPrinter._print_color("GRAY", myPrinterColors.GRAY)
myPrinter._print_color("RED", myPrinterColors.RED)
myPrinter._print_color("GREEN", myPrinterColors.GREEN)
myPrinter._print_color("YELLOW", myPrinterColors.YELLOW)
myPrinter._print_color("BLUE", myPrinterColors.BLUE)
myPrinter._print_color("MAGENTA", myPrinterColors.MAGENTA)
myPrinter._print_color("CYAN", myPrinterColors.CYAN)
myPrinter._print_color("WHITE", myPrinterColors.WHITE)
myPrinter._print_color("REVERSE", myPrinterColors.REVERSE)