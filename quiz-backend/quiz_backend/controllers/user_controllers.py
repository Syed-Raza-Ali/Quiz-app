from quiz_backend.utils.imports import (User , Token , UserModel, select, Session, passwordintoHash,verifyPassword)
from quiz_backend.utils.exception import ConflictException

def signUp(user_form: UserModel, session : Session):
    users = session.exec(select(User).where(User.user_email == user_form.user_email)).all()
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