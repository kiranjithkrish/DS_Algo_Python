def validStartingCityOne(distances, fuel, mpg):
    noOfCities = len(distances)
    for startingCityIdx in range(len(distances)):
        milesRemaining = 0
        for currentCityIdx in range(startingCityIdx, startingCityIdx+noOfCities):
            currentCityIdx = currentCityIdx%noOfCities
            if milesRemaining<0:
                break
            distanceToGo  = distances[currentCityIdx]
            fuelAtCity = fuel[currentCityIdx]
            milesRemaining  += fuelAtCity*mpg-distanceToGo
        if milesRemaining>=0:
            return startingCityIdx       
    return -1

def validStartingCityTwo(distances, fuel, mpg):
    noOfCities = len(distances)
    milesRemaining = 0
    minIndex = 0
    minMilesRemaining = 0
    for currentCityIdx in range(noOfCities):
        currentCityIdx = currentCityIdx%noOfCities
        if milesRemaining<minMilesRemaining:
            minMilesRemaining = milesRemaining
            minIndex = currentCityIdx
        distanceToGo  = distances[currentCityIdx]
        fuelAtCity = fuel[currentCityIdx]
        milesRemaining  += fuelAtCity*mpg-distanceToGo
    if milesRemaining>=0:
        return minIndex       
    return -1

    # def validStartingCityThree(distance, fuel, mpg):
    #     noOfCities = len(distances)
    #     minMilesRemainingCandidate = 0
    #     minCityCandidate = 0
    #     for currentCityIdx in range(1, noOfCities):
    #         distanceToPreviousCity = distances[currentCityIdx-1]
    #         fuelFromPreviousCity = fuel[currentCityIdx-1]
    #         milesRemaining = fuelFromPreviousCity*mpg - distanceToPreviousCity
    #         if milesRemaining<minMilesRemainingCandidate:
    #             minMilesRemainingCandidate = milesRemaining
    #             minCityCandidate = currentCityIdx
    #     return minCityCandidate

def validStartingCity(distances, fuel, mpg):
    fuelLeft = 0
    startingCity = 0
    totalFuel = 0
    numberOfCities = len(distances)
    for f in fuel:
        totalFuel += f
    totalMileage = mpg*totalFuel
    for i in range(numberOfCities):
        startingCity = i
        currentDistance = 0
        for j in range(i,len(distances)+i):
            city = j%len(distances)
            mileage = mpg*(fuel[city]+fuelLeft)
            if distances[city]>mileage:
                fuelLeft = 0
                break 
            else:
                fuelLeft = (mileage-distances[city])/mpg    
                currentDistance += distances[city]
        if currentDistance == totalMileage:
            return startingCity
    return -1


def circleArray(distances, start):
    for i in range(start,(len(distances)+start)):
        index = i%len(distances)
        print(distances[index])
distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10
#circleArray(distances, 3)
city = validStartingCityThree(distances, fuel, mpg)
print(city)