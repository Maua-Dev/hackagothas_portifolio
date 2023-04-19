

from abc import abstractmethod
import abc
from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal

from src.shared.domain.entities.criminalrecord import CriminalRecord


class ICriminalRecordRepository(abc.ABC):
    
    @abstractmethod
    def create_criminalrecord(self, criminalrecord: CriminalRecord) -> CriminalRecord:
        pass
    
    @abstractmethod
    def get_criminalrecord(self, criminalrecord: CriminalRecord) -> CriminalRecord:
        pass
    
    @abstractmethod
    def create_criminal(self, criminal: Criminal) -> Criminal: 
        pass
    
    @abstractmethod
    def get_criminal(self, criminal: Criminal) -> Criminal:
        pass
    
    @abstractmethod
    def create_crime(self, crime: Crime) -> Crime:
        pass
    
    @abstractmethod
    def get_crime(self, id: int) -> Crime:
        pass