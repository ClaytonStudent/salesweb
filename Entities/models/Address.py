from dataclasses import dataclass

from sqlalchemy import *
from sqlalchemy.orm import relationship, Mapped, mapped_column

from models.base import Base


@dataclass
class Address(Base):
    __tablename__ = 'Address'
    id: Mapped[int] = mapped_column(primary_key=True)
    Street: Mapped[str] = mapped_column()
    HouseNr: Mapped[str] = mapped_column()
    Province: Mapped[str] = mapped_column()
    Country: Mapped[str] = mapped_column()
    PostCode: Mapped[str] = mapped_column()
    Provider: Mapped["Provider"] = relationship(back_populates="Address")
    Customer: Mapped["Customer"] = relationship(back_populates="Address")

    def __repr__(self):
        return f"id: {self.id}"