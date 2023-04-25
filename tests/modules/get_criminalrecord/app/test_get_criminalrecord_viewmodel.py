from src.modules.get_criminalrecord.app.get_criminalrecord_viewmodel import GetCriminalRecordViewmodel
from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminalrecord import CriminalRecord
from src.shared.domain.enums.crime_enum import CRIME
from src.shared.domain.enums.danger_score_enum import DANGER_SCORE
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.infra.repositories.criminalrecord_repository_mock import CriminalRecordRepositoryMock


class Test_GetCriminalRecordViewmodel:
    criminal = Criminal(
        id=1,
        name="IGAO DE LP VULGO ESTORA POO",
        description="Furlan is a Automato",
        gender=GENDER.FEMALE,
        region="Mauá",
    )
    crime = Crime(
        id=5,
        criminal=criminal,
        crime=CRIME.MURDER,
        region="Mauá",
        date="20-01-2021",
        num_victims=1,
    )
    criminalrecord = CriminalRecord(
        id=3,
        criminal=criminal,
        crimes=[crime],
        arrested=True,
        score=DANGER_SCORE.ONESTAR,
    )

    def test_get_criminalrecord_viewmodel(self):
        criminalrecord_viewmodel = GetCriminalRecordViewmodel(self.criminalrecord).to_dict()

        assert criminalrecord_viewmodel == {
            "criminalrecord":{
                "id_criminalrecord":3,
                "criminal":{
                    "id_criminal":1,
                    "name":"IGAO DE LP VULGO ESTORA POO",
                    "description":"Furlan is a Automato",
                    "gender":"FEMALE",
                    "region_criminal":"Mauá"
                },
                "crimes":[
                {
                    "id_crime":5,
                    "criminal":{
                        "id_criminal":1,
                        "name":"IGAO DE LP VULGO ESTORA POO",
                        "description":"Furlan is a Automato",
                        "gender":"FEMALE",
                        "region_criminal":"Mauá"
                    },
                    "crime":"MURDER",
                    "region_crime":"Mauá",
                    "date":"20-01-2021",
                    "num_victims":1
                }
                ],
                "arrested":True,
                "score":"ONESTAR"
            },
            "message":"Criminal record was retrieved successfully"
        }

        