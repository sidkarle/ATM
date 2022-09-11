user_input=int(input("Enter your 4 digit pin number: "))
limit = 25000
if(user_input == 1234):
    print("1-Withdraw")
    print("2-Balance Enquiry")
    print("3-Fast Cash")
    a = int(input("Please choose transactions: "))
    if (a == 1):
        w=int(input("Enter withdraw amount: "))
        if (w< limit and w%100 == 0):
            print("Please take your amount:", w)
        else:
             print("Invalid cash")

    elif(a==2):
        print("Your available amount : ",limit)

    elif (a == 3):
        print("1->5,000")
        print("2->10,000")
        print("3->15,000")
        print("4->20,000")
        f = int(input("Enter fast cash option: "))
        if (f == 1 and 5000 < limit):
            print("please take cash 5000")
        elif (f == 2 and 10000 < limit):
            print("please take cash 10000")
        elif (f == 3 and 15000 < limit):
            print("please take cash 15000")
        elif (f == 4 and 20000 < limit):
            print("please take cash 20000")
        else:
            print("Invalid fast cash option")
    else:
        print("Wrong choice")
else:
    print("Wrong pin number")
