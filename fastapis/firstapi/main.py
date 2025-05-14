from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


# User model
class User(BaseModel):
    id: int
    name: str


# In-memory storage (like a fake database)
users: List[User] = []


# Get all users
@app.get("/users", response_model=List[User])
def get_users():
    return users


# Add a new user
@app.post("/users", response_model=User)
def add_user(user: User):
    # Check if ID already exists
    for u in users:
        if u.id == user.id:
            raise HTTPException(status_code=400, detail="User ID already exists.")
    users.append(user)
    return user


# Update user
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User):
    for index, u in enumerate(users):
        if u.id == user_id:
            users[index] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found.")


# Delete user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for index, u in enumerate(users):
        if u.id == user_id:
            del users[index]
            return {"message": "User deleted successfully."}
    raise HTTPException(status_code=404, detail="User not found.")
