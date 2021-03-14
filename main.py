from User import User
import bluetooth
import time

        
def main():

    # Get all users specified in file
    userList = populateUsersFromFile()

    ###### For testing purposes, let's print all the users from our users.txt file #####
    print(summary(userList))
    #exit()

    #Infinite loop that looks for users indefinitely
    while True:
        lookFor(userList)
        print(summary(userList))
        #writeFiles(userList)
        time.sleep(5)
    

# This method will take the users stored in users.txt
# Returns: List of User objects
def populateUsersFromFile():

    userList = []

    #Initiate Users with points from the points.txt file
    with open("users.txt", "r") as usersFile:

        # Read the users file and place contents in this 
        usersData = usersFile.read()

        # Get each line of text file into an array
        # usersArray contains an array of all users raw data
        # If there is a space in the name, the split will not work.
        # when new devices with spaces in their names appear, rewrite them with underscores to save
        usersArray = usersData.split()
        print(usersArray)

        # for every user in the array, create a user object with the provided params and add it to the users array
        for user in usersArray:
            userTruple = user.split("~") # splits user line into ["name", "BT ID", "100"]
            newUser = User(userTruple[0], userTruple[1], int(userTruple[2]))
            userList.append(newUser)

    return userList

    
## Iterates through the list of users and looks for the Bluetooth Address
def lookFor(userList):

    # standard points
    stdPoints = 10

    # change this to for user in userList
    for user in userList:
        print("Looking for: " + user.name)
        result = bluetooth.lookup_name(user.BTid, timeout=4) # result contains the name of the device being searched
        findNearbyDevices(10) # prints any discoverable device nearby

        # if we find the user close by:
        # Add points, change status
        if(result != None):
            user.addPoints(stdPoints)
            user.setActive(True)
            print("+10")

            # FYI
            print(result)
        else:
            user.setActive(False)
            user.addPoints(-1)
            print("-1")

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

def findNearbyDevices(n):
    # nearby devices is a list of tuples, First: BTid, Second: Name
    nearbyDevices = bluetooth.discover_devices(duration=n, lookup_names=True, flush_cache=True, lookup_class=False)
    print(nearbyDevices)
    
    # if nearbydevices is not empty, we want to create new users and add them to the list.
    # if BTid already in our list of registered users, ignore it.
    # make function return a list of users, add them where we call this.
    # if dupllicate names with same BTid, put a (2) next to it, and (3) ... (n)
    

# returns a string summary of all users
def summary(userList):
    s = ""
    for user in userList:
        s += user.toString() + "\n"
    return s
                    


main()
