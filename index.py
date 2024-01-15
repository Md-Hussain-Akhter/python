print("                 ****WELCOME TO MY PYTHON ****" )

#List is used to multiple value store in a single varible

studentName = ["Hussain"]#list create by student
studentRollno = [12]     #list create by student
studentBranch = ["co"]   #list create by student

while True:
    print("Check your Choice and check Again to continue...\n 1. New Account Created\n 2. Login student")
    #int is use to string to canvert to numrical varible. It is used to convert the user's input into an integer.
    choice = int(input("Choice conditions: "))

#if condiction is used to codiction check true or false
    if choice == 1:
        # Input student values from the user
        #input methad is used to input value from the keybord
        Name = input("Enter student name: ")
        Rollno = input("Enter student Rollno: ")
        Branch = input("Enter student Branch: ")
                    
        # Add the values to the lists
        #append the value to the list of value to be inserted into the list of values
        studentName.append(Name)      #Store a value from the list
        studentRollno.append(Rollno)  #Store a value from the list
        studentBranch.append(Branch)  #Store a value from the list

    elif choice == 2:
        # Check the list and display the values
        userName = input("Enter user name: ")
        userPassword = input("Enter user Password: ")
        
        if userName == "hussain Akhter" and userPassword == "123":
            print("Login successfully, see the stored data for more information...")
            print("Roll Numbers:", studentRollno)
            print("Names:", studentName)
            print("Branches:", studentBranch)
     #else method is used to laste condiction use this block
    else:
        print("Invalid choice. Please enter 1 or 2.")


    # studentName=["Hussain"]
    # studentRollno=[12]
    # studentBranch=["co"]
    # Name=input("Enter studet name:")
    # Rollno=input("Enter student Rollno:")
    # Branch=input("Enter student Branch:")
    
    
    # studentName.append(Name)
    # studentRollno.append(Rollno)
    # studentBranch.append(Branch)

    # print(studentName)
    # print(studentRollno)
    # print(studentBranch)
    # if(studentName==studentName and studentRollno==studentRollno and studentBranch==studentBranch):
    #     print("login ")
    # else:
    #     print("note this collage stuend, student id card is collage")
