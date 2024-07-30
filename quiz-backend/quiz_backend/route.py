from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from quiz_backend.db.db_connector import get_session , create_table
from contextlib import asynccontextmanager
from quiz_backend.models.user_models import User
# import quiz_backend.models.admin_models 
import quiz_backend.models.quiz_models
from quiz_backend.utils.imports import NotfoundException, InvalidInputException, ConflictException , Annotated, Depends
 
@asynccontextmanager
async def lifeSpan(app: FastAPI):
    """
    Async context manager to handle application lifespan events.
    
    Args:
        app (FastAPI): The FastAPI application instance
    Yeild:
        None: Nothing is yeilded

    """
    print("create table....")
    create_table()
    yield


app = FastAPI(lifespan=lifeSpan)


@app.exception_handler(NotfoundException)
def not_found(request: Request , exception : NotfoundException):
    return JSONResponse(status_code=404, content=f"{exception.not_found} not found")

@app.exception_handler(ConflictException)
def confict_exeception(request: Request , exception : ConflictException):
    return JSONResponse(status_code=404, content=f"This {exception.conflict_input} already exist !")

@app.exception_handler(InvalidInputException)
def invalid_exeception(request: Request , exception : InvalidInputException):
    return JSONResponse(status_code=404, content=f"This {exception.invalid_input} already exist !")
@app.get('/')
def home():
    return "Welcome to Quiz app project"


@app.post('/api/userSignup')
def userSignup():
    pass


def getUser():
    return  "Raza"
@app.get("/api/user")
def postLogin(getUser : Annotated[str, Depends(getUser)]):
    print(getUser)


# @app.get("/api/getUser")
# def getUser(user : str):
#     """ 
#     Route to  get user details

#     Args:
#         user (str): USer identifier.
#     Returns:
#         str: Success message if user found else raises NotFoundException

#     """

#     if user=="Raza":
#         raise NotfoundException("User")
#     return "user has found"
