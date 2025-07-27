# 1)Create a new database with a table named Roster that has three fields: Name, Species, and Age. The Name and Species columns should be text fields, and the Age column should be an integer field.

import sqlite3

create_table = """
    Create table Roster(
    Name TEXT,
    Species TEXT,
    age INT
    );
"""


with sqlite3.connect("new_database.db") as conn:
    cur = conn.cursor()
    cur.execute(create_table)

# 2)Populate your new table with the following values:
import sqlite3
# Name	Species	Age
# Benjamin Sisko	Human	40
# Jadzia Dax	Trill	300
# Kira Nerys	Bajoran	29

query_script = (
    ('Benjamin Sisko','Human', 40),
    ('Jadzia Dax','Trill', 300),
    ('Kira Nerys','Bajoran',29)
)

with sqlite3.connect("new_database.db") as conn:
    cur = conn.cursor()
    cur.executemany("Insert into Roster values (?,?,?)", query_script)


# 3)Update the Name of Jadzia Dax to be Ezri Dax

import sqlite3

with sqlite3.connect("new_database.db") as conn:
    cur = conn.cursor()
    cur.execute("Update Roster Set  name = ? where species = ? and age = ?", ("Ezri Dax", "Trill", 300))

# 4)Display the Name and Age of everyone in the table classified as Bajoran.

import sqlite3

with sqlite3.connect("new_database.db") as conn:
    cur = conn.cursor()
    data = cur.execute("Select * from Roster where Species = 'Bajoran'")

print(data.fetchall())
