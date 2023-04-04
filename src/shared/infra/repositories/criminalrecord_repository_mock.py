

from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminalrecord import CriminalRecord
from src.shared.domain.enums.crime_enum import CRIME
from src.shared.domain.enums.danger_score_enum import DANGER_SCORE
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.repositories.criminalrecord_repository_interface import ICriminalRecordRepository


class CriminalRecordRepositoryMock(ICriminalRecordRepository):
    criminalrecords: list[CriminalRecord]
    criminals: list[Criminal]  
    crimes: list[Crime]
    
    def __init__(self):
        self.criminals = [
            Criminal(name="Furlan", description="Furlan is a Automato", gender=GENDER.MALE, region="Mauá"),
            Criminal(name="Vanderlei", description="HAHA Matlab", gender=GENDER.MALE, region="Mauá"),
            Criminal(name="Patricia Antonio", description="Smile", gender=GENDER.FEMALE, region="São Paulo"),
            Criminal(name="Prino", description="Smoke maker", gender=GENDER.MALE, region="Osasco"),
        ]
        
        self.crimes = [
            Crime(id=1, criminal=self.criminals[0], crime=CRIME.MURDER, region="Mauá", date="20-01-2021", num_victims=1),
            Crime(id=2, criminal=self.criminals[1], crime=CRIME.ROBBERY, region="São Paulo", date="02-04-2023", num_victims=1),
            Crime(id=3, criminal=self.criminals[2], crime=CRIME.TERRORISM, region="Mauá", date="01-03-2023", num_victims=5),
            Crime(id=4, criminal=self.criminals[3], crime=CRIME.MURDER, region="Mauá", date="02-03-2023", num_victims=1),
        ]
        
        self.criminalrecords = [
            CriminalRecord(id=1, criminal=self.criminals[0], crimes=[self.crimes[0]], arrested=False, score=DANGER_SCORE.ONESTAR),
            CriminalRecord(id=2, criminal=self.criminals[1], crimes=[self.crimes[1]], arrested=True, score=DANGER_SCORE.FOURSTAR),
            CriminalRecord(id=3, criminal=self.criminals[2], crimes=[self.crimes[2], self.crimes[3]], arrested=True, score=DANGER_SCORE.FIVESTAR),
        ]
        
    def create_criminalrecord(self, criminalrecord: CriminalRecord) -> CriminalRecord:
        self.criminalrecords.append(criminalrecord)
        return criminalrecord
    
    def get_criminalrecord(self, id: int) -> CriminalRecord:
        for criminalrecord in self.criminalrecords:
            if criminalrecord.id == id:
                return criminalrecord
        return None
    