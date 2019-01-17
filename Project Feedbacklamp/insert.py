import psycopg2
from config import config

def insert_deelnemer(studentnr, voornaam, achternaam):
    """"insert een nieuwe deelnemer in de deelnemers tabel"""
    sql = """INSERT INTO deelnemers(studentnr, voornaam, achternaam)
            VALUES(%s, %s, %s);"""
    conn = None
    try:
        # read the database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (studentnr, voornaam, achternaam))
        #commit the changes to the database
        conn.commit()
        #close communication with the datbase
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


insert_deelnemer('1749751', 'youri', 'de vor')