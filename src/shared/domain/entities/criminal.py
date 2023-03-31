
import abc

from src.shared.domain.enums.gender_enum import GENDER
from src.shared.helpers.errors.domain_errors import EntityError


class Criminal(abc.ABC):
    name: str
    description: str
    gender: GENDER
    region: str
    
    def __init__(self, name: str, description: str, gender: GENDER, region: str):
        
        if type(name) != str:
            raise EntityError('Name must be a string')
        self.name = name
        
        if type(description) != str:
            raise EntityError('Description must be a string')
        self.description = description
        
        if type(gender) != GENDER:
            raise EntityError('GENDER must be a GENDER')
        self.gender = gender
        
        if type(region) != str:
            raise EntityError('Region must be a string')
        self.region = region
        
    @staticmethod
    def validate_name(name: str) -> bool:
        if type(name) != str:
            return False
        if len(name) <= 2:
            return False
        return True
    