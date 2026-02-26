# # password manager


# while True:
#  print("1.Save website name and password")
#  print("2.View all saved passwords")
#  print("3.search password")
#  print("4.exit")

#  choice = input("Enter your choice: ")
  
#  if choice == 1:
#        website = input("Enter Website name: ")
#        password = input("Enter your password: ") 

#  elif choice == 2:
#    pass
   
 
#  elif choice == 3:
#    pass
   
 
#  elif choice == 4:
#        print("Exited")
#        break



# #  with open("data.txt",'a') as f:
# #     f.write(input("Enter password: "))


# #  with open("data.txt",'r') as f:
# #     print(f.read())




while True:
 print("1. Save website name and password")
 print("2. view all passwords")
 print("3. search for a password")
 print("4. Exit")

 choice = input("Enter your choice: ")


 if choice == "1":
        website = input("Enter website name: ")
        password = input("Enter your Password: ")
        
        with open("Data.txt", "a") as f:
             f.write(website + "=" + password + "\n")

        print("Password saved!!")
        

 elif choice == "2":
        with open("Data.txt", "r") as f:
             print(f.readlines())
        
 elif choice == "3":
        search = input("Enter website name: ")
        found = False
        
        with open("Data.txt", 'r') as f:
             for i in f:
                data= i.strip().split("=")
                if data[0] == search:
                     print("password is: ", data[1])
                     found = True 
             if found == False:
                    print("Website not found")
            
            
 elif choice == "4":
       print("Exited")
       break

 else:

    print("Invalid choice! Try again.")
