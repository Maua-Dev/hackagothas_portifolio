from abc import ABC, abstractmethod

from src.shared.domain.entities.crime import Crime

class ICrimeRepository(ABC):

    @abstractmethod
    def create_crime(self, crime: Crime) -> Crime:
        pass
    
    @abstractmethod
    def get_crime(self, id: int) -> Crime:
        pass