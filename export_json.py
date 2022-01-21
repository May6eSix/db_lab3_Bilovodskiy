import json
import psycopg2

username = 'Bilovodskiy_I'
password = '1234'
database = 'laptops'
host = 'localhost'
port = '5432'


TABLES = [
    'laptop',
    'cpu',
    'gpu',
    'os'
]

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

data = {}
with conn:
    cur = conn.cursor()

    for table_name in TABLES:
        cur.execute('SELECT * FROM ' + table_name)
        rows = []
        fields = [x[0] for x in cur.description]

        for row in cur:
            rows.append(dict(zip(fields, row)))

        data[table_name] = rows

with open('all_data.json', 'w') as outf:
    json.dump(data, outf, default=str)