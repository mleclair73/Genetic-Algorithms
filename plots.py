import ga_words
import ga_words_population
import matplotlib.pyplot as plt
import time

#10 random strings
#figure out how to generate in code
target = ["jXySgdZ0S2","aaB4byAytR","yjRL53yMr7","jAQuu6cXyy","FQ8ohbHF1i",
          "9Ei4Jn06h1","WafCYz1xil","7biRCOPa2E","INxUFVbbzM","tLYIjK84tS"]
targetIncreasingLength = ["a"*x for x in range(1,40)]


tLength = [len(x) for x in target]

mutationRate = [x*.01 for x in range(21)]
numGens = [x*25 for x in range(13)]
totalPop = [x*500 for x in range(1,11)]

gentoSolve = []
avgFit = []
poolSize = []
best = []
bestFit = []
runTime = []
init = time.time()
for x in targetIncreasingLength:
    popul = ga_words_population.pop(totalPop[2], len(x), mutationRate[2])
    #print(x)
    start = time.time()
    for i in range(numGens[5]):
        popul.draw(x)
        #print(i)
        #print(len(popul.matingPool) / len(popul.population))
        #print(len(popul.matingPool))

        #print(popul.averageFitness)
        if popul.targetFound(x):
            gentoSolve.append(i)
            #print("Target found in ", i ," generations")
            break
    end = time.time()
    runTime.append(end-start)
    if not popul.targetFound(x):
        gentoSolve.append(0)
        #print("Target found in ", 0 ," generations")
        break
    #print(end-start, "seconds")

    #print("avg", popul.averageFitness)
    avgFit.append(popul.averageFitness)
    #print("MatingPool Size: ", len(popul.matingPool))
    poolSize.append(len(popul.matingPool))
    #print("best ", repr(popul.bestSoln.getPhrase()))
    best.append(repr(popul.bestSoln.getPhrase()))
    #print("best " , popul.bestFitness)
    bestFit.append(popul.bestFitness)
#for x, i in enumerate(target):
fin = time.time()
plt.figure(1)
plt.xlabel("String Length")
plt.ylabel("Generations to Solve")
plt.title("String Length v. Generations to Solve")
plt.plot(gentoSolve)


plt.figure(2)
plt.xlabel("String Length")
plt.ylabel("Time to Solve (s)")
plt.title("String Length v. Time to Solve")
plt.plot(runTime)
plt.show()
print(fin-init)
