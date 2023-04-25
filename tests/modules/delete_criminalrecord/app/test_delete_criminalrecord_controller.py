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
        assert response.body == "the criminal record with id 1 was deleted"

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