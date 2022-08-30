
import csv

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine

db=SQLAlchemy()

engine = create_engine('sqlite:///data.db', echo=True)

metadata = MetaData()
# Define the table with sqlalchemy:
petrol = Table('Petrol', metadata,
    Column('id',Integer, primary_key=True),
    Column('Country',String(100)),
    Column('Daily Oil Consumption (Barrels)',Integer),
    Column('World Share',String(20)),
    Column('Yearly Gallons Per Capita',Integer),
    Column('Price Per Gallon (USD)',Integer),
    Column('Price Per Liter (USD)',Integer),
    Column('Price Per Liter (PKR)',Integer),
    Column('GDP Per Capita ( USD )',Integer),
    Column('Gallons GDP Per Capita Can Buy',Integer),
    Column('xTimes Yearly Gallons Per Capita Buy',Integer),
    Column('World Share1',Integer),

)
metadata.create_all(engine)
insert_query = petrol.insert()


with open('Petrol.csv', 'r', encoding="utf-8") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    engine.execute(
        insert_query,
        [{
        "Country": row[0],
        "Daily Oil Consumption (Barrels)": row[1],
        "World Share": row[2],
        "Yearly Gallons Per Capita": row[3],
        "Price Per Gallon (USD)": row[4],
        "Price Per Liter (USD)": row[5],
        "Price Per Liter (PKR)": row[6],
        "GDP Per Capita ( USD )": row[7],
        "Gallons GDP Per Capita Can Buy": row[8],
        "xTimes Yearly Gallons Per Capita Buy": row[9],
        "World Share1": row[10]}
            for row in csv_reader]
    )