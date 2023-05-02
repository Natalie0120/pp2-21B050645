import psycopg2
from config import config

table_name = 'phones'
phone_table = (
    """
    CREATE TABLE phones (
        id serial PRIMARY KEY,
        name VARCHAR (50) NOT NULL,
        phone VARCHAR (50) NOT NULL,
        category VARCHAR (50)
    );
    """
)

conn = None
def init():
    global tables, conn
    try:
        params = config()
        conn = psycopg2.connect(**params)

        # create tables
        cur = conn.cursor()
        cur.execute("select exists(select * from information_schema.tables where table_name=%s)", (table_name,))
        isExists = cur.fetchone()[0]
        cur.close()
        
        if not isExists:
            cur = conn.cursor()
            cur.execute(phone_table)
            cur.close()
            conn.commit()

        print('Connection succesfully!')
    except Exception as e:
        print('Error with connection!')
        print(str(e))
        exit()

def close():
    conn.close()

def get_contacts(filter = False):
    global conn

    condition = ''
    if filter:
        condition = f"WHERE LOWER({filter['type']}) LIKE '%{filter['value']}%'"

    try:
        query = f"SELECT * FROM {table_name} {condition}"
        # get all
        cur = conn.cursor()
        cur.execute(query)
        data = cur.fetchall()
        if len(data) == 0:
            cur.close()
            return False
        else:
            cur.close()
            return data

    except Exception as e:
        print('Error with database!')
        print(str(e))
        exit()

def call_func(str, params):
    cur = conn.cursor()
    cur.callproc(str, params)
    data = cur.fetchall()
    cur.close()
    return data

def call_proc(name, phone):
    cur = conn.cursor()
    cur.execute('call add_contact(%s, %s)', (name, phone))
    conn.commit()
    cur.close()
    return True

def get_by_ID(id):
    global conn
    try:
        query = f"SELECT * FROM {table_name} WHERE id = {id}"
        # get all
        cur = conn.cursor()
        cur.execute(query)
        contact = cur.fetchone()
        return contact

    except Exception as e:
        print('Error with database!')
        print(str(e))
        exit()

def add_contact(data):
    global conn
    try:
        query = f"""
            INSERT INTO {table_name} (name, phone, category)
            VALUES(%s, %s, %s) RETURNING id;
        """
        # get all
        cur = conn.cursor()
        cur.executemany(query, data)
        cur.close()
        conn.commit()
    except Exception as e:
        print('Error with database!')
        print(str(e))
        exit()


def update_contact(id, name, phone, cat):
    global conn
    try:
        query = f"""
        UPDATE {table_name}
        set name = %s,
            phone = %s,
            category = %s
        where id = %s;
        """
        # get all
        cur = conn.cursor()
        cur.execute(query, (name, phone, cat, id))
        cur.close()
        conn.commit()
    except Exception as e:
        print('Error with database!')
        print(str(e))
        exit()

def delete_contact(id):
    global conn
    try:
        query = f"""
        DELETE from {table_name}
        where id = %s;
        """
        # get all
        cur = conn.cursor()
        cur.execute(query, (id,))
        cur.close()
        conn.commit()
    except Exception as e:
        print('Error with database!')
        print(str(e))
        exit()