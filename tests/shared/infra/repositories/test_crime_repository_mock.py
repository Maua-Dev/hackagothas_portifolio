
from src.shared.infra.repositories.crime_repository_mock import CrimeRepositoryMock

class Test_CrimeRepositoryMock:
    def test_create_crime(self):
        repo = CrimeRepositoryMock()
        length_before = len(repo.crimes)
        
        crime = repo.crimes[0]
        
        crime_response = repo.create_crime(crime=crime)
        
        length_after = len(repo.crimes)
        
        assert length_before == length_after - 1
        assert crime_response == crime
        
        
        
        