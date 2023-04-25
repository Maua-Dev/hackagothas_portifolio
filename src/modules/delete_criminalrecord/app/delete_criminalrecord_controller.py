from src.modules.delete_criminalrecord.app.delete_criminalrecord_usecase import (
    DeleteCriminalRecordUsecase,
)
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.helpers.external_interfaces.http_codes import (
    OK,
    BadRequest,
    InternalServerError,
    Forbidden,
)
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.infra.repositories.criminalrecord_repository_mock import (
    CriminalRecordRepositoryMock,
)


class DeleteCriminalRecordController:
    repo = CriminalRecordRepositoryMock()

    def __init__(self, usecase: DeleteCriminalRecordUsecase):
        self.deleteCriminalRecordUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            id_criminalrecord = request.data.get("id_criminalrecord")
            if id_criminalrecord is None:
                raise MissingParameters("id_criminalrecord")

            if self.repo.delete_criminalrecord(id=id_criminalrecord) is None:
                print("AJIHSFGIAUYFBVUHYASVFGJHASVGUFHVAUHFVASYUBVFYSABVFA")
                raise NoItemsFound("id_criminalrecord")

            return OK(
                body=f"the criminal record with id {id_criminalrecord} was deleted"
            )

        except EntityError as err:
            return BadRequest(body=err.message)

        except ForbiddenAction as err:
            return Forbidden(body=err.message)

        except MissingParameters as err:
            print(request.data.get("id_criminalrecord"))
            print(request.data.get("id_criminalrecord") is None)
            print(self.repo.delete_criminalrecord(id=id_criminalrecord) is None)
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
