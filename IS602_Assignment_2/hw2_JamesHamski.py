class CarEvaluation:
    'a simple class that represents a car evaluation'
    
    carCount = 0
    def __init__(self, brand, price, safety_rating):
        self.brand = brand
        self.price = price
        self.safety_rating = safety_rating

        CarEvaluation.carCount += 1

    def showEvaluation(self):
        'Describes the evaluation of each car in a sentence.'
        print "The %s has a %s price and it's safety is rated a %i" % (self.brand, self.price, self.safety_rating)

def sortbyprice(L, sort):
    'Sorts the prices from either least to greates (asc) or greatest to least (des)'
    #I feel like this is sloppy and could be way better
    if sort == "asc":
        sortBool = True
    else:
        sortBool = False

    for i in L:
        if i.price == "High":
            i.price = 1
        elif i.price == "Med":
            i.price = 2
        elif i.price == "Low":
            i.price = 3
    #useful: https://wiki.python.org/moin/HowTo/Sorting
    sortedList = sorted(L, key=lambda CarEvaluation: CarEvaluation.price, reverse = sortBool)
    brandSorted = []
    for i in sortedList:
        brandSorted.append(i.brand)
    return brandSorted

    
def searchforsafety(L, rating):
    'Using input of a list of class CarEvaluation and a rating integer, returns whether that rating exists (T/F)'
    ratingList = []
    for i in L:
        # should probably use "rating in L" format but am unsure how to deploy it across the list
        if i.safety_rating == rating:
            ratingList.append(i.safety_rating)
        return len(ratingList) >=1 


if __name__ == "__main__":
    eval1 = CarEvaluation("Ford", "High", 2)
    eval2 = CarEvaluation("GMC", "Med", 4)
    eval3 = CarEvaluation("Toyota", "Low", 3)

    print "Car Count = %d" % CarEvaluation.carCount

    eval1.showEvaluation()
    eval2.showEvaluation()
    eval3.showEvaluation()

    L = [eval1, eval2, eval3]

    print sortbyprice(L, "asc") #[Toyota, GMC, Ford]
    print sortbyprice(L, "des") #[Ford, GMC, Toyota]
    print searchforsafety(L, 2) #true
    print searchforsafety(L, 1) #falsse