# allowed papers: 100, 50, 10, 5, and rest of request

money = 500
request = 277

def ATM(request,money):
    if money > request :
        money -= request
        while request > 0:
                if request>100 :
                    print "give 100"
                    request-=100
                else :
                    if request>50 :
                        print "give 50"
                        request-=50
                    else :
                        if request>10 :
                            print "give 10"
                            request-=10
                        else :
                            if request>5 :
                                print "give 5"
                                request-=5
                            else :
                                print "give " , request
                                request=0
    print "money = " +str(money )

                       
ATM (request,money )            
                
    
