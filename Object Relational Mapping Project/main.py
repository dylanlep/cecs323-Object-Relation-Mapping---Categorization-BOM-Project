import logging

from sqlalchemy import select
from sqlalchemy import and_

from db_connection import engine, Session
from orm_base import Base

# Import your new Task 1 classes here. 
# This ensures SQLAlchemy "sees" them and creates the tables.
from Part import Part
from Vendor import Vendor
from Assembly import Assembly
from PiecePart import PiecePart
from AssemblyPart import AssemblyPart

# (You can leave the menu imports here for Task 2, 
# but for Task 1 we just want to create the tables)
from menu_definitions import *

sess = Session

#region Add
def add(sess):
    menu_action = add_menu.menu_prompt()
    exec(menu_action)

def add_piece_part(sess):
    # get info needed to create piece part
    name = input('Enter piece part name: ')
    num = input('Enter piece part number: ')
    vendor = None

    # search for the vendor of the part
    vendor_name = input('Enter vendor name: ')
    result = sess.execute(
        select(Vendor).where(Vendor.name == vendor_name)
    )

    vendor = result.scalars().first()
    
    # if vendor cannot be found, then we cannot create the piece part
    if vendor is None:
        print(f'Vendor with name {vendor_name} could not be found.')
    else:
        sess.add(PiecePart(name, num, vendor))

def add_assembly(sess):
    name = input('Enter assembly name: ')
    num = input('Enter assembly number: ')

    sess.add(Assembly(name, num))

def add_assembly_part(sess):
    component_part = None
    assembly_part = None
    quantity = 0

    # search for the component part
    component_name = input('Enter component name: ')
    result = sess.execute(
        select(Part).where(Part.name == component_name)
    )

    component_part = result.scalars().first()

    if (component_part is None):
        print(f'Component with name {component_name} could not be found.')
        return

    # search for the assembly part
    assembly_name = input('Enter assembly name: ')
    result = sess.execute(
        select(Part).where(Part.name == assembly_name)
    )

    assembly_part = result.scalars().first()

    if (assembly_part is None):
        print(f'Assembly with name {assembly_name} could not be found.')
        return

    # finally, get the quantity, and add it to the table
    quantity = int(input('Enter quantity used: '))

    sess.add(AssemblyPart(assembly_part, component_part, quantity))

def add_vendor(sess):
    name = input('Enter vendor name: ')
    sess.add(Vendor(name))
#endregion

#region Report Data
def report_data(sess):
    menu_action = report_data_menu.menu_prompt()
    exec(menu_action)

def report_data_part(sess):
    # find part
    name = input("Enter part name: ")
    result = sess.execute(
        select(Part).where(Part.name == name)
    )
    part = result.scalars().first()

    # if part could not be found, then we cannot print its data
    if part is None:
        print(f"Part with name {name} could not be found.")

    # otherwise, we print its data
    else:
        print(part)

def report_data_assembly_part(sess):
    # get necessary details to locate assembly part
    assembly_name = input("Enter assembly name: ")
    component_name = input("Enter component name: ")

    # locate assembly part
    result = sess.execute(
        select(AssemblyPart).where(
            and_(
                AssemblyPart.assembly_part_name == assembly_name,
                AssemblyPart.component_part_name == component_name
            )
        )
    )
    assembly_part = result.scalars().first()

    # if matching assembly part cannot be found, then we cannot print its data
    if assembly_part is None:
        print(f"Assembly part with assembly {assembly_name} and component {component_name} could not be found.")

    # otherwise, we print its data
    else:
        print(assembly_part)

def report_data_vendor(sess):
    # get vendor whose data is to be reported
    vendor_name = input('Enter vendor name: ')
    result = sess.execute(
        select(Vendor).where(Vendor.name == vendor_name)
    )

    vendor = result.scalars().first()
    
    # if vendor cannot be found, then we cannot print its data
    if vendor is None:
        print(f"Vendor with name {vendor_name} could not be found.")

    # otherwise, we print its data
    else:
        print(f"{vendor}")
#endregion

#region Delete
def delete(sess):
    menu_action = delete_menu.menu_prompt()
    exec(menu_action)

def delete_part(sess):
    # get part to delete
    name = input("Enter part name: ")
    result = sess.execute(
        select(Part).where(Part.name == name)
    )
    part = result.scalars().first()

    # if part could not be found, then deletion cannot be done
    if part is None:
        print(f"Part with name {name} could not be found.")
        return
    
    # otherwise, let's check if any assembly parts depend on this part; if so,
    # then we once again cannot delete this object
    result = sess.execute(
        select(AssemblyPart).where(AssemblyPart.assembly_part_name == name)
    )

    if result.scalars().first() is not None:
        print(f"Part is the assembly of an assembly part.")
        return
    
    result = sess.execute(
        select(AssemblyPart).where(AssemblyPart.component_part_name == name)
    )

    if result.scalars().first() is not None:
        print("Part is a component of an assembly part.")
        return
    
    # only if we are able to get here do we finally delete the part!
    sess.delete(part)

def delete_assembly_part(sess):
    # look for assembly part
    assembly_name = input("Enter assembly name: ")
    component_name = input("Enter component name: ")

    result = sess.execute(
        select(AssemblyPart).where(
            and_(
                AssemblyPart.assembly_part_name == assembly_name,
                AssemblyPart.component_part_name == component_name
            )
        )
    )
    assembly_part = result.scalars().first()

    # if assembly part could not be found, then no deletion can be done
    if assembly_part is None:
        print(f"Assembly part with assembly {assembly_name} and component {component_name} could not be found.")
    
    # otherwise, perform deletion!
    else:
        sess.delete(assembly_part)

def delete_vendor(sess):
    # get vendor to be deleted
    name = input("Enter vendor name: ")
    result = sess.execute(
        select(Vendor).where(Vendor.name == name)
    )
    vendor = result.scalars().first()

    # if vendor could not be found, then no deletion can be done
    if vendor is None:
        print(f"Vendor with name {name} could not be found.")
        return

    # otherwise, look for piece parts that rely on this vendor
    result = sess.execute(
        select(PiecePart).where(PiecePart.vendor_name == vendor.name)
    )
    dependent_part = result.scalars().first()

    # if any exist, then we cannot delete this vendor!
    if (dependent_part is not None):
        print(f"Piece part with name {dependent_part.name} depends on this vendor.")
        return
    
    # otherwise, delete it
    sess.delete(vendor)
#endregion

#region Update
def update(sess):
    menu_action = update_menu.menu_prompt()
    exec(menu_action)

def update_assembly_part(sess):
    # look for assembly part
    assembly_name = input("Enter assembly name: ")
    component_name = input("Enter component name: ")

    result = sess.execute(
        select(AssemblyPart).where(
            and_(
                AssemblyPart.assembly_part_name == assembly_name,
                AssemblyPart.component_part_name == component_name
            )
        )
    )
    assembly_part = result.scalars().first()

    # if assembly part cannot be found, then modification cannot be made
    if assembly_part is None:
        print(f"Assembly part with assembly {assembly_name} and component {component_name} could not be found.")

    # otherwise, let the user modify the quantity
    else:
        quantity = int(input("Enter new quantity: "))
        assembly_part.quantity = quantity

#endregion

if __name__ == "__main__":
    print("Starting Part Categorization BOM Project...")
    
    # orm_base.py will prompt you for the schema name automatically.
    # Make sure you have run 'CREATE SCHEMA <your_schema_name>;' in Postgres first.
    
    try:
        print("Dropping existing tables...")
        Base.metadata.drop_all(engine)
        
        print("Creating new tables based on Task 1 Mapped Classes...")
        Base.metadata.create_all(engine)
        
        print("-" * 30)
        print("TASK 1 SUCCESSFUL: Tables created in PostgreSQL.")
        print("-" * 30)
        
    except Exception as e:
        print(f"An error occurred during table creation: {e}")

    # For Task 1, we don't need the menu loop yet. 
    # You can exit here, or comment this out until you start Task 2.
    menu_action: str = ''
    while menu_action != menu_main.last_action():
        menu_action = menu_main.menu_prompt()
        exec(menu_action)