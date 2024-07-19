from quiz_backend.utils.imports import (User , Token , UserModel, select, Session, passwordintoHash)


def signUp(user_form: UserModel, session : Session):
    # TODO: verify id user is already exist
    user_exist = session.exec(select(User).where(User.user_email == user_form.user_email)).all()
    
    hashed_password = passwordintoHash(user_form.user_password)
    user = User(user_name=user_form.user_name, user_email=user_form.user_email,user_password=hashed_password)
    session.add(user)
    session.commit()    
    session.refresh(user)

    # TODO: generate access token and refresh token     