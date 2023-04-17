

from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.repositories.criminal_repository_interface import ICriminalRepository


class CriminalRepositoryMock(ICriminalRepository):
    criminals: list[Criminal]
    
    def __init__(self):
        self.criminals = [
                Criminal(id=1, name="Furlan", description="Furlan is a Automato", gender=GENDER.MALE, region="Mauá"),
                Criminal(id=2, name="Vanderlei", description="HAHA Matlab", gender=GENDER.MALE, region="Mauá"),
                Criminal(id=3, name="Patricia Antonio", description="Smile", gender=GENDER.FEMALE, region="São Paulo"),
                Criminal(id=4, name="Prino", description="Smoke maker", gender=GENDER.MALE, region="Osasco"),
            ]
        
    def create_criminal(self, criminal: Criminal) -> Criminal:
        self.criminals.append(criminal)
        return criminal
    
    def get_criminal(self, id: int) -> Criminal:
        for criminal in self.criminals:
            if criminal.id == id:
                return criminal
        return None