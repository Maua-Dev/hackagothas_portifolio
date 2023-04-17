
from src.shared.infra.repositories.criminal_repository_mock import CriminalRepositoryMock


class Test_CriminalRespositoryMock:
    def test_create_criminal(self):
        repo = CriminalRepositoryMock()
        length_before = len(repo.criminals)
        
        criminal = repo.criminals[0]        
        
        criminal_response = repo.create_criminal(criminal=criminal)
        
        length_after = len(repo.criminals)
        
        assert length_before == length_after - 1
        assert criminal_response == criminal
        
        