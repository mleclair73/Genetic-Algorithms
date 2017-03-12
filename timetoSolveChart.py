import ga_words
import ga_words_population
import matplotlib.pyplot as plt
import time
import random

#10 random strings
#figure out how to generate in code
target = ["jXySgdZ0S2","aaB4byAytR","yjRL53yMr7","jAQuu6cXyy","FQ8ohbHF1i",
          "9Ei4Jn06h1","WafCYz1xil","7biRCOPa2E","INxUFVbbzM","tLYIjK84tS"]
targetIncreasingLength = ["a"*x for x in range(1,40)]
tLength = [len(x) for x in target]
mutationRate = [x*.01 for x in range(21)]
numGens = [x*25 for x in range(1,13)]
totalPop = [x*100 for x in range(1,50)]
prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']

gentoSolve = []
avgFit = []
poolSize = []
best = []
bestFit = []
runTime = []
init = time.time()

for popSize in totalPop[:10]:
    tmp_gentoSolve = []
    tmp_avgFit = []
    tmp_poolSize = []
    tmp_best = []
    tmp_bestFit = []
    tmp_runTime = []
    for word in targetIncreasingLength[:16]:

        popul = ga_words_population.pop(popSize, len(word), mutationRate[2])
        #print(x)
        start = time.time()

        for i in range(numGens[1]):
            popul.draw(word)
            #print(i)
            #print(len(popul.matingPool) / len(popul.population))
            #print(len(popul.matingPool))

            #print(popul.averageFitness)
            if popul.targetFound:
                tmp_gentoSolve.append(i)
                #print("Target found in ", i ," generations")
                break
        end = time.time()
        tmp_runTime.append(end-start)
        if not popul.targetFound:
            tmp_gentoSolve.append(0)
            #print("Target found in ", 0 ," generations")
            break
        #print(end-start, "seconds")

        #############################################
        #store iteration data
        #print("avg", popul.averageFitness)
        tmp_avgFit.append(popul.averageFitness)
        #print("MatingPool Size: ", len(popul.matingPool))
        tmp_poolSize.append(len(popul.matingPool))
        #print("best ", repr(popul.bestSoln.getPhrase()))
        tmp_best.append(repr(popul.bestSoln.getPhrase()))
        #print("best " , popul.bestFitness)
        tmp_bestFit.append(popul.bestFitness)

    #store run data
    #print(tmp_gentoSolve)
    gentoSolve.append(tmp_gentoSolve)
    avgFit.append(tmp_avgFit)
    poolSize.append(tmp_poolSize)
    best.append(tmp_best)
    bestFit.append(tmp_bestFit)
    runTime.append(tmp_runTime)
    #print(gentoSolve)

#for x, i in enumerate(target):
fin = time.time()
plt.figure(1)
plt.xlabel("String Length")
plt.ylabel("Generations to Solve")
plt.title("String Length v. Generations to Solve")


print(gentoSolve)
for i, popSizeResult in enumerate(gentoSolve[:10]):
    plt.plot(popSizeResult, color=random.choice(colors), label=totalPop[i])
plt.legend(loc=0)


plt.figure(2)
plt.xlabel("String Length")
plt.ylabel("Time to Solve (s)")
plt.title("String Length v. Time to Solve")
for i, popSizeResult in enumerate(runTime[:10]):
    plt.plot(popSizeResult, color=random.choice(colors), label=totalPop[i])
plt.legend(loc=0)
plt.show()

print(fin-init)
