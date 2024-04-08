from dataclasses import dataclass

from sqlalchemy import *
from sqlalchemy.orm import relationship, Mapped, mapped_column

from models.base import Base


@dataclass
class Customer(Base):
    __tablename__ = 'Customer'
    id: Mapped[int] = mapped_column(primary_key=True)
    Name: Mapped[str] = mapped_column()
    Email: Mapped[str] = mapped_column()
    Phone: Mapped[str] = mapped_column()
    TaxNumber: Mapped[str] = mapped_column()
    Address: Mapped["Address"] = relationship(back_populates="Customer")
    Address_id: Mapped[int] = mapped_column(ForeignKey("Address.id"))

    def __repr__(self):
        return f"Customer: Name: {self.Name}, Address: {self.Address}, Phone: {self.Phone}"