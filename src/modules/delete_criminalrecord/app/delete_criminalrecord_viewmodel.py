from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminalrecord import CriminalRecord
from src.shared.domain.enums.danger_score_enum import DANGER_SCORE
from src.shared.domain.enums.gender_enum import GENDER


class CriminalViewmodel:
    id: int
    name: str
    description: str
    gender: GENDER
    region: str

    def __init__(self, criminal: Criminal):
        self.id = criminal.id
        self.name = criminal.name
        self.description = criminal.description
        self.gender = criminal.gender
        self.region = criminal.region

    def to_dict(self):
        return {
            "id_criminal": self.id,
            "name": self.name,
            "description": self.description,
            "gender": self.gender.value,
            "region_criminal": self.region,
        }


class CriminalRecordViewmodel:
    id: int
    criminal: Criminal
    arrested: bool
    score: DANGER_SCORE

    def __init__(self, criminalrecord: CriminalRecord):
        self.id = criminalrecord.id
        self.criminal = CriminalViewmodel(criminalrecord.criminal)
        self.arrested = criminalrecord.arrested
        self.score = criminalrecord.score

    def to_dict(self):
        return {
            "id_criminalrecord": self.id,
            "criminal": self.criminal.to_dict(),
            "arrested": self.arrested,
            "score": self.score.value,
        }


class DeleteCriminalRecordViewmodel:
    criminalrecord: CriminalRecordViewmodel

    def __init__(self, criminalrecord: CriminalRecord):
        self.criminalrecord = CriminalRecordViewmodel(criminalrecord)

    def to_dict(self):
        return {
            "criminalrecord": self.criminalrecord.to_dict(),
            "message": "the criminal record was deleted",
        }
