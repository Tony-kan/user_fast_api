from fastapi import FastAPI
from typing import List
from models import User, Gender, Role


app = FastAPI()


db: List[User] = [
    User(
        id=uuid4(),
        first_name="Jamila",
        last_name="Ahmed",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=uuid4(),
        first_name="Alex",
        last_name="medai",
        gender=Gender.male,
        roles=[Role.admin]
    ),
    User(
        id=uuid4(),
        first_name="Jones",
        last_name="saint",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]


@app.get("/")
def root():
    return {"Hello": " Fast APi"}
