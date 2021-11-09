from sqlalchemy.orm.session import Session
from db.models.customers import Customer
from schemas.customers import CustomerCreate

def create_new_customer(customer:CustomerCreate,db:Session):
    customer = Customer(name=customer.name,
                        lastname=customer.lastname,
                        email=customer.email,
                        location=customer.location)
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer
    
def get_all_customers(db:Session):
    customers = db.query(Customer).all()
    return customers