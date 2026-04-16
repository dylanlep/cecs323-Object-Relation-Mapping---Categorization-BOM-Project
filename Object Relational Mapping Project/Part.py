from orm_base import Base
from sqlalchemy import String, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

class Part(Base):
    __tablename__ = "parts"
    
    # We use 'part_type' as the discriminator to tell SQLAlchemy 
    # if a row is an Assembly or a PiecePart.
    name: Mapped[str] = mapped_column('name', String(80), primary_key=True)
    number: Mapped[str] = mapped_column('number', String(10), nullable=False, unique=True)
    part_type: Mapped[str] = mapped_column('part_type', String(20), nullable=False)

    __table_args__ = (
        CheckConstraint("length(name) >= 3", name="parts_name_min_check"),
        CheckConstraint("length(number) >= 1", name="parts_number_min_check"),
    )

    __mapper_args__ = {
        "polymorphic_on": "part_type",
        "polymorphic_identity": "part"
    }

    def __init__(self, name: str, number: str):
        self.name = name
        self.number = number

    def __str__(self):
        return f"Part: {self.name} [#{self.number}]"