import bluetooth
import time
        
def main():
    # Read source files and convert into lists
    addressesArray = [line.rstrip('\n') for line in open("BTaddresses.txt", "r")]
    namesArray = [line.rstrip('\n') for line in open("BTnames.txt", "r")]
    timesProgramRan = 1
    
    #Infinite loop that looks for new devices until program is stopped.            timesProgramRan = 1
    while True:
        nearby_devices = bluetooth.discover_devices(duration=2, lookup_names=True)
        print ("Discoverable devices in range" + str(nearby_devices))
        for addr, name in nearby_devices:
            if(addr not in addressesArray):
                addressesArray.append(addr)
            if(name not in namesArray):
                print ("NEW DEVICE: " + str(name))
                namesArray.append(name)
                
        writeFiles(namesArray, addressesArray)
                
        print("Times program ran = " + str(timesProgramRan))
        timesProgramRan = timesProgramRan + 1
        time.sleep(2)


# update names and addresses        
def writeFiles(namesList, addressList):
    print ("Saving...")
    with open("BTaddresses.txt", "r+") as addressFile:
        with open("BTnames.txt", "r+") as namesFile:
                addressFile.truncate()
                namesFile.truncate()
                nameEntries = len(namesList)
                addressEntries = len(addressList)

                    #Rewrite the BTaddress.txt & the BTnames.txt
                for i in range(nameEntries):
                    if i == nameEntries-1: # Add new line if more items pending
                        namesFile.write(namesList[i])
                        addressFile.write(addressList[i])
                    else:
                        namesFile.write(namesList[i] + "\n")
                        addressFile.write(addressList[i] + "\n")
                print ("SAVED!\n")

main()
