import psycopg2

CONNECTION_URI = 'postgresql://habrpguser:pgpwd4habr@127.0.0.1:5432/habrdb'
try:
    with psycopg2.connect(CONNECTION_URI) as conn:
        with conn.cursor() as cursor:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM courses')
            print(cursor.fetchall())
except:
    print('can`t connect to database')
