from orm_base import Base
from sqlalchemy import ForeignKey, Integer, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

class AssemblyPart(Base):
    __tablename__ = "assembly_parts"
    
    assembly_part_name: Mapped[str] = mapped_column(ForeignKey("assemblies.part_name"), primary_key=True)
    component_part_name: Mapped[str] = mapped_column(ForeignKey("parts.name"), primary_key=True)
    quantity: Mapped[int] = mapped_column('quantity', Integer, nullable=False)

    # Back-references
    assembly: Mapped["Assembly"] = relationship("Assembly", back_populates="categories", foreign_keys=[assembly_part_name])
    component: Mapped["Part"] = relationship("Part", foreign_keys=[component_part_name])

    __table_args__ = (
        CheckConstraint("quantity >= 1 AND quantity <= 20", name="assembly_parts_quantity_range"),
    )

    def __init__(self, assembly, component, quantity: int):
        self.assembly = assembly
        self.component = component
        self.quantity = quantity
    
    def __str__(self):
        return f"Assembly: {self.assembly.name}, Component: {self.component.name}, Quantity: {self.quantity}"