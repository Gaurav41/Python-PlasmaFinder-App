import sys

import mysql.connector
import traceback
import Users

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="root",
#   database = "plasmafinderdb"
# )
# flag = False
# print(mydb)
# mycursor = mydb.cursor()
# mycursor.execute("SHOW DATABASES")
# tup = ("plasmafinderdb",)
# for x in mycursor:
#   print(x)
#   if x == tup:
#       print("True")
#       flag = True
#
#
# if flag == False :
#     mycursor.execute("CREATE DATABASE plasmafinderdb")
#     print("db created")




class DataBaseConnection:

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="plasmafinderdb"
        )
        self.mycursor = self.mydb.cursor()


    def getUserData(self,userid):
        try:
            sql = f"SELECT * FROM users WHERE id = %s"
            self.mycursor.execute(sql,(userid,))
            myresult = self.mycursor.fetchone()
            #print(myresult)
            return myresult
        except Exception as e:
            print("Error:", e.__class__())
            print("Something went wrong")
            # print(traceback.print_exc())

    def getUsersData(self):
        pass

    def addUserDataToDb(self,obj):
        sql = 'INSERT INTO users (name, uname, password, email, blood_group, mobile, age, gender, role, city) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

        data = obj.getUserData()
        val = tuple(data.values())
        #val = (obj.name,obj.userName,obj.password, obj.email, obj.bg, obj.mobile, obj.age, obj.gender,obj.role)
        #(val)
        result = False

        try:
            self.mycursor.execute(sql,val)
            self.mydb.commit()
            result = True


        except Exception as e:
            print("Error:", e.__class__())
            print("Something went wrong")

        print (f"{self.mycursor.rowcount} record inserted.")
        return result



    def isUsernameAvaliable(self,username):
        isavaliable = True
        try:
            mycursor = self.mydb.cursor()
            mycursor.execute("SELECT uname FROM users")
            usernames = mycursor.fetchall()

            for x in usernames:
                if x[0] == username:
                    isavaliable = False
                    break

        except Exception as e:
            print("Error:", e.__class__())
            print("Something went wrong")

        return isavaliable


    def verifyLoginCredentials(self,uname,password):
        myresult = ""
        try:
            sql = f"SELECT * FROM users WHERE uname = '{uname}' and password = '{password}'"
            # sql = "SELECT * FROM users WHERE uname = "+ uname + "and password=" +password

            # uname = "GP" or "1" = "1" and password = 123 or 1 = 1
            # Username: "GP" or "1" = "1"
            # Password: 123 or 1 = 1
            self.mycursor.execute(sql)

            myresult = self.mycursor.fetchall()

        except Exception as e:
            print("Error:", e.__class__())
            print("Something went wrong")

        else:
            if len(myresult) != 0:
                return True
            else:
                return False

    def getAllPlasmaDonorsData(self,query):
        result = []
        data = ()
        try:
            #sql = f"select name, blood_group, age,email, mobile, city from users WHERE role = 'Donor'"
            self.mycursor.execute(query)
            data = self.mycursor.fetchall()

        # except:
        #     # traceback.print_exc()
        #     print("Error:", sys.exc_info()[0])

        except Exception as e:
            print("Error:", e.__class__())
            print("Something went wrong")

        donor = {}
        for x in data:
            donor["Name"] = x[0]
            donor["Blood Group"] = x[1]
            donor["Age"] = x[2]
            donor["Email"] = x[3]
            donor["Mobile"] = x[4]
            donor["city"] = x[5]
            result.append(donor)
            donor = {}
        return result

    def getUserId(self,uname):
        sql = f"SELECT id FROM users WHERE uname = '{uname}' "
        myresult = ""
        try:
            self.mycursor.execute(sql)
            myresult = self.mycursor.fetchone()
            # print("ID:", myresult[0])

        # except:
        #     # traceback.print_exc()
        #     print("Error:", sys.exc_info()[0])

        except Exception as e:
            print("Error:", e.__class__())
            print("Something went wrong")

        else:
            return myresult[0]

    def updateUsername(self,username,userid):

        sql = 'UPDATE users set uname = %s WHERE id = %s'
        val = (username,userid )
        result = False

        try:
            self.mycursor.execute(sql,val)
            self.mydb.commit()
            result = True

        # except:
        #     # traceback.print_exc()
        #     print("Error:", sys.exc_info()[0])

        except Exception as e:
            print("Error:", e.__class__())
            print("Something went wrong")

        print ("Username updated")
        return result

    def updateName(self,name,userid):

        sql = 'UPDATE users set name = %s WHERE id = %s'
        val = (name,userid )
        result = False

        try:
            self.mycursor.execute(sql,val)
            self.mydb.commit()
            result = True


        except Exception as e:

            print("Error:", e.__class__())

            print("Something went wrong")

        print ("Name updated")
        return result


    def updateEmail(self,email,userid):

        sql = 'UPDATE users set email = %s WHERE id = %s'
        val = (email,userid )
        result = False

        try:
            self.mycursor.execute(sql,val)
            self.mydb.commit()
            result = True

        except Exception as e:
            print("Error:", e.__class__())
            print("Something went wrong")

        print ("Email updated")
        return result


    def updateBg(self,bg,userid):

        sql = 'UPDATE users set blood_group = %s WHERE id = %s'
        val = (bg,userid )
        result = False

        try:
            self.mycursor.execute(sql,val)
            self.mydb.commit()
            result = True

        except Exception as e:
            print("Error:", e.__class__())
            print("Something went wrong")

        print ("Blood group updated")
        return result

    def updateMob(self,mob,userid):

        sql = 'UPDATE users set mob = %s WHERE id = %s'
        val = (mob,userid )
        result = False

        try:
            self.mycursor.execute(sql,val)
            self.mydb.commit()
            result = True

        except Exception as e:
            print("Error:", e.__class__())
            print("Something went wrong")

        print ("Mobile number updated")
        return result

    def updateAge(self,age,userid):

        sql = 'UPDATE users set age = %s WHERE id = %s'
        val = (age,userid )
        result = False

        try:
            self.mycursor.execute(sql,val)
            self.mydb.commit()
            result = True

        except Exception as e:
            print("Error:", e.__class__())
            print("Something went wrong")

        print ("Age updated")
        return result

    def updateGender(self, gender, userid):

        sql = 'UPDATE users set gender = %s WHERE id = %s'
        val = (gender, userid)
        result = False

        try:
            self.mycursor.execute(sql, val)
            self.mydb.commit()
            result = True

        except Exception as e:
            print("Error:", e.__class__())
            print("Something went wrong")

        print("Gender updated")
        return result

    def updateRole(self, role, userid):

        sql = 'UPDATE users set role = %s WHERE id = %s'
        val = (role, userid)
        result = False

        try:
            self.mycursor.execute(sql, val)
            self.mydb.commit()
            result = True

        except Exception as e:
            print("Error:", e.__class__())
            print("Something went wrong")

        print("Role updated")
        return result

    def updateCity(self, city, userid):

        sql = 'UPDATE users set city = %s WHERE id = %s'
        val = (city, userid)
        result = False

        try:
            self.mycursor.execute(sql, val)
            self.mydb.commit()
            result = True

        except Exception as e:
            print("Error:", e.__class__())
            print("Something went wrong")

        print("city updated")
        return result


    def updateProfile(self,col, value, userid):

        sql = f"UPDATE users set {col} = %s WHERE id = %s"
        val = (value, userid)
        result = False

        try:
            self.mycursor.execute(sql, val)
            self.mydb.commit()
            result = True

        except Exception as e:
            print("Error:", e.__class__())
            print("Something went wrong")

        print(f"{col} updated")
        return result

# DataBaseConnection().updateProfile("name","abc",1)