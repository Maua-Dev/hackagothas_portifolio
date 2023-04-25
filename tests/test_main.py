

import json
import pytest
from src.modules.update_criminalrecord.app.update_criminalrecord_presenter import (
    update_criminalrecord_presenter,
)

def update_criminalrecord(data: dict = None):
    event = {"body": json.dumps({k: v for k, v in data.items()})}

    response = update_criminalrecord_presenter(event, None)
    return response


class Test_Main():
    

    def test_main(self):
        response = update_criminalrecord(data={
        "id_criminalrecord":1,
        "criminal":{
            "id_criminal":1,
            "name":"lil pump",
            "description":"he is a rapper",
            "gender":"MALE",
            "region_criminal":"USA"
        },
        "crimes":[
            {
                "id_crime":1,
                "criminal":{
                    "id_criminal":1,
                    "name":"lil pump",
                    "description":"he is a rapper",
                    "gender":"MALE",
                    "region_criminal":"USA"
                },
                "crime":"MURDER",
                "region_crime":"ATLANTA",
                "date":"20-01-2022",
                "num_victims":1
            }
        ],
        "arrested":True,
        "score":"ONESTAR"
        })
        
        
        assert response["status_code"] == 200
        
    