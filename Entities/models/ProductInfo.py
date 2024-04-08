from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import *
from sqlalchemy.orm import relationship, Mapped, mapped_column

from models.base import Base


@dataclass
class ProductInfo(Base):
    __tablename__ = 'ProductInfo'
    id: Mapped[int] = mapped_column(primary_key=True)
    StoreLocation: Mapped[str] = mapped_column()
    Discount: Mapped[float] = mapped_column()
    Tax: Mapped[float] = mapped_column()
    CommissionRate: Mapped[float] = mapped_column()
    ImgPath: Mapped[str] = mapped_column()
    Description: Mapped[str] = mapped_column()
    DataCreated: Mapped[datetime] = mapped_column()

    ProductId: Mapped[int] = mapped_column(ForeignKey("Product.id"))
    Product: Mapped["Product"] = relationship(back_populates="ProductInfos")

    def __repr__(self):
        return f"id: {self.id}"
