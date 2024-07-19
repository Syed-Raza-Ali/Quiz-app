from jose import jwt,JWTError
from passlib.context import CryptContext
from datetime import timedelta
from quiz_backend.setting import algorithm,secret_key


pwd_context = CryptContext(schemes="bcrypt")
secret_key = "417242608b7b26062c4a07efc0aca5772d7f80181a8e1144c3bae953049e"

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


def verifyPassword():
    ...


def tokenService():
    ...
