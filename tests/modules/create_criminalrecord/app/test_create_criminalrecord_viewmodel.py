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
            "crime": {
                "id": 1,
                "criminal": {
                    "id": 1,
                    "name": "Furlan",
                    "description": "Furlan is a Automato",
                    "gender": "MALE",
                    "region": "Mauá",
                },
                "crimes": [
                    {
                        "id": 1,
                        "criminal": {
                            "id": 1,
                            "name": "Furlan",
                            "description": "Furlan is a Automato",
                            "gender": "MALE",
                            "region": "Mauá",
                        },
                        "crime": "MURDER",
                        "region": "Mauá",
                        "date": "20-01-2021",
                        "num_victims": 1,
                    }
                ],
                "arrested": False,
                "score": "LIGHT",
            },
            "message": "the criminal record was created",
        }
