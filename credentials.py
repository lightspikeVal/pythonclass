# Authorship and license
import re
def authorship():
    """This library is built by Smart Bob, under the license of Creative Commons Native 1.0"""
    print("Hover over the function to see!")

#Start of Library---------------------------
def username():
    """Ask the user the username."""
    usrnm=input("Enter your username: ")
    r=re.search("[a-z]",usrnm)
    if r:
        print("Successful")
        return usrnm
    else:
        print( "Username can only include a-z." )

def password():
    """Ask the user the password"""
    pswrd=input("Enter your password: ")
    r= re.search("[a-zA-Z0-9]",pswrd)
    if r:
        print("Successful")
        return pswrd
    else:
        print("Password must include a-z A-Z 0-9")    
def login(a,b):
    """Add the place that you stored user data in Parameter A & user password data in Parameter B
    Note: The index of the user's username and password must be the same in order to work accuratly"""
    usrg=input("Enter username: ")
    psrg=input("Enter password: ")
    index=-1
    for i in range(len(a)):
        if a[i]==usrg:
            index=i
            break
    if index==-1:
        print("Username not found!")
        return "UNUSRNM"    
    if b[index]==psrg:
        print("Successful Login!")
        return "SCCSL001"
    else:
        print("Login fail")
        return "UNPWD"

def register(a,b):
    """This function accepts username and password and checks whether it meets the password requirements, and then it will save it to your given database.
     Parameters: 
          a= Enter your list name e.g(mylist) for usernames
          b = Enter your list name e.g(mypwlist) for passwords"""
    iof=0
    while iof==0:
        usrnm=input("Enter your username: ")
        r=re.search("[a-z]",usrnm)
        if r:
            print("Successful")
            a.append(usrnm)
            iof=1
        else:
            print( "Username can only include a-z." )
    iof=0
    while iof==0:
        pswrd=input("Enter your password: ")
        r= re.search("[a-zA-Z0-9]",pswrd)
        if r:
            print("Successful")
            b.append(pswrd)
            iof=1
        else:
            print("Password must include a-z A-Z 0-9")
def regimail(a,b,c):
    """This function asks the user to input mail instead of username.
    A = Email list
    B = Password list
    C = Username list"""
    iof=0
    while iof==0:
        erg=input("Enter email: ")
        valid=re.search(r"^[a-zA-Z0-9.+_-]+@[a-z0-9]+\.(org|com|io|tech|shop|edu|gov|co|gg|dev|net)+$",erg)
        if valid:
            print("Successful!")
            a.append(erg)
            iof=1
        else:
            print("Email must be valid")
    iof = 0
    while iof==0:
        usrnm=input("Enter your username: ")
        r=re.search("[a-z]",usrnm)
        if r:
            print("Successful")
            c.append(usrnm)
            iof=1
        else:
            print( "Username can only include a-z." )
    iof=0
    while iof==0:
        pswrd=input("Enter your password: ")
        r= re.search("[a-zA-Z0-9]",pswrd)
        if r:
            print("Successful")
            b.append(pswrd)
            iof=1
        else:
            print("Password must include a-z A-Z 0-9")
        
    