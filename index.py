import psycopg2
from variables import *
from create_tables import createTables

try:
  connection = psycopg2.connect('host={host} port={port} dbname={dbname} \
               user={user} password={password}'.format(host=PG_HOST, \
               port=PG_PORT, dbname=PG_DATABASE, user=PG_USER, \
               password=PG_PASSWORD))
except psycopg2.Error as e:
  print(e)

cursor = connection.cursor()
cursor.execute('CREATE SCHEMA IF NOT EXISTS {};'.format(PG_SCHEMA))
connection.commit()

createTables(connection, cursor)