-- Created by Redgate Data Modeler (https://datamodeler.redgate-platform.com)
-- Last modification date: 2026-02-28 23:07:12.897

-- tables
-- Table: assemblies
CREATE TABLE assemblies (
    part_name varchar(80)  NOT NULL,
    CONSTRAINT assemblies_pk PRIMARY KEY (part_name)
);

-- Table: assembly_parts
CREATE TABLE assembly_parts (
    assembly_part_name varchar(80)  NOT NULL,
    component_part_name varchar(80)  NOT NULL,
    quantity int  NOT NULL CHECK (quantity >= 1 AND quantity <= 20),
    CONSTRAINT assembly_parts_pk PRIMARY KEY (assembly_part_name,component_part_name)
);

-- Table: parts
CREATE TABLE parts (
    name varchar(80)  NOT NULL CHECK (length(name) >= 3 AND length(name) <= 80),
    number varchar(10)  NOT NULL CHECK (length(number) >= 1 AND length(number) <= 10),
    CONSTRAINT parts_ak_01 UNIQUE (number) NOT DEFERRABLE  INITIALLY IMMEDIATE,
    CONSTRAINT parts_pk PRIMARY KEY (name)
);

-- Table: piece_parts
CREATE TABLE piece_parts (
    part_name varchar(80)  NOT NULL,
    vendor_name varchar(80)  NOT NULL,
    CONSTRAINT piece_parts_pk PRIMARY KEY (part_name)
);

-- Table: vendors
CREATE TABLE vendors (
    name varchar(80)  NOT NULL CHECK (length(name) >= 3 AND length(name) <= 80),
    CONSTRAINT vendors_pk PRIMARY KEY (name)
);

-- foreign keys
-- Reference: assemblies_parts (table: assemblies)
ALTER TABLE assemblies ADD CONSTRAINT assemblies_parts
    FOREIGN KEY (part_name)
    REFERENCES parts (name)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: assembly_parts_assemblies (table: assembly_parts)
ALTER TABLE assembly_parts ADD CONSTRAINT assembly_parts_assemblies
    FOREIGN KEY (assembly_part_name)
    REFERENCES assemblies (part_name)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: assembly_parts_parts (table: assembly_parts)
ALTER TABLE assembly_parts ADD CONSTRAINT assembly_parts_parts
    FOREIGN KEY (component_part_name)
    REFERENCES parts (name)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: piece_parts_parts (table: piece_parts)
ALTER TABLE piece_parts ADD CONSTRAINT piece_parts_parts
    FOREIGN KEY (part_name)
    REFERENCES parts (name)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: piece_parts_vendors (table: piece_parts)
ALTER TABLE piece_parts ADD CONSTRAINT piece_parts_vendors
    FOREIGN KEY (vendor_name)
    REFERENCES vendors (name)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.