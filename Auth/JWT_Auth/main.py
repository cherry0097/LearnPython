from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlmodel import SQLModel
from passlib.context import CryptContext

from datetime import timedelta, datetime, timezone
import jwt

import secrets

SECRET_KEY = secrets.token_hex(50)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1

fake_database = {
    "TestUser1":{
        "username": "TestUser1",
        "full_name": "Test User 1",
        "email": "testuser1@gmail.com",
        "hashed_password": "$2b$12$HBV4bE4M89yLaTCYe6JDMeXO5noq8UeQs3HNCrLkYH59sqeBlYlkq",
        "disabled": False,
    },
    "TestUser2":{
        "username": "TestUser2",
        "full_name": "Test User 2",
        "email": "testuser2@gmail.com",
        "hashed_password": "$2b$12$doL5Fp1wERqPoxcIXi85ueImZmI9ufgT3hyD1yu7vNiQ.d24zl6zy",
        "disabled": False,
    },

}

class Token(SQLModel):
    access_token: str
    token_type: str

class TokenData(SQLModel):
    username: str | None = None

class User(SQLModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str



app = FastAPI()
pwd_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    print(f'''[verify_password]I have received a request from authenticate_user function. I will user pwd_context to verify the password: {pwd_context.verify(plain_password, hashed_password)}''')
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db, username: str):
    print(f'''[get_user]I have came from authenticate_user funtion and I will check if {username} present in the database or not?...''')
    if username in db:
        user_dict = db[username]
        print(f'''[get_user]I found the user: {username} on the database and and I am sending a class of with the user details from the database.''')
        return UserInDB(**user_dict)
    
def authenticate_user(fake_db, username: str, password: str):
    print(f'''[authenticate_user]From the post I have came and now I will use get_user function to find the user {username} on the database...''')
    user = get_user(fake_db, username)
    print(f'''[authenticate_user]From the get_user I have received the user "{user}" as a class''')
    if not user:
        return False
    print(f'''[authenticate_user]I am verifying the password using the funtion verify_password({password}, {user.hashed_password})''')
    if not verify_password(password, user.hashed_password):
        return False
    print(f'''[authenticate_user]From verify_password I have received: {verify_password(password, user.hashed_password)}''')
    print(f'''[authenticate_user]I am sending the user class''')
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    print(f'''[create_access_token]Hi, I am create_access_token and I received a request from post???...''')
    to_encode = data.copy()
    print(f'''[create_access_token]Okey I need to encode: {data}. Let's endcode this: {to_encode}''')
    print(f'''[create_access_token]Let me check if the expires_delta is True or False: {expires_delta}''')
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes = 15)
    print(f'''[create_access_token]So, expire is: {expire}''')
    to_encode.update({"exp": expire})
    print(f'''[create_access_token]Let me update the to_encode: {to_encode}''')
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)
    print(f'''[create_access_token]I have encoded the jwt and here is the {encoded_jwt}''')
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    print(f'''[get_current_user] I have recevied an request from get_current_active_user to check the token and return the value.''')
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Couldn't validate the credentials",
        headers = {"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithm = [ALGORITHM])
        print(f'''[get_current_user] So the payload is: {payload}''')
        username = payload.get("sub")
        print(f'''[get_current_user] I have serached "sub" on payload and found: {username}''')
        if username is None:
            raise credentials_exception
        print(f'''[get_current_user] The toke data is a class''')
        token_data = TokenData(username = username)
    except:
        raise credentials_exception
    
    user = get_user(fake_database, username = token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    print(f'''[get_current_active_user] I have received the request for active users from GET. However, I will check get_current_user''')
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> Token:
    print(f'''[POST]We will going to authenticate the user from the detials:
          username: {form_data.username}
          password: {form_data.password} Function authenticate_user is working...''')
    user = authenticate_user(fake_database, form_data.username, form_data.password)
    print(f'''[POST]From authenticate_user we have received the user class''')
    if not user:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Incorrect username or password",
            headers = {"WWW-Authenticate": "Bearer"}
        )
    access_token_expires = timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    print(f'''[POST]We set the time delay:{access_token_expires}''')
    print(f'''[POST]To create the access token we are going to use create_access_token function''')
    access_token = create_access_token(
        data = {"sub": user.username},
        expires_delta = access_token_expires
    )
    print(f'''[POST]We have creared the access token with the time dely: {access_token}''')
    return Token(access_token = access_token, token_type = "bearer")


@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    print(f'''[read_users_me]Okey... You want to know the current user? Let us check the get_current_active_user function''')
    return current_user