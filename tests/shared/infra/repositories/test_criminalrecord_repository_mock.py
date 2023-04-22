from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.infra.repositories.criminalrecord_repository_mock import (
    CriminalRecordRepositoryMock,
)


class Test_CriminalRecordRepositoryMock:
    def test_create_criminalrecord(self):
        repo = CriminalRecordRepositoryMock()
        length_before = len(repo.criminalrecords)

        criminalrecord = repo.criminalrecords[0]

        criminalrecord_response = repo.create_criminalrecord(
            criminalrecord=criminalrecord
        )

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

    def test_create_criminal(self):
        repo = CriminalRecordRepositoryMock()
        length_before = len(repo.criminals)

        criminal = repo.criminals[0]

        criminal_response = repo.create_criminal(criminal=criminal)

        length_after = len(repo.criminals)

        assert length_before == length_after - 1
        assert criminal_response == criminal

    def test_get_criminal(self):
        repo = CriminalRecordRepositoryMock()

        criminal_response = repo.get_criminal(id=repo.criminals[0].id)

        assert criminal_response == repo.criminals[0]

    def test_get_criminal_not_found(self):
        repo = CriminalRecordRepositoryMock()

        criminal_response = repo.get_criminal(id=-1)

        assert criminal_response == None

    def test_create_crime(self):
        repo = CriminalRecordRepositoryMock()
        length_before = len(repo.crimes)

        crime = repo.crimes[0]

        crime_response = repo.create_crime(crime=crime)

        length_after = len(repo.crimes)

        assert length_before == length_after - 1
        assert crime_response == crime

    def test_get_crime(self):
        repo = CriminalRecordRepositoryMock()

        crime_response = repo.get_crime(id=repo.crimes[0].id)

        assert crime_response == repo.crimes[0]

    def test_get_criminal_not_found(self):
        repo = CriminalRecordRepositoryMock()

        crime_response = repo.get_crime(id=-1)

        assert crime_response == None

    def test_update_criminalrecord(self):
        repo = CriminalRecordRepositoryMock()

        criminalrecord = repo.criminalrecords[0]
        criminalrecord.arrested = True

        criminalrecord_response = repo.update_criminalrecord(
            criminalrecord=criminalrecord,
            id=1,
        )

        assert criminalrecord_response == criminalrecord

    def test_update_criminalrecord_id_not_found(self):
        repo = CriminalRecordRepositoryMock()

        criminalrecord = repo.criminalrecords[0]
        criminalrecord.arrested = True

        criminalrecord_response = repo.update_criminalrecord(
            criminalrecord=criminalrecord,
            id=5,
        )

        assert criminalrecord_response == None
