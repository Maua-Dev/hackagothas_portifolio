from src.modules.get_criminalrecord.app.get_criminalrecord_controller import GetCriminalRecordController
from src.modules.get_criminalrecord.app.get_criminalrecord_usecase import GetCriminalRecordUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.criminalrecord_repository_mock import CriminalRecordRepositoryMock


class Test_GetUserController:
    def test_get_user_controller(self):
        repo = CriminalRecordRepositoryMock()
        usecase = GetCriminalRecordUsecase(repo)
        controller = GetCriminalRecordController(usecase)

        response = controller(request = HttpRequest(body = {"id_criminalrecord": 1}))

        assert response.status_code == 200
        assert response.body["message"] == "Criminal record was retrieved successfully"
        assert response.body["criminalrecord"]["id_criminalrecord"] == repo.criminalrecords[0].id
        assert response.body["criminalrecord"]["criminal"]["id_criminal"] == repo.criminalrecords[0].criminal.id
        assert response.body["criminalrecord"]["criminal"]["name"] == repo.criminalrecords[0].criminal.name
        assert response.body["criminalrecord"]["criminal"]["description"] == repo.criminalrecords[0].criminal.description
        assert response.body["criminalrecord"]["criminal"]["gender"] == repo.criminalrecords[0].criminal.gender.value
        assert response.body["criminalrecord"]["criminal"]["region_criminal"] == repo.criminalrecords[0].criminal.region
        assert response.body["criminalrecord"]["crimes"][0]["id_crime"] == repo.criminalrecords[0].crimes[0].id
        assert response.body["criminalrecord"]["crimes"][0]["crime"] == repo.criminalrecords[0].crimes[0].crime.value
        assert response.body["criminalrecord"]["crimes"][0]["region_crime"] == repo.criminalrecords[0].crimes[0].region
        assert response.body["criminalrecord"]["crimes"][0]["date"] == repo.criminalrecords[0].crimes[0].date
        assert response.body["criminalrecord"]["crimes"][0]["num_victims"] == repo.criminalrecords[0].crimes[0].num_victims
        assert response.body["criminalrecord"]["arrested"] == repo.criminalrecords[0].arrested
        assert response.body["criminalrecord"]["score"] == repo.criminalrecords[0].score.value