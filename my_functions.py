
def database_func(choice):
    import mysql.connector
    try:
        with mysql.connector.connect(
                user=input("Enter username: "),
                password=input("Enter password: "),
                host="localhost"
                ) as connection:
            create_users_db = choice
            with connection.cursor() as cursor:
                cursor.execute(choice)

    except mysql.connector.Error as err:
        print(err)

def database_connect():
    from test import connect_password
    import mysql.connector
    db = mysql.connector.connect(host='localhost', user='root', password=connect_password, database="transport_management_system")
    mycursor = db.cursor()

