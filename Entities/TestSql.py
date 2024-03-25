from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models.Address import Address
from models.Customer import Customer
from models.Product import Product
from models.ProductInfo import ProductInfo
from models.Provider import Provider

engine = create_engine("postgresql+psycopg2://postgres:admin@localhost:5432/salesweb")

with Session(engine) as session:
    session.query(Provider).delete()
    session.query(Address).delete()
    session.query(Product).delete()
    session.query(ProductInfo).delete()
    session.commit()

a1 = Address(HouseNr="H1", PostCode="P1", Province="Pr1", Country="C1", Street="S1")
a2 = Address(HouseNr="H2", PostCode="P2", Province="Pr2", Country="C2", Street="S2")
p1 = Provider(Name="P1", TaxNumber="T1", Email="E1", Phone="P1")
p2 = Provider(Name="P2", TaxNumber="T2", Email="E2", Phone="P2")

c1 = Customer(Name="P1", TaxNumber="T1", Email="E1", Phone="P1")
c2 = Customer(Name="P2", TaxNumber="T2", Email="E2", Phone="P2")
p1.Address = a1
p2.Address = a2
c1.Address = a1
c2.Address = a2
with Session(engine) as session:
    session.add(p1)
    session.add(p2)
    session.add(c1)
    session.add(c2)
    session.commit()

with Session(engine) as session:
    providers = session.execute(select(Provider)).all()
    for provider in providers:
        print(provider)

    customers = session.execute(select(Customer)).all()
    for customer in customers:
        print(customer)

