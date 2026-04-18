from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from Part import Part

class PiecePart(Part):
    __tablename__ = "piece_parts"
    
    part_name: Mapped[str] = mapped_column('part_name', 
                                          ForeignKey("parts.name", ondelete="CASCADE"), 
                                          primary_key=True)
    vendor_name: Mapped[str] = mapped_column('vendor_name', 
                                            ForeignKey("vendors.name"), 
                                            nullable=False)

    __mapper_args__ = {"polymorphic_identity": "piece_part"}

    def __init__(self, name: str, number: str, vendor):
        super().__init__(name, number)
        self.vendor_name = vendor.name
    
    def __str__(self):
        return f"{super().__str__()}, Vendor: {self.vendor_name}"