import words_dna
import words_dna_population
import matplotlib.pyplot as plt
import time

#10 random strings
target = ["jXySgdZ0S2","aaB4byAytR","yjRL53yMr7","jAQuu6cXyy","FQ8ohbHF1i",
          "9Ei4Jn06h1","WafCYz1xil","7biRCOPa2E","INxUFVbbzM","tLYIjK84tS"]
tLength = [len(x) for x in target]
mutationRate = [x*.01 for x in range(21)]
numGens = [x*25 for x in range(13)]
totalPop = [x*50 for x in range(1,110)]

gentoSolve = []
#avgFit = []
#poolSize = []
#best = []
#bestFit = []
runTime = []

#iterate through each population size
for x in totalPop:

    #initialize population of given size
    popul = words_dna_population.pop(x, tLength[1], mutationRate[2])
    start = time.time()

    #run for numGens[5] generations
    for i in range(numGens[5]):

        #draw towards target 1
        popul.draw(target[1])

        #target found handler
        if popul.targetFound:
            gentoSolve.append(i)
            end = time.time()
            runTime.append(end-start)
            break

    #target not found handler
    if not popul.targetFound:
        gentoSolve.append(0)
        runTime.append(0)

    # store other values
    # avgFit.append(popul.averageFitness)
    # poolSize.append(len(popul.matingPool))
    # best.append(repr(popul.bestSoln.getPhrase()))
    # bestFit.append(popul.bestFitness)

plt.xlabel("Total Population Size")
plt.ylabel("Runtime (s)")
plt.title("Total Population Size v. Runtime")
plt.plot(totalPop, runTime)
plt.show()

print("Runtime = ", fin-init)
