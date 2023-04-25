from src.modules.create_criminalrecord.app.create_criminalrecord_viewmodel import (
    CreateCriminalRecordViewmodel,
)
from src.shared.infra.repositories.criminalrecord_repository_mock import (
    CriminalRecordRepositoryMock,
)


class Test_CreateCriminalRecordViewmodel:
    def test_create_criminalrecord_viewmodel(self):
        repo = CriminalRecordRepositoryMock()

        criminalrecord = repo.criminalrecords[0]

        criminalrecord_viewmodel = CreateCriminalRecordViewmodel(
            criminalrecord
        ).to_dict()

        assert criminalrecord_viewmodel == {
            "criminalrecord": {
                "id_criminalrecord": 1,
                "criminal": {
                    "id_criminal": 1,
                    "name": "Furlan",
                    "description": "Furlan is a Automato",
                    "gender": "MALE",
                    "region_criminal": "Mauá",
                },
                "crimes": [
                    {
                        "id_crime": 1,
                        "criminal": {
                            "id_criminal": 1,
                            "name": "Furlan",
                            "description": "Furlan is a Automato",
                            "gender": "MALE",
                            "region_criminal": "Mauá",
                        },
                        "crime": "MURDER",
                        "region_crime": "Mauá",
                        "date": "20-01-2021",
                        "num_victims": 1,
                    }
                ],
                "arrested": False,
                "score": "ONESTAR",
            },
            "message": "the criminal record was created",
        }
