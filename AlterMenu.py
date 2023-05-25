import mysql.connector

def alter(dbuser,dbpass):
    cnx = mysql.connector.connect(user=dbuser, password=dbpass,
                              host='127.0.0.1',
                              database='ARTMUSEUM')

    cursor = cnx.cursor()
    while True:
        print("\n (0) add exhibition")
        print(" (1) add collection")
        print(" (2) add artist")
        print(" (3) add art")
        print(" (4) delete exhibition")
        print(" (5) delete Collection")
        print(" (6) delete artist")
        print(" (7) delete art")
        print(" (8) Go back")

        ans = str(input("\n  ->  "))

    
        if ans == "0":
            ename = str(input("exibition name ->  "))
            startdate = str (input("start date (YYYY-MM-DD) ->  "))
            enddate = str (input("end date (YYYY-MM-DD) ->  "))


            cursor.execute("INSERT INTO EXHIBITION (Ename, Start_date, End_date) VALUES (%s,%s,%s)",(ename,startdate,enddate,))
            cnx.commit()

        if ans == "1":
            colname = str(input("Collection name ->  "))
            coltype = str(input("Collection type ->  "))
            coldesc = str(input("Collection description ->  "))
            coladdr = str(input("Collection address ->  "))
            colphon = str(input("Collection phonenumber ->  "))
            colperson = str(input("Collection contact person ->  "))
        

            cursor.execute("INSERT INTO COLLECTIONS (Cname, Ctype, Cdescription, Caddress, Cphone, Contact_person) VALUES (%s,%s,%s,%s,%s,%s)",(colname,coltype,coldesc,coladdr,colphon,colperson,))
            cnx.commit()

        if ans == "2":
            aname = str(input("name of artist  ->  "))
            dateborn = str (input("start year (YYYY) ->  "))
            datedied = str (input("death year (YYYY) ->  "))
            country = str(input("Country of artist  ->  "))
            description = str(input("description of artist  ->  "))
            Epoch = str(input("Epoch of artist  ->  "))
            style = str(input("style of artist  ->  "))

            cursor.execute("INSERT INTO ARTIST (Aname,Date_born,Date_died,Country_of_origin,Cdescription,Epoch,Main_style) VALUES (%s,%s,%s,%s,%s,%s,%s)",(aname,dateborn,datedied,country,description,Epoch,style,))
            cnx.commit()

        if ans == "3":
            idnum = str(input("ID of art Object  ->"))
            artist = str(input("artist of art Object(must be same as artist name)  ->"))
            artyear = str(input("year of art Object  ->"))
            title = str(input("Title of art Object  ->"))
            adescription = str(input("description of art Object  ->"))
            origin = str(input("origin of art Object  ->"))
            Epoch = str(input("Epoch of art  ->  "))
            collection = str(input("collection of art ('NA' if none, must be same as collection name) ->  "))
            exhibition = str(input("exhibition of art ('NA' if none, must be same as exhibition name) ->  "))

            cursor.execute("INSERT INTO ART_OBJECT (ID_no, Artist, Artyear, Title, Cdescription, origin, Epoch, Collection, Exibition) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(idnum,artist,artyear,title,adescription,origin,Epoch,collection,exhibition,))
            cnx.commit()

            while(True):
                print("Is this a \n(1)painting \n(2)sculpture \n(4)Statue \n(4)other")

                ans2 = str(input("  ->  "))

                if ans2 == "1":
                    paint_type = str(input("\npaint type of art  ->  "))
                    drawn_on = str(input("drawn_on  ->  "))
                    style = str(input("style of art  ->"))


                    cursor.execute("INSERT INTO PAINTINGS (ID_no, Paint_type, Drawn_on, Style) VALUES (%s,%s,%s,%s)", (idnum,paint_type,drawn_on,style,))
                
                    cursor.execute('INSERT INTO ART_TYPE (ID_no, Painting, Sculpture, Statue, Other) VALUES (%s,%s,%s,%s,%s)',(idnum,'yes','no','no','no'))

                    cnx.commit()
                    break
            
                if ans2 == "2":
                    matireal = str(input("material of sculpture  ->  "))
                    height = str(input("height  ->  "))
                    weight = str(input("weight  ->  "))
                    style = str(input("style of art  ->"))


                    cursor.execute("INSERT INTO SCULPTURES (ID_no, Material, Height, Weight, Style) VALUES (%s,%s,%s,%s,%s)", (idnum,matireal,height,weight,style,))
                
                    cursor.execute('INSERT INTO ART_TYPE (ID_no, Painting, Sculpture, Statue, Other) VALUES (%s,%s,%s,%s,%s)',(idnum,'no','yes','no','no'))

                    cnx.commit()
                    break

                if ans2 == "3":
                    matireal = str(input("material of statue  ->  "))
                    height = str(input("height  ->  "))
                    weight = str(input("weight  ->  "))
                    style = str(input("style of art  ->"))


                    cursor.execute("INSERT INTO STATUES (ID_no, Material, Height, Weight, Style) VALUES (%s,%s,%s,%s,%s)", (idnum,matireal,height,weight,style,))
                
                    cursor.execute('INSERT INTO ART_TYPE (ID_no, Painting, Sculpture, Statue, Other) VALUES (%s,%s,%s,%s,%s)',(idnum,'no','no','yes','no'))

                    cnx.commit()
                    break

                if ans2 == "4":
                    o_type = str(input("type of art  ->  "))
                    style = str(input("style of art  ->"))


                    cursor.execute("INSERT INTO OTHER (ID_no, Otype, Style) VALUES (%s,%s,%s)", (idnum,o_type,style,))
                
                    cursor.execute('INSERT INTO ART_TYPE (ID_no, Painting, Sculpture, Statue, Other) VALUES (%s,%s,%s,%s,%s)',(idnum,'no','no','no','yes'))

                    cnx.commit()
                    break

                else:

                    print("\nPlease choose correct option")

            while True:
                print("\n Is this a (1)permanant piece\n(2)borrowed piece")

                ans3 = str(input("\n  ->  "))

                if ans3 == "1":
                    date_aquired = str(input("Date Of Aquiry (YYYY-MM-DD)  ->  "))
                    Pstatus = str(input("Status of object  ->  "))
                
                    cursor.execute("INSERT INTO PERMANANT (ID_no, Date_acquired, PStatus) VALUES (%s,%s,%s)", (idnum, date_aquired, Pstatus,))
                    cnx.commit()
                    break
            
                if ans3 == "2":
                    date_borrowed = str(input("Date Of borrow (YYYY-MM-DD)  ->  "))
                    date_returned = str(input("Date Of return (YYYY-MM-DD)  ->  "))
                
                    cursor.execute("INSERT INTO BORROWED (ID_no, Date_Borrowed, Date_Returned) VALUES (%s,%s,%s)", (idnum, date_borrowed,date_returned,))
                    cnx.commit()
                    break

                else:

                    print("\nPlease choose correct option")


        if ans == "4":
            ename = str(input("exibition name to delete ->  "))

            cursor.execute("DELETE FROM EXHIBITION, WHERE EName = %s",(ename,))

            cnx.commit()

        if ans == "5":
            cname = str(input("Collection name to delete ->  "))

            cursor.execute("DELETE FROM COLLECTIONS, WHERE CName = %s",(cname,))

            cnx.commit()

        if ans == "6":
            aname = str(input("artist name to delete ->  "))

            cursor.execute("DELETE FROM ARTIST, WHERE AName = %s",(aname,))

            cnx.commit()
        
        if ans == "7":
            artid = str(input("art id to delete ->  "))

            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute("DELETE FROM ART_TYPE WHERE ID_no = %s;",(artid,))
            cursor.execute("DELETE FROM PERMANANT WHERE ID_no = %s;",(artid,))
            cursor.execute("DELETE FROM art_object WHERE ID_no = %s;",(artid,))
            cursor.execute("SET FOREIGN_KEY_CHECKS=1;")

            cnx.commit()
        
        if ans == "8":
            break

        else:
            
            print("\nPlease choose correct option")
