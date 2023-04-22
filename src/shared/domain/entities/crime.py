

import abc

from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.crime_enum import CRIME


class Crime(abc.ABC):
    id: int
    criminal: Criminal
    crime: CRIME
    region: str
    date: str # DD-MM-YYYY
    num_victims: int
    
    def __init__(self, id: int, criminal: Criminal, crime: CRIME, region: str, date: str, num_victims: int):
        
        if type(id) != int:
            raise Exception("Invalid id")
        self.id = id
        
        if type(criminal) != Criminal:
            raise Exception("Invalid criminal")
        self.criminal = criminal
        
        if type(crime) != CRIME:
            raise Exception("Invalid crime")
        self.crime = crime
        
        if type(region) != str:
            raise Exception("Invalid region")
        self.region = region
        
        if type(date) != str:
            raise Exception("Invalid date")
        self.date = date
        
        if type(num_victims) != int:
            raise Exception("Invalid num_victims")
        self.num_victims = num_victims
    
    @staticmethod
    def validate_num_victims(num_victims: int) -> bool:
        if type(num_victims) != int:
            return False
        if num_victims < 0:
            return False
        return True

    @staticmethod
    def validate_date(date: str) -> bool:
        if type(date) != str:
            return False
        if len(date) != 10:
            return False
        return True
     
    def __eq__(self, other) -> bool:
        return self.id == other.id and self.criminal == other.criminal and self.crime == other.crime and self.region == other.region and self.date == other.date and self.num_victims == other.num_victims