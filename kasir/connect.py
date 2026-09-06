import mysql.connector

def hubungkan_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",       
        database="db_kasir"
    )

# db = hubungkan_db()
# if db.is_connected():
#     print("berhasil")