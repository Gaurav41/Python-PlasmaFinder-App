import sys
import Login
import Register
import Profile
import Users
import traceback
import MyError
import Validate

#print("Main class")
LOGGED_USER = ""
LOGGED_USER_ID = 0
exitFlag = True

def logout():
    global exitFlag
    exitFlag = False

def login():
    try:
        Login.getCredentials()
        if (Login.varifyCredentials() != True):
            raise MyError.MyError("Invalid Credentials")
        else:
            global LOGGED_USER, LOGGED_USER_ID
            LOGGED_USER, LOGGED_USER_ID = Login.getLoggedInUser()
            # while (exitFlag):

    except  MyError.MyError as e:
        print(e)
        login()

    try:
        while (exitFlag):
            menu2()
    except Exception:
        # traceback.print_exc()
        print("Error:", sys.exc_info()[0])



def register():
    try:
        reg = Register.Register()

        if reg.getDataFromUser():
            print("\n--User Registration successful")
        else:
            print("\n--User Registration Failed")
    except Exception as e:
        # print(e)
        print("Error:", sys.exc_info()[0])

def menu1():
    try:
        menu_list={
            "1" : "Login",
            "2" : "Register"

        }
        operations = {
            "1": login,
            "2": register
        }
        print("\n")
        print("#" * 20 +" Menu " +"#" * 20)
        print("Select menu")
        for k, v in menu_list.items():
            print(f"{k} : {v}")
        ip = input("Choice: ").strip()
        print("#" * 20 )
        operations[ip]()
    except:
        # traceback.print_exc()
        print("Error:", sys.exc_info()[0])
        print("Enter Valid Choice")
        menu1()


def menu2():
    user_obj = Users.User()
    menu_list={
        "1" : "View Profile",
        "2" : "Edit Profile",
        "3" : "Search Plasma Donor",
        "4": "Search Plasma Donor in City",
        "5": "Logout"
    }
    operations2 = {
        "1": user_obj.viewProfile,
        "2": user_obj.editProfile,
        "3": user_obj.searchPlasmaDonor,
        "4": user_obj.searchPlasmaDonor,
        "5": logout
    }
    print("\n")
    print("#" * 20)
    print("Select menu")
    for k, v in menu_list.items():
        print(f"{k} : {v}")
    try:
        ip = input("Choice: ").strip()
        print("#" * 20)

        if ip == "1":
            user_obj.viewProfile(LOGGED_USER_ID)
        elif ip == "2":
            user_obj.editProfile(LOGGED_USER_ID)
        elif ip =="3":
            bg = input("Enter blood group: ").strip()
            while Validate.isValidBloodGroup(bg) == False:
                bg = input("Enter blood group: ").strip()
            data = user_obj.searchPlasmaDonor(bg)
            i = 1
            if data:
                for donor in data:
                    print(f"donor {i}:")
                    print(f"Name: {donor['Name']}")
                    print(f"Blood Group: {donor['Blood Group']}")
                    print(f"Age: {donor['Age']}")
                    print(f"city: {donor['city']}")
                    print(f"Mobile: {donor['Mobile']}")
                    print(f"Email: {donor['Email']}")
                    print()
                    i += 1
            else:
                print("No donor found")
        elif ip =="4":
            bg = input("Enter blood group: ").strip()
            while Validate.isValidBloodGroup(bg) == False:
                bg = input("Enter blood group: ").strip()

            city = input("Enter City: ").strip()
            while Validate.isValidCity(city) == False:
                city = input("Enter City: ").strip()

            data = user_obj.searchPlasmaDonor(bg,city)
            i = 1
            if data:
                for donor in data:
                    print (f"donor {i}:")
                    print(f"Name: {donor['Name']}")
                    print(f"Blood Group: {donor['Blood Group']}")
                    print(f"Age: {donor['Age']}")
                    print(f"city: {donor['city']}")
                    print(f"Mobile: {donor['Mobile']}")
                    print(f"Email: {donor['Email']}")
                    print()
                    i += 1
            else:
                print(f"No plasma donor for blood group {bg}found in {city}")

        elif ip =="5":
            logout()

        else:
            print("Enter Valid Choice")


    except:
        # traceback.print_exc()
        print("Error:", sys.exc_info()[0])
        print("Enter Valid Choice")
        menu1()

while(exitFlag):
    menu1()

print("Exit")





