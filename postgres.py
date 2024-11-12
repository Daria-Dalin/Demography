#pip install psycopg2
import psycopg2

try:
    #connection = psycopg2.connect(user="postgres", password="123",
                                  #host="127.0.0.1", port="5432",
                                  #database='lib')
    con = psycopg2.connect(user='postgres', password='123', host='10.10.103.252',
                           port='5432', database='Lib')
    print(con)

    cursor = con.cursor()
    res = cursor.execute("select id from reader;")
    result_set = cursor.fetchall()
    for record in result_set:
        print("Result", record)
    con.close()
except:
    print("error")