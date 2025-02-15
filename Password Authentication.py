import getpass
db={ 'mani' : '009',
    'Diya' : '2020',
    'Hema' : '1994'
}

n=1
while n<=3:
    username= input("Enter your Username: ")
    password=getpass.getpass("Enter your Password: ")
    if username in db and db[username] == password:
        print('Verified')
        break
    else:
        print("Incorrect User name or Password.")
        n+=1
if n>3:
    print("Too Many attempts.Account locked")





                
        


