from src.modules.create_criminalrecord.app.create_criminalrecord_controller import CreateCriminalRecordController
from src.modules.create_criminalrecord.app.create_criminalrecord_usecase import CreateCriminalRecordUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.criminalrecord_repository_mock import CriminalRecordRepositoryMock


class Test_CreateCriminalRecordController:

    def test_create_criminalrecord_controller(self):
        repo = CriminalRecordRepositoryMock()
        usecase = CreateCriminalRecordUsecase(repo)
        controller = CreateCriminalRecordController(usecase)

        request = HttpRequest(body={
            "criminalrecord_id":9,
            "criminal":{
                "criminal_id":8,
                "name":"Prino",
                "description":"Smoke Maker",
                "gender":"MALE",
                "criminal_region":"ZN"
            },
            "crimes":[
                {
                    "crime_id":6,
                    "criminal":{
                        "criminal_id":8,
                        "name":"Prino",
                        "description":"Smoke Maker",
                        "gender":"MALE",
                        "criminal_region":"ZN"
                    },
                    "crime_type":"DRUG-OFFENSES",
                    "crime_region":"ABC",
                    "date":"20-04-2023",
                    "num_victims":96
                }
            ],
            "arrested":False,
            "score":"HIGH"
        })

        response = controller(request=request)

        assert response.status_code == 201
        assert response.body["massege"] == "the criminal record was created"
        assert response.body["criminalrecord"]["criminalrecord_id"] == 9
        assert response.body["criminalrecord"]["criminal"]["criminal_id"] == 8
        assert response.body["criminalrecord"]["criminal"]["name"] == "Prino"
        assert response.body["criminalrecord"]["criminal"]["description"] == "Smoke Maker"
        assert response.body["criminalrecord"]["criminal"]["gender"] == "MALE"
        assert response.body["criminalrecord"]["criminal"]["criminal_region"] == "ZN"
        assert response.body["criminalrecord"]["crimes"][0]["crime_id"] == 6
        assert response.body["criminalrecord"]["crimes"][0]["crime_type"] == "DRUG_OFFENSES"
        assert response.body["criminalrecord"]["crimes"][0]["crime_region"] == "ABC"
        assert response.body["criminalrecord"]["crimes"][0]["date"] == "20-04-2023"
        assert response.body["criminalrecord"]["crimes"][0]["num_victims"] == 96
        assert response.body["criminalrecord"]["arrested"] == False
        assert response.body["criminalrecord"]["score"] == "HIGH"