from sqlalchemy import create_engine, text
from decouple import config

db_connection_string = "mysql+pymysql://"+config("username")+":"+config("password")+"@"+config("host")+ "/"+ config("database")+"?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

def load_dictionary():
    units_list = {}

    with engine.connect() as conn:
        # Query the units_list table
        query = text("SELECT unit_group, unit_name, unit_value FROM units_list")
        result = conn.execute(query)

        # Populate the units_list dictionary
        for row in result:
            unit_group = row[0]
            unit_name = row[1]
            unit_value = row[2]

            if unit_group not in units_list:
                units_list[unit_group] = {}

            units_list[unit_group][unit_name] = unit_value

    return units_list