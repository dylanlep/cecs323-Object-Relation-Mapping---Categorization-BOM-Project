import logging
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
from menu_definitions import menu_main

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