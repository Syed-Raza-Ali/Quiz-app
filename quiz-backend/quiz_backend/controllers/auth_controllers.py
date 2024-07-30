from typing import Any
from jose import jwt,JWTError
from passlib.context import CryptContext
from datetime import timedelta
from quiz_backend.utils.types import TokenType
from quiz_backend.setting import algorithm,secret_key


pwd_context = CryptContext(schemes="bcrypt")
# secret_key = "in env"

def generateToken(data : dict, expiry_time : timedelta):
    try:
        to_encode_data = data.copy()
        to_encode_data.update({
            "exp": expiry_time
        })

        token =  jwt.encode(to_encode_data, secret_key ,algorithm=algorithm)
        return token
    except JWTError as je:
        raise je

def decodeToken(token:str):
    try:
        decoded_data = jwt.decode(token, secret_key, algorithm=algorithm)
        return decoded_data
    except JWTError as je:
        raise je

def passwordintoHash(plaintext : str):
    hashedpassword = pwd_context.hash(plaintext)
    return hashedpassword


def verifyPassword(hashPass : str , plainText : str):
    verify_password = pwd_context.verify(plainText , hash=hashPass)
    return verify_password


def generateAccessAndRefreshToken(user_details: dict[str, Any]):
    data = {
        "user_name": user_details["user_name"],
        "user_email": user_details["user_email"]
    }
    access_token = generateToken(data, user_details["access_expiry_time"])
    refresh_token = generateToken(data, user_details["refresh_expiry_time"])
    
    return{
        "access_token": access_token,
        "refresh_token": refresh_token
    }





def tokenService():
    ...
