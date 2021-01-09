#adopted from: https://paragonie.com/blog/2016/02/how-safely-store-password-in-2016
import bcrypt 
import hmac
import string


class Password:
    def hash_password(self, password_string):
        hashed_password = bcrypt.hashpw(password_string, bcrypt.gensalt())
        return hashed_password

    def hash_check(self, cleartext_password, hashed_password):
        if (hmac.compare_digest(bcrypt.hashpw(cleartext_password, hashed_password), hashed_password)):
            print("Yes")
        else:
            print("No")    

    def pwd_complex(password):
        if len(password) < 5 or len(password) >10:
            return False
        elif password.isupper() == False:
            return False
        elif password.islower() == False:
            return False
        else:
            return True


#pw = input("Passwort: ")
#password = str.encode(pw) #Conversion string to bytes

