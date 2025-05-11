from datetime import datetime, timedelta, timezone

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from sqlmodel import SQLModel
import secrets
from fastapi.middleware.cors import CORSMiddleware

import jwt
import json



SECRET_KEY = "36ac56154eead93a9b06caf59c0fb3a3bb980923433b7edcfcd2b1a02685fcb7aa273dd322379789348fabd353a706dc0ebe"
print(SECRET_KEY)
ALGORITHM = 'HS256'
ACCESS_EXPIRE_MINUTES = 30

fake_database = {
    "TestUser1":{
        "id": 121,
        "username": "NicolasTesla",
        "fname": "Nicolas",
        "lname": "Tesla",
        "Salary": 45000,
        "hashed_password": "$2b$12$tSSCiO8n8QBHKMH0BteiduBWK7uBcsA9zeYuRZMOv4EwUtjm4mFLa",
    }
}

class Token(SQLModel):
    access_token: str
    token_type: str

class User(SQLModel):
    id: int
    username: str | None = None
    fname: str | None = None
    lname: str | None = None
    Salary: float | None = None

class UserInDb(User):
    hashed_password: str

pwd_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto") # Algorithm to hash or de-hashed the given string.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "token")
app = FastAPI()

def get_user(db, id: int):
    print(f"Check id: {id} in database: {db}")
    for user_data in db.values():
        if user_data["id"] == int(id):
            print(f"found: {user_data}")
            return UserInDb(**user_data)

def authenticateUser(fake_db, id: int, password: str):
    print(f"Authenticate user: {id}, {password}")
    user = get_user(fake_db, id)
    print(f"Got user: {user}")
    if not user:
        return False
    if not pwd_context.verify(password, user.hashed_password):
        return False
    return user

def createAccessToken(data: dict, expire_delta: timedelta | None = None):
    to_encode = data.copy()
    if expire_delta:
        expire = datetime.now(timezone.utc) + expire_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes = 5)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)
    print(f"encoded_jwt: {encoded_jwt}")
    return encoded_jwt

async def getUser(token: str = Depends(oauth2_scheme)):
    credential_excepetions = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Couldn't validate the credentials",
        headers = {"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(f"Decoded payload: {payload}")
        user_id = payload.get("sub")
        if not user_id:
            raise credential_excepetions
    except InvalidTokenError as e:
        print(f"JWT decode error: {str(e)}")
        raise credential_excepetions
    user = get_user(fake_database, int(user_id))
    return user

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/post/")
async def loginForAccessToken(form_data: OAuth2PasswordRequestForm = Depends()) -> Token:
    incorrect_password = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Incorrect user id or password",
        headers = {"WWW-Authenticate": "Bearer"},
    )
    print(f"User ID: {form_data.username}, Password: {form_data.password}")
    user = authenticateUser(fake_database, form_data.username, form_data.password)
    print(f"user is: {user}")
    if not user:
        raise incorrect_password
    access_token_expire = timedelta(minutes = ACCESS_EXPIRE_MINUTES)
    access_token = createAccessToken(data = {"sub": str(user.id)}, expire_delta = access_token_expire)
    return Token(access_token = access_token, token_type = "bearer")


@app.get("/")
async def getUserDetails(current_user: User = Depends(getUser)):
    user_details = {"ID": current_user.id,
             "username": current_user.username,
             "fname": current_user.fname,
             "lname": current_user.lname,
             "Salary": current_user.Salary}
    print(f"user_details = {user_details}")
    return user_details








