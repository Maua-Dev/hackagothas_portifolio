from src.modules.delete_criminalrecord.app.delete_criminalrecord_controller import (
    DeleteCriminalRecordController,
)
from src.modules.delete_criminalrecord.app.delete_criminalrecord_usecase import (
    DeleteCriminalRecordUsecase,
)
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.criminalrecord_repository_mock import (
    CriminalRecordRepositoryMock,
)


class Test_DeleteCriminalRecordController:
    def test_delete_criminalrecord_controller(self):
        repo = CriminalRecordRepositoryMock()
        usecase = DeleteCriminalRecordUsecase(repo)
        controller = DeleteCriminalRecordController(usecase)

        request = HttpRequest(
            body={
                "id_criminalrecord": 1,
            }
        )

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body["message"] == "the criminal record was deleted"
        assert response.body["criminalrecord"]["id_criminalrecord"] == 1
        assert response.body["criminalrecord"]["criminal"]["name"] == "Furlan"
        assert (
            response.body["criminalrecord"]["criminal"]["description"]
            == "Furlan is a Automato"
        )
        assert response.body["criminalrecord"]["criminal"]["gender"] == "MALE"
        assert response.body["criminalrecord"]["criminal"]["region_criminal"] == "Mauá"
        assert response.body["criminalrecord"]["arrested"] == False
        assert response.body["criminalrecord"]["score"] == "ONESTAR"

    def test_delete_criminalrecord_controller_invalid_id(self):
        repo = CriminalRecordRepositoryMock()
        usecase = DeleteCriminalRecordUsecase(repo)
        controller = DeleteCriminalRecordController(usecase)

        request = HttpRequest(
            body={
                "id_criminalrecord": 10,
            }
        )

        response = controller(request=request)

        assert response.body == "No items found for id_criminalrecord"
        assert response.status_code == 404
