

from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.crime_enum import CRIME
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.repositories.crime_repository_interface import ICrimeRepository


class CrimeRepositoryMock(ICrimeRepository):
    crimes: list[Crime]
    
    
    
    def __init__(self):
        self.criminals = [
            Criminal(id=1, name="Furlan", description="Furlan is a Automato", gender=GENDER.MALE, region="Mauá"),
            Criminal(id=2, name="Vanderlei", description="HAHA Matlab", gender=GENDER.MALE, region="Mauá"),
            Criminal(id=2, name="Patricia Antonio", description="Smile", gender=GENDER.FEMALE, region="São Paulo"),
            Criminal(id=3, name="Prino", description="Smoke maker", gender=GENDER.MALE, region="Osasco"),
        ]
        
        self.crimes = [
            Crime(id=1, criminal=self.criminals[0], crime=CRIME.MURDER, region="Mauá", date="20-01-2021", num_victims=1),
            Crime(id=2, criminal=self.criminals[1], crime=CRIME.ROBBERY, region="São Paulo", date="02-04-2023", num_victims=1),
            Crime(id=3, criminal=self.criminals[2], crime=CRIME.TERRORISM, region="Mauá", date="01-03-2023", num_victims=5),
            Crime(id=4, criminal=self.criminals[3], crime=CRIME.MURDER, region="Mauá", date="02-03-2023", num_victims=1),
        ]
        
    def create_crime(self, crime: Crime) -> Crime:
        self.crimes.append(crime)
        return crime