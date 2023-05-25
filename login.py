import mysql.connector

def login(UserID,PassID,dbuser,dbpass):
    cnx = mysql.connector.connect(user=dbuser, password=dbpass,
                              host='127.0.0.1',
                              database='ARTMUSEUM')

    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM USERS WHERE UserId = %s AND PassID = %s', (UserID, PassID,))

    account = cursor.fetchone()

    if (account):
        print("Admin Login Confirmed!\n Welcome!")

        if account[2] == 'admin':
            return "admin"
        elif account[2] == 'user':
            return "user"
        
    else:
        print("wrong Username or password")
