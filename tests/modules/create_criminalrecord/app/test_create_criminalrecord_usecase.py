

# import pytest
# from src.modules.create_criminalrecord.app.create_criminalrecord_usecase import CreateCriminalRecordUsecase
# from src.shared.helpers.errors.usecase_errors import ForbiddenAction
# from src.shared.infra.repositories.criminalrecord_repository_mock import CriminalRecordRepositoryMock


# class Test_CreateCriminalRecordUsecase:
#     def test_create_criminalrecord_usecase(self):
#         repo = CriminalRecordRepositoryMock()
#         usecase = CreateCriminalRecordUsecase(repo)
#         criminalrecord = repo.criminalrecord[0]
#         assert usecase(criminalrecord) == criminalrecord
#         with pytest.raises(ForbiddenAction):
#             usecase(criminalrecord)