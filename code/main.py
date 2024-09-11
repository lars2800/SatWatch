#----------------#
# Import libarys #
#----------------#
import sys
import json
import os

import api as API
import cli as CLI

#------#
# Code #
#------#

class Contex:
    def __init__(self) -> None:
        """

        This class holds datta which allows for easy context

        """
        pass

    def saveConfig(self,filePathAndName:str="config.json",exclude:list[str] = []) -> None:
        """
        Saves all the attributes in the class ( except this function and the load function )

        Args:
            filePathAndName (str, optional): The path for the config file. Defaults to "config.json".
            exclude (list[str], optional): What atributes to not save. Defaults to [].
        """        

        exclude.append("saveConfig")
        exclude.append("loadConfig")

        # Find and filter attributes
        filtered_attributes = [attr for attr in dir(self) if (not attr.startswith('__')) and not ( attr in exclude )]

        # Make config dictionary with attribute name and value
        configDict = {}
        for attr in filtered_attributes:
            configDict[attr] = self.__getattribute__(attr)

        # Save dictionary
        file = open(filePathAndName,"w")
        json.dump(configDict,file,indent=4)
        file.close()
    
    def loadConfig(self,filePathAndName:str="config.json") -> None:
        """
        Loads a config

        Args:
            filePathAndName (str, optional): Path of the file name. Defaults to "config.json".
        """        

        # Load dictionary
        file = open(filePathAndName,"r")
        configDictionary = json.load(file)
        file.close()

        # Apply config
        for attrName in configDictionary:

            attrValue = configDictionary[attrName]
            self.__setattr__(attrName,attrValue)

def uiLoop(ctx:Contex) -> None:

    def clearAndPrintBanner():
        ctx.cli.clearLastMesseages()
        ctx.cli.log(CLI.BANNER)

    uiContinou = True

    while ( uiContinou ):
        ctx.cli.log(CLI.BANNER)
        menuIndex = ctx.cli.choose_option("Select an menu ( use arrow keys and enter button )", ["Config","Find sattelites","Quit"] )

        if (menuIndex == 1):
            # Find sattelites
            clearAndPrintBanner()
            menuIndex = ctx.cli.choose_option("Select an menu ( use arrow keys and enter button )", ["Scan for visible sattelites above you","Scan for radio-visible sattelites above you","Return"] )

            if (menuIndex == 0):
                # Scan for visible sattelites above you
                pass

            elif (menuIndex == 1):
                # Scan for radio-visible sattelites above you
                pass

            elif (menuIndex == 2):
                # Return = do nothing ( will just return to main menu )
                pass

        elif (menuIndex == 0):
            # Config
            pass

        elif (menuIndex == 2):
            # Quit
            uiContinou = False
        
        if uiContinou:
            # If there is an next frame clear for the next frame
            ctx.cli.clearLastMesseages()

def main(args:list[str]) -> int:

    # Create an context and load the config into it
    ctx = Contex()
    ctx.loadConfig( "config.json" )

    # Intizialze liabrys / submodules
    ctx.cli = CLI.CLI() # type:ignore
    ctx.api = API.API( apiKey = ctx.api_key, baseUrl = "https://api.n2yo.com/rest/v1/satellite/" ) # type:ignore

    # Save configuration
    ctx.saveConfig( "config.json", exclude = ["cli","api"] )

    # Menus and ui
    uiLoop(ctx)

    # Return exit code
    return 1


#--------------#
# Intizialazer #
#--------------#
if __name__ == "__main__":

    exitCode = main(sys.argv)

    print(f"Program exited with error code: {exitCode}")

    exit(exitCode)