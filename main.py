from fastapi import FastAPI
from typing import List
from models import User, Gender, Role
from uuid import UUID, uuid4


app = FastAPI()


db: List[User] = [
    User(
        id=UUID("afdd0b40-9ae8-41e8-8bca-fae744b3f752"),
        first_name="Jamila",
        last_name="Ahmed",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=UUID("1bfb6d5b-ba02-4703-8895-39968de21e40"),
        first_name="Alex",
        last_name="medai",
        gender=Gender.male,
        roles=[Role.admin]
    ),
    User(
        id=UUID("618738f9-c233-4bbc-926f-17b3e0487945"),
        first_name="Jones",
        last_name="saint",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]


@app.get("/")
def root():
    return {"Hello": " Fast APi"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}
