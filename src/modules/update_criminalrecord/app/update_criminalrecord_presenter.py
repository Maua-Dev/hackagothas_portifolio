from src.modules.update_criminalrecord.app.update_criminalrecord_controller import (
    UpdateCriminalRecordController,
)
from src.modules.update_criminalrecord.app.update_criminalrecord_usecase import (
    UpdateCriminalRecordUsecase,
)
from src.shared.helpers.external_interfaces.http_fastapi_requests import (
    FastAPIHttpRequest,
    FastAPIHttpResponse,
)
from src.shared.infra.repositories.criminalrecord_repository_mock import (
    CriminalRecordRepositoryMock,
)


def update_criminalrecord_presenter(event, context):
    repo = CriminalRecordRepositoryMock()
    usecase = UpdateCriminalRecordUsecase(repo)
    controller = UpdateCriminalRecordController(usecase)

    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        status_code=response.status_code, body=response.body, headers=response.headers
    )
    return httpResponse.to_dict()
