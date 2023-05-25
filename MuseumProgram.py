import mysql.connector
import login
import AdminMenu
import AlterMenu
import BrowseMenu

def main():
    ids=str(input("database user ID - "))
    password = str(input("database user password - "))
    print("\n\nWELCOME TO ART MUSEUM allinone PROGRAM")
    print("-----------------------------------------------")
    print("\n\nPlease login or select Guest option")
    while(True):
        print("\n(0) User Login")
        print("(1) Guest Login")
        print("(2) Exit")
        ans = str(input("\n  ->  "))

        if ans == "0":
            userid = str(input("\nenter username = "))
            passid = str(input("\nenter password = "))

            usertype = login.login(userid,passid,ids,password)

            if usertype == "admin":
                AdminMenu.AdminMenu(ids,password)

            if usertype == "user":
                while True:
                    ans = str(input("\n(1)alter menu\n(2)Browse menu \n  ->  "))
                    
                    if ans == "1":
                        AlterMenu.alter(ids,password)
                    elif ans =="2":
                        BrowseMenu.browse(ids,password)
                    else:
                        print("Invalid option :(")
        
        elif ans == "1":

            print("\nYou are now using guest mode")

            BrowseMenu.browse()

        elif ans == "2":
            exit()
            
        else:
            print("\nchoose correct option!")

        



main()