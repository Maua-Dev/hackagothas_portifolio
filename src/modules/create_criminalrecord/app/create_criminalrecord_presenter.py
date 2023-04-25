from src.modules.create_criminalrecord.app.create_criminalrecord_controller import (
    CreateCriminalRecordController,
)
from src.modules.create_criminalrecord.app.create_criminalrecord_usecase import (
    CreateCriminalRecordUsecase,
)
from src.shared.helpers.external_interfaces.http_fastapi_requests import (
    FastAPIHttpRequest,
    FastAPIHttpResponse,
)
from src.shared.infra.repositories.criminalrecord_repository_mock import (
    CriminalRecordRepositoryMock,
)


def create_criminalrecord_presenter(event, context):
    repo = CriminalRecordRepositoryMock()
    usecase = CreateCriminalRecordUsecase(repo)
    controller = CreateCriminalRecordController(usecase)

    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        status_code=response.status_code, body=response.body, headers=response.headers
    )
    return httpResponse.to_dict()
