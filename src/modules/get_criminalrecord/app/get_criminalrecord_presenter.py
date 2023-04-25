from src.modules.get_criminalrecord.app.get_criminalrecord_controller import (
    GetCriminalRecordController,
)
from src.modules.get_criminalrecord.app.get_criminalrecord_usecase import (
    GetCriminalRecordUsecase,
)
from src.shared.helpers.external_interfaces.http_fastapi_requests import (
    FastAPIHttpRequest,
    FastAPIHttpResponse,
)
from src.shared.infra.repositories.criminalrecord_repository_mock import (
    CriminalRecordRepositoryMock,
)


def get_criminalrecord_presenter(event, context):
    repo = CriminalRecordRepositoryMock()
    usecase = GetCriminalRecordUsecase(repo)
    controller = GetCriminalRecordController(usecase)

    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        status_code=response.status_code, body=response.body, headers=response.headers
    )
    return httpResponse.to_dict()
