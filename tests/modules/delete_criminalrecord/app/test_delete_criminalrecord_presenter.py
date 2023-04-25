import json
from src.modules.delete_criminalrecord.app.delete_criminalrecord_presenter import (
    delete_criminalrecord_presenter,
)


class Test_DeleteCriminalRecordPresenter:
    def test_delete_criminalrecord_presenter(self):
        event = {"body": '{"id_criminalrecord": 1}'}

        response = delete_criminalrecord_presenter(event, None)

        expected = "the criminal record with id 1 was deleted"

        assert response["status_code"] == 200
        assert json.loads(response["body"]) == expected

    def test_update_criminalrecord_presenter_invalid_id(self):
        event = {"body": '{"id_criminalrecord": 10}'}

        response = delete_criminalrecord_presenter(event, None)

        assert response["status_code"] == 404
