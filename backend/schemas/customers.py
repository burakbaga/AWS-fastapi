from pydantic import BaseModel,EmailStr

class CustomerCreate(BaseModel):
    name:str
    lastname:str
    email:EmailStr
    location:str

class ShowCustomer(BaseModel):
    name:str
    lastname:str
    email:EmailStr
    location:str

    class Config():
        orm_mode = True