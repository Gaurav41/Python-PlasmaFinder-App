# print("Registration form")
import re
import Users
import DataBaseConnection
import Validate as v
class Register:

    def __init__(self):
        self.db = DataBaseConnection.DataBaseConnection()
        pass
    def confirmedPass(self,p1,p2):
        if( p1 == p2):
            return True
        return False

    def getDataFromUser(self):

        """ Take data from user through std input device
        """
        result = False
        print("-"*20," Registration form ","-"*20)
        print("Enter following details")
        name = input("Name: ").strip()
        while v.isvalidFullName(name) == False:
            name = input("Name: ").strip()


        uname = input("Username: ").strip()
        while self.db.isUsernameAvaliable(uname) == False:
            print("\n--Username already exists")
            uname = input("Enter Unique Username: ").strip()
        while  v.isValidUserName(uname) == False:
            uname = input("Enter Unique Username: ").strip()


        password = input("Password: ").strip()
        while v.isValidPassword(password)== False:
            password = input("Password: ").strip()

        vPassword = input("Verify Password: ").strip()
        while (self.confirmedPass(password,vPassword) == False):
            print("\n--Password Missmatched")
            vPassword = input("Verify Password: ").strip()

        age = int(input("Age: ").strip())
        while v.isValidAge(age) == False:
            age = int(input("Age: ").strip())

        gender = input("Gender(M/F/Other): ").strip()
        while v.isValidGender(gender) ==False:
            gender = input("Gender(M/F/Other): ").strip()

        blood_group = input("Blood Group (eg A+):").strip()
        while v.isValidBloodGroup(blood_group) == False:
            blood_group = input("Blood Group (eg A+):").strip()

        email = input("Email: ").strip()
        while v.isValidEmail(email) == False:
            email = input("Email: ").strip()

        mobile = (input("Mobile: ").strip())
        while v.isValidMobileNo(mobile) == False:
            mobile = (input("Mobile: ").strip())



        role = input("Role(Donor/Receiver): ").strip()
        while v.isValidRole(role) == False:
            role = input("Role(Donor/Receiver): ").strip()

        city = input("City: ").strip()
        while v.isValidCity(city) == False:
            city = input("City: ").strip()

        print("-"*40)

        users_obj = Users.User()
        users_obj.setUserData(name, uname, password,email,blood_group,mobile,age,gender,role,city)

        result  =  self.db.addUserDataToDb(users_obj)
        return (result)

    def register_user(self):
        #db connection
        return True




# email = "gauravPingale@gmail.com"

# passw = input("pass")
# print(validatePassword(passw))
# obj = Register()
#
# obj.getDataFromUser()