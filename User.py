class User:
    def __init__(self, name, BTid, points):
        self.name = name
        self.BTid = BTid
        self.points = points
        self.status = False

    def addPoints(self, newPoints):
        self.points += newPoints

    def toString(self):
        # based on name length, make the spaces a different length so the all match.
        spacesArray = [] # 10 spaces
        spacesStr = ""
        nameLength = len(self.name)
        spaceLength = 15 - nameLength
        if(spaceLength < 0):
            spaceLength = 0
        # create an array with the correct number of spaces
        for i in range (spaceLength):
            spacesArray.append(" ")

        # create a string with the right number of spaces based on the array
        for spaceItem in spacesArray:
            spacesStr += spaceItem
            

        return self.name + spacesStr + " | Total points:  " + str(self.points)

    def toFile(self):
        return self.name + "~" + self.BTid + "~" + str(self.points)


    def setActive(self, status):
        self.status = status

    def isActive(self):
        return (self.status)