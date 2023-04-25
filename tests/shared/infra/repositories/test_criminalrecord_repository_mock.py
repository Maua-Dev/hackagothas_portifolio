from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminalrecord import CriminalRecord
from src.shared.domain.enums.crime_enum import CRIME
from src.shared.domain.enums.danger_score_enum import DANGER_SCORE
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
        criminal = Criminal(
            id=1,
            name="Furlas",
            description="Furlan is a Automato",
            gender=GENDER.FEMALE,
            region="Mauá",
        )
        crime = Crime(
            id=5,
            criminal=criminal,
            crime=CRIME.MURDER,
            region="Mauá",
            date="20-01-2021",
            num_victims=1,
        )
        criminalrecord = CriminalRecord(
            id=1,
            criminal=criminal,
            crimes=[crime],
            arrested=True,
            score=DANGER_SCORE.ONESTAR,
        )

        criminalrecord_response = repo.update_criminalrecord(
            criminalrecord=criminalrecord
        )

        assert criminalrecord_response == criminalrecord

    def test_update_criminalrecord_id_not_found(self):
        repo = CriminalRecordRepositoryMock()
        criminal = Criminal(
            id=1,
            name="Furlas",
            description="Furlan is a Automato",
            gender=GENDER.FEMALE,
            region="Mauá",
        )
        crime = Crime(
            id=5,
            criminal=criminal,
            crime=CRIME.MURDER,
            region="Mauá",
            date="20-01-2021",
            num_victims=1,
        )
        criminalrecord = CriminalRecord(
            id=10,
            criminal=criminal,
            crimes=[crime],
            arrested=True,
            score=DANGER_SCORE.ONESTAR,
        )

        criminalrecord_response = repo.update_criminalrecord(
            criminalrecord=criminalrecord
        )

        assert criminalrecord_response == None

    def test_delete_criminalrecord(self):
        repo = CriminalRecordRepositoryMock()
        criminalrecord_removed = repo.criminalrecords[0]

        length_before = len(repo.criminalrecords)

        criminalrecord_response = repo.delete_criminalrecord(id=1)

        length_after = len(repo.criminalrecords)

        assert criminalrecord_removed == criminalrecord_response
        assert length_after == length_before - 1

    def test_delete_criminalrecord_invalid_id(self):
        repo = CriminalRecordRepositoryMock()

        criminalrecord_response = repo.delete_criminalrecord(id=5)

        assert criminalrecord_response == None
