from .create_criminalrecord_usecase import CreateCriminalRecordUsecase
from .create_criminalrecord_viewmodel import CreateCriminalRecordViewmodel
from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminalrecord import CriminalRecord
from src.shared.domain.enums.crime_enum import CRIME
from src.shared.domain.enums.danger_score_enum import DANGER_SCORE
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction
from src.shared.helpers.external_interfaces.http_codes import BadRequest, Created, Forbidden, InternalServerError
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse

class CreateCriminalRecordController:
    def __init__(self, usecase: CreateCriminalRecordUsecase):
        self.createCriminalRecordUsecase = usecase
        
    def __call__(self, request: HttpRequest) -> HttpResponse:
        try: 
            if request.data.get("criminalrecord_id") == None:
                raise MissingParameters("criminalrecord_id")
            if request.data.get("criminal") == None:
                raise MissingParameters("criminal")
            if request.data.get("crime") == None:
                raise MissingParameters("crime")
            if request.data.get("arrested") == None:
                raise MissingParameters("arrested")
            if request.data.get("score") == None:
                raise MissingParameters("score")
            
            if type(request.data.get("criminal")) is not dict:
                    raise EntityError("criminal of criminal record")
            
            criminal = request.data.get("criminal")

            if criminal.get("criminal_id") is None:
                raise MissingParameters("criminal_id")
            if criminal.get("name") is None:
                raise MissingParameters("name")
            if criminal.get("description") is None:
                raise MissingParameters("description")
            if criminal.get("gender") is None:
                raise MissingParameters("gender")
            if criminal.get("criminal_region") is None:
                raise MissingParameters("criminal_region")
            
            if type(request.data.get("crimes")) is not list:
                raise EntityError("crimes")
            
            crimes = request.data.get("crimes")
            crimes_type = [crime_type.value for crime_type in CRIME]
            crimes_entity = []

            for crime in crimes:
                if type(crime) is not dict:
                    raise EntityError("Invalid crimes")
                if crime.get("crime_id") is None:
                    raise MissingParameters("crime_id")
                if crime.get("crime_type") is None:
                    raise MissingParameters("crime_type")
                if crime.get("crime_region") is None:
                    raise MissingParameters("crime_region")
                if crime.get("date") is None:
                    raise MissingParameters("date")
                if crime.get("num_victims") is None:
                    raise MissingParameters("num_victims")
                
                if type(crime.get("crime")) is not str:
                    raise EntityError("Invalid Crime")
                if crime.get("crime") not in crimes_type:
                    raise EntityError("Invalid Crime")
                crime_type = CRIME[crime.get("crime")]

                if type(crime.get(criminal)) is not dict:
                    raise MissingParameters("criminal of crime")
                
                criminal_inside_crime = crime.get("criminal")

                if criminal_inside_crime is None:
                    raise MissingParameters("criminal")
                if criminal_inside_crime.get("criminal_id") is None:
                    raise MissingParameters("criminal_id")
                if criminal_inside_crime.get("name") is None:
                    raise MissingParameters("name")
                if criminal_inside_crime.get("description") is None:
                    raise MissingParameters("description")
                if criminal_inside_crime.get("gender") is None:
                    raise MissingParameters("gender")
                if criminal_inside_crime.get("criminal_region") is None:
                    raise MissingParameters("criminal_region")
                
                if type(criminal_inside_crime.get("gender")) is not str:
                    raise EntityError("Invalid Gender")
                if criminal_inside_crime.get("gender") not in [gender_entity.value for gender_entity in GENDER]:
                    raise EntityError("Invalid Gender")
                gender_entity = GENDER[criminal.get("gender")]

                criminal_entity = Criminal(
                    id=criminal_inside_crime.get("criminal_id"),
                    name=criminal_inside_crime.get("name"),
                    description=criminal_inside_crime.get("description"),
                    region=criminal_inside_crime.get("criminal_region"),
                    gender=gender_entity,
                )

                crime_entity = Crime(
                    id=crime.get("crime_id"),
                    criminal=dict(criminal_entity),
                    crime=crime_type,
                    region=crime.get("crime_region"),
                    date=crime.get("date"),
                    num_victims=crime.get("num_victims")
                )

                crimes_entity.append(crime_entity)

            if type(criminal.get("gender")) is not str:
                raise EntityError("Invalid Gender")
            if criminal.get("gender") not in [gender.value for gender in GENDER]:
                raise EntityError("Invalid Gender")
            gender = GENDER[criminal.get("gender")]

            if type(request.data.get("score")) is not str:
                raise EntityError("Invalid Score")
            if request.data.get("score") not in [score.value for score in DANGER_SCORE]:
                raise EntityError("Invalid Score")
            score_type = DANGER_SCORE[request.data.get("score")]
                
            criminal = Criminal(
                id=criminal.get("criminal_id"),
                name=criminal.get("name"),
                description=criminal.get("description"),
                gender=gender,
                region=criminal.get("criminal_region")
            )

            criminalrecord = CriminalRecord(
                id=request.data.get("criminalrecord_id"),
                criminal=dict(criminal),
                crimes=crimes_entity,
                arrested=request.data.get("arrested"),
                score=score_type,
            )

            criminalrecord_response = self.createCriminalRecordUsecase(criminalrecord=criminalrecord)
            viewmodel = CreateCriminalRecordViewmodel(criminalrecord_response)

            return Created(body=viewmodel.to_dict)
            
        except EntityError as err:
            return BadRequest(body=err.message)
        
        except ForbiddenAction as err:
            return Forbidden(body=err.message)
        
        except MissingParameters as err:
            return BadRequest(body=err.message)
        
        except Exception as err:
            return InternalServerError(body=err.args[0])