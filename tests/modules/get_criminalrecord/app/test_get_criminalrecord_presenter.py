import json

from src.modules.get_criminalrecord.app.get_criminalrecord_presenter import (
    get_criminalrecord_presenter,
)


class Test_GetCriminalRecordPresenter:
    def test_get_criminalrecord_presenter(self):
        event = {"body": '{"id_criminalrecord": 1}'}

        response = get_criminalrecord_presenter(event, None)

        expected = {
            "criminalrecord": {
                "id_criminalrecord": 1,
                "criminal": {
                    "id_criminal": 1,
                    "name": "Furlan",
                    "description": "Furlan is a Automato",
                    "gender": "MALE",
                    "region_criminal": "Mauá",
                },
                "crimes": [
                    {
                        "id_crime": 1,
                        "criminal": {
                            "id_criminal": 1,
                            "name": "Furlan",
                            "description": "Furlan is a Automato",
                            "gender": "MALE",
                            "region_criminal": "Mauá",
                        },
                        "crime": "MURDER",
                        "region_crime": "Mauá",
                        "date": "20-01-2021",
                        "num_victims": 1,
                    }
                ],
                "arrested": False,
                "score": "ONESTAR",
            },
            "message": "Criminal record was retrieved successfully",
        }

        assert response["status_code"] == 200
        assert json.loads(response["body"]) == expected

    def test_get_criminalrecord_presenter_invalid_id(self):
        event = {"body": '{"id_criminalrecord": 10}'}

        response = get_criminalrecord_presenter(event, None)

        assert response["status_code"] == 404
