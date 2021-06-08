import DataBaseConnection


uname = ""
password = ""
loggedInUser = ""
loggedInUserId = 0

# print("Login Module")
def getCredentials():

    print("-"*20,"Login Form","-"*20)
    global uname
    uname = input("Username: ").strip()
    global password
    password = input("Password: ").strip()


def varifyCredentials():
    #data from data base
    DBobj = DataBaseConnection.DataBaseConnection()
    isVerified =  DBobj.verifyLoginCredentials(uname,password)

    if isVerified:
        print("\n--Login successful")
        global loggedInUser
        loggedInUser = uname
        global loggedInUserId
        loggedInUserId = DBobj.getUserId(uname)
        return True
    else:
        # print("\n--Login Failed")
        # print("Enter valid Credential")
        return False

def getLoggedInUser():
    return  (loggedInUser,loggedInUserId)




# getCredentials()
# print(uname)
# print(password)
# varifyCredentials()
# print(getLoggedInUser())