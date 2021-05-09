import random
import mysql.connector
my_db1=mysql.connector.connect(host='localhost',user='root',password='shalu18#',database='eshop')
my_cursor1=my_db1.cursor()
menu_list=[]
order_list=[]
def Billing():
    print('============================')
    print('your orders:')
    if len(order_list)==0:
        print('Your cart is empty')
    else:
        print('===============')
        for i in order_list:
            print(i)
        print('Billing')
        n=input('Enter your user name:')
        m=input('Enter your password:')
        q2='insert into purchase(id,name,mail,orders,Total_bill)/values(%s,%s,%s,%s,%s)'
        t=(n,m,str(order_list))
        my_cursor1.execute(q2,t)
        my_db1.commit()
        print('Total bill:')
def Booking():
    print('========================== Welcome to Shals Eshop======================== ')
    print('Products Available:')
    for menu in menu_list:
        print(menu.get('id'),menu.get('name'),menu.get('price'),menu.get('$'))
    while True:  
        query = 'insert into menu_list(id,name,price) values( %s, %s, %s)'
        mycursor1=my_db1.cursor()
        mycursor.execute('select * from menu_list')
        data=mycursor1.fetchall()
        while True:
            print('='*50)
            print("1. User order \ n2. Cancel order \ n3. Confirm menu \ n4. Checkout")
            server = int(input("Please select service:"))
        if server == 1:
                while True:
                        menu_add = input("Please enter the Product  number or enter Y to end the order:")
                        if menu_add.upper() != 'Y':
                                for m in menu_list:
                                        if m.get('id')== int(menu_add):
                                                Order_list.append(m)
                                                break
                        else:
                                print('================== Ordered =====================')
                                total_price = 0
                                for order in Order_list:
                                        print(order.get('name'),order.get('price'),order.get('$'))
                                        total_price += int(order.get('price'))					
                                print('Subtotal: {} Rs.'.format(total_price))
                                break
        elif server == 2:
                menu_del = input("Please enter the number of the product to be cancelled:")
                for order in Order_list:
                        if order.get('id') == int(menu_del):
                                Order_list.remove(order)
                                print('================== Ordered =====================')
                                total_price = 0
                                for order in Order_list:
                                        print(order.get('name'),order.get('price'),order.get('$'))
                                        total_price += int(order.get('price'))					
                                print('Subtotal: {} Rs.'.format(total_price))
        elif server == 3:
                print('================== Ordered =====================')
                total_price = 0
                for order in Order_list:
                        print(order.get('name'),order.get('price'),order.get('$'))
                        total_price += int(order.get('price'))					
                print('Subtotal: {} Rs.'.format(total_price))         
        elif server == 4:  
                print('================= Your consumption menu =======================')     
                total_price = 0
                for order in Order_list:
                        print(order.get('name'),order.get('price'),order.get('$'))
                        total_price += int(order.get('price'))
		
                print('Total consumption: {} Rs.'.format(total_price))
			
                print('================== Welcome you to visit again, goodbye! =====================')
                break

        
