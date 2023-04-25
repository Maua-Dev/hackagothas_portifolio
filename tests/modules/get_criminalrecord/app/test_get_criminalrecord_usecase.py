import pytest
from src.modules.get_criminalrecord.app.get_criminalrecord_usecase import GetCriminalRecordUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.criminalrecord_repository_mock import CriminalRecordRepositoryMock


class Test_GetCriminalRecordUsecase():
    
    def test_get_criminalrecord_usecase(self):
        repo = CriminalRecordRepositoryMock()
        usecase = GetCriminalRecordUsecase(repo)

        criminalrecord_response = usecase(criminalrecord_id=1)

        assert repo.criminalrecords[0] == criminalrecord_response

    def test_get_criminalrecord_usecase_with_wrong_id(self):
        repo = CriminalRecordRepositoryMock()
        usecase = GetCriminalRecordUsecase(repo)

        with pytest.raises(NoItemsFound):
            usecase(criminalrecord_id=0)
