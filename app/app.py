"""API Main"""

from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from sqlmodel import Session, SQLModel

from .db import get_session, engine


SessionDep = Annotated[Session, Depends(get_session)]


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(lifespan=lifespan)

origins = ["localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def home():
    return RedirectResponse("/docs")
