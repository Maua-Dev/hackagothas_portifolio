

import pytest
from src.modules.create_criminalrecord.app.create_criminalrecord_usecase import CreateCriminalRecordUsecase
from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminalrecord import CriminalRecord
from src.shared.domain.enums.crime_enum import CRIME
from src.shared.domain.enums.danger_score_enum import DANGER_SCORE
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.helpers.errors.usecase_errors import ForbiddenAction
from src.shared.infra.repositories.criminalrecord_repository_mock import CriminalRecordRepositoryMock


class Test_CreateCriminalRecordUsecase:
    criminal = Criminal(id=1, name="Furlas", description="Furlan is a Automato", gender=GENDER.FEMALE, region="Mauá")
    crime = Crime(id=5, criminal=criminal, crime=CRIME.MURDER, region="Mauá", date="20-01-2021", num_victims=1)
    criminalrecord = CriminalRecord(id=5, criminal=criminal, crimes=[crime], arrested=False, score=DANGER_SCORE.ONESTAR)
    criminalrecord2 = CriminalRecord(id=3, criminal=criminal, crimes=[crime], arrested=False, score=DANGER_SCORE.ONESTAR)
    
    def test_create_criminalrecord_usecase(self):
        
        repo = CriminalRecordRepositoryMock()
        usecase = CreateCriminalRecordUsecase(repo)
        
        length_before = len(repo.criminalrecords)
        
        criminalrecord_response = usecase(criminalrecord=self.criminalrecord)
        
        length_after = len(repo.criminalrecords)
        
        assert length_after == length_before + 1
        assert criminalrecord_response == self.criminalrecord
        
    def test_create_criminalrecord_usecase_id_already_exists(self):
        repo = CriminalRecordRepositoryMock()
        usecase = CreateCriminalRecordUsecase(repo)
        
        criminalrecord = self.criminalrecord2
        
        with pytest.raises(ForbiddenAction):
            criminalrecord_response = usecase(criminalrecord=criminalrecord)
        
        