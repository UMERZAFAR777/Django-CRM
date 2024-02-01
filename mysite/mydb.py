import mysql.connector


database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'umer2222'
)


cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE company")

print("All DONE!")
















