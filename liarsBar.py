# This probability distribution is only valid for Devil version

# Globals
totalCards = 20
favCards = 8
normCards = 12

# 2 <= playersPlaying <= 4
# 0 <= favYouHave <= 5

def varFact(start, howManyTimes):
    # End is not included
    product = 1
    for i in range(howManyTimes):
        product *= start-i
    return product

def nChoosek(n, k):
    product = varFact(n, k)/varFact(k, k)
    return product



def ProbabilityDistribution(playersPlaying, favYouHave):
    # This is probability of exactly one given that I have seen my 5 cards. This is the case for players Playing
    remainingCards = (playersPlaying-1)*5
    favRemaining = favCards - favYouHave
    normRemaining = normCards - (5-favYouHave)
    PExactlyXs = []
    
    for i in range(1, min(favRemaining, remainingCards)+1):
        PExactlyX = nChoosek(remainingCards, i)*varFact(favRemaining, i)*varFact(normRemaining, min(remainingCards-i, normRemaining))/varFact(totalCards-5, remainingCards)
        PExactlyXs.append(PExactlyX)


        
    return PExactlyXs


def Exactly(PExactlyXs):
    length = len(PExactlyXs)
    sum = 0
    decidingProbability = 0.8
    for i in PExactlyXs:
        sum += i
        if sum >= decidingProbability:
            print(PExactlyXs)
            return f"There are probably atmost {PExactlyXs.index(i)+1} fav cards"
    


print(Exactly(ProbabilityDistribution(2, 3)))


