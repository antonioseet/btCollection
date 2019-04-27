import bluetooth
import time


        
def main():
    # Read source files and convert into lists
    with open("BTaddresses.txt", "r") as addresses:
        with open("BTnames.txt", "r") as names:
            # List part
            addressFile = addresses.read()
            addressesArray = addressFile.split()

            namesFile = names.read()
            namesArray = namesFile.split()
            print("Names in File = "+str(namesArray))
            
            #Infinite loop that looks for new devices until program is stopped.            timesProgramRan = 1
            while True:

                nearby_devices = bluetooth.discover_devices(duration=2, lookup_names=True)
                print(str(nearby_devices)+" Devices Found during BT SEARCH")
                for addr, name in nearby_devices:
                    if(addr not in addressesArray):
                       addressesArray.append(addr)
                    if(name not in namesArray):
                        namesArray.append(name)

                print("Processing... " + str(addressesArray))
                print("Processing... " + str(namesArray))
                writeFiles(namesArray, addressesArray)

                
                
                print("Times program ran = " + str(timesProgramRan))
                timesProgramRan = timesProgramRan + 1
                time.sleep(2)
    


# update names and addresses        
def writeFiles(namesList, addressList):
    print("Saving...")
    with open("BTaddresses.txt", "r+") as addressFile:
        with open("BTnames2.txt", "r+") as namesFile:
                addressFile.truncate()
                namesFile.truncate()
                nameEntries = len(namesList)
                addressEntries = len(addressList)
                print(str(nameEntries) + " names to record. And " + str(addressEntries) + " addresses")

                #if(numEntries > 0):
                print(str(namesList) + "|" + str(addressList))

                    #Rewrite the BTaddress.txt & the BTnames.txt
                for i in range(nameEntries):
                    print ("i = " +str(i))
                    if i == nameEntries-1: #(is this the last item we are recording?)
                        namesFile.write(namesList[i])
                    else:
                        namesFile.write(namesList[i] + "\n")

                for i in range(addressEntries):
                    print(i)
                    if i == addressEntries - 1:
                        addressFile.write(addressList[i])
                    else:
                        addressFile.write(addressList[i] + "\n")
                print("SAVED!\n")




                    


main()
