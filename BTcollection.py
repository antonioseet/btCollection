#import bluetooth
import time
        
def main():
    # Read source files and convert into two lists, one for Bluetooth adresses and one for names. 
    ## WILL REPLACE WITH TUPLES or USER class list.
    ### This should also take into account the points lists.
    addressesArray = [line.rstrip('\n') for line in open("BTaddresses.txt", "r")]
    namesArray = [line.rstrip('\n') for line in open("BTnames.txt", "r")]
    timesProgramRan = 1
    
    """
    #Infinite loop that looks for new devices until program is stopped.            timesProgramRan = 1
    while True:

        newDevices = False
        print("Run #" + str(timesProgramRan))
        print("Searching...")

        nearby_devices = bluetooth.discover_devices(duration=2, lookup_names=True)
        print("Devices* in range" + str(nearby_devices))

        # Loop that checks all unknown addresses and adds them to the list.
        for addr, name in nearby_devices:
            if(addr not in addressesArray):
                addressesArray.append(addr)

            if(name not in namesArray):
                print ("NEW DEVICE: " + str(name))
                newDevices = True
                namesArray.append(name)
                
        if(newDevices):
            print("Saving...")
            writeFiles(namesArray, addressesArray)
        else:
            print("No new devices to save.")
                
        timesProgramRan = timesProgramRan + 1
        print()
        time.sleep(2)
        """


# update names and addresses        
def writeFiles(namesList, addressList):
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
                print ("Files saved!\n")

main()
