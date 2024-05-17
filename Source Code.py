from cryptography.fernet import Fernet
import math, random
import smtplib

def OTP(gid):
    gmail=gid
    digit="1234567890"
    otp=""
    for i in range(4):
        otp+= digit[math.floor(random.random() * 10)]
    tsg=otp
    Mail(gmail,otp)
    return otp
    
def Mail(gmail,otp):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("tagorepattela1012@gmail.com", "hqwgvpudolgvmijo")
    receiver=gmail
    message = "your otp is "+str(otp)
    s.sendmail("tagorepattela1012@gmail.com", receiver , message)
    s.quit()
        
def encrypted(v,id):
    message = v
    gid=id
    key = Fernet.generate_key()
    fernet = Fernet(key)
    s=fernet
    encMessage = fernet.encrypt(message.encode())
    print("encrypted data: ", encMessage)
    abc=OTP(gid)
    tsg=input("enter the otp: ")
    if tsg==abc:
        decMessage = s.decrypt(encMessage).decode()
        print("decrypted data: ", decMessage)
    else:
        encrypted(v,id)

def login():
    
    while (True):
        h=input("register or login?")
        a=h.lower()
        if a=="register":
            dup=input("enter user name: ")
            if dup in user_name :
                print("user name already exist")
                login()
            user_name.append(dup)
            password.append(input("enter password:  "))
            mail_id.append(input("enter your gmail: "))
            return user_name, password
        elif a=="login":
            b=input("enter user name:")
            c=input("enter password")
            if  b in user_name and c in password:
                d=user_name.index(b)
                e=password[d]
                if c==e:
                    print("valid user")
                    v=input("enter the data that should be encrypted: ")
                    id=mail_id[d]
                    encrypted(v,id)
                else:
                    print("invalid user name or password")
            else:
                print("invalid user name or password")
        else:
            print("invalid option")
user_name=["tagore","sravya","prema sai"]
password=["sai","12345","19341a0470"]
mail_id=["tagore.pattela.143@gmail.com","sravyanistala@gmail.com","premasaijaddu@gmail.com"]
while(True):
    name,pws=login()
