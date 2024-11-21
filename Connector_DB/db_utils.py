"""Have db_utils file and use exception handling -
Python database file: connecting to a database,
executing queries, and handling transactions"""
#connects sql to python
import mysql.connector
from config import USER, PASSWORD, HOST, db_name

class DbConnectionError(Exception):
    pass

#(mysql.connector)
def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx

# JSON handling functions

def get_all_items():
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """SELECT * FROM sprite"""
        cur.execute(query)
        result = cur.fetchall()  # this is a list with db records where each record is a tuple

        return result

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
#gets a list of all the deserts from the deser_menu sql file

def delete_items_by_id(id):
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        del_query = """DELETE FROM sprite WHERE sprite_id = {}""".format(id)
        cur.execute(del_query)

        db_connection.commit()  # IMPORTANT!!! Commit the transaction to apply the deletion

        # you can leave little messages for yourself and debugging like this
        print(f"Record with dessert_id {id} deleted successfully.")

        # NOTE - I've added this so I can return the remaining students back to my API
        # I don't need to do this but this is something that I've decided my app does
        select_query = "SELECT * FROM desert_menu"
        cur.execute(select_query)
        remaining_records = cur.fetchall()  # Get all remaining records

        return remaining_records


    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
def add_new_item(sprite_id, name, damage, health):
    try:
        db_name = 'game_init'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """
            UPDATE  spriteu
            WHERE name = '{name}'
            """.format(sprite_id=sprite_id, name=name, damage=damage, health=health)
        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

if __name__ == "__main__":
    # print("TESTING DB CONNECTION")
    get_all_items()
    # gets all desserts
    delete_items_by_id(2)
    #deletes menu item
    add_new_item(()
    #adds a new dessert item
