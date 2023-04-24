from fastapi import FastAPI
from src.modules.update_criminalrecord.app.update_criminalrecord_presenter import (
    update_criminalrecord_presenter,
)

app = FastAPI()


@app.post("/update_criminalrecord/")
def update_criminalrecord(data: dict = None):
    event = {"body": {k: str(v) for k, v in data.items()}}

    response = update_criminalrecord_presenter(event, None)
    return response
