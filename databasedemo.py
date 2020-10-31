import psycopg2
connection = psycopg2.connect('dbname=postgres user=postgres password=20loves12')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE table3 (
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')

cursor.execute('INSERT INTO table3 (id, completed) VALUES (1,true);')
connection.commit()

connection.close()
cursor.close()
