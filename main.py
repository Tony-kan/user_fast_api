from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Gender, Role, UserUpdateRequest
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
    for existing_user in db:
        if existing_user.id == user.id:
            raise HTTPException(
                status_code=400,
                detail=f"User with id: {user.id} already exists"
            )
    db.append(user)
    return {"id": user.id}


@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return {"message": "User updated successfully"}
            # db.remove(user)
            # db.append(newUser)
    raise HTTPException(
        status_code=404,
        detail=f"User with id: {user_id} does not exist"
    )


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"message": "User deleted successfully"}
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )
