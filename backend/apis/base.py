from fastapi import APIRouter, applications
from apis.version1 import route_customers

api_router = APIRouter()

api_router.include_router(route_customers.router,prefix="/customer",tags=["customer"])