import re

def isValidPassword(password):

    flag = 0
    if (len(password) < 8):
        print("Password should contain at least 8 char")
        flag = -1

    elif not re.search("[a-z]", password):
        print("Password should contain at least 1 lowercase alphabate")
        flag = -1

    elif not re.search("[A-Z]", password):
        print("Password should contain at least 1 Uppercase alphabate")
        flag = -1

    elif not re.search("[0-9]", password):
        print("Password should contain at least 1 digit")
        flag = -1

    elif not re.search("[_@$]", password):
        print("Password should contain at least 1 special char (_@$)")
        flag = -1

    elif re.search("\s", password):
        print("Password should not contain any space")
        flag = -1

    else:
        flag = 0
        #print("Valid Password")
        # break
        return True

    if flag == -1:
        print("Not a Valid Password")
        return False

def isValidMobileNo(mob):

    if re.search("[0-9]{10}",mob):

        return True
    else:
        print("Invalid Mobile number")
        return False

def isValidUserName(uname):
    if re.search("\s", uname):
        print("Username should not contain any space")
        return False
    else:
        return True

def isvalidFullName(fname):
    if re.search("[0-9!@#$%^&*()_+]", fname):
        print("Username should not contain any number")
        return False
    else:
        return True

def isValidBloodGroup(bg):
    blood_groups = ["A+","A-","B+","B-","AB-","AB+","O+","O-"]
    if bg in blood_groups:
        return True
    else:
        print("Invalid blood group")
        print("Valid blood groups: ",blood_groups)
        return False

def isValidAge(age):
    if(1 < age < 150):
        return True
    else:
        print("Invalid age")
        return False


def isValidGender(gender):
    if(gender == "M" or gender == "F" or gender == "Other"):
        return True
    else:
        print("Invalid Gender")
        return False

def isValidEmail(email):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if re.search(regex, email):
        return True
    else:
        print("Invalid email")
        return False

def isValidRole(role):
    if role == "Donor" or role == "Receiver":
        return True
    else:
        return False

def isValidCity(city):
    if len(city) > 2 and re.search("[A-za-z]", city):
        return True
    else:
        print("Invalid City Name")
        return False