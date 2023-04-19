

from src.shared.domain.entities.crime import Crime
from src.shared.domain.repositories.criminalrecord_repository_interface import ICriminalRecordRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction


class CreateCrimeUsecase:
    def __init__(self, repo_crime: ICriminalRecordRepository):
        self.repo = repo_crime
        
    def __call__(self, crime: Crime):
        crime_with_same_id = self.repo.get_crime(crime.id)
        if crime_with_same_id is not None:
            raise ForbiddenAction("Crime already exists")
        return self.repo.create_crime(crime)