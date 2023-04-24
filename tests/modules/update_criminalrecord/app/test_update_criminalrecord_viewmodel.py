from src.modules.update_criminalrecord.app.update_criminalrecord_viewmodel import (
    UpdateCriminalRecordViewmodel,
)
from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminalrecord import CriminalRecord
from src.shared.domain.enums.crime_enum import CRIME
from src.shared.domain.enums.danger_score_enum import DANGER_SCORE
from src.shared.domain.enums.gender_enum import GENDER


class Test_CreateCriminalRecordViewmodel:
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
    criminalrecord_with_same_id = CriminalRecord(
        id=3,
        criminal=criminal,
        crimes=[crime],
        arrested=True,
        score=DANGER_SCORE.ONESTAR,
    )

    def test_create_criminalrecord_viewmodel(self):
        criminalrecord_viewmodel = UpdateCriminalRecordViewmodel(
            self.criminalrecord_with_same_id
        ).to_dict()

        assert criminalrecord_viewmodel == {
            "criminalrecord": {
                "id_criminalrecord": 3,
                "criminal": {
                    "id_criminal": 1,
                    "name": "IGAO DE LP VULGO ESTORA POO",
                    "description": "Furlan is a Automato",
                    "gender": "FEMALE",
                    "region_criminal": "Mauá",
                },
                "crimes": [
                    {
                        "id_crime": 5,
                        "criminal": {
                            "id_criminal": 1,
                            "name": "IGAO DE LP VULGO ESTORA POO",
                            "description": "Furlan is a Automato",
                            "gender": "FEMALE",
                            "region_criminal": "Mauá",
                        },
                        "crime": "MURDER",
                        "region_crime": "Mauá",
                        "date": "20-01-2021",
                        "num_victims": 1,
                    }
                ],
                "arrested": True,
                "score": "LIGHT",
            },
            "message": "the criminal record was updated",
        }
