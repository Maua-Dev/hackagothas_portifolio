

import abc
from src.shared.domain.entities.crime import Crime

from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.danger_score_enum import DANGER_SCORE


class CriminalRecord(abc.ABC):
    id: int
    criminal: Criminal
    crimes: list[Crime]
    arrested: bool
    score: DANGER_SCORE
    
    def __init__(self, id: int, criminal: Criminal, crimes: list[Crime], arrested: bool, score: DANGER_SCORE):
        
        if type(id) != int:
            raise Exception("Invalid id")
        self.id = id
        
        if type(criminal) != Criminal:
            raise Exception("Invalid criminal")
        self.criminal = criminal
        
        if type(crimes) != list:
            raise Exception("Invalid crimes")
        self.crimes = crimes
        
        if type(arrested) != bool:
            raise Exception("Invalid arrested")
        self.arrested = arrested
        
        if type(score) != DANGER_SCORE:
            raise Exception("Invalid score")
        self.score = score
        
    def __eq__(self, other) -> bool:
        return self.id == other.id and self.criminal == other.criminal and self.crimes == other.crimes and self.arrested == other.arrested and self.score == other.score