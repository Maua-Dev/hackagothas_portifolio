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
                raise MissingParameters("id_criminalrecord")
            if request.data.get("criminal") is None:
                raise MissingParameters("criminal")
            if request.data.get("crimes") is None:
                raise MissingParameters("crime")
            if request.data.get("arrested") is None:
                raise MissingParameters("arrested")
            if request.data.get("score") is None:
                raise MissingParameters("score")

            if type(request.data.get("criminal")) is not dict:
                raise EntityError("Invalid criminal")

            criminal = request.data.get("criminal")

            if criminal.get("id_criminal") is None:
                raise MissingParameters("id_criminal")
            if criminal.get("name") is None:
                raise MissingParameters("name")
            if criminal.get("description") is None:
                raise MissingParameters("description")
            if criminal.get("gender") is None:
                raise MissingParameters("gender")
            if criminal.get("region_criminal") is None:
                raise MissingParameters("region_criminal")

            if type(request.data.get("crimes")) is not list:
                raise EntityError("Invalid crimes")

            crimes = request.data.get("crimes")
            crimes_type = [crime_type.value for crime_type in CRIME]
            crimes_entity = []

            for crime in crimes:
                if type(crime) is not dict:
                    raise EntityError("Invalid crimes")
                if crime.get("id_crime") is None:
                    raise MissingParameters("id_crime")
                if crime.get("crime") is None:
                    raise MissingParameters("crime")
                if crime.get("region_crime") is None:
                    raise MissingParameters("region_crime")
                if crime.get("date") is None:
                    raise MissingParameters("date")
                if crime.get("num_victims") is None:
                    raise MissingParameters("num_victims")

                if type(crime.get("crime")) is not str:
                    raise EntityError("Invalid crime")
                if crime.get("crime") not in crimes_type:
                    raise EntityError("Invalid crime")
                crime_type = CRIME[crime.get("crime")]

                if crime.get("criminal") is None:
                    raise MissingParameters("criminal")
                if crime.get("criminal").get("id_criminal") is None:
                    raise MissingParameters("id_criminal")
                if crime.get("criminal").get("name") is None:
                    raise MissingParameters("name")
                if crime.get("criminal").get("description") is None:
                    raise MissingParameters("description")
                if crime.get("criminal").get("gender") is None:
                    raise MissingParameters("gender")
                if crime.get("criminal").get("region_criminal") is None:
                    raise MissingParameters("region_criminal")

                if type(crime.get("criminal").get("gender")) is not str:
                    raise EntityError("Invalid gender")
                if crime.get("criminal").get("gender") not in [
                    gender_entity.value for gender_entity in GENDER
                ]:
                    raise EntityError("Invalid gender")
                gender_entity = GENDER[criminal.get("gender")]

                criminal_entity = Criminal(
                    id=crime.get("criminal").get("id_criminal"),
                    name=crime.get("criminal").get("name"),
                    description=crime.get("criminal").get("description"),
                    region=crime.get("criminal").get("region_criminal"),
                    gender=gender_entity,
                )

                crime_entity = Crime(
                    id=crime.get("id_crime"),
                    criminal=criminal_entity,
                    crime=crime_type,
                    region=crime.get("region_crime"),
                    date=crime.get("date"),
                    num_victims=crime.get("num_victims"),
                )

                crimes_entity.append(crime_entity)

            if type(criminal.get("gender")) is not str:
                raise EntityError("Invalid gender")
            if criminal.get("gender") not in [gender.value for gender in GENDER]:
                raise EntityError("Invalid gender")
            gender = GENDER[criminal.get("gender")]

            if type(request.data.get("score")) is not str:
                raise EntityError("Invalid score")
            scores_types_values = [score.value for score in DANGER_SCORE]
            if request.data.get("score") not in scores_types_values:
                raise EntityError("Invalid score")
            score_type = DANGER_SCORE[request.data.get("score")]

            criminal = Criminal(
                id=criminal.get("id_criminal"),
                name=criminal.get("name"),
                description=criminal.get("description"),
                gender=gender,
                region=criminal.get("region_criminal"),
            )

            criminalrecord = CriminalRecord(
                id=request.data.get("id_criminalrecord"),
                criminal=criminal,
                crimes=crimes_entity,
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
