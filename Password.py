#adopted from: https://paragonie.com/blog/2016/02/how-safely-store-password-in-2016
import bcrypt 
import hmac
import string
from json import load
import hashlib 


class Password:
    def hash_password(self, password_string):
        hashed_password = bcrypt.hashpw(password_string, bcrypt.gensalt())
        return hashed_password

    def hash_check(self, cleartext_password, hashed_password):
        if (hmac.compare_digest(bcrypt.hashpw(cleartext_password, hashed_password), hashed_password)):
            print("Yes")
        else:
            print("No")    

    def pwd_complex(self,password):
        with open('pwd_complexity.json','r') as file:
            criteria = load(file)
            spCharater = criteria['existSpecialCharacter']
            upperCase = criteria['existUpperCase']
            lowerCase = criteria['existLowerCase']
            number = criteria['existNumber']
            spCharaterList = criteria['specialCharaterList']
            maxLen = criteria['maxLength']
            minLen = criteria['minLength']
            charaterType = criteria['charaterType']
            
            #print (spCharater)
            
            if len(password) < minLen:
                return False, "Make sure your password is at least " + str(minLen) + " letters"

            if len(password) > maxLen:
                return False, "Make sure your password is at max " + str(maxLen) + " letters"
            
            if number is True: 
                if any(str.isdigit(password) for password in password) != number:
                    return False, "Make sure your password contain one number"
                else:
                    pass
                    
            if upperCase is True: 
                if any(password.isupper() for password in password) != upperCase:
                    return False, "Make sure your password contain one uppercase letter"
                else:
                    pass

            if lowerCase is True:
                if  any(password.islower() for password in password) != lowerCase:
                        return False, "Make sure your password contain one lowercase letter"
                else:
                    pass
                
            if spCharater  is True:
                if any(cha in spCharaterList for cha in password) != True:
                    return False, "Make sure your password contain one special charater"
                else:
                    pass
            
            if any(cha not in charaterType for cha in password):
                return False, "Make sure to enter allowed charaters"
                
            else:
                return True
 
        


#pw = input("Passwort: ")
#password = str.encode(pw) #Conversion string to bytes

