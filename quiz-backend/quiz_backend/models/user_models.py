from sqlmodel import SQLModel, Field
from typing import Optional


class LoginModel(SQLModel):
    user_email : str
    user_password : str

class UserModel(LoginModel):
    user_name : str


# user class is used to store user data (user meanse quiz performer)

class User(UserModel, table = True): 
    user_id : Optional[int] = Field(None, primary_key=True)
    # user_name : str
    # user_emal : str
    # TODO:
    # phone_number : int
    # user_password : str


# token for used to user identity 

class Token(SQLModel, table = True):   
    token_id: Optional[int] = Field(None, primary_key=True)
    user_id : int = Field(int, foreign_key="user.user_id")
    refresh_token:str    