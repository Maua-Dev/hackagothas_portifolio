from src.modules.create_criminalrecord.app.create_criminalrecord_controller import (
    CreateCriminalRecordController,
)
from src.modules.create_criminalrecord.app.create_criminalrecord_usecase import (
    CreateCriminalRecordUsecase,
)
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.criminalrecord_repository_mock import (
    CriminalRecordRepositoryMock,
)


class Test_CreateCriminalRecordController:
    def test_create_criminalrecord_controller(self):
        repo = CriminalRecordRepositoryMock()
        usecase = CreateCriminalRecordUsecase(repo)
        controller = CreateCriminalRecordController(usecase)

        request = HttpRequest(
            body={
                "id_criminalrecord": 9,
                "criminal": {
                    "id_criminal": 8,
                    "name": "Prino",
                    "description": "Smoke Maker",
                    "gender": "MALE",
                    "region_criminal": "ZN",
                },
                "crimes": [
                    {
                        "id_crime": 6,
                        "criminal": {
                            "id_criminal": 8,
                            "name": "Prino",
                            "description": "Smoke Maker",
                            "gender": "MALE",
                            "region_criminal": "ZN",
                        },
                        "crime": "DRUG_OFFENSES",
                        "region_crime": "ABC",
                        "date": "20-04-2023",
                        "num_victims": 96,
                    }
                ],
                "arrested": False,
                "score": "FOURSTAR",
            }
        )

        response = controller(request=request)

        assert response.status_code == 201
        assert response.body["message"] == "the criminal record was created"
        assert response.body["criminalrecord"]["id_criminalrecord"] == 9
        assert response.body["criminalrecord"]["criminal"]["id_criminal"] == 8
        assert response.body["criminalrecord"]["criminal"]["name"] == "Prino"
        assert (
            response.body["criminalrecord"]["criminal"]["description"] == "Smoke Maker"
        )
        assert response.body["criminalrecord"]["criminal"]["gender"] == "MALE"
        assert response.body["criminalrecord"]["criminal"]["region_criminal"] == "ZN"
        assert response.body["criminalrecord"]["crimes"][0]["id_crime"] == 6
        assert response.body["criminalrecord"]["crimes"][0]["crime"] == "DRUG_OFFENSES"
        assert response.body["criminalrecord"]["crimes"][0]["region_crime"] == "ABC"
        assert response.body["criminalrecord"]["crimes"][0]["date"] == "20-04-2023"
        assert response.body["criminalrecord"]["crimes"][0]["num_victims"] == 96
        assert response.body["criminalrecord"]["arrested"] == False
        assert response.body["criminalrecord"]["score"] == "FOURSTAR"

    def test_create_criminalrecord_controller_missing_id(self):
        repo = CriminalRecordRepositoryMock()
        usecase = CreateCriminalRecordUsecase(repo)
        controller = CreateCriminalRecordController(usecase)

        request = HttpRequest(
            body={
                "criminal": {
                    "id_criminal": 8,
                    "name": "Prino",
                    "description": "Smoke Maker",
                    "gender": "MALE",
                    "region_criminal": "ZN",
                },
                "crimes": [
                    {
                        "id_crime": 6,
                        "criminal": {
                            "id_criminal": 8,
                            "name": "Prino",
                            "description": "Smoke Maker",
                            "gender": "MALE",
                            "region_criminal": "ZN",
                        },
                        "crime": "DRUG_OFFENSES",
                        "region_crime": "ABC",
                        "date": "20-04-2023",
                        "num_victims": 96,
                    }
                ],
                "arrested": False,
                "score": "FOURSTAR",
            }
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field id_criminalrecord is missing"