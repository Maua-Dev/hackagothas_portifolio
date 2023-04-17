
import abc

from src.shared.domain.enums.gender_enum import GENDER
from src.shared.helpers.errors.domain_errors import EntityError


class Criminal(abc.ABC):
    id: int
    name: str
    description: str
    gender: GENDER
    region: str
    
    def __init__(self, id: int, name: str, description: str, gender: GENDER, region: str):
        
        if type(id) != int:
            raise EntityError('Name must be a interger')
        self.id = id
        
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
    
    @staticmethod 
    def validate_id(id: int) -> bool:
        if id < 0: 
            return False
        if type(id) != int:
            return False 
        return True
    
    def __eq__(self, other) -> bool: 
        return self.name == other.name and self.description == other.description and self.gender == other.gender and self.region == other.region