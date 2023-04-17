

import pytest
from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminalrecord import CriminalRecord
from src.shared.domain.enums.crime_enum import CRIME
from src.shared.domain.enums.danger_score_enum import DANGER_SCORE
from src.shared.domain.enums.gender_enum import GENDER


class Test_CriminalRecord():
    
    criminal = Criminal(id=1, name="Furlan", description="LINUX", gender=GENDER.MALE, region="Brazil")
    crimes = [
        Crime(id=1, criminal=criminal, crime=CRIME.THEFT, region="Brazil", date="2020-01-01", num_victims=1),
        Crime(id=2, criminal=criminal, crime=CRIME.TERRORISM, region="Brazil", date="2020-01-01", num_victims=2),
        Crime(id=3, criminal=criminal, crime=CRIME.MURDER, region="Brazil", date="2020-01-01", num_victims=3)
    ]
    
    def test_criminalrecord(self):
        
        criminalrecord = CriminalRecord(id=1, criminal=self.criminal, crimes=self.crimes, arrested=True, score=DANGER_SCORE.ONESTAR)
        
        assert criminalrecord.id == 1
        assert criminalrecord.criminal == self.criminal
        assert criminalrecord.crimes == self.crimes
        assert criminalrecord.arrested == True
        assert criminalrecord.score == DANGER_SCORE.ONESTAR
        
    def test_criminalrecord_invalid_id(self):
        with pytest.raises(Exception):
            criminalrecord = CriminalRecord(id="1", criminal=self.criminal, crimes=self.crimes, arrested=True, score=DANGER_SCORE.ONESTAR)
    
    def test_criminalrecord_invalid_criminal(self):
        with pytest.raises(Exception):
            criminalrecord = CriminalRecord(id=1, criminal=1, crimes=self.crimes, arrested=True, score=DANGER_SCORE.ONESTAR)
    
    def test_criminalrecord_invalid_crimes(self):
        with pytest.raises(Exception):
            criminalrecord = CriminalRecord(id=1, criminal=self.criminal, crimes=1, arrested=True, score=DANGER_SCORE.ONESTAR)
    
    def test_criminalrecord_invalid_arrested(self):
        with pytest.raises(Exception):
            criminalrecord = CriminalRecord(id=1, criminal=self.criminal, crimes=self.crimes, arrested=1, score=DANGER_SCORE.ONESTAR)
    
    def test_criminalrecord_invalid_score(self):
        with pytest.raises(Exception):
            criminalrecord = CriminalRecord(id=1, criminal=self.criminal, crimes=self.crimes, arrested=True, score=1)
    