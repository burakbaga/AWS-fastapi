from typing import List
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from db.crud.customers import create_new_customer,get_all_customers
from db.session import get_db

from schemas.customers import CustomerCreate,ShowCustomer

router = APIRouter()

@router.post("/",response_model=ShowCustomer)
def create_customer(customer:CustomerCreate,db:Session=Depends(get_db)):
    customer = create_new_customer(customer,db)
    return customer

@router.get("/get-all-customer",response_model=List[ShowCustomer])
def get_all(db:Session=Depends(get_db)):
    customers = get_all_customers(db=db)
    return customers
