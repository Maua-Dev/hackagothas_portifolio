


from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.infra.repositories.criminalrecord_repository_mock import CriminalRecordRepositoryMock


class Test_CriminalRecordRepositoryMock():
    def test_create_criminalrecord(self):
        repo = CriminalRecordRepositoryMock()
        length_before = len(repo.criminalrecords)
        
        criminalrecord = repo.criminalrecords[0]        
        
        criminalrecord_response = repo.create_criminalrecord(criminalrecord=criminalrecord)
        
        length_after = len(repo.criminalrecords)
        
        assert length_before == length_after - 1
        assert criminalrecord_response == criminalrecord
        
    def test_get_criminalrecord(self):
        repo = CriminalRecordRepositoryMock()
        
        criminalrecord_response = repo.get_criminalrecord(id=repo.criminalrecords[0].id)
        
        assert criminalrecord_response == repo.criminalrecords[0]
    
    def test_get_criminalrecord_not_found(self):
        repo = CriminalRecordRepositoryMock()
        
        criminalrecord_response = repo.get_criminalrecord(id=-1)
        
        assert criminalrecord_response == None