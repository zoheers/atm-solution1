# allowed papers: 100, 50, 10, 5, and rest of request

money = 500
request = 277

def ATM(request,money):
    if request <=0:
        print "shoud be positive number "
    elif money > request :
            money -= request
            while request > 0:
                    if request>100 :
                        print "give 100"
                        request-=100
                    elif request>50 :
                        print "give 50"
                        request-=50
                    elif request>10 :
                        print "give 10"
                        request-=10
                    elif request>5 :
                         print "give 5"
                         request-=5
                    else :
                          print "give " , request
                          request=0
    print "money = " +str(money )

                       
ATM (request,money )  
          
                
    
