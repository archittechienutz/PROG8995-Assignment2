from fastapi import FastAPI, HTTPException
from app.database import SessionLocal, engine
from app.models import Base, User, UserCreate
import logging

Base.metadata.create_all(bind=engine)

logging.basicConfig(
    filename='app/logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)
app = FastAPI()

@app.post("/user")
def create_user(user: UserCreate):
    db = SessionLocal()
    db_user = User(first_name=user.first_name, last_name=user.last_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    logging.info(f"Created user {user.first_name} {user.last_name}")
    return {"id": db_user.id}

@app.get("/user/{user_id}")
def get_user(user_id: int):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    db.close()
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")
