from User import User
import bluetooth
import time


        
def main():
    #Initiate Users with points from the points.txt file
    with open("points.txt", "r") as points:

        #read the points file and turn into array
        pointsFile = points.read()
        pointsArray = pointsFile.split()
        
    ## WHENEVER YOU ADD A NEW USER
    ## REMEMBER TO ADD A NEW POINT VALUE TO "points.txt"
        tony = User("Tony", "3C:BB:FD:70:65:5E", int(pointsArray[0]))
        sam = User("Sam", "98:FE:94:64:db:69", int(pointsArray[1]))
        dave = User("David", "8C:8E:F2:4E:0E:11", int(pointsArray[2]))
        tony2 = User("S9+", "A4:07:B6:89:85:14", int(pointsArray[3]))

        userList = [tony,sam,dave,tony2]

        #Infinite loop that looks for users indefinitely
        while True:
    
            lookFor(userList)
            writeFiles(userList)
    
            time.sleep(10)
    
##goes through the list of users and looks for the Bluetooth Address
def lookFor(userList):

    for i in range(len(userList)):
    
        print ("Looking for: " + userList[i].name)
        result = bluetooth.lookup_name(userList[i].BTid , timeout=4)
        
    
        if(result != None):
            userList[i].points+=10
            userList[i].status = 1
            print ("+10 points!!")
            print ("Total: "+ str(userList[i].points))

            print ("RESULT: " + result)
        
        else:
            userList[i].status = 0
            print (userList[i].name +" is OUT")
            print ("Total: "+ str(userList[i].points))
        print ("")

##Update files & Save point progress        
def writeFiles(userList):
    print("Saving...")

    # nested with opens because we want to all three files at the same time
    with open("BTnames.txt", "r+") as names:
        with open("points.txt", "r+") as points:
            with open("status.txt", "r+") as status:
                points.truncate()
                status.truncate()
                names.truncate()
                numUsers = len(userList)

                #Rewrite the points.txt & the status.txt
                for i in range(numUsers):
                    if i == numUsers-1:
                        points.write(str(userList[i].points))
                        status.write(str(userList[i].status))
                        names.write(userList[i].name)
                    else:
                        points.write(str(userList[i].points) + "\n")
                        status.write(str(userList[i].status) + "\n")
                        names.write(userList[i].name + "\n")
                print("****Data saved: Safe to close****\n")




                    


main()
