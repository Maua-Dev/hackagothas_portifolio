

import pytest
from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.crime_enum import CRIME
from src.shared.domain.enums.gender_enum import GENDER


class Test_Crime():
    
    criminal = Criminal(name="Furlan", description="LINUX", gender=GENDER.MALE, region="Brazil")

    def test_crime(self):
        crime = Crime(id=1, criminal=self.criminal, crime=CRIME.THEFT, region="Brazil", date="2020-01-01", num_victims=1)
        
        assert crime.id == 1
        assert crime.criminal == self.criminal
        assert crime.crime == CRIME.THEFT
        assert crime.region == "Brazil"
        assert crime.date == "2020-01-01"
        assert crime.num_victims == 1
        
    def test_crime_invalid_id(self):
        with pytest.raises(Exception):
            crime = Crime(id="1", criminal=self.criminal, crime=CRIME.THEFT, region="Brazil", date="2020-01-01", num_victims=1)
        
    def test_crime_invalid_criminal(self):
        with pytest.raises(Exception):
            crime = Crime(id=1, criminal=1, crime=CRIME.THEFT, region="Brazil", date="2020-01-01", num_victims=1)
    
    def test_crime_invalid_crime(self):
        with pytest.raises(Exception):
            crime = Crime(id=1, criminal=self.criminal, crime=1, region="Brazil", date="2020-01-01", num_victims=1)
            
    def test_crime_invalid_region(self):
        with pytest.raises(Exception):
            crime = Crime(id=1, criminal=self.criminal, crime=CRIME.THEFT, region=1, date="2020-01-01", num_victims=1)
            
    def test_crime_invalid_date(self):
        with pytest.raises(Exception):
            crime = Crime(id=1, criminal=self.criminal, crime=CRIME.THEFT, region="Brazil", date=1, num_victims=1)
    
    def test_crime_invalid_num_victims(self):
        with pytest.raises(Exception):
            crime = Crime(id=1, criminal=self.criminal, crime=CRIME.THEFT, region="Brazil", date="2020-01-01", num_victims="1")
        