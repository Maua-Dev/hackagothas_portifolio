from abc import ABC, abstractmethod

from src.shared.domain.entities.criminal import Criminal

class ICriminalRepository(ABC):
    
    @abstractmethod
    def create_criminal(self, criminal: Criminal) -> Criminal: 
        pass
    
    