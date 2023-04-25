from src.modules.get_criminalrecord.app.get_criminalrecord_usecase import GetCriminalRecordUsecase
from src.modules.get_criminalrecord.app.get_criminalrecord_viewmodel import GetCriminalRecordViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, Forbidden
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse


class GetCriminalRecordController:
    def __init__(self, usecase: GetCriminalRecordUsecase):
        self.GetCriminalRecordUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.data.get("id_criminalrecord") is None:
                raise MissingParameters("id_criminalrecord")
            
            criminalrecord = self.GetCriminalRecordUsecase(criminalrecord_id=request.data.get("id_criminalrecord"))

            viewmodel = GetCriminalRecordViewmodel(criminalrecord=criminalrecord)

            response = OK(viewmodel.to_dict())
            
            return response
        
        except EntityError as err:
            return BadRequest(body=err.message)

        except ForbiddenAction as err:
            return Forbidden(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
