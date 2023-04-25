import pytest
from src.modules.update_criminalrecord.app.update_criminalrecord_usecase import (
    UpdateCriminalRecordUsecase,
)
from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminalrecord import CriminalRecord
from src.shared.domain.enums.crime_enum import CRIME
from src.shared.domain.enums.danger_score_enum import DANGER_SCORE
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.helpers.errors.usecase_errors import ForbiddenAction
from src.shared.infra.repositories.criminalrecord_repository_mock import (
    CriminalRecordRepositoryMock,
)


class Test_UpdateCriminalRecordUsecase:
    criminal = Criminal(
        id=1,
        name="IGAO DE LP VULGO ESTORA POO",
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
    criminalrecord_with_invalid_id = CriminalRecord(
        id=5,
        criminal=criminal,
        crimes=[crime],
        arrested=False,
        score=DANGER_SCORE.ONESTAR,
    )
    criminalrecord_with_same_id = CriminalRecord(
        id=3,
        criminal=criminal,
        crimes=[crime],
        arrested=True,
        score=DANGER_SCORE.ONESTAR,
    )

    def test_update_criminalrecord_usecase(self):
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)

        length_before = len(repo.criminalrecords)

        criminal_response = usecase(criminalrecord=self.criminalrecord_with_same_id)

        length_after = len(repo.criminalrecords)

        assert length_before == length_after
        assert repo.criminalrecords[2] == criminal_response

    def test_update_criminalrecord_usecase_invalid_id(self):
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)

        with pytest.raises(ForbiddenAction):
            criminalrecord_response = usecase(
                criminalrecord=self.criminalrecord_with_invalid_id
            )
