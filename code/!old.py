import requests
import json
import os

# Replace with your N2YO API key
API_KEY = 'ZHT2AY-4LDBFN-HEHXQP-5BZ4'
BASE_URL = 'https://api.n2yo.com/rest/v1/satellite'

# Replace with your location coordinates
LATITUDE  = 51.024
LONGITUDE = 4.4834
ALTITUDE = 0  # Altitude in meters
CATOGORY = 18 # 18 = radio ( mory catogorys at https://www.n2yo.com/api/ )

# Function to get satellites in sight
def get_satellites_in_radio_sight():

    url = f"{BASE_URL}/above/{LATITUDE}/{LONGITUDE}/{ALTITUDE}/90/{CATOGORY}/?apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    return data['above']

# Function to get predicted positions
def get_predicted_position(satellite_id):
    url = f'{BASE_URL}/positions/{satellite_id}/{LATITUDE}/{LONGITUDE}/{ALTITUDE}/60/?apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data['positions']

# Function that prints a welcome banner
def print_welcome_banner():
    print("""
  █████████             █████       ███████████                              █████     
 ███░░░░░███           ░░███       ░█░░░███░░░█                             ░░███      
░███    ░░░   ██████   ███████     ░   ░███  ░  ████████   ██████    ██████  ░███ █████
░░█████████  ░░░░░███ ░░░███░          ░███    ░░███░░███ ░░░░░███  ███░░███ ░███░░███ 
 ░░░░░░░░███  ███████   ░███           ░███     ░███ ░░░   ███████ ░███ ░░░  ░██████░  
 ███    ░███ ███░░███   ░███ ███       ░███     ░███      ███░░███ ░███  ███ ░███░░███ 
░░█████████ ░░████████  ░░█████        █████    █████    ░░████████░░██████  ████ █████
 ░░░░░░░░░   ░░░░░░░░    ░░░░░        ░░░░░    ░░░░░      ░░░░░░░░  ░░░░░░  ░░░░ ░░░░░ 
""")

def prompt_options(options:list[str]) -> int: # type:ignore
    for i,e in enumerate(options):
        print(f"{i} | {e}")
    
    retry = True
    while ( retry ):
        ans = input("What option do u want to use? (input index) ")
        
        try:
            ansInt = int(ans)

            if ( ansInt < 0):
                print(f"Cannot select negative index")
            
            else:
                if ( ansInt > (len(options)-1)):
                    print("Cannot select an index that does not exsit")
                
                else:
                    return ansInt
        
        except:
            print(f"Cannot convert: '{ans}' to an integer ")

def load_config() -> None:
    global API_KEY
    global BASE_URL
    global LATITUDE
    global LONGITUDE
    global ALTITUDE
    global CATOGORY

    settings = json.load( open("config.json") )

    API_KEY  = settings["API_KEY"]
    BASE_URL = settings["BASE_URL"]
    LATITUDE = settings["LATITUDE"]
    LONGITUDE = settings["LONGITUDE"]
    ALTITUDE = settings["ALTITUDE"]
    CATOGORY = settings["CATOGORY"]

def save_config() -> None:
    global API_KEY
    global BASE_URL
    global LATITUDE
    global LONGITUDE
    global ALTITUDE
    global CATOGORY

    settings = {}

    settings["API_KEY"] = API_KEY
    settings["BASE_URL"] = BASE_URL
    settings["LATITUDE"] = LATITUDE
    settings["LONGITUDE"] = LONGITUDE
    settings["ALTITUDE"] = ALTITUDE
    settings["CATOGORY"] = CATOGORY

    json.dump(settings,open("config.json","w"))

def clear() -> None:
    os.system("cls")

def prompt_multi_options(options:list[str]) -> list[int]: # type:ignore
    for i,e in enumerate(options):
        print(f"{i} | {e}")
    
    retry = True
    while ( retry ):
        retry = False

        answers = input("What options do u want to use? (input indexes seperated by comma) ").replace(" ","").split(",")
        _r = []

        for i in answers:

            try:
                ansInt = int(i)

                if ( ansInt < 0):
                    retry = True
                    print(f"Cannot select negative index")
                
                else:
                    if ( ansInt > (len(options)-1)):
                        retry = True
                        print("Cannot select an index that does not exsit")
                        _r.clear()
                    
                    else:
                        _r.append(ansInt)

            
            except:
                retry = True
                print(f"Cannot convert: '{i}' to an integer ")
                _r.clear()

    return _r

# Main function
def main():
    global API_KEY
    global BASE_URL
    global LATITUDE
    global LONGITUDE
    global ALTITUDE
    global CATOGORY

    load_config()

    def menuClear():
        clear()
        print_welcome_banner()
    
    while True:
        menuClear()

        selected_option = prompt_options(["Scan for sattelites now in radar view","Config","Predict sattelites"])
        satellites = []
        satelliteNames = []
        predictedSatellites = []

        if selected_option == 2:
            menuClear()
            print(satelliteNames)

            print("Select what sattelites to exclude:")
            prompt_multi_options( satelliteNames )

        if selected_option == 1:

            menuClear()
            selected_option = prompt_options([
                f"Return",
                f"n2yo apikey (current: {API_KEY})",
                f"base url  (current: {BASE_URL})",
                f"latitude  (current: {LATITUDE})",
                f"longitude (current: {LONGITUDE})",
                f"altitude  (current: {ALTITUDE})",
                f"filter catogory (current: {CATOGORY})",
            ])

            if ( selected_option == 1 ):
                menuClear()
                API_KEY = input(f"Editing API_KEY (current: {API_KEY}) type new value: ")
            
            if ( selected_option == 2 ):
                menuClear()
                BASE_URL = input(f"Editing BASE_URL (current: {BASE_URL}) type new value: ")

            if ( selected_option == 3 ):
                menuClear()
                LATITUDE = input(f"Editing LATITUDE (current: {LATITUDE}) type new value: ")
            
            if ( selected_option == 4 ):
                menuClear()
                LONGITUDE = input(f"Editing LATITUDE (current: {LONGITUDE}) type new value: ")
            
            if ( selected_option == 5 ):
                menuClear()
                ALTITUDE = input(f"Editing LATITUDE (current: {ALTITUDE}) type new value: ")
            
            if ( selected_option == 6 ):
                menuClear()
                CATOGORY = input(f"Editing LATITUDE (current: {CATOGORY}) type new value: ")
            
            save_config()

        if selected_option == 0:
            menuClear()
            print(f"Fetching sattelites around {LATITUDE}lat {LONGITUDE}long")
            satellites = get_satellites_in_radio_sight()
            print(f"Done sattelites arte now loaded")
            satelliteNames = [e["satname"] for e in satellites]

            for i in satelliteNames:
                print(i)
             
            input("Oke")


if __name__ == '__main__':
    main()
