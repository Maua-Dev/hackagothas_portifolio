from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminalrecord import CriminalRecord
from src.shared.domain.enums.crime_enum import CRIME
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


class CrimeViewmodel:
    id: int
    criminal: Criminal
    crime: CRIME
    region: str
    date: str  # DD-MM-YYYY
    num_victims: int

    def __init__(self, crime: Crime):
        self.id = crime.id
        self.criminal = CriminalViewmodel(crime.criminal)
        self.crime = crime.crime
        self.region = crime.region
        self.date = crime.date
        self.num_victims = crime.num_victims

    def to_dict(self):
        return {
            "id_crime": self.id,
            "criminal": self.criminal.to_dict(),
            "crime": self.crime.value,
            "region_crime": self.region,
            "date": self.date,
            "num_victims": self.num_victims,
        }


class CriminalRecordViewmodel:
    id: int
    criminal: Criminal
    crimes: list[Crime]
    arrested: bool
    score: DANGER_SCORE

    def __init__(self, criminalrecord: CriminalRecord):
        self.id = criminalrecord.id
        self.criminal = CriminalViewmodel(criminalrecord.criminal)
        self.crimes = [CrimeViewmodel(crime) for crime in criminalrecord.crimes]
        self.arrested = criminalrecord.arrested
        self.score = criminalrecord.score

    def to_dict(self):
        return {
            "id_criminalrecord": self.id,
            "criminal": self.criminal.to_dict(),
            "crimes": [crime.to_dict() for crime in self.crimes],
            "arrested": self.arrested,
            "score": self.score.value,
        }


class UpdateCriminalRecordViewmodel:
    criminalrecord: CriminalRecordViewmodel

    def __init__(self, criminalrecord: CriminalRecord):
        self.criminalrecord = CriminalRecordViewmodel(criminalrecord)

    def to_dict(self):
        return {
            "criminalrecord": self.criminalrecord.to_dict(),
            "message": "the criminal record was updated",
        }
