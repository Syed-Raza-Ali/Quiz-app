from quiz_backend.setting import access_expiry_time, refresh_expiry_time
from quiz_backend.utils.imports import (
    User , Token , UserModel, LoginModel, select, Session, passwordintoHash,verifyPassword , generateToken, decodeToken, ConflictException, InvalidInputException, NotfoundException, Annotated, Depends  )
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from quiz_backend.controllers.auth_controllers import generateAccessAndRefreshToken



# Schmea for token 
auth_schema = OAuth2PasswordBearer(tokenUrl="")


# this signUP function is validate user and generate access and refresh tokens
def signUp(user_form: UserModel, session : Session):
    users = session.exec(select(User))
    hashed_password = passwordintoHash(user_form.user_password)

    for user in users :
        is_email_exist = user.user_email == user_form.user_email
        is_password_exist = verifyPassword(user.user_password, user_form.user_password) 
        if is_email_exist and is_password_exist :
            raise ConflictException("email and password")
        elif is_email_exist :
            raise ConflictException("email")
        elif is_password_exist :
            raise ConflictException("password")
     
    user = User(user_name=user_form.user_name, user_email=user_form.user_email,user_password=hashed_password)
    session.add(user)
    session.commit()    
    session.refresh(user)

    # TODO: generate access token and refresh token
          
    data = {
        "user_name" : user.user_name,
        "user_email" : user.user_email,
        "access_expiry_time" : access_expiry_time,
        "refresh_expiry_time" : refresh_expiry_time
    }
    # access_token = generateToken(data=data , expiry_time=access_expiry_time)
    # refresh_token = generateToken(data=data , expiry_time=refresh_expiry_time)
    
    token_data = generateAccessAndRefreshToken(data)
    token = Token(user_id=user.user_id ,refresh_token=token_data["refresh_token"],)
    session.add(token)
    session.commit()
    return token_data

 
def login(login_form : OAuth2PasswordRequestForm, session: Session):
    users = session.exec(select(User))
    for user in users:
        user_email = user.user_email
        verify_password = verifyPassword(user.user_password, login_form.password)
        if user_email == login_form.username and verify_password :
                     data = {
                "user_name" : user.user_name,
                "user_email" : user.user_email,
                "access_expiry_time" : access_expiry_time,
                "refresh_expiry_time" : refresh_expiry_time
            }
                    #  access_token = generateToken(data=data , expiry_time=access_expiry_time)
                    #  refresh_token = generateToken(data=data , expiry_time=refresh_expiry_time)
                    
                     token_data = generateAccessAndRefreshToken(data)
                     token = session.exec(select(Token).where(Token.user_id == user.user_id)).one()
                     token.refresh_token = token_data["refresh_token"]
                     session.add(token)
                     session.commit()
                     session.refresh(token)
                     return token_data
                    
        else:
             raise InvalidInputException("Email or password")
        



def getUser(token : Annotated[str, Depends(auth_schema)], session: Session):
    try:
        if token:
            data = decodeToken(token)
            user_email = data['user_email']
            user = session.exec(select(User).where(User.user_email == user_email)).one()
            return user
    except :
         raise NotfoundException("Token")

          

















