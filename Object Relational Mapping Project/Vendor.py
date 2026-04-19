from orm_base import Base
from sqlalchemy import String, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

class Vendor(Base):
    __tablename__ = "vendors"

    name: Mapped[str] = mapped_column('name', String(80), primary_key=True)

    piece_parts: Mapped[List["PiecePart"]] = relationship(
        back_populates="vendor"
    )

    __table_args__ = (
        CheckConstraint("length(name) >= 3", name="vendors_name_min_check"),
    )

    def __init__(self, name: str):
        self.name = name
        
    def __str__(self):
        return f"Vendor: {self.name}"
