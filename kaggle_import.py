import csv
import psycopg2

username = 'Bilovodskiy_I'
password = '1234'
database = 'laptops'
host = 'localhost'
port = '5432'


INPUT_CSV_FILE = 'Final_Dataframe.csv'

query_0 = '''
CREATE TABLE new_laptops
(
    brand varchar(40) ,
    laptop_name character varying(40),
    display_size  character varying(40),
    processor_type character varying(40),
    graphics_card character varying(40),
    disk_space character varying(40),
    discount_price character varying(40),
    old_price character varying(40),
    ratings_5max character varying(40)
)
'''

query_1 = '''
DELETE FROM new_laptops
'''

query_2 = '''
INSERT INTO new_laptops ( brand, laptop_name,display_size,processor_type, graphics_card, disk_space, discount_price, old_price, ratings_5max) 
VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s )
'''

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS new_laptops')
    cur.execute(query_0)
    cur.execute(query_1)

    with open(INPUT_CSV_FILE, 'r') as file:
        reader = csv.DictReader(file)
        for idx, row in enumerate(reader):

            values = ( row['brand'], row['laptop_name'],row['display_size'],row['processor_type'], row['graphics_card'], row['disk_space'], row['discount_price'], row['old_price'], row['ratings_5max'])
            cur.execute(query_2, values)

    conn.commit()