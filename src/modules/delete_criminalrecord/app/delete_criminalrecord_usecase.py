from src.shared.domain.repositories.criminalrecord_repository_interface import (
    ICriminalRecordRepository,
)
from src.shared.helpers.errors.usecase_errors import ForbiddenAction


class DeleteCriminalRecordUsecase:
    def __init__(self, repo_criminalrecord: ICriminalRecordRepository):
        self.repo = repo_criminalrecord

    def __call__(self, id_criminalrecord: int):
        criminalrecord = self.repo.delete_criminalrecord(id=id_criminalrecord)
        if criminalrecord is None:
            raise ForbiddenAction("CriminalRecord doesn't exists")
        return criminalrecord
