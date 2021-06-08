
def menu1(userid):
    try:
        menu_list={
            "1" : "Name",
            "2" : "Username",
            "3" : "Email",
            "4" : "Blood Group",
            "5" : "mobile no",
            "6" :  "Age",
            "7" : "Gender",
            "8" : "Role",
            "9" : "City"

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
        print("Enter Valid Choice")
        menu1()

