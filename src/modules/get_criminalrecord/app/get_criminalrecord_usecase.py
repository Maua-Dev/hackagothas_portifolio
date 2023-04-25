from src.shared.domain.entities.criminalrecord import CriminalRecord
from src.shared.domain.repositories.criminalrecord_repository_interface import ICriminalRecordRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class GetCriminalRecordUsecase:
    def __init__(self, repo_criminal: ICriminalRecordRepository):
        self.repo = repo_criminal

    def __call__(self, criminalrecord_id: int) -> CriminalRecord:

        if not CriminalRecord.validate_criminalrecord_id(criminalrecord_id):
            raise EntityError("Invalid criminalrecord_id")

        criminalrecord_with_same_id = self.repo.get_criminalrecord_by_id(criminalrecord_id=criminalrecord_id)

        if criminalrecord_with_same_id is None:
            raise NoItemsFound("CriminalRecord doesn't exists")
        
        return criminalrecord_with_same_id
       