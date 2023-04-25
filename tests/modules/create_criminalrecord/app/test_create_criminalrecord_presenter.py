import json
from src.modules.create_criminalrecord.app.create_criminalrecord_presenter import (
    create_criminalrecord_presenter,
)


class Test_UpdateCriminalRecordPresenter:
    def test_update_criminalrecord_presenter(self):
        event = {
            "body": '{"id_criminalrecord": 5, "criminal": {"id_criminal": 4, "name": "lil pump", "description": "he is a rapper", "gender": "MALE", "region_criminal": "USA"}, "crimes": [{"id_crime": 5, "criminal": {"id_criminal": 4, "name": "lil pump", "description": "he is a rapper", "gender": "MALE", "region_criminal": "USA"}, "crime": "MURDER", "region_crime": "ATLANTA", "date": "20-01-2022", "num_victims": 1}], "arrested": true, "score": "ONESTAR"}'
        }

        response = create_criminalrecord_presenter(event, None)

        expected = {
            "criminalrecord": {
                "id_criminalrecord": 5,
                "criminal": {
                    "id_criminal": 4,
                    "name": "lil pump",
                    "description": "he is a rapper",
                    "gender": "MALE",
                    "region_criminal": "USA",
                },
                "crimes": [
                    {
                        "id_crime": 5,
                        "criminal": {
                            "id_criminal": 4,
                            "name": "lil pump",
                            "description": "he is a rapper",
                            "gender": "MALE",
                            "region_criminal": "USA",
                        },
                        "crime": "MURDER",
                        "region_crime": "ATLANTA",
                        "date": "20-01-2022",
                        "num_victims": 1,
                    }
                ],
                "arrested": True,
                "score": "ONESTAR",
            },
            "message": "the criminal record was created",
        }

        assert response["status_code"] == 201
        assert json.loads(response["body"]) == expected

    def test_update_criminalrecord_presenter_missing_id(self):
        event = {
            "body": json.dumps(
                {
                    "criminal": {
                        "id_criminal": 5,
                        "name": "lil pump",
                        "description": "he is a rapper",
                        "gender": "MALE",
                        "region_criminal": "USA",
                    },
                    "crimes": [
                        {
                            "id_crime": 4,
                            "criminal": {
                                "id_criminal": 5,
                                "name": "lil pump",
                                "description": "he is a rapper",
                                "gender": "MALE",
                                "region_criminal": "USA",
                            },
                            "crime": "MURDER",
                            "region_crime": "ATLANTA",
                            "date": "20-01-2022",
                            "num_victims": 1,
                        },
                    ],
                    "arrested": True,
                    "score": "ONESTAR",
                }
            )
        }

        response = create_criminalrecord_presenter(event, None)

        assert response["status_code"] == 400
