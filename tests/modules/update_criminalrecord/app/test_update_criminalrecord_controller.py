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
                "criminal": {},
                "crimes": {},
                "id_criminal": 1,
                "name": "lil pump",
                "description": "he is a rapper",
                "gender": "MALE",
                "region_criminal": "USA",
                "id_crime": 1,
                "crime": "MURDER",
                "region_crime": "ATLANTA",
                "date": "20-01-2022",
                "num_victims": 1,
                "arrested": True,
                "score": "LIGHT",
            }
        )

        response = controller(request=request)

        assert response.status_code == 201
        assert response.body["message"] == "the criminal record was updated"
        assert response.body["criminalrecord"]["id_criminalrecord"] == 1
        assert response.body["criminalrecord"]["arrested"] == True
