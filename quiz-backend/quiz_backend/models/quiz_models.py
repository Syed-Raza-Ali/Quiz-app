from sqlmodel import SQLModel, Field
from typing import Optional

# category means javascript,typescript,python etc

class Category(SQLModel, table = True): 
    category_id : Optional[int] = Field(None,primary_key=True)
    category_name : str
    category_description: str


# level means advance , basic , intermediate etc

class QuizLevel(SQLModel, table=True): 
    quiz_level_id:Optional[int] = Field(None,primary_key=True)
    quiz_level: str
    category_id : int = Field(int, foreign_key= "category.category_id") 

# quiz question / answer

class Quiz(SQLModel, table = True): 
    question_id : Optional[int] = Field(None , primary_key=True)
    question : str     
    quiz_level_id : int = Field(int, foreign_key= "quizlevel.quiz_level_id")

# choices for the questions

class Choices(SQLModel, table = True):
    choice_id : Optional[int] = Field(None, primary_key=True)
    quiz_id : int = Field(int, foreign_key= "quiz.question_id")
    choice : str
    status : bool = False
