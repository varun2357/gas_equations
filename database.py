from sqlalchemy import create_engine, text
from decouple import config

db_connection_string = "mysql+pymysql://" + config("username") + ":" + config("password") + "@" + config("host") + "/" + config("database") + "?charset=utf8mb4"

engine = create_engine(
    db_connection_string,
    connect_args={"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}},
)


def load_dictionary():
    units_list = {}

    with engine.connect() as conn:
        query = text("SELECT unit_group, unit_name, unit_value FROM units_list")
        result = conn.execute(query)

        for row in result:
            unit_group = row[0]
            unit_name = row[1]
            unit_value = row[2]

            if unit_group not in units_list:
                units_list[unit_group] = {}

            units_list[unit_group][unit_name] = unit_value

    return units_list


def load_conversion_history():
    with engine.connect() as conn:
        query = text("SELECT input1, input2, input3, result, category FROM conversion_history ORDER BY id DESC LIMIT 20")
        result = conn.execute(query)

        history = []
        for row in result:
            entry = {
                'input1': row[0],
                'input2': row[1],
                'input3': row[2],
                'result': row[3],
                'category': row[4]
            }
            history.append(entry)

    return history

def load_size_history():
    with engine.connect() as conn:
        query = text("SELECT sg1, sg2, t1, t2, p1, p2, result, category FROM size_history ORDER BY id DESC LIMIT 20")
        result = conn.execute(query)

        history = []
        for row in result:
            entry = {
                'sg1': row[0],
                'sg2': row[1],
                't1': row[2],
                't2': row[3],
                'p1': row[4],
                'p2': row[5],
                'result': row[6],
                'category': row[7]
            }
            history.append(entry)

    return history

def store_conversion(input1, input2, input3, result, category):
    with engine.connect() as conn:
        # Insert the new conversion record
        query_insert = text("INSERT INTO conversion_history (input1, input2, input3, result, category) VALUES (:input1, :input2, :input3, :result, :category)")
        conn.execute(query_insert, {"input1": input1, "input2": input2, "input3": input3, "result": result, "category": category})

        # Check the total number of rows in the table
        query_count = text("SELECT COUNT(*) FROM conversion_history")
        count = conn.execute(query_count).scalar()

        # Delete oldest records if the table exceeds 40 rows
        if count > 50:
            delete_count = count - 20  # Delete the excess records to keep only 20 rows
            query_delete = text("DELETE FROM conversion_history WHERE id IN (SELECT id FROM (SELECT id FROM conversion_history ORDER BY id ASC LIMIT :delete_count) AS subquery)")
            conn.execute(query_delete, {"delete_count": delete_count})

def store_size(sg1, sg2, t1, t2, p1, p2, result, category):
    with engine.connect() as conn:
        # Insert the new size record
        query_insert = text("INSERT INTO size_history (sg1, sg2, t1, t2, p1, p2, result, category) VALUES (:sg1, :sg2, :t1, :t2, :p1, :p2, :result, :category)")
        conn.execute(query_insert, {"sg1": sg1, "sg2": sg2, "t1": t1, "t2": t2, "p1": p1, "p2": p2, "result": result, "category": category})

        # Check the total number of rows in the table
        query_count = text("SELECT COUNT(*) FROM size_history")
        count = conn.execute(query_count).scalar()

        # Delete oldest records if the table exceeds 40 rows
        if count > 50:
            delete_count = count - 20  # Delete the excess records to keep only 20 rows
            query_delete = text("DELETE FROM size_history WHERE id IN (SELECT id FROM (SELECT id FROM size_history ORDER BY id ASC LIMIT :delete_count) AS subquery)")
            conn.execute(query_delete, {"delete_count": delete_count})