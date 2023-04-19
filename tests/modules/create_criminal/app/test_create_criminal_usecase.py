
from src.modules.create_criminal.app.create_criminal_usecase import CreateCriminalUsecase
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.infra.repositories.criminal_repository_mock import CriminalRepositoryMock


class Test_CreateCriminalUsecase:
    criminal = Criminal(id=6, name="Calvas", description="Very nice guy", gender=GENDER.OTHER, region="SP")
    
    def test_create_criminal_usecase(self):
        repo = CriminalRepositoryMock()
        usecase = CreateCriminalUsecase(repo_criminal=repo)
        
        length_before = len(repo.criminals)
        
        criminal_response = usecase(criminal=self.criminal)
        
        length_after = len(repo.criminals)
        
        assert length_after == length_before + 1
        assert criminal_response == self.criminal