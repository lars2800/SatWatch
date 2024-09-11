#----------------#
# Import libarys #
#----------------#
import requests
import json

#------#
# Code #
#------#
class API:
    def __init__(self,apiKey:str,baseUrl:str = "https://api.n2yo.com/rest/v1/satellite/") -> None:
        self.apiKey  = apiKey
        self.baseUrl = baseUrl
    
    def tle(self,NoradId:int) -> dict:
        """
        Retrieve the Two Line Elements (TLE) for a satellite identified by NORAD id.

        Args:
            NoradId (int): The norad id off the sattelite

        Raises:
            Exception: An http(s) error like 404

        Returns:
            dict: Data off the sattelite 
        """        

        url = f"{self.baseUrl}/tle/{NoradId}"

        response = requests.get(url + f"&apiKey={self.apiKey}")

        if ( response.status_code == 200 ):
            return response.json()
        
        else:
            raise Exception(f"Error: {response.status_code} whilst retrieving data from {url}")
    
    def positions(self,NoradId:int,ObserverLattitude:float,ObserverLongitude:float,ObserverAltitude:float,SecondsinFuture:int = 10) -> dict:
        """
        Retrieve the future positions of any satellite as groundtrack (latitude, longitude) to display orbits on maps. 
        Also return the satellite's azimuth and elevation with respect to the observer location. 
        Each element in the response array is one second of calculation. 
        First element is calculated for current UTC time.

        Args:
            NoradId (int): The sattelite NoradId
            ObserverLattitude (float): Lattitude of observer
            ObserverLongitude (float): Longitude of observer
            ObserverAltitude (float):  Alttitude of observer
            SecondsinFuture (int, optional): How much positions in the future too return. Defaults to 10. Max 300.

        Raises:
            Exception: An http(s) error like 404

        Returns:
            dict: Data off the sattelite 
        """        

        url = f"{self.baseUrl}/positions/{NoradId}/{ObserverLattitude}/{ObserverLongitude}/{ObserverAltitude}/{SecondsinFuture}"

        response = requests.get(url + f"&apiKey={self.apiKey}")

        if ( response.status_code == 200 ):
            return response.json()
        
        else:
            raise Exception(f"Error: {response.status_code} whilst retrieving data from {url}")
    
    def visualpasses(self,NoradId:int,ObserverLattitude:float,ObserverLongitude:float,ObserverAltitude:float,DaysInFuture:int,MinVisibility:int) -> dict:
        """
        Get predicted visual passes for any satellite relative to a location on Earth. 
        A "visual pass" is a pass that should be optically visible on the entire (or partial) duration of crossing the sky.
        For that to happen, the satellite must be above the horizon, 
        illumintaed by Sun (not in Earth shadow), 
        and the sky dark enough to allow visual satellite observation.

        Args:
            NoradId (int): Satellite NORAD id
            ObserverLattitude (float): Observers lattitude
            ObserverLongitude (float): Observers longitude
            ObserverAltitude (float):  Observers lattitude
            DaysInFuture (int): The days into the future to predict for
            MinVisibility (int): How manny seconds the sattelite should be vissible

        Raises:
            Exception: An http(s) error like 404

        Returns:
            dict: Data off the sattelite
        """        

        url = f"{self.baseUrl}/visualpasses/{NoradId}/{ObserverLattitude}/{ObserverLongitude}/{ObserverAltitude}/{DaysInFuture}/{MinVisibility}"

        response = requests.get(url + f"&apiKey={self.apiKey}")

        if ( response.status_code == 200 ):
            return response.json()
        
        else:
            raise Exception(f"Error: {response.status_code} whilst retrieving data from {url}")
    
    def radiopasses(self,NoradId:int,ObserverLattitude:float,ObserverLongitude:float,ObserverAltitude:float,DaysInFuture:int,MinElevation:int) -> dict:
        """
        Get predicted visual passes for any satellite relative to a location on Earth. 
        A "visual pass" is a pass that should be optically visible on the entire (or partial) duration of crossing the sky.
        For that to happen, the satellite must be above the horizon, 
        illumintaed by Sun (not in Earth shadow), 
        and the sky dark enough to allow visual satellite observation.

        Args:
            NoradId (int): Norad sattelite id
            ObserverLattitude (float): Observers lattitude
            ObserverLongitude (float): Observers longtitude
            ObserverAltitude (float): Observers alltitude
            DaysInFuture (int): Days in the future too look too
            MinElevation (int): Highest alltitude off sattelite

        Raises:
            Exception: An http(s) error like 404

        Returns:
            dict: Data off the sattelite
        """        

        url = f"{self.baseUrl}/radiopasses/{NoradId}/{ObserverLattitude}/{ObserverLongitude}/{ObserverAltitude}/{DaysInFuture}/{MinElevation}"

        response = requests.get(url + f"&apiKey={self.apiKey}")

        if ( response.status_code == 200 ):
            return response.json()
        
        else:
            raise Exception(f"Error: {response.status_code} whilst retrieving data from {url}")
    
    def above(self,ObserverLattitude:float,ObserverLongitude:float,ObserverAltitude:float,SearchRadius:int,CatogoryId:int = 18) -> dict:
        """
        The "above" function will return all objects within a given search radius above observer's location. The radius (θ), expressed in degrees, is measured relative to the point in the sky directly above an observer (azimuth).

        Args:
            ObserverLattitude (float): The observers lattitude
            ObserverLongitude (float): The observers longitude
            ObserverAltitude (float): The observers alltitude
            SearchRadius (int): Radius to scan angle
            CatogoryId (int, optional): The catogory to filter. Defaults to 18 (radio).

        Raises:
            Exception: An http(s) error like 404

        Returns:
            dict: Data off the sattelite
        """        
        url = f"{self.baseUrl}/above/{ObserverLattitude}/{ObserverLongitude}/{ObserverAltitude}/{SearchRadius}/{CatogoryId}"

        response = requests.get(url + f"&apiKey={self.apiKey}")

        if ( response.status_code == 200 ):
            return response.json()
        
        else:
            raise Exception(f"Error: {response.status_code} whilst retrieving data from {url}")