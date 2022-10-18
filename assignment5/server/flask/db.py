import sqlite3
from pathlib import Path

import pandas as pd
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

Path("data.db").touch()

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

petrol_data = pd.read_csv("Petrol Dataset.csv")

petrol_data.to_sql("petrol", connection, if_exists="replace", index=False)

connection.commit()
connection.close()
