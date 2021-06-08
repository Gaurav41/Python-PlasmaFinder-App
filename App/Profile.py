import Users
import DataBaseConnection

def viewProfile(username):
    data = DataBaseConnection.DataBaseConnection().getUserData(username)
    userId, name, username, password, email, blood_group, mobile, dob, gender, role = data
    print(f"Id:{userId} ")
    print("Name: ",name)
    print("Username: ",username)
    print("Email: ", email)
    print("Blood Group: ",blood_group)
    print("mobile no: ",mobile)
    print("DOB: ",dob)
    print("Gender: ",gender)
    print("Role:",role)


def editProfile(uname):
    # print("Select field which u want to edit")
    # menu_list = {
    #     "1": "Name",
    #     "2": "Email",
    #     "3": "Blood Group",
    #     "4": "mobile no",
    #     "5": "DOB",
    #     "6": "Gender",
    #     "7": "Role"
    # }
    # print("\n")
    # print("#" * 20)
    # print("Select menu")
    # for k, v in menu_list.items():
    #     print(f"{k} : {v}")
    # ip = input("Choice: ")
    # print("#" * 20)
    print("Service Unavaliable")
    pass

