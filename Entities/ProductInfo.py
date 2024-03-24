from dataclasses import dataclass

from sqlalchemy import Column, Integer, String, Float, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
@dataclass
class ProductInfo(Base):
    __tablename__ = 'ProductInfo'
    id = Column(Integer, primary_key=True)
    StoreLocation = Column(String)
    Discount = Column(Float)
    Tax = Column(Float)
    CommissionRate = Column(Float)
    ImgPath = Column(String)
    Description = Column(String)
    DataCreated = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"id: {self.id}"