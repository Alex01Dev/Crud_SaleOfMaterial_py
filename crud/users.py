import models.user
import schemas.users
from sqlalchemy.orm import Session

def get_users(db: Session, skip: int = 0, limit: int = 0):
    return db.query(models.user.User).offset(skip).limit(limit).all()

def get_user(db: Session, id: int):
    return db.query(models.user.User).filter(models.user.User.id == id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.user.User).filter(models.user.User.email == email).first()


def create_user(db: Session, user: schemas.users.userCreate):
    db_user = get_user_by_email(db, user.email)
    if db_user:
        return None

    new_user = models.user.User(
        name=user.name,
        lastName=user.lastName,
        typeUser=user.typeUser,
        userName=user.userName,
        email=user.email,
        password=user.password,
        phoneNumber=user.phoneNumber,
        status=user.status,
        registrationDate=user.registrationDate,
        updateDate=user.updateDate
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_user(db: Session, id: int, user: schemas.users.userUpdate):
    db_user = db.query(models.user.User).filter(models.user.User.id == id).first()
    if not db_user:
        return None
    
    for key, value in user.dict(exclude_unset=True).items():
        setattr(db_user, key, value)
    
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, id: int):
    db_user = db.query(models.user.User).filter(models.user.User.id == id).first()
    if not db_user:
        return None
    
    db.delete(db_user)
    db.commit()
    return db_user