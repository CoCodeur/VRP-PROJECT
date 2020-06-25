import numpy as np, random, operator, pandas as pd, matplotlib.pyplot as plt, time, os as os, json as json

from City import City
from Fitness import Fitness


def createRoute(cityList):
    route = random.sample(cityList, len(cityList))

    return route

def initialPopulation(popSize, cityList):
    population = []

    for i in range(0, popSize):
        population.append(createRoute(cityList))
    return population

def rankRoutes(population):
    fitnessResults = {}
    for i in range(0,len(population)):
        fitnessResults[i] = Fitness(population[i]).routeFitness()
    return sorted(fitnessResults.items(), key = operator.itemgetter(1), reverse = True)


def selection(popRanked, eliteSize):
    # Liste vide des resultats
    selectionResults = []
    # init d'un dataframe contenant notre population (avec un colonne ID et une avec son score Fitness)
    df = pd.DataFrame(np.array(popRanked), columns=["Index", "Fitness"])
    # ajout d'une colonne avec la valeur du fitness cumulé avec ceux ci-dessus
    df['cum_sum'] = df.Fitness.cumsum()
    # ajout d'une colonne avec le pourcentage de prise de cette individu.
    df['cum_perc'] = 100 * df.cum_sum / df.Fitness.sum()

    # ajout d'un ou des membre(s) élite(s) dans notre selection
    for i in range(0, eliteSize):
        selectionResults.append(popRanked[i][0])
    # choix de manière aléatoire d'individu (en fonction de son pourcentage)
    for i in range(0, len(popRanked) - eliteSize):
        pick = 100 * random.random()
        for i in range(0, len(popRanked)):
            if pick <= df.iat[i, 3]:
                selectionResults.append(popRanked[i][0])
                break
    return selectionResults

def matingPool(population, selectionResults):
    #liste des choix
    matingpool = []
    #Pour tout element des resultats, si l'index est égale à l'index de la selection, on l'ajoute dons notre liste
    for i in range(0, len(selectionResults)):
        index = selectionResults[i]
        matingpool.append(population[index])
    return matingpool


def breed(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []

    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))

    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childP1.append(parent1[i])

    childP2 = [item for item in parent2 if item not in childP1]

    child = childP1 + childP2
    return child


def breedPopulation(matingpool, eliteSize):
    children = []
    length = len(matingpool) - eliteSize
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0, eliteSize):
        children.append(matingpool[i])

    for i in range(0, length):
        child = breed(pool[i], pool[len(matingpool) - i - 1])
        children.append(child)
    return children


def mutate(individual, mutationRate):
    for swapped in range(len(individual)):
        if (random.random() < mutationRate):
            swapWith = int(random.random() * len(individual))

            city1 = individual[swapped]
            city2 = individual[swapWith]

            individual[swapped] = city2
            individual[swapWith] = city1

    return individual


def mutatePopulation(population, mutationRate):
    mutatedPop = []

    for ind in range(0, len(population)):
        mutatedInd = mutate(population[ind], mutationRate)
        mutatedPop.append(mutatedInd)
    return mutatedPop

def nextGeneration(currentGen, eliteSize, mutationRate):
    popRanked = rankRoutes(currentGen)
    selectionResults = selection(popRanked, eliteSize)
    matingpool = matingPool(currentGen, selectionResults)
    children = breedPopulation(matingpool, eliteSize)
    nextGeneration = mutatePopulation(children, mutationRate)
    return nextGeneration


def geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations):
    pop = initialPopulation(popSize, population)
    print("Initial distance: " + str(1 / rankRoutes(pop)[0][1]))

    for i in range(0, generations):
        pop = nextGeneration(pop, eliteSize, mutationRate)

    print("Final distance: " + str(1 / rankRoutes(pop)[0][1]))
    bestRouteIndex = rankRoutes(pop)[0][0]
    bestRoute = pop[bestRouteIndex]
    return bestRoute


def geneticAlgorithmPlot(population, popSize, eliteSize, mutationRate, generations):
    pop = initialPopulation(popSize, population)
    progress = []
    progress.append(1 / rankRoutes(pop)[0][1])

    for i in range(0, generations):
        pop = nextGeneration(pop, eliteSize, mutationRate)
        progress.append(1 / rankRoutes(pop)[0][1])

    plt.plot(progress)
    plt.ylabel('Distance')
    plt.xlabel('Generation')
    plt.show()

cityList = []

nombreVille = input('Selectionner le nombre de ville (10-1000) \n')

for i in range(0,int(nombreVille)):
    cityList.append(City(x=int(random.random() * 200), y=int(random.random() * 200)))

#geneticAlgorithm(population=cityList, popSize=100, eliteSize=20, mutationRate=0.01, generations=500)



#geneticAlgorithmPlot(population=cityList, popSize=100, eliteSize=20, mutationRate=0.01, generations=500)
path = os.path.join('JSON', 'test' + nombreVille + '.json')

resultat = []


for j in range(0, 5):
     start = time.time()
     geneticAlgorithm(population=cityList, popSize=100, eliteSize=50, mutationRate=0.01, generations=500)
     end = (time.time()) - start
     resultat.append(end)


with open(path, 'w') as f:
    json.dump(resultat, f)



