import random

All_Accounts_Lists = {}
All_Accounts_Passwords = {}
All_Accounts_Money = {}

def check_strength(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/~`" for c in password)
    length = len(password)

    if length >= 8 and has_upper and has_lower and has_digit and has_special:
        return "Strong"
    elif length >= 6 and (has_upper or has_lower) and has_digit:
        return "Medium"
    else:
        return "Weak"

def more_operations():
    print("")
    print("TO CONTINUE CHOOSE THE FOLLOWING OPTIONS")
    print("-----------------------------------------------------------------------------------------------------------------------------")
    print("0. HELP")
    print("1. Create an Account")
    print("2. Delete an Account")
    print("3. Update an Account")
    print("4. Deposit Money")
    print("5. Debit Amount")
    print("6. Balance Enquiry")
    print("7. Display Account Details")
    print("8. EXIT")
    print("-----------------------------------------------------------------------------------------------------------------------------")
    option = int(input("Enter the Option :"))
    return option

def create_account():
    print(" ")
    name = input("Enter Your Full Name : ")
    print(" ")

    while(True):
        dob = input("Enter Your Birth Date [dd-mm-yyyy] : ")
        year = int(dob[-4:])
        if year > 2007:
            print("Your are not eligible to open an New Account !!!")
            return
        break
    print(" ")

    parent_name = input("Enter your Father/Mother/Guardian Name : ")
    print(" ")

    while True:
        acc_type = input("Account Type [Savings/Fixed]: ")
        if acc_type.lower() in ["savings", "fixed"]:
            break
        print("The Account Type is Unavailable!!")
    print(" ")

    acc_number = "ABC"+str(random.randint(1234567890,10000000000)) 

    address = input("Enter Your Current Address :") 
    print(" ")

    while True:
        phno = input("Enter Your Phone Number: ")
        if len(phno) == 10 and phno.isdigit():
            phno = "+91"+phno
            break
        print("Please enter a valid 10-digit phone number!")
    print(" ")

    gmail = input("Please enter your G-Mail ID : ")
    print(" ")
  
    credit = input("Do you want to Deposit Any Money ? [ YES/NO ] : ")
    if(credit.lower()=='yes'):
        print(" ")
        money = input("Enter the Amount :")
    print(" ")

    while True:
        password = input("Enter Your Password For Security(Any) : ")
        strength = check_strength(password)
        print(f"Password strength: {strength}")

        if strength == "Weak":
            print("❌ Password is too weak! Please try again.\n")
            continue

        confirm = input("Re-enter your password to confirm: ")
        if password == confirm:
            print("✅ Password confirmed successfully!")
            break
        else:
            print("❌ Passwords do not match! Please try again.\n")
    print(" ")
    print(" ")

    print("Your Account has been Created Successfully")
    print("-----------------------------------------------------------------------------------------------------------------------------")
    print("The Details of Your Account are : ")
    print("-----------------------------------------------------------------------------------------------------------------------------")
    print("🧾 ACCOUNT NUMBER : ",acc_number)
    print(" ")
    print("🔑 YOUR PASSWORD : ",password)
    print(" ")
    print("🧾 YOUR ACCOUNT TYPE : ",acc_type)
    print(" ")
    print("📛 NAME OF THE USER : ",name)
    print(" ")
    print("📅 DATE OF BIRTH : ",dob)
    print(" ")
    print("🧑‍🍼 FATHER/MOTHER/GUARDIAN NAME : ",parent_name)
    print(" ")
    print("🏡 ADDRESS : ",address)
    print(" ")
    print("📞 PHNO : ",phno)
    print(" ")
    print("📧 G-MAIL : ",gmail)
    print(" ")
    print("💰 BALANCE : ",money)
    print(" ")
    print("-----------------------------------------------------------------------------------------------------------------------------")
    print("✅YOU SUCCESSFULLY ENTERD DETAILS ! 🎉")
    print("-----------------------------------------------------------------------------------------------------------------------------")

    confirm = int(input("Enter '1' to Confirm Details (or) Enter '0' to re-enter Details : "))

    if confirm :
        All_Accounts_Lists[acc_number] = [acc_type,name,dob,parent_name,address,phno,gmail]
        All_Accounts_Passwords[acc_number] = password
        All_Accounts_Money[acc_number] = money
        print("✅✅✅CONGRATULATIONS ! YOU HAVE CREATED AN ACCOUNT IN OUR 'ABC' BANK ! 🎉🎉🎉")
    else:
        create_account()
    print("-----------------------------------------------------------------------------------------------------------------------------")


def delete_account():
    acc_number = input("Enter Your Account NUmber : ")
    if acc_number in All_Accounts_Passwords :
        password = input("Enter Your Password : ")
    else :
        print("There is no Existing Account Available !!!")
        return
    if password == All_Accounts_Passwords[acc_number] :
        decision = input("Enter '1' to CONFIRM DELETION of Account (or) Enter '0' EXIT : ")
        if decision:
            All_Accounts_Passwords[acc_number].pop()
            All_Accounts_Lists[acc_number].pop()
            All_Accounts_Money[acc_number].pop()
            print("✅ ACCOUNT HAVE BEEN DELETED SUCCESSFULLY !!!")
    else:
        print("❌ ERROR - THE PASSWORD YOU ENTERED IS INCORRECT !")
    return


def update_account():
    acc_number = input("Enter Your Account NUmber : ")
    if acc_number in All_Accounts_Passwords :
        password = input("Enter Your Password : ")
    else :
        print("There is no Existing Account Available !!!")
        return
    if password == All_Accounts_Passwords[acc_number] :
        while True:
            print("-----------------------------------------------------------------------------------------------------------------------------")
            print("Updation Codes :")
            print("101 . Update PHNO ")
            print("102 . Update Mail ")
            print("103 . Update DATE OF BIRTH ")
            print("104 . Account TYPE ")
            print("105 . Full Name")
            print("106 . Guardian Name ")
            print("107 . Address")
            print("108 . EXIT ")
            print("-----------------------------------------------------------------------------------------------------------------------------")
            updation = int(input("Enter Your Option for UPDATION : "))
            print("-----------------------------------------------------------------------------------------------------------------------------")

            if updation==101: 
                while True:
                    print("Your Existing Phno is ",All_Accounts_Lists[acc_number][5])
                    print(" ")
                    phno = input("Enter Your NEW Phone Number : ")
                    if len(phno) == 10 and phno.isdigit():
                        phno = "+91"+phno
                        All_Accounts_Lists[acc_number][5] = phno
                        print("✅ UPDATION OF PHONE NUMBER COMPLETED !")
                        print("-----------------------------------------------------------------------------------------------------------------------------")  
                        break
                    print("Please enter a valid 10-digit phone number!")
            elif updation==102:
                print("Your Existing Email is ",All_Accounts_Lists[acc_number][6])
                print(" ")
                gmail = input("Enter Your NEW Mail ID : ")
                All_Accounts_Lists[acc_number][6] = gmail
                print("✅ UPDATION OF GMAIL ID COMPLETED !")
                print("-----------------------------------------------------------------------------------------------------------------------------")
            elif updation==103:
                print("Your Existing Date of Birth is ",All_Accounts_Lists[acc_number][2])
                print(" ")
                while(True):
                    dob = input("Enter Your NEW Birth Date [dd-mm-yyyy] : ")
                    year = int(dob[-4:])
                    if year > 2007:
                        print("Enter Valid Date of Birth !!! [ Date you entered is less than 18 year (or) The Format is Wrong ]")
                    else:
                        All_Accounts_Lists[acc_number][2] = dob
                        print("✅ UPDATION OF DATE OF BIRTH COMPLETED !") 
                        print("-----------------------------------------------------------------------------------------------------------------------------")
                        break
            elif updation==104:
                print("Your Existing Account Type is ",All_Accounts_Lists[acc_number][0])
                print(" ")
                while True:
                    acc_type = input("Enter New Account Type [Savings/Fixed] : ")
                    if acc_type.lower() in ["savings", "fixed"]:
                        All_Accounts_Lists[acc_number][0] = acc_type
                        print("✅ UPDATION OF ACCOUNT TYPE COMPLETED !") 
                        print("-----------------------------------------------------------------------------------------------------------------------------")
                        break
                    else:
                        print("The Account Type is Unavailable!!")
            elif updation==105:
                print("Your Existing Account Type is ",All_Accounts_Lists[acc_number][1])
                name = input("Enter Your Full NAME : ")
                All_Accounts_Lists[acc_number][1] = name
                print("✅ UPDATION OF ACCOUNT TYPE COMPLETED !") 
                print("-----------------------------------------------------------------------------------------------------------------------------")
            elif updation==106:
                print("Existing Guardian Name is ",All_Accounts_Lists[acc_number][3])
                print(" ")
                parent_name = input("Enter your New Guardian Name : ")
                All_Accounts_Lists[acc_number][3] = parent_name
                print("✅ UPDATION OF YOUR GUARDIAN NAME COMPLETED !") 
                print("-----------------------------------------------------------------------------------------------------------------------------")
            elif updation==107:
                print("Existing Address is ",All_Accounts_Lists[acc_number][4])
                print(" ")
                address = input("Enter your New Address : ")
                All_Accounts_Lists[acc_number][4] = address
                print("✅ UPDATION OF YOUR ADDRESS COMPLETED !") 
                print("-----------------------------------------------------------------------------------------------------------------------------")
            elif updation==108:
                return
    else:
        return
    

def deposit_money():
    print("-----------------------------------------------------------------------------------------------------------------------------")
    acc_number = input("Enter Your Account NUmber : ")
    print(" ")
    if acc_number in All_Accounts_Passwords :
        password = input("Enter Your Password : ")
    else :
        print("There is no Existing Account Available !!!")
        print("-----------------------------------------------------------------------------------------------------------------------------")
        return
    if password == All_Accounts_Passwords[acc_number] :
        print(" ")
        dep_money = input("Enter your Deposit Money : ")
        All_Accounts_Money[acc_number] = int(All_Accounts_Money[acc_number])+int(dep_money)
        print("✅ YOUR MONEY HAVE BEEN DEPOSITED SUCCESSFULLY !!") 
        print("Your Current Balance is : Rs.",All_Accounts_Money[acc_number])
        print("-----------------------------------------------------------------------------------------------------------------------------")
    else:
        print("❌ You Entered Wrong Password !!")
        print("-----------------------------------------------------------------------------------------------------------------------------")


def debit_amount():
    print("-----------------------------------------------------------------------------------------------------------------------------")
    acc_number = input("Enter Your Account NUmber : ")
    print(" ")
    if acc_number in All_Accounts_Passwords :
        password = input("Enter Your Password : ")
    else :
        print("There is no Existing Account Available !!!")
        print("-----------------------------------------------------------------------------------------------------------------------------")
        return
    if password == All_Accounts_Passwords[acc_number] :
        print(" ")
        debit_money = input("Enter your Debit Amount : ")
        if int(All_Accounts_Money[acc_number])-int(debit_money) < 0 :
            print("❌ The Amount you entered can't be DEBITED !!!")
            print("Your Current Balance is : Rs.",All_Accounts_Money[acc_number])
            print("-----------------------------------------------------------------------------------------------------------------------------")
        else:
            All_Accounts_Money[acc_number] = int(All_Accounts_Money[acc_number])-int(debit_money)
            print("✅ YOUR MONEY HAVE BEEN DEBITED SUCCESSFULLY !!") 
            print("Your Remaining Balance is : Rs.",All_Accounts_Money[acc_number])
            print("-----------------------------------------------------------------------------------------------------------------------------")
    else:
        print("❌ You Entered Wrong Password !!")
        print("-----------------------------------------------------------------------------------------------------------------------------")


def balance_enquiry():
    print("-----------------------------------------------------------------------------------------------------------------------------")
    acc_number = input("Enter Your Account NUmber : ")
    print(" ")
    if acc_number in All_Accounts_Passwords :
        password = input("Enter Your Password : ")
    else :
        print("There is no Existing Account Available !!!")
        print("-----------------------------------------------------------------------------------------------------------------------------")
        return
    if password == All_Accounts_Passwords[acc_number] :
        print("Account Number : ",acc_number)
        print("BALANCE : ",All_Accounts_Money[acc_number])
        print("-----------------------------------------------------------------------------------------------------------------------------")
        print("✅ YOUR BALANCE HAVE BEEN FETCHED SUCCESSFULLY !!")
        print("-----------------------------------------------------------------------------------------------------------------------------")
    else:
        print("❌ You Entered Wrong Password !!")
        print("-----------------------------------------------------------------------------------------------------------------------------")


def display_details():
    print("-----------------------------------------------------------------------------------------------------------------------------")
    acc_number = input("Enter Your Account NUmber : ")
    print(" ")
    if acc_number in All_Accounts_Passwords :
        password = input("Enter Your Password : ")
    else:
        print("There is no Existing Account Available !!!")
        print("-----------------------------------------------------------------------------------------------------------------------------")
        return
    if password == All_Accounts_Passwords[acc_number] :
        print("-----------------------------------------------------------------------------------------------------------------------------")
        print("The Details of Your Account are : ")
        print("-----------------------------------------------------------------------------------------------------------------------------")
        print("🧾 ACCOUNT NUMBER : ",acc_number)
        print(" ")
        print("🔑 YOUR PASSWORD : ",password)
        print(" ")
        print("🧾 YOUR ACCOUNT TYPE : ",All_Accounts_Lists[acc_number][0])
        print(" ")
        print("📛 NAME OF THE USER : ",All_Accounts_Lists[acc_number][1])
        print(" ")
        print("📅 DATE OF BIRTH : ",All_Accounts_Lists[acc_number][2])
        print(" ")
        print("🧑‍🍼 FATHER/MOTHER/GUARDIAN NAME : ",All_Accounts_Lists[acc_number][3])
        print(" ")
        print("🏡 ADDRESS : ",All_Accounts_Lists[acc_number][4])
        print(" ")
        print("📞 PHNO : ",All_Accounts_Lists[acc_number][5])
        print(" ")
        print("📧 G-MAIL : ",All_Accounts_Lists[acc_number][6])
        print(" ")
        print("💰 BALANCE AMOUNT : ",All_Accounts_Money[acc_number])
        print(" ")
        print("-----------------------------------------------------------------------------------------------------------------------------")
        print("✅ YOUR DETAILS DISPLAYED SUCCESSFULLY !!")
        print("-----------------------------------------------------------------------------------------------------------------------------")
    else:
        print("❌ You Entered Wrong Password !!")
        print("-----------------------------------------------------------------------------------------------------------------------------")


if __name__ == "__main__" :
    print("_____________________________________________________________________________________________________________________________")
    print(" ")
    print("-------------------------------------------> 🎉🎊 WELCOME TO 'ABC' BANK  🎊🎉 <--------------------------------------------")
    print("_____________________________________________________________________________________________________________________________")
    print(" ")
    print("")
    while True:
        print("TO CONTINUE, CHOOSE AN OPTION - If you are new , Why don't you try to create an account? ☺️")
        print("-----------------------------------------------------------------------------------------------------------------------------")
        print("0. HELP")
        print("1. Create an Account")
        print("2. Delete an Account")
        print("3. Update an Account")
        print("4. Deposit Money")
        print("5. Debit Amount")
        print("6. Balance Enquiry")
        print("7. Display Account Details")
        print("8. EXIT")
        print("-----------------------------------------------------------------------------------------------------------------------------")
        option = int(input("Enter your option : "))

        if option == 0 :
            option = more_operations()
        if option == 1 :
            create_account()
        elif option == 2 :
            delete_account()
        elif option == 3 :
            update_account()
        elif option == 4 :
            deposit_money()
        elif option == 5 :
            debit_amount()
        elif option == 6 :
            balance_enquiry()
        elif option == 7 :
            display_details()
        elif option == 8 :
            print("--------------------------------------------------THANKS FOR USING OUR SERVICES....☺️--------------------------------------------")
            print("_____________________________________________________________________________________________________________________________")

            break
        else :
            print("PLEASE ENTER A VALID OPTION ! --------------------------->")