from datetime import datetime

import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from utils import logging
from utils.models import Mood

logger = logging.get_logger(level="INFO", name=__name__)


app = FastAPI()

try:
    db = pd.read_csv("db.csv", sep=";")
except:
    db = pd.DataFrame()


@app.get("/ping")
async def ping():
    status = 200
    if 1:
        status = 200
    else:
        status = 400
    return JSONResponse(status_code=status, content="pong!")


@app.get("/text")
async def text():
    try:
        text = list(db.sample(1)["text"])[0]
        return JSONResponse(status_code=200, content=text)
    except Exception as e:
        return JSONResponse(status_code=500, content=f"Something went wrong: {e}")


@app.post("/mood")
async def mood(request: Mood):
    global db
    try:
        db = pd.concat(
            [
                db,
                pd.DataFrame(
                    {
                        "mood": [request.mood],
                        "text": [request.text],
                        "time": [datetime.now()],
                    }
                ),
            ]
        )
        db.to_csv("db.csv", index=False)
    except ValueError as e:
        error_msg = f"Service failed with error: {e}"
        logger.exception(e)
        raise HTTPException(status_code=400, detail=error_msg)
    except Exception as e:
        error_msg = f"Service failed with error: {e}"
        logger.exception(e)
        raise HTTPException(status_code=500, detail=error_msg)
    response = {"data added": 1}
    return JSONResponse(status_code=200, content=response)


@app.get("/mean")
async def mean():
    try:
        return JSONResponse(status_code=200, content={"mean_mood": db["mood"].mean()})
    except Exception as e:
        return JSONResponse(status_code=500, content=f"Something went wrong: {e}")
