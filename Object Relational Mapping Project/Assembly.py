from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from Part import Part
from AssemblyPart import AssemblyPart

class Assembly(Part):
    __tablename__ = "assemblies"
    
    part_name: Mapped[str] = mapped_column('part_name', 
                                          ForeignKey("parts.name", ondelete="CASCADE"), 
                                          primary_key=True)
    
    # List of components (The 'children' in the parent-child relationship)
    categories: Mapped[List["AssemblyPart"]] = relationship(
        back_populates="assembly",
        cascade="all, save-update, delete-orphan",
        foreign_keys=[AssemblyPart.assembly_part_name]
    )

    __mapper_args__ = {"polymorphic_identity": "assembly"}

    def __init__(self, name: str, number: str):
        super().__init__(name, number)