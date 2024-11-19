# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import pymysql
import pymysql.cursors
import dotenv
import os

TABLE_NAME = "customers"
dotenv.load_dotenv()

connection = pymysql.connect(host=os.environ["MYSQL_HOST"],user=os.environ["MYSQL_USER"],password=os.environ["MYSQL_PASSWORD"],database=os.environ["MYSQL_DATABASE"],charset="utf8mb4",cursorclass=pymysql.cursors.DictCursor)

#No cursorclass use o SScursor caso o banco de dados utilize muitas gigas de dados para mostrar ai é mais facil para mostrar sem utilizar muito memoria




with connection:
    with connection.cursor() as cursor:
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} (id INT NOT NULL AUTO_INCREMENT,nome VARCHAR(50) NOT NULL,idade INT NOT NULL,PRIMARY KEY (id))")

        #CUIDADOS:ISSO APAGA A TABELA
        cursor.execute(f"TRUNCATE TABLE {TABLE_NAME}")
    connection.commit()

    with connection.cursor() as cursor:
        sql = (f"INSERT INTO {TABLE_NAME} (nome,idade) VALUES (%s,%s)")

        result = cursor.execute(sql,("lucas",18))
        #print(result)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (f"INSERT INTO {TABLE_NAME} (nome,idade) VALUES (%(nome)s,%(idade)s)")

        data = {"nome":"bruna","idade":17}

        result = cursor.execute(sql,data)
        #print(result)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (f"INSERT INTO {TABLE_NAME} (nome,idade) VALUES (%(nome)s,%(idade)s)")

        data2 = ({"nome":"jonas","idade":44},{"nome":"mamae","idade":49})

        result = cursor.executemany(sql,data2)
        #print(result)
    connection.commit()

    with connection.cursor() as cursor:
        #menor_id = int(input('digite o menor id: '))
        #maior_id = int(input('digite o maior id: '))
        menor_id = 2
        maior_id = 4
        sql = (f'SELECT * FROM {TABLE_NAME} WHERE id BETWEEN %s AND %s')
        cursor.execute(sql,(menor_id,maior_id))
        #joga numa tupla para ter dados salvos sem esgotar:data5
        data5 = cursor.fetchall()

        #for row in data5:
            #print(row)

    with connection.cursor() as cursor:
        sql = (f'DELETE FROM {TABLE_NAME} WHERE id = %s')

        cursor.execute(sql,(4))
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME}')
        #joga numa tupla para ter dados salvos sem esgotar:data5
        data5 = cursor.fetchall()

        #for row in data5:
            #print(row)

    with connection.cursor() as cursor:
        sql = (f'UPDATE {TABLE_NAME} SET nome=%s,idade=%s WHERE id = %s')

        cursor.execute(sql,("bruno",25,3))
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME}')

        #joga numa tupla para ter dados salvos sem esgotar:data5
        

        #print()
        #print("for 1: ")
        #for row in cursor.fetchall():
            #print(row)

        #print()
        #print("for 2: ")
        #cursor.scroll(1,"absolute")
        #for row in cursor.fetchall():
            #print(row)

    with connection.cursor() as cursor:

        cursor.execute(f"SELECT * FROM {TABLE_NAME} ORDER BY id DESC LIMIT 1")
        lastidfromselect = cursor.fetchone()
        
        result_value = cursor.execute(f'SELECT * FROM {TABLE_NAME}')

        data6 = cursor.fetchall()

        for row in data6:
            print(row)

        print(result_value)
        print(len(data6))
        print(cursor.rowcount)#retorna a contagem da ultima execução
        print(lastidfromselect["id"])
        print(cursor.rownumber)#saber qual linha voce esta no cursor