from src.modules.update_criminalrecord.app.update_criminalrecord_viewmodel import (
    UpdateCriminalRecordViewmodel,
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
    BadRequest,
    Created,
    InternalServerError,
    Forbidden,
)
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.modules.update_criminalrecord.app.update_criminalrecord_usecase import (
    UpdateCriminalRecordUsecase,
)


class UpdateCriminalRecordController:
    def __init__(self, usecase: UpdateCriminalRecordUsecase):
        self.updateCriminalRecordUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.data.get("id_criminalrecord") is None:
                raise MissingParameters("Missing id_criminalrecord")
            if request.data.get("id_criminal") is None:
                raise MissingParameters("Missing id_criminal")
            if request.data.get("name") is None:
                raise MissingParameters("Missing name")
            if request.data.get("description") is None:
                raise MissingParameters("Missing description")
            if request.data.get("gender") is None:
                raise MissingParameters("Missing gender")
            if request.data.get("region_criminal") is None:
                raise MissingParameters("Missing region_criminal")
            if request.data.get("id_crime") is None:
                raise MissingParameters("Missing id_crime")
            if request.data.get("crime") is None:
                raise MissingParameters("Missing crime")
            if request.data.get("region_crime") is None:
                raise MissingParameters("Missing region_crime")
            if request.data.get("date") is None:
                raise MissingParameters("Missing date")
            if request.data.get("num_victims") is None:
                raise MissingParameters("Missing num_victims")
            if request.data.get("arrested") is None:
                raise MissingParameters("Missing arrested")
            if request.data.get("score") is None:
                raise MissingParameters("Missing score")

            if type(request.data.get("crime")) is not str:
                raise EntityError("Invalid crime")
            crimes_types_values = [crime.value for crime in CRIME]
            if request.data.get("crime") not in crimes_types_values:
                raise EntityError("Invalid crime")
            crime_type = CRIME[request.data.get("crime")]

            if type(request.data.get("score")) is not str:
                raise EntityError("Invalid score")
            scores_types_values = [score.value for score in DANGER_SCORE]
            if request.data.get("score") not in scores_types_values:
                raise EntityError("Invalid score")
            score_type = DANGER_SCORE[request.data.get("score")]

            if type(request.data.get("gender")) is not str:
                raise EntityError("Invalid gender")
            genders_types_values = [gender.value for gender in GENDER]
            if request.data.get("gender") not in genders_types_values:
                raise EntityError("Invalid gender")
            gender_types = GENDER[request.data.get("gender")]

            criminal = Criminal(
                id=request.data.get("id_criminal"),
                name=request.data.get("name"),
                description=request.data.get("description"),
                gender=gender_types,
                region=request.data.get("region_criminal"),
            )

            crime = Crime(
                id=request.data.get("id_crime"),
                criminal=criminal,
                crime=crime_type,
                date=request.data.get("date"),
                num_victims=request.data.get("num_victims"),
                region=request.data.get("region_crime"),
            )

            criminalrecord = CriminalRecord(
                id=request.data.get("id_criminalrecord"),
                criminal=criminal,
                crimes=[crime],
                arrested=request.data.get("arrested"),
                score=score_type,
            )

            criminalrecord_response = self.updateCriminalRecordUsecase(
                criminalrecord=criminalrecord
            )
            viewmodel = UpdateCriminalRecordViewmodel(criminalrecord_response)

            return Created(body=viewmodel.to_dict())

        except EntityError as err:
            return BadRequest(body=err.message)

        except ForbiddenAction as err:
            return Forbidden(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
