#----------------#
# Import libarys #
#----------------#
import msvcrt

#--------------------------------#
# Define constants and variables #
#--------------------------------#

BANNER = """
  █████████             █████       ███████████                              █████     
 ███░░░░░███           ░░███       ░█░░░███░░░█                             ░░███      
░███    ░░░   ██████   ███████     ░   ░███  ░  ████████   ██████    ██████  ░███ █████
░░█████████  ░░░░░███ ░░░███░          ░███    ░░███░░███ ░░░░░███  ███░░███ ░███░░███ 
 ░░░░░░░░███  ███████   ░███           ░███     ░███ ░░░   ███████ ░███ ░░░  ░██████░  
 ███    ░███ ███░░███   ░███ ███       ░███     ░███      ███░░███ ░███  ███ ░███░░███ 
░░█████████ ░░████████  ░░█████        █████    █████    ░░████████░░██████  ████ █████
 ░░░░░░░░░   ░░░░░░░░    ░░░░░        ░░░░░    ░░░░░      ░░░░░░░░  ░░░░░░  ░░░░ ░░░░░ 
"""

#------#
# Code #
#------#

class CLI:
    def __init__(self) -> None:
        """

        Class that holds all CLI functions and variables ( this classed is preficed with static )

        """        
        self.COLOR_HEADER = '\033[95m'
        self.COLOR_OKBLUE = '\033[94m'
        self.COLOR_OKCYAN = '\033[96m'
        self.COLOR_OKGREEN = '\033[92m'
        self.COLOR_WARNING = '\033[93m'
        self.COLOR_FAIL = '\033[91m'
        self.COLOR_ENDC = '\033[0m'
        self.COLOR_BOLD = '\033[1m'
        self.COLOR_UNDERLINE = '\033[4m'

        self.ANSII_MOVE_CURSOR_RIGHT = "\033[1C"
        self.ANSII_MOVE_CURSOR_LEFT  = "\033[1D"
        self.ANSII_MOVE_CURSOR_DOWN  = "\033[1B"
        self.ANSII_MOVE_CURSOR_UP    = "\033[1A"

        self.logBuffer = []

    def choose_option(self,title:str,options:list[str],cursor:str = "> ") -> int:
        """
        Creates an CLI selection menu with options

        Args:
            title (str): The title card
            options (list[str]): The options the user can select
            selector (str, optional): The cursur. Defaults to ">".

        Returns:
            int: The index from options selected
        """

        textLength = 0
        cursorIndex = 0

        cont = True

        while cont:
            
            t = f"{title}\n"
            textLength = textLength + len(t)
            self.log(t, end="")

            for i, e in enumerate(options):

                # Check if an cusrsor needs to be used
                if i != cursorIndex:

                    # Without cursor
                    t = f"{" "*len(cursor)}{e}\n"
                    textLength = textLength + len(t)
                    self.log(t, end="")

                else:

                    # With cursor
                    t = f"{cursor}{e}\n"
                    textLength = textLength + len(t)
                    self.log(t, end="")

            c = msvcrt.getwch()
            if ( c == "P" ):
                cursorIndex = max(0,min(cursorIndex + 1, len(options) - 1))
            if ( c == "H" ):
                cursorIndex = max(0,min(cursorIndex - 1, len(options) - 1))
            if ( c == "\r" ):
                cont = False

            if cont == True:
                self.log("\033[F" * (len(options) + 1), end="")  # Move the cursor up
            


        return cursorIndex

    def choose_options(self,title:str,options:list[str],selector:str = "* ",cursor = "> ") -> list[int]:
        """
        Creates an CLI selection menu with multible options

        Args:
            title (str): The title card
            options (list[str]): The options the user can select
            selector (str, optional): The cursur. Defaults to ">".

        Returns:
            int: The index from options selected
        """

        textLength = 0
        cursorIndex = 0
        cursorIndexes = []

        cont = True

        while cont:
            
            t = f"{title}\n"
            textLength = textLength + len(t)
            self.log(t, end="")

            for i, e in enumerate(options):

                if (i == cursorIndex):

                    t = f"{cursor}{e}\n"
                    textLength = textLength + len(t)
                    self.log(t, end="")
                
                # Check if an cusrsor needs to be used
                elif not (i in cursorIndexes): #i != cursorIndex:

                    t = f"{" "*len(cursor)}{e}\n"
                    textLength = textLength + len(t)
                    self.log(t, end="")

                else:

                    # With cursor
                    t = f"{selector}{e}\n"
                    textLength = textLength + len(t)
                    self.log(t, end="")

            c = msvcrt.getwch()
            if ( c == "P" ):
                cursorIndex = max(0,min(cursorIndex + 1, len(options) - 1))
            if ( c == "H" ):
                cursorIndex = max(0,min(cursorIndex - 1, len(options) - 1))
            if ( c == " " ):
                if not (cursorIndex in cursorIndexes):
                    cursorIndexes.append(cursorIndex)
                else:
                    cursorIndexes.remove(cursorIndex)
            if ( c == "\r" ):
                cont = False

            if cont == True:
                self.log("\033[F" * (len(options) + 1), end="")  # Move the cursor up
        


        return cursorIndexes

    def ask_integer(self,messeage:str="",allowNegative:bool=True,strict:bool=False,errorFloatingNumber:str="Number must be hole (input %s)",errorConversion:str="Str -> Int conversion error (found %s)",errorNegative:str="Integer must be positive (input was: %s)",errorStrict:str="Integer cannot be zero (input was: %s)") -> int:
        retry = True

        while ( retry ):
            answer = input(messeage)

            try:
                int(answer)

                if (int(answer) < 0 and allowNegative == False):
                    self.log(errorNegative % answer)
                
                else:
                    if ( int(answer) == 0 and strict == True ):
                        self.log(errorStrict % answer)
                    
                    else:

                        if (str(int(answer)) == answer):
                            retry = False
                        
                        else:
                            self.log(errorFloatingNumber % answer)

            except:
                self.log(errorConversion % answer)
        
        return int(answer)

    def log(self,msg:str,end:str="\n") -> None:   
        fmsg = msg + end
        print(msg,end=end)

        for t in fmsg.split("\n"):

            if len(t) != 0:
                self.logBuffer.append( { "length":len(t), "text":t } )

    def clearBuffer(self) -> None:
        self.logBuffer = []
    
    def clearMessagesFromBuffer(self) -> None:

        print(f"{self.ANSII_MOVE_CURSOR_UP * len(self.logBuffer)}",end="")

        for i in self.logBuffer:
            print(f"{" "*len(i["text"])}{self.ANSII_MOVE_CURSOR_DOWN}",end="")

cli = CLI()
cli.log("abc")
cli.log("def")
#cli.clearMessagesFromBuffer()