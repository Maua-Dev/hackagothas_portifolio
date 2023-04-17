
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
        
    def test_get_criminal(self):
        repo = CriminalRepositoryMock()
        
        criminal_response = repo.get_criminal(id=repo.criminals[0].id)
        
        assert criminal_response == repo.criminals[0]
        
    def test_get_criminal_not_found(self):
        repo = CriminalRepositoryMock()
        
        criminal_response = repo.get_criminal(id=-1)
        
        assert criminal_response == None