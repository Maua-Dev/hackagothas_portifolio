from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminalrecord import CriminalRecord
from src.shared.domain.repositories.criminalrecord_repository_interface import (
    ICriminalRecordRepository,
)
from src.shared.helpers.errors.usecase_errors import ForbiddenAction


class UpdateCriminalRecordUsecase:
    def __init__(self, repo_criminalrecord: ICriminalRecordRepository):
        self.repo = repo_criminalrecord

    def __call__(self, criminalrecord: CriminalRecord):
        criminalrecord_with_same_id = self.repo.update_criminalrecord(
            criminalrecord=criminalrecord
        )
        if criminalrecord_with_same_id is None:
            raise ForbiddenAction("CriminalRecord doesn't exists")
        return self.repo.update_criminalrecord(criminalrecord=criminalrecord)
