 
 
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.repositories.criminalrecord_repository_interface import ICriminalRecordRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction


class CreateCriminalUsecase:
    def __init__(self, repo_criminal: ICriminalRecordRepository):
        self.repo = repo_criminal
        
    def __call__(self, criminal: Criminal):
        criminal_with_same_id = self.repo.get_criminal(criminal.id)
        if criminal_with_same_id is not None:
            raise ForbiddenAction("Criminal already exists")
        return self.repo.create_criminal(criminal)