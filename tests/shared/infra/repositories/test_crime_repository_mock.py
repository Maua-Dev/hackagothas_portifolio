
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
        
    def test_get_crime(self):
        repo = CrimeRepositoryMock()
        
        crime_response = repo.get_crime(id=repo.crimes[0].id)
        
        assert crime_response == repo.crimes[0]
        
    def test_get_criminal_not_found(self):
        repo = CrimeRepositoryMock()
        
        crime_response = repo.get_crime(id=-1)
        
        assert crime_response == None