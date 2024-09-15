import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "rustamjon1",
    database = "book"
)

cursor = mydb.cursor()
# cursor.execute("select * from book")
# result = cursor.fetchall()
# result = cursor.fetchone()
# result = cursor.fetchmany(5)


# cursor.execute("insert into book values(11,'Shum bola',500,10,1,2,10)")
# # print(result)

# mydb.commit()
# print(cursor.rowcount)
# for i in result:
#     print(i)

cursor.execute("""
                delete from book where id = 11;               
                """)
mydb.commit()
print(cursor.rowcount)

cursor.execute("select * from book")
result = cursor.fetchall()
for i in result:
    print(i)