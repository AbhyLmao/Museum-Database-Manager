import mysql.connector

def browse(dbuser,dbpass):
    cnx = mysql.connector.connect(user=dbuser, password=dbpass,
                              host='127.0.0.1',
                              database='ARTMUSEUM')

    cursor = cnx.cursor()

    while True:
        print("\n Browse Menu ")

        print("\n(1) show exhibitons")
        print("(2) show collections")
        print("(3) show artists")
        print("(4) See art -")
        print("(0) go back")

        ans = str(input("  ->  "))

        if ans == "1":

            cursor.execute("SELECT * from EXHIBITION;")

            data = cursor.fetchall()
        
            if (data):
                print("\nEXHIBITION NAME ")
                for i in range(0,len(data)):
                    print(i+1,"-",data[i][0])    

        elif ans == "2":

            cursor.execute("SELECT * from COLLECTIONS;")

            data = cursor.fetchall()

            if (data):
                print("\n COLLECTIONS NAME ")
                for i in range(0,len(data)):
                    print(i+1,"-",data[i][0])   
        
        elif ans == "3":

            cursor.execute("SELECT * from ARTIST;")

            data = cursor.fetchall()
        
            if (data):
                print("\n ARTIST NAME ")
                for i in range(0,len(data)):
                    print(i+1,"-",data[i][0]) 

        elif ans =="4":
            
            while True:
                print("\n(1) art by exhibitons")
                print("(2) art by collections")
                print("(3) art by artist")
                print("(4) more details on art by ID")
                print("(0) go back")


                ans2 = str(input("\nhow would you like to see your art  ->  "))

                if ans2 == "1":
                    ename = str(input("Please enter exhibition name  ->  "))
                    cursor.execute("SELECT * from ART_OBJECT where Exibition = %s",(ename,))

                    data=cursor.fetchall()

                    if(data):
                        print("\nArt in the",ename,"Exhibition")

                        for i in range(0,len(data)):
                            print("\n\nArtID =",data[i][0] ,"\nArtName =",data[i][3])
                    
                    else:
                        print("invalid input :(")
                
                elif ans2 == "2":
                    cname = str(input("Please enter Collection name  ->  "))
                    cursor.execute("SELECT * from ART_OBJECT where Collection = %s",(cname,))

                    data=cursor.fetchall()

                    if(data):  

                        print("\nArt in the",cname,"Collection")

                        for i in range(0,len(data)):
                            print("\n\nArtID =",data[i][0] ,"\nArtName =",data[i][3])
                    
                    else:
                        print("invalid input :(")


                elif ans2 == "3":
                    aname = str(input("Please enter Artist name  ->  "))
                    cursor.execute("SELECT * from ART_OBJECT where Artist = %s",(aname,))

                    data=cursor.fetchall()

                    if(data):
                        print("\nArt by",aname)
                        for i in range(0,len(data)):
                            print("\n\nArtID =",data[i][0] ,"\nArtName =",data[i][3])
                    
                    else:
                        print("invalid input :(")

                
                elif ans2 == "4":
                    ArtID = str(input("Please enter ID of art you want more details of ->  "))

                    cursor.execute("SELECT * from ART_OBJECT where ID_no = %s",(ArtID,))

                    data=cursor.fetchone()

                    if(data):
                        print("\nTitle  ->  ", data[3])
                        print("artist  ->  ", data[1])
                        print("description  ->  ", data[4])
                        print("This piece was made in  ->  ", data[2])

                    else:
                        print("invalid input :(")

                    cursor.execute("SELECT * FROM ART_TYPE WHERE ID_no = %s",(ArtID,))
                    data=cursor.fetchone()

                    if data:
                        if(data[1]=="yes"):
                            print("This piece is a Painting")

                            cursor.execute("SELECT * FROM PAINTINGS WHERE ID_no = %s",(ArtID,))
                            data=cursor.fetchone()

                            if data:
                                print("paint type  ->  ", data[1])
                                print("drawn on  ->  ", data[2])
                                print("style  ->  ", data[3])

                        elif(data[2]=="yes"):
                            print("This piece is a Sculpture")
                            cursor.execute("SELECT * FROM SCULPTURES WHERE ID_no = %s",(ArtID,))
                            data=cursor.fetchone()

                            if data:
                                print("material  ->  ", data[1])
                                print("Height  ->  ", data[2],"cm")
                                print("Weight  ->  ", data[3],"Kg")
                                print("style  ->  ", data[4])

                        elif(data[3]=="yes"):
                            print("This piece is a Statue")
                            cursor.execute("SELECT * FROM STATUES WHERE ID_no = %s",(ArtID,))
                            data=cursor.fetchone()

                            if data:
                                print("material  ->  ", data[1])
                                print("Height  ->  ", data[2],"cm")
                                print("Weight  ->  ", data[3],"Kg")
                                print("style  ->  ", data[4])


                        elif(data[4]=="yes"):
                            print("This piece is another form of art")
                            cursor.execute("SELECT * FROM PAINTINGS WHERE ID_no = %s",(ArtID,))
                            data=cursor.fetchone()

                            if data:
                                print("object type  ->  ", data[1])
                                print("style  ->  ", data[2])

                    cursor.execute("SELECT * FROM PERMANANT WHERE ID_no = %s",(ArtID,))
                    data=cursor.fetchone()

                    if data:
                        print("date aquired  ->  ",data[1])
                        print("status  ->  ", data[2])


                    cursor.execute("SELECT * FROM BORROWED WHERE ID_no = %s",(ArtID,))
                    data=cursor.fetchone()

                    if data:
                        print("date Borrowed  ->  ",data[1])
                        print("date Returned  ->  ",data[2])
                

                elif ans2 == "0":
                    break

                else:
                    print("Invalid input")
                
            
        elif ans == "0":
            break

        else:
            print("Invalid input")
        