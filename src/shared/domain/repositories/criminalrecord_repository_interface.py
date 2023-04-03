

from abc import abstractmethod
import abc

from src.shared.domain.entities.criminalrecord import CriminalRecord


class ICriminalRecordRepository(abc.ABC):
    
    @abstractmethod
    def create_criminalrecord(self, criminalrecord: CriminalRecord) -> CriminalRecord:
        pass
    
    @abstractmethod
    def get_criminalrecord(self, criminalrecord: CriminalRecord) -> CriminalRecord:
        pass