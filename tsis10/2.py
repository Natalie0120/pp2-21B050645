import psycopg2
from psycopg2 import Error
def record_to_db(name,score):
    try:
        connection=psycopg2.connect(user='postgres',password='Prom2021',host='localhost',port='5432',database='postgres')
        cursor=connection.cursor()
        cursor.execute('SELECT EXISTS(select from SCORE where name=%s)',(name,))
        if cursor.fetchone()[0]:
            cursor.execute('UPDATE score SET score=%s where name=%s',(score,name))
            connection.commit()
        else:
            cursor.execute('INSERT INTO score VALUES(%s,%s)',(name,score))
            connection.commit()
    except (Exception,Error) as error:
        print(error)
    finally:
        if connection:
            cursor.close()
            connection.close()