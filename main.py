from User import User
import bluetooth
import time
import random

        
def main():

    # Get all users specified in file
    userList = populateUsersFromFile("users.txt")

    ###### For testing purposes, let's print all the users from our users.txt file #####
    print(summary(userList))
    #exit()

    #Infinite loop that looks for users indefinitely
    while True:
        findNearbyDevices(userList, 10)
        lookForUser(userList)
        writeSaveFile(userList)
        time.sleep(10)

def mainTest():
    # Get all users specified in file
    userList = populateUsersFromFile("users.txt")

    ###### For testing purposes, let's print all the users from our users.txt file #####
    print(summary(userList))
    #exit()

    #Infinite loop that looks for users indefinitely
    while True:
        fakeNearby(userList) # bring in the user list to add new users if found.
        print(summary(userList))
        #lookForUser(userList)
        writeSaveFile(userList)
        time.sleep(10)
    

# This method will take the users stored in users.txt
# Returns: List of User objects
def populateUsersFromFile(filename):

    userList = []

    #Initiate Users with points from the points.txt file
    with open(filename, "r") as usersFile:

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

    
## Iterates through the list of users and looks for each Bluetooth Address in the array of users 
def lookForUser(userList):

    # standard points
    stdPoints = 10

    # change this to for user in userList
    for user in userList:
        print("Looking for: " + user.name)
        result = bluetooth.lookup_name(user.BTid, timeout=4) # result contains the name of the device being searched

        # if we find the user close by:
        # Add points, change status
        if(result != None):
            user.addPoints(stdPoints)
            user.setActive(True)
            print("+" + str(stdPoints))

            # FYI
            print(result)
        else:
            user.setActive(False)
            user.addPoints(-1)
            print("-1")
    
    print("Final results: \n " + summary(userList))

##Update files & Save point progress        
def writeSaveFile(userList):
    print("Saving...")

    usersFile = open("users.txt", "w")
        
    usersFile.truncate()
    length = len(userList)
    last = length - 1
    # Using length in order to detect last item
    for i in range(length):
        if(i != last):
            usersFile.write(userList[i].toFile() + "\n")
        else:
            usersFile.write(userList[i].toFile())
    print("SAVED")

def findNearbyDevices(userList, duration):
    # nearby devices is a list of tuples, First: BTid, Second: Name
    nearbyDevices = bluetooth.discover_devices(duration=duration, lookup_names=True, flush_cache=True, lookup_class=False)
    #print(nearbyDevices)
    
    # if dupllicate names with same BTid, put a (2) next to it, and (3) ... (n)
    for address, name in nearbyDevices:

        # if new address
        if(not addressInUserList(address, name, userList)):
            noSpacesName = noSpaces(name)
            # if the new address has the same name as another user
            if(nameInUserList(noSpacesName, userList)):
                n = 0
                # Generate a random 4 digit number
                for i in range(3):
                    n += random.randint(1,9)
                    n *= 10
                n += random.randint(0,9)
                noSpacesName = noSpacesName + " #" + str(n)
            
            print("saved: " + noSpacesName)

            newUser = User(noSpacesName, address, 0)
            userList.append(newUser)
                    
#fakes the response from finding devices
def fakeNearby(userList):
    nearbyDevices = [("74:42:2B:13:0B:C9", "iPhone"), ("74:42:1B:13:0B:C9", "iPhone 3"), ("74:42:7B:13:0B:C9", "iPhone 2"), ("74:42:8J:13:0B:C9", "iPhone 2")]
    for address, name in nearbyDevices:
        # if new address
        if(not addressInUserList(address, name, userList)):
            # if new address has the same name as another user
            noSpacesName = noSpaces(name)
            if(nameInUserList(noSpacesName, userList)):
                n = 0
                # Generate a random 4 digit number
                for i in range(3):
                    n += random.randint(1,9)
                    n *= 10
                n += random.randint(0,9)
                noSpacesName = noSpacesName + " #" + str(n)
            
            print("saved: " + noSpacesName)

            newUser = User(noSpacesName, address, 0)
            userList.append(newUser)

# checks if a list of users contains a user with the same BTid
def addressInUserList(BTid, name, userList):

    for user in userList:
        if(BTid == user.BTid):
            print(name + " ADDRESS already exists as: " + user.name)
            return True
    return False
# Checks if a list of users contains a user with the same name
def nameInUserList(name, userList):

    for user in userList:
        if(name == user.name):
            print(name + " NAME already exists as: " + user.name)
            return True
    return False


# returns a string summary of all users
def summary(userList):
    s = ""
    for user in userList:
        s += user.toString() + "\n"
    return s

## Returns a string with no spaces
def noSpaces(s):
    newString = ""
    for c in s:
        if(c == ' '):
            newString += '_'
        else:
            newString += c

    return newString



mainTest()
