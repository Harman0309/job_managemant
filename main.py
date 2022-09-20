from fastapi import FastAPI

from . import user

app = FastAPI()

app.include_router(user.router)
