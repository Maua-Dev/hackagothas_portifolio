from src.modules.delete_criminalrecord.app.delete_criminalrecord_usecase import (
    DeleteCriminalRecordUsecase,
)
from src.modules.delete_criminalrecord.app.delete_criminalrecord_viewmodel import (
    DeleteCriminalRecordViewmodel,
)
from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminalrecord import CriminalRecord
from src.shared.domain.enums.crime_enum import CRIME
from src.shared.domain.enums.danger_score_enum import DANGER_SCORE
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction
from src.shared.helpers.external_interfaces.http_codes import (
    OK,
    BadRequest,
    InternalServerError,
    Forbidden,
)
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse
from src.shared.helpers.errors.controller_errors import MissingParameters


class DeleteCriminalRecordController:
    def __init__(self, usecase: DeleteCriminalRecordUsecase):
        self.deleteCriminalRecordUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.data.get("id_criminalrecord") is None:
                raise MissingParameters("id_criminalrecord")

            criminalrecord_response = self.deleteCriminalRecordUsecase(
                id=request.data.get("id_criminalrecord")
            )
            viewmodel = DeleteCriminalRecordViewmodel(criminalrecord_response)

            return OK(body=viewmodel.to_dict())

        except EntityError as err:
            return BadRequest(body=err.message)

        except ForbiddenAction as err:
            return Forbidden(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
