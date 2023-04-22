

import pytest
from src.modules.create_crime.app.create_crime_usecase import CreateCrimeUsecase
from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.crime_enum import CRIME
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.helpers.errors.usecase_errors import ForbiddenAction
from src.shared.infra.repositories.criminalrecord_repository_mock import CriminalRecordRepositoryMock


class Test_CreateCrimeUsecase:
    criminal = Criminal(id=1, name="Furlan", description="Furlan is a Automato", gender=GENDER.MALE, region="Mauá")
    crime = Crime(id=7, criminal=criminal, crime=CRIME.MURDER, region="Mauá", date="20-01-2021", num_victims=1)
    crime_with_same_id = Crime(id=1, criminal=criminal, crime=CRIME.MURDER, region="Mauá", date="20-01-2021", num_victims=1)

    
    def test_create_crime_use(self):
        repo = CriminalRecordRepositoryMock()
        usecase = CreateCrimeUsecase(repo)
        
        length_before = len(repo.crimes)
        
        crimes_response = usecase(crime=self.crime)
        
        length_after = len(repo.crimes)
        
        assert length_after == length_before + 1
        assert crimes_response == self.crime

    def test_create_crime_usecase_id_already_exists(self):
        repo = CriminalRecordRepositoryMock()
        usecase = CreateCrimeUsecase(repo)
        
        crime = self.crime_with_same_id
        
        with pytest.raises(ForbiddenAction):
            crime_response = usecase(crime=crime)