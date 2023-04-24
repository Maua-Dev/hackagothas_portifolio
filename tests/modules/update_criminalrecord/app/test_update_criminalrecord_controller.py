from src.modules.update_criminalrecord.app.update_criminalrecord_controller import (
    UpdateCriminalRecordController,
)
from src.modules.update_criminalrecord.app.update_criminalrecord_usecase import (
    UpdateCriminalRecordUsecase,
)
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.criminalrecord_repository_mock import (
    CriminalRecordRepositoryMock,
)


class Test_UpdateCriminalRecordController:
    def test_update_criminalrecord_controller(self):
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)
        controller = UpdateCriminalRecordController(usecase)

        request = HttpRequest(
            body={
                "id_criminalrecord": 1,
                "criminal": {
                    "id_criminal": 1,
                    "name": "lil pump",
                    "description": "he is a rapper",
                    "gender": "MALE",
                    "region_criminal": "USA",
                },
                "crimes": [
                    {
                        "id_crime": 1,
                        "criminal": {
                            "id_criminal": 1,
                            "name": "lil pump",
                            "description": "he is a rapper",
                            "gender": "MALE",
                            "region_criminal": "USA",
                        },
                        "crime": "MURDER",
                        "region_crime": "ATLANTA",
                        "date": "20-01-2022",
                        "num_victims": 1,
                    },
                ],
                "arrested": True,
                "score": "ONESTAR",
            }
        )

        response = controller(request=request)

        assert response.status_code == 201
        assert response.body["message"] == "the criminal record was updated"
        assert response.body["criminalrecord"]["id_criminalrecord"] == 1
        assert response.body["criminalrecord"]["criminal"]["id_criminal"] == 1
        assert response.body["criminalrecord"]["criminal"]["name"] == "lil pump"
        assert (
            response.body["criminalrecord"]["criminal"]["description"]
            == "he is a rapper"
        )
        assert response.body["criminalrecord"]["criminal"]["gender"] == "MALE"
        assert response.body["criminalrecord"]["criminal"]["region_criminal"] == "USA"
        assert response.body["criminalrecord"]["crimes"][0]["id_crime"] == 1
        assert response.body["criminalrecord"]["crimes"][0]["crime"] == "MURDER"
        assert response.body["criminalrecord"]["crimes"][0]["region_crime"] == "ATLANTA"
        assert response.body["criminalrecord"]["crimes"][0]["date"] == "20-01-2022"
        assert response.body["criminalrecord"]["crimes"][0]["num_victims"] == 1
        assert response.body["criminalrecord"]["arrested"] == True
        assert response.body["criminalrecord"]["score"] == "ONESTAR"
