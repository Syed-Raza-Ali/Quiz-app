from jose import jwt,JWTError
from passlib.context import CryptContext
from datetime import timedelta
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
         

def passwordintoHash(plaintext : str):
    hashedpassword = pwd_context.hash(plaintext)
    return hashedpassword


def verifyPassword(hashPass : str , plainText : str):
    verify_password = pwd_context.verify(plainText , hash=hashPass)
    return verify_password


def tokenService():
    ...
