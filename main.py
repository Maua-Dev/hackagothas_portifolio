import json
from fastapi import FastAPI
from src.modules.get_criminalrecord.app.get_criminalrecord_presenter import (
    get_criminalrecord_presenter,
)
from src.modules.update_criminalrecord.app.update_criminalrecord_presenter import (
    update_criminalrecord_presenter,
)

from src.modules.create_criminalrecord.app.create_criminalrecord_presenter import (
    create_criminalrecord_presenter,
)

app = FastAPI()


@app.post("/update_criminalrecord/")
def update_criminalrecord(data: dict = None):
    event = {"body": json.dumps({k: v for k, v in data.items()})}

    response = update_criminalrecord_presenter(event, None)
    return response


@app.post("/create_criminalrecord/")
def create_criminalrecord(data: dict = None):
    event = {"body": json.dumps({k: v for k, v in data.items()})}

    response = create_criminalrecord_presenter(event, None)
    return response


@app.get("/get_criminalrecord/")
def get_criminalrecord(id_criminalrecord=None):
    request = {
        "body": {},
        "headers": {},
        "query_params": {"id_criminalrecord": int(id_criminalrecord)},
    }
    response = get_criminalrecord_presenter(request, None)
    return response
