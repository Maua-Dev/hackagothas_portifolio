from src.modules.delete_criminalrecord.app.delete_criminalrecord_controller import (
    DeleteCriminalRecordController,
)
from src.modules.delete_criminalrecord.app.delete_criminalrecord_usecase import (
    DeleteCriminalRecordUsecase,
)
from src.shared.helpers.external_interfaces.http_fastapi_requests import (
    FastAPIHttpRequest,
    FastAPIHttpResponse,
)
from src.shared.infra.repositories.criminalrecord_repository_mock import (
    CriminalRecordRepositoryMock,
)


def delete_criminalrecord_presenter(event, context):
    repo = CriminalRecordRepositoryMock()
    usecase = DeleteCriminalRecordUsecase(repo)
    controller = DeleteCriminalRecordController(usecase)

    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        status_code=response.status_code, body=response.body, headers=response.headers
    )
    return httpResponse.to_dict()
