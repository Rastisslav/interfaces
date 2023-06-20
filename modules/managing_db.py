import psycopg2
import os


from psycopg2.extras import Json
from dotenv import load_dotenv


load_dotenv()

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')

conn = psycopg2.connect(database=POSTGRES_DB,
                        user=POSTGRES_USER,
                        password=POSTGRES_PASSWORD,
                        host='db',
                        port=POSTGRES_PORT)

cursor = conn.cursor()


def create_db_and_table():

    cursor.execute("DROP TABLE IF EXISTS interfaces")

    sql = '''CREATE TABLE interfaces(id SERIAL PRIMARY KEY,
                                    connection INTEGER,
                                    name VARCHAR(255) NOT NULL,
                                    description VARCHAR(255),
                                    config json,
                                    type VARCHAR(50),
                                    infra_type VARCHAR(50),
                                    port_channel_id INTEGER,
                                    max_frame_size INTEGER)'''
    cursor.execute(sql)


def add_to_table(list):

    for unit in list:
        sql = '''INSERT INTO interfaces(id, 
                                        connection, 
                                        name, 
                                        description, 
                                        config, 
                                        type, 
                                        infra_type, 
                                        port_channel_id,
                                        max_frame_size)
                                            VALUES (%s, 
                                                    %s, 
                                                    %s, 
                                                    %s, 
                                                    %s, 
                                                    %s, 
                                                    %s, 
                                                    %s, 
                                                    %s)'''

        cursor.execute(sql,(unit.id,
                            unit.connection,
                            unit.name,
                            unit.description,
                            Json(unit.config),
                            unit.type,
                            unit.infra_type,
                            unit.port_ide,
                            unit.mtu))


def quit_db():
    conn.commit()
    conn.close()
