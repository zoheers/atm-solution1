balance = 500

request = 275
def withdraw(balance,request): 
    print "---------new withdraw --------------"
    print "Current balance = "+ str(balance)
    print "--"
    if   request > balance:
       print("Can't give you all this money !!")

    elif request < 0:
        print("More than zero plz!")

    else:
        
        balance-=request
        while request > 0:
             if request >= 100:
                request -= 100
                print("give 100")
             elif request >= 50:
                 request -= 50
                 print("give 50")
             elif request >= 10:
                request -= 10
                print("give 10")
             elif request >= 5:
                request -= 5
                print("give 5")
             elif request < 5:
                print("give " + str(request))
                request = 0
    print "the new balance = ", balance
    return balance
balance=withdraw(balance,-20)
balance=withdraw(balance,600)
balance=withdraw(balance,request)
balance=withdraw(balance,balance)


