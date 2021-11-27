class password_management:
    database={}
    def __init__(self,username):
        self.username=username
    def new_user(self):
        self.database[self.username]=input("Please set new password\n").lstrip().rstrip()
        print(f"Your password has been set.\nYour username is {self.username}.\nYour password is {self.database[self.username]}\nPlease login with new Password.")
    def old_user(self):
        password=input("Please enter password\n").lstrip().rstrip()
        if password == self.database[self.username]:
            print("Successful Login")
            return True
        else:
            print("Incorrect Password")
            print("Please Retry Login")
            return False

def password_sys(username):
    user=password_management(username)
    if username in user.database:
        auth = user.old_user()
    else:
        user.new_user()
        auth = False
    return auth
