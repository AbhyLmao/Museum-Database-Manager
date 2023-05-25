import mysql.connector
import AlterMenu
import BrowseMenu

def AdminMenu(dbuser,dbpass):
    cnx = mysql.connector.connect(user=dbuser, password=dbpass,
                              host='127.0.0.1',
                              database='ARTMUSEUM')

    cursor = cnx.cursor()


    while True:
        print ("\nWhat would you like to do today?")

        print ("\n\n(0) Add Users")
        print ("(1) Delete Users")
        print ("(2) Show Users")
        print ("(3) Alter data")
        print ("(4) Browse data")
        print ("(5) run sql command")
        print ("(6) run sql file")
        print ("(7) Log out")

        ans = str(input("  ->  "))

        if ans == ("0"):
            userid = str(input("enter new UserID  ->  "))
            passid = str(input("enter new PassID  ->  "))
            usertype = str(input("enter new Utype  ->  "))

            cursor.execute("INSERT INTO USERS (UserID, PassID, Utype) VALUES (%s,%s,%s);",(userid,passid,usertype,))

            cnx.commit()
            print("\n\n Done!\n")

        elif ans == "1":
            userid = str(input("enter UserID to delete ->  "))

            cursor.execute("DELETE FROM USERS WHERE UserID = %s ;",(userid,))
            cnx.commit()
            print("\n  ",userid," deleted!")

        elif ans == "2":

            cursor.execute("SELECT * FROM USERS;")
            rows=cursor.fetchall()
    
            # print(rows)
            for row in rows:
                for col in row:
                    print(col,end=' ')
                print()

        elif ans == "3":
            
            AlterMenu.alter(dbuser,dbpass)

        elif ans == "4":

            BrowseMenu.browse(dbuser,dbpass)

        elif ans == "5":
            query = str(input(" -> "))

            cursor.execute(query)
            cnx.commit()

        elif ans == "6":
            fd = open("QUERIES.sql", 'r')
            sqlFile = fd.read()
            fd.close()

            
            sqlCommands = sqlFile.split(';')
            newsqlcommands = []
            
            newnewsql = []

            for subsd in sqlCommands:
                newsqlcommands.append(subsd.replace("\n",""))

            for i in newsqlcommands:
                i = i+";"
                newnewsql.append(i)

            print(newnewsql)
           
            for comand in newnewsql:
                try:
                    cursor.execute(comand)
                
                    data = cursor.fetchall()
                    if(data):
                        for j in range(0,len(data)):
                            print(data[j])

                        print("\n\n\n")
                    else:
                        ("invalid")
                except:
                    print("invalid")

                


        elif ans == "7":
            cnx.close()
            break
            
        else:
            print("not valid :(")


    


