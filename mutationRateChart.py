import ga_words
import ga_words_population
import matplotlib.pyplot as plt
import time

#10 random strings
#figure out how to generate in code
target = ["jXySgdZ0S2","aaB4byAytR","yjRL53yMr7","jAQuu6cXyy","FQ8ohbHF1i",
          "9Ei4Jn06h1","WafCYz1xil","7biRCOPa2E","INxUFVbbzM","tLYIjK84tS"]
#targetIncreasingLength = ["a"*x for x in range(1,40)]


tLength = [len(x) for x in target]

mutationRate = [x*.01 for x in range(21)]
numGens = [x*25 for x in range(13)]
totalPop = [x*50 for x in range(1,110)]

gentoSolve = []
avgFit = []
poolSize = []
best = []
bestFit = []
runTime = []

for x in totalPop:
    popul = ga_words_population.pop(x, tLength[1], mutationRate[2])
    print("Population: ", x)
    start = time.time()
    for i in range(numGens[5]):
        popul.draw(target[1])
        #print(i)
        #print(len(popul.matingPool) / len(popul.population))
        #print(len(popul.matingPool))

        #print(popul.averageFitness)
        if popul.targetFound(target[1]):
            gentoSolve.append(i)
            end = time.time()
            runTime.append(end-start)
            print("Target found in ", (end-start), " seconds")
            print("Target found in ", i ," generations")
            break

    if not popul.targetFound(target[1]):
        gentoSolve.append(0)
        runTime.append(0)
        print("Target found not found")

    #print("avg", popul.averageFitness)
    avgFit.append(popul.averageFitness)
    #print("MatingPool Size: ", len(popul.matingPool))
    poolSize.append(len(popul.matingPool))
    #print("best ", repr(popul.bestSoln.getPhrase()))
    best.append(repr(popul.bestSoln.getPhrase()))
    #print("best " , popul.bestFitness)
    bestFit.append(popul.bestFitness)
#for x, i in enumerate(target):


plt.plot(totalPop, runTime)
plt.show()
#print(runTime)
