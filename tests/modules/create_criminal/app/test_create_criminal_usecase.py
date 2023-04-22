
import pytest
from src.modules.create_criminal.app.create_criminal_usecase import CreateCriminalUsecase
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.helpers.errors.usecase_errors import ForbiddenAction
from src.shared.infra.repositories.criminalrecord_repository_mock import CriminalRecordRepositoryMock



class Test_CreateCriminalUsecase:
    criminal = Criminal(id=6, name="Calvas", description="Very nice guy", gender=GENDER.OTHER, region="SP")
    criminal_with_same_id = Criminal(id=3, name="Calvas", description="Very nice guy", gender=GENDER.OTHER, region="SP")
    
    def test_create_criminal_usecase(self):
        repo = CriminalRecordRepositoryMock()
        usecase = CreateCriminalUsecase(repo_criminal=repo)
        
        length_before = len(repo.criminals)
        
        criminal_response = usecase(criminal=self.criminal)
        
        length_after = len(repo.criminals)
        
        assert length_after == length_before + 1
        assert criminal_response == self.criminal
        
    def test_create_criminal_usecase_id_already_exists(self):
        repo = CriminalRecordRepositoryMock()
        usecase = CreateCriminalUsecase(repo)
        
        criminal = self.criminal_with_same_id
        
        with pytest.raises(ForbiddenAction):
            criminal_response = usecase(criminal=criminal)