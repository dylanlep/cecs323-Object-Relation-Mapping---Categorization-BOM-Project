import logging
from sqlalchemy import select

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
    pass

def add_vendor(sess):
    name = input('Enter vendor name: ')
    sess.add(Vendor(name))

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