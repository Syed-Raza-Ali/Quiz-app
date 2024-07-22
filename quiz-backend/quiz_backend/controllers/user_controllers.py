from quiz_backend.setting import access_expiry_time, refresh_expiry_time
from quiz_backend.utils.imports import (
    User , Token , UserModel, LoginModel, select, Session, passwordintoHash,verifyPassword , generateToken , ConflictException, InvalidInputException)


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
    #      
    data = {
        "user_name" : user.user_name,
        "user_email" : user.user_email
    }
    access_token = generateToken(data=data , expiry_time=access_expiry_time)
    refresh_token = generateToken(data=data , expiry_time=refresh_expiry_time)
    token = Token(refresh_token=refresh_token)
    session.add(token)
    session.commit()
    return {
        "access_token":access_token,
        "refresh_token":refresh_token
    }


def login(login_form : LoginModel, session: Session):
    users = session.exec(select(User))
    for user in users:
        user_email = user.user_email
        verify_password = verifyPassword(user.user_password, login_form.user_password)
        if user_email == login_form.user_email and verify_password :
                     data = {
                "user_name" : user.user_name,
                "user_email" : user.user_email
            }
                     access_token = generateToken(data=data , expiry_time=access_expiry_time)
                     refresh_token = generateToken(data=data , expiry_time=refresh_expiry_time)
                     token = Token(refresh_token=refresh_token)
                     session.add(token)
                     session.commit()
                     session.refresh(token)
                     return {
                        "access_token":access_token,
                        "refresh_token":refresh_token
                    }
                    
        else:
             raise InvalidInputException("Email or password")
