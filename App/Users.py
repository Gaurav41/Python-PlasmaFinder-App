import DataBaseConnection
import Validate


class User:

    def __init__(self):
        self.db_obj = DataBaseConnection.DataBaseConnection()
        self.v = Validate
        self.__fullname__ = ""
        self.__userName__ = ""
        self.__password__ = ""
        self.__email__ = ""
        self.__bg__ = ""
        self.__mobile__ = ""
        self.__age__ = ""
        self.__gender__ = ""
        self.__role__ = ""
        self.__city__ = ""

    def setUserData(self, name, uname, pswd,email,bg,mobile,age,gender,role,city):
        self.__fullname__ = name
        self.__userName__ = uname
        self.__password__ = pswd
        self.__email__ = email
        self.__bg__ = bg
        self.__mobile__ = mobile
        self.__age__ = age
        self.__gender__ = gender
        self.__role__ = role
        self.__city__ = city



    def getUserData(self):
        data = {
            "name":self.__fullname__,
            "username":self.__userName__,
            "password":self.__password__,
            "email"  :self.__email__,
            "bg":self.__bg__,
            "mobile": self.__mobile__,
            "age" : self.__age__,
            "gender" : self.__gender__,
            "role" : self.__role__,
            "city" : self.__city__
        }
        return data

    def viewProfile(self,userid):
        data = self.db_obj.getUserData(userid)
        userId, name, username, password, email, blood_group, mobile, age, gender, role, city = data
        # print(f"Id:{userId} ")
        print("1.Name: ", name)
        print("2.Username: ", username)
        print("3.Email: ", email)
        print("4.Blood Group: ", blood_group)
        print("5.Mobile no: ", mobile)
        print("6.Age: ", age)
        print("7.Gender: ", gender)
        print("8.Role:", role)
        print("9.City:", city)

    def editProfile(self,userid):
        print("Select field which u want to edit")
        self. viewProfile(userid)
        operations = {
            "1": "Name",
            "2": "Username",
            "3": "Email",
            "4": "Blood Group",
            "5": "mobile no",
            "6": "DOB",
            "7": "Gender",
            "8": "Role"
        }

        ip = input("Choice: ")

        if ip == "1":
            def update_name():
                name = input("Enter new Name: ")
                if self.v.isvalidFullName(name):
                    self.db_obj.updateName(name, userid)
                else:
                    print("Name is invalid..try with Correct Name")
                    update_name()
            update_name()



        elif ip == "2":
            def update_uname():
               username = input("Enter new User name: ")
               if self.v.isValidUserName(username):
                   if self.db_obj.isUsernameAvaliable(username):
                       self.db_obj.updateUsername(username,userid)
                   else:
                       print("Username not avaliable")
                       update_uname()

               else:
                   print("Username is invalid..try with different Username")
                   update_uname()

            update_uname()

        elif ip == "3":
           def update_email():
               email = input("Enter email: ")
               if self.v.isValidEmail(email):
                   self.db_obj.updateEmail(email, userid)
               else:
                   print("Email is invalid..try with correct Email")
                   update_email()

           update_email()

        elif ip == "4":
            def update_bg():
                bg = input("Enter Blood Group: ")
                if self.v.isValidBloodGroup(bg):
                    self.db_obj.updateBg(bg, userid)
                else:
                    print("Blood Group is invalid")
                    update_bg()

            update_bg()


        elif ip == "5":
            def update_mob():
                mob = input("Enter Mobile number: ")
                if self.v.isValidMobileNo(mob):
                    self.db_obj.updateMob(mob, userid)
                else:
                    print("Mobile Number is invalid")
                    update_mob()

            update_mob()

        elif ip == "6":
            def update_age():
                age = input("Enter age : ")
                if self.v.isValidAge(age):
                    self.db_obj.updateAge(age, userid)
                else:
                    print("Age is invalid")
                    update_age()

            update_age()
        elif ip == "7":
            def update_gender():
                gender = input("Enter Gender(M/F/O) ")
                if self.v.isValidGender(gender):
                    self.db_obj.updateGender(gender, userid)
                else:
                    print("Gender Number is invalid")
                    update_gender()

            update_gender()

        elif ip == "8":
            def update_role():
                role = input("Enter role(Donor/Receiver) ")
                if self.v.isValidRole(role):
                    self.db_obj.updateRole(role, userid)
                else:
                    print("Role Number is invalid")
                    update_role()

            update_role()

    def searchPlasmaDonor(self,bg,city =""):
        if city !="":
            sql = f"select name, blood_group, age,email, mobile, city from users WHERE role = 'Donor' AND blood_group= '{bg}' AND city ='{city}'"
        else:
            sql = f"select name, blood_group, age,email, mobile, city from users WHERE role = 'Donor' AND blood_group= '{bg}'"
        data = self.db_obj.getAllPlasmaDonorsData(sql)
        return data
        # i = 0
        # if data:
        #     for donor in data:
        #         print (f"donor {i}: {donor}")
        #         i += 1
        # else:
        #     print("No donor found")

        # for k,v in data:
        #     print(k +" : " +v)




# obj = User()
# obj.searchPlasmaDonor()