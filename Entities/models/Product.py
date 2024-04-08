from dataclasses import dataclass
from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.ProductInfo import ProductInfo
from models.base import Base
from sqlalchemy import *


@dataclass
class Product(Base):
    __tablename__ = 'Product'
    id: Mapped[int] = mapped_column(primary_key=True)
    ProductName: Mapped[str] = mapped_column()
    MainCategory: Mapped[str] = mapped_column()
    SubCategory: Mapped[str] = mapped_column()
    UuID: Mapped[str] = mapped_column()
    ProductInfos: Mapped[List["ProductInfo"]] = relationship()

    def __repr__(self):
        return f"ProductName: {self.ProductName}"
