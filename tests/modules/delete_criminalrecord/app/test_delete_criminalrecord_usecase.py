import pytest
from src.modules.delete_criminalrecord.app.delete_criminalrecord_usecase import (
    DeleteCriminalRecordUsecase,
)
from src.shared.helpers.errors.usecase_errors import ForbiddenAction
from src.shared.infra.repositories.criminalrecord_repository_mock import (
    CriminalRecordRepositoryMock,
)


class Test_DeleteCriminalRecordUsecase:
    def test_delete_criminalrecord_usecase(self):
        repo = CriminalRecordRepositoryMock()
        usecase = DeleteCriminalRecordUsecase(repo)

        length_before = len(repo.criminalrecords)

        criminalrecord_removed = repo.criminalrecords[0]

        criminal_response = usecase(id_criminalrecord=1)

        length_after = len(repo.criminalrecords)

        assert length_after == length_before - 1
        assert criminalrecord_removed == criminal_response

    def test_update_criminalrecord_usecase_invalid_id(self):
        repo = CriminalRecordRepositoryMock()
        usecase = DeleteCriminalRecordUsecase(repo)

        with pytest.raises(ForbiddenAction):
            criminalrecord_response = usecase(id_criminalrecord=10)
