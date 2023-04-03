
from src.shared.domain.entities.criminalrecord import CriminalRecord
from src.shared.domain.repositories.criminalrecord_repository_interface import ICriminalRecordRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction


class CreateCriminalRecordUsecase:

    def __init__(self, repo_criminalrecord: ICriminalRecordRepository):
        self.repo = repo_criminalrecord

    def __call__(self, criminalrecord: CriminalRecord):
        if self.repo.get_criminalrecord(criminalrecord.id) is not None:
            raise ForbiddenAction("Criminal Record already exists")
        return self.repo.create_criminalrecord(criminalrecord)