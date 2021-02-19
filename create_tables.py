from schema import schema
from variables import PG_SCHEMA

def createTables(connection, cursor):
  """
  Создает в БД пустые таблицы согласно схемам
  """
  for table in schema:
    fields = ''
    pkey = ''
    for field in table['fields']:
      if 'pkey' in field:
        pkey = field['name']
      fields = fields + '{name} {type} {restrictions},' \
        .format(name=field['name'], type=field['type'], \
        restrictions=' '.join(field['restrictions']))
    cursor.execute('CREATE TABLE IF NOT EXISTS {schema}.{table} ({fields}, \
      PRIMARY KEY ({pkey}));' \
      .format(schema=PG_SCHEMA, table=table['tablename'], fields=fields[:-1], \
      pkey=pkey))
  connection.commit()