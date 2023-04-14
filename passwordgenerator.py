import random
import string
# string.ascii_letters , string.ascii_lowercase,string.ascii_uppercase,string.digits,string.punctuation
# a password consists of lower case letters , upper case letters, special symbols,numbers
#dicti = {1:'uppercase',2:'lowercase',3:'symbols',4:'digits'}

#type_of_password = int(input("enter:\n1 to have a password which only consists of alphabets\n2 to have a password which consists of a combination of alphabets and letters\n3 to have a password of combination of alphabets,letters and symbols\n"))

#length_of_password = int(input("enter length of password:"))

def passwordgenerator(length_of_password,type_of_password):
    password = ''
    for i in range(0,length_of_password):
        a = random.randrange(1,type_of_password+2)
        if a==1:
            password = password + random.choice(string.ascii_uppercase)
        elif a==2:
            password = password + random.choice(string.ascii_lowercase)
        elif a==4 and type_of_password!=1 and type_of_password!=2:
            password = password + random.choice(string.punctuation)
        elif a==3 and type_of_password!=1:
            password = password + random.choice(string.digits)
    return password
#print(password)

