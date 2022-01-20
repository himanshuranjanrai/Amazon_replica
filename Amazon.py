class admin_login:
    def __init__(self):
        self.products=dict([])

    def add_product(self,product_id,product_name,Manufacturer_name,product_price,product_discount,Total_stock_available):
        self.products[product_id]={}    
        self.products[product_id]["product_id"]=product_id
        self.products[product_id]["product_name"]=product_name
        self.products[product_id]["Manufacturer_name"]=Manufacturer_name
        self.products[product_id]["product_price"]=product_price
        self.products[product_id]["product_discount"]=product_discount
        self.products[product_id]["Total_stock_available"]= Total_stock_available

    def admin_options(self):
        print("********************")
        print("1.Create Product") 
        print("2.View Product List")
        print("3.View order details")
        print("4.Update Product")
        print("5.Delete Product")
        print("6.Logout")
        print("********************")

    def view_product(self):
        for i in self.products.keys():
            print("Product_id:",self.products[i]["product_id"])
            print("Product_name:",self.products[i]["product_name"])
            print("Manufacturer_name:",self.products[i]["Manufacturer_name"])
            print("product_price:",self.products[i]["product_price"])
            print("product_discount:",self.products[i]["product_discount"])
            print("Total_stock_available:",self.products[i]["Total_stock_available"])
            print()

    def update_product(self,product_id,Update_opt):
        if Update_opt==1:
            new=int(input("Enter updated ID:"))
            self.products[product_id]["product_id"]=new
        elif Update_opt==2:
            new=input("Enter updated Name:")
            self.products[product_id]["product_name"]=new
        elif Update_opt==3:
            new=input("Enter updated Manufacturer Name:")
            self.products[product_id]["Manufacturer_name"]=new
        elif Update_opt==4:
            new=int(input("Enter updated Price:"))
            self.products[product_id]["product_price"]=new
        elif Update_opt==5:
            new=int(input("Enter updated Discount:"))
            self.products[product_id]["product_discount"]=new 
        else:
            new=int(input("Enter updated stock:"))
            self.products[product_id]["Total_stock_available"]=new

    def delete_product(self,product_id):
        return self.products.pop(product_id)
    
    
class member_login:
    def __init__(self):
        self.members=dict([])
        self.orders=dict([])

    def add_member(self,member_name,Email,Full_address,password):
        self.members[Email]={}   
        self.members[Email]["member_name"]=member_name
        self.members[Email]["Email"]=Email
        self.members[Email]["Full_address"]=Full_address
        self.members[Email]["password"]=password
        
    def update_member(self,Email,option):
        if option==1:
            new_password=input("Enter new password for update")
            self.members[Email]["password"]=password
        elif option==2:
            new=input("Enter new Email for update")
            self.members[Email]["Full_address"]=Full_address
        else:
            print("Invalid option")
            
    def member_options(self):
        print("********************")
        print("1.Create New order") 
        print("2.View Order History")
        print("3.Update profile")
        print("4.Logout")
        print("********************")
    
    def order_detail(self,order_id,product_id,product_name,product_price,product_discount,quantity,Total_price):
        self.orders[order_id]={}    
        self.orders[order_id]["product_id"]=product_id
        self.orders[order_id]["product_name"]=product_name
        self.orders[order_id]["product_price"]=product_price
        self.orders[order_id]["product_discount"]=product_discount
        self.orders[order_id]["Quantity"]=quantity
        self.orders[order_id]["Total_price"]=Total_price

    def view_orders(self):
        for i in self.orders.keys():
            print("Product_id:",self.orders[i]["product_id"])
            print("Product_name:",self.orders[i]["product_name"])
            print("product_price:",self.orders[i]["product_price"])
            print("product_discount:",self.orders[i]["product_discount"])
            print("Quantity purchased:",self.orders[i]["Quantity"])
            print("Total_price:",self.orders[i]["Total_price"])
            
        
                
new_admins=[]
new_admins_pass=[]
Admin=admin_login()
order_no=0
total_price=0
Member=member_login()
session=1
while (session==1):
    print("Welcome To Amazon Shopping ")
    print("For Admin Login press A")
    print("For Member Login press M")
    val=input("Enter Your choice here(A/M):")
    if val=="A":
        print("For Excisting Admin Login Press 1 ")
        print("For New Admin Login Press 2 ")
        n=int(input("Enter Your choice:"))
        if n==1:
            username=input("Username:")
            password=input("Password:")
            if username=="admin" and password=="admin":
                logo=2
                while (logo==2):
                    Admin.admin_options()
                    opt=int(input("Enter Your Choice"))
                    if opt==1:
                        product_id = int(input("Enter Product_id : "))
                        product_name = input("Enter Product Name : ")
                        Manufacturer_name = input("Enter Manufacturer: ")
                        product_price = int(input("Enter Price:"))
                        product_discount = int(input("Enter Discount: "))
                        Total_stock_available=int(input("Enter Number of stock"))
                        Admin.add_product(product_id,product_name,Manufacturer_name,product_price,product_discount,Total_stock_available)
                        logo!=1
                        
                    elif opt==2:
                        Admin.view_product()
                        logo!=1

                    elif opt==3:
                        try:
                            for i in Member.members.keys():
                                print("Name:",Member.members[i]["member_name"])
                                print("Email:",Member.members[i]["Email"])
                                print("Address:",Member.members[i]["Full_address"])
                                Member.view_orders()
                        except:
                            print("No order details")
                            logo!=1
                            
                    elif opt==4:
                        Admin.view_product()
                        product_ID=int(input("Enter the product ID to be updated"))
                        print("********************")
                        print("1.Product ID") 
                        print("2.Product Name")
                        print("3.Manufacturer Name")
                        print("4.Product price")
                        print("5.Product Discount")
                        print("6.Number of stocks")
                        print("********************")
                        num=int(input("In which choice you want  to update:"))
                        Admin.update_product(product_ID,num)
                        logo!=1

                    elif opt==5:
                        Admin.view_product()
                        product_ID=int(input("Enter the product ID to be deleted:"))
                        if product_ID in Admin.products:
                            Admin.delete_product(product_ID)
                            logo!=1
                        else:
                            print("Product ID not available")
                            print("Want to enter more (Y/N)?")
                            logo!=1
                    elif opt==6:
                        break
                       
            else:
                print("Invalid credentials")
                print("Please Login with correct login details")
                
        if n==2:
            new_username=input("Create Your username")
            new_password=input("Create Your Password")
            new_admins.append(new_username)
            new_admins_pass.append(new_password)
            print("You have created admin id")
            print("Enter your credentials for login")
            username=input("Username:")
            password=input("Password:")
            Admin2=admin_login()
            if username in new_admins and password in new_admins_pass :
                logo=2
                while (logo==2):
                    Admin.admin_options()
                    opt=int(input("Enter Your Choice"))
                    if opt==1:
                        product_id = int(input("Enter Product_id : "))
                        product_name = input("Enter Product Name : ")
                        Manufacturer_name = input("Enter Manufacturer: ")
                        product_price = int(input("Enter Price:"))
                        product_discount = int(input("Enter Discount: "))
                        Total_stock_available=int(input("Enter Number of stock"))
                        Admin.add_product(product_id,product_name,Manufacturer_name,product_price,product_discount,Total_stock_available)
                        logo!=1
                        
                    elif opt==2:
                        Admin.view_product()
                        logo!=1

                    elif opt==3:
                        try:
                            for i in Member.members.keys():
                                print("Name:",Member.members[i]["member_name"])
                                print("Email:",Member.members[i]["Email"])
                                print("Address:",Member.members[i]["Full_address"])
                                Member.view_orders()
                        except:
                            print("No order details")
                            logo!=1
                            
                    elif opt==4:
                        Admin.view_product()
                        product_ID=int(input("Enter the product ID to be updated"))
                        print("********************")
                        print("1.Product ID") 
                        print("2.Product Name")
                        print("3.Manufacturer Name")
                        print("4.Product price")
                        print("5.Product Discount")
                        print("6.Number of stocks")
                        print("********************")
                        num=int(input("In which choice you want  to update:"))
                        Admin.update_product(product_ID,num)
                        logo!=1

                    elif opt==5:
                        Admin.view_product()
                        product_ID=int(input("Enter the product ID to be deleted:"))
                        if product_ID in Admin.products:
                            Admin.delete_product(product_ID)
                            logo!=1
                        else:
                            print("Product ID not available")
                            print("Want to enter more (Y/N)?")
                            logo!=1
                    elif opt==6:
                        break
                       
            else:
                print("Invalid credentials")
                print("Please Login with correct login details")
                
               
        else:
            print("Incorrect option..try again")

            
    elif val=="M":
        print("For New Member Login Press 1 ")
        print("Excisting member Login Press 2 ")
        n=int(input("Enter Your choice:"))
        if n==1:
            member_name=input("Enter Your Full name:")
            Email=input("Enter Your Email id (This is your username):")
            Full_address=input("Enter Your Full Address:")
            password=input("create your password:")
            Member.add_member(member_name,Email,Full_address,password)
            print("member successfully created")
            print("Login with email id and your password")
            username=input("Username(EMAIL):")
            new_password=input("Password:")
            if username==Member.members[Email]["Email"] and new_password==Member.members[Email]["password"]:
                print()
                print("successfully member login")
                login=True
                while(login==True):
                     Member.member_options()
                     opt=int(input("Enter Your Choice"))
                     if opt==1:
                         Admin.view_product()
                         product_ID = list(map(int,input("\nEnter the ids separated by (comma):").split(",")))
                         for ids in product_ID:
                             if ids in  Admin.products:
                                 print("Product_id:", Admin.products[ids]["product_id"])
                                 print("Product_name:", Admin.products[ids]["product_name"])
                                 print("Manufacturer_name:", Admin.products[ids]["Manufacturer_name"])
                                 print("product_price:", Admin.products[ids]["product_price"])
                                 print("product_discount:", Admin.products[ids]["product_discount"])
                                 print("Total_stock_available:", Admin.products[ids]["Total_stock_available"])
                                 print()
                                 conform = input("\nDo you want to place an order on the above shown product : Y/N ")
                                 if conform == 'Y' or conform == 'y':
                                     quantity=int(input("Enter the Number of quantity You want"))
                                     Total_price=quantity*((Admin.products[ids]["product_price"])-(Admin.products[ids]["product_discount"]))
                                     print("\n Successfully placed the order on the product:",Admin.products[ids]["product_id"])
                                     order_no+= 1
                                     print("Your order number is : ",order_no)
                                     Admin.products[ids]["Total_stock_available"]-= quantity
                                     Member.order_detail(order_no,Admin.products[ids]["product_id"],Admin.products[ids]["product_name"],Admin.products[ids]["product_price"],Admin.products[ids]["product_discount"],quantity,Total_price)           
                                 elif conform == 'N' or conform == 'n':
                                     print("The order is not placed. You can carry on with you purchase. Happy shopping!!!!")
                                 else:
                                     print("\nYou have entered wrong option. Please enter again\n")
                             else:
                                 print("\nYou have entered invalid id. Please enter valid id\n")

                     elif opt==2:
                         Member.view_orders()

                     elif opt==3:
                         Email=input("Enter your email")
                         print("********************")
                         print("1.Update Password") 
                         print("2.Update address")
                         option=int(input("Enter your choice:"))
                         Member.update_member(Email,option)

                     elif opt==4:
                         break
            
            else:
                print("Invalid credentials")
                print("Please Login with correct login details")

        elif n==2:
            username=input("Username(EMAIL):")
            new_password=input("Password:")
            if username==Member.members[Email]["Email"] and new_password==Member.members[Email]["password"]:
                print()
                print("successfully member login")
                login=True
                while(login==True):
                    Member.member_options()
                    opt=int(input("Enter Your Choice"))
                    if opt==1:
                        Admin.view_product()
                        product_ID = int(input("\nEnter the ids separated by (comma):").split(","))
                        for ids in product_ID:
                            if ids in  Admin.products:
                                print("Product_id:", Admin.products[ids]["product_id"])
                                print("Product_name:", Admin.products[ids]["product_name"])
                                print("Manufacturer_name:", Admin.products[ids]["Manufacturer_name"])
                                print("product_price:", Admin.products[ids]["product_price"])
                                print("product_discount:", Admin.products[ids]["product_discount"])
                                print("Total_stock_available:", Admin.products[ids]["Total_stock_available"])
                                print()
                                conform = input("\nDo you want to place an order on the above shown product : Y/N ")
                                if conform == 'Y' or conform == 'y':
                                    quantity=int(input("Enter the Number of quantity You want"))
                                    Total_price=quantity*((Admin.products[ids]["product_price"])-(Admin.products[ids]["product_discount"]))
                                    print("\nSuccessfully placed the order on the product:",Admin.products[ids]["product_id"])
                                    order_no+= 1
                                    print("Your order number is : ", order_no)
                                    Admin.products[ids]["Total_stock_available"]-= quantity
                                    Member.order_detail(order_no,Admin.products[ids]["product_id"],Admin.products[ids]["product_name"],Admin.products[ids]["product_price"],Admin.products[ids]["product_discount"],quantity,Total_price)           
                                elif conform == 'N' or conform == 'n':
                                    print("The order is not placed. You can carry on with you purchase. Happy shopping!!!!")
                                else:
                                    print("\nYou have entered wrong option. Please enter again\n")
                            else:
                                print("\nYou have entered invalid id. Please enter valid id\n")

                    elif opt==2:
                        Member.view_orders()

                    elif opt==3:
                        Email=input("Enter your email")
                        print("********************")
                        print("1.Update Password") 
                        print("2.Update address")
                        option=int(input("Enter your choice:"))
                        Member.update_member(Email,option)

                    elif opt==4:
                        break
            
                else:
                     print("Invalid credentials")
                     print("Please Login with correct login details")

            else:
                print("Invalid credentials")
                print("Please Login with correct login details")

            
            

