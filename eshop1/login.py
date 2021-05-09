import random
import mysql.connector
my_db=mysql.connector.connect(host='localhost',user='root',password='shalu18#',database='eshop')
my_cursor=my_db.cursor()
def Create_Account():
    name=input('Enter your username:')
    password=input('Enter your password:')
    mail=input('Enter your mail id:')
    Adress=input('Enter your address:')
    userid=random.randrange(100,100)
    que1='insert into userdetails(userid,name,password,mail,Adress)\values(%s,%s,%s,%s,%s)'
    val1=(userid,name,password,mail,Adress)
    my_cursor.execute(que1,val1)
    my_db.commit()
    print('Your account has been created')

def sign_in():
    user_name1=input('Enter your username:')
    pass1=input('Enter your password:')
    user_name=(user_name1,)
    pass2=(pass1,)
    my_cursor.execute(user_name,pass2)
    q=my_cursor.fetchall()
    if q==pass2:
        print('Successfull signed in')
    else:
        print('Invalid username and passsword')
        sign_in()
    print('------------------------')
        
    
    
    
