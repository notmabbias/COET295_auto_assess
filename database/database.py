import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'car_data.db')


def getVehicleID(year, make, model):
    # initialize database connection
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # search db for model and make
    cursor.execute("SELECT vehicle_id FROM Vehicles WHERE model=:model AND make=:make AND year=:year",
                   {'model': model, 'make': make, 'year': year})
    result = cursor.fetchone()

    # print error and return zero on failure
    if (result == None):
        print(f"{year} {make} {model} does not exist in the database.")
        return 0
    # returns as tuple, so store single ID value as int
    vID = result[0]

    conn.close()
    return vID