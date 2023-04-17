

import pytest
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.gender_enum import GENDER


class Test_Criminal():
    
    def test_criminal(self):
        criminal = Criminal(id=1, name="Furlan", description="LINUX", gender=GENDER.MALE, region="Brazil")
        
        
        assert criminal.id == 1
        assert criminal.name == "Furlan"
        assert criminal.description == "LINUX"
        assert criminal.gender == GENDER.MALE
        assert criminal.region == "Brazil"
        
    def test_criminal_invalid_id(self):
        with pytest.raises(Exception):
            criminal = Criminal(id="1", name="Furlan",  description="LINUX", gender=GENDER.MALE, region="Brazil")
        
    def test_criminal_invalid_name(self):
        with pytest.raises(Exception):
            criminal = Criminal(id=1, name=1,  description="LINUX", gender=GENDER.MALE, region="Brazil")
            
    def test_criminal_invalid_description(self):
        with pytest.raises(Exception):
            criminal = Criminal(id=1, name="Furlan", description=1, gender=GENDER.MALE, region="Brazil")
            
    def test_criminal_invalid_gender(self):
        with pytest.raises(Exception):
            criminal = Criminal(id=1, name="Furlan", description="LINUX", gender=1, region="Brazil")
            
    def test_criminal_invalid_region(self):
        with pytest.raises(Exception):
            criminal = Criminal(id=1, name="Furlan", description="LINUX", gender=GENDER.MALE, region=1)