 
 
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.repositories.criminal_repository_interface import ICriminalRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction


class CreateCriminalUsecase:
    def _init_(self, repo_criminal: ICriminalRepository):
        self.repo = repo_criminal
        
    def __call__(self, criminal: Criminal):
        criminal_with_same_id = self.repo.get_criminal(criminal.id)
        if criminal_with_same_id is not None:
            raise ForbiddenAction("Criminal already exists")
        return self.repo.create_criminal(criminal)