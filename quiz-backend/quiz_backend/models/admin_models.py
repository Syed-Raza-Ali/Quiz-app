from typing import Optional
from sqlmodel import SQLModel, Field

# admin classused to store admin data

class Admin(SQLModel, table = True): 
    admin_id : Optional[int] = Field(None, primary_key=True)
    admin_email : str
    admin_name : str
    admin_password : str