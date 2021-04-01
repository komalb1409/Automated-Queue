import queue
#from main import count
#print(count)
q = queue.Queue(maxsize=20)
def addQueue(c):
    q.put(c)
#delete and print current token
def cToken():
    currentToken =q.get()
    return currentToken
 
#server=["free","free","free"]
import array as arr
s = arr.array('i', [0,0,0])


#def customerType():
#def getwaitingTime():
  #  return waitingtime
#def incrementWaitingTime():
   # waitingtime+=1
#def setwaitingTime(time):
   # waitingtime=time


status="free"
def setBusy(n):
    s[n]=1
def setFree(n):
    s[n]=0
def getfreeServer():
    serverid=-1
    for i in range(3):
        if s[i]==0:
            return i
def noOfBusyServer():
    busy=0
    for i in range(3):
        if s[i]==1:
            busy=1+busy
    return busy
def setServerBusy(n):
    setBusy(n)
def setServerFree(n):
    setFree(n)
def staff(s1):
    print ("Do you want to set counter free")
    print("Press 1 if yes else any other number")
    ch=int(input())
    if ch==1:
     setServerFree(s1)
    else :
        b1=noOfBusyServer()
        print ("Number of busy counter are     "+str(b1))
        
        print("******************************************")
   
         
def server():
    for i in range( q.qsize()):
        b=noOfBusyServer()
       # print(b)
        #print (s)
        print("--------------------------------------")
        s1=getfreeServer()
        if b==3:
            print("No free counter kindly wait")
            
        else:
            s1=getfreeServer()


            setServerBusy(s1)
           # print(s)
            a= str(s1+1)
            b=str(cToken())
           
            print(a+"   Counter is free     "+" token number "+b+"  reach at desired counter ")
            #print("-------------------------------")
            # print(str("-------------------"))
            staff(s1)
        
            
def main():
    addQueue(1)
    addQueue(2)
    addQueue(3)
    addQueue(4)
    addQueue(5)
    
    server()
    
#print (count)

main()    
