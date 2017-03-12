import words_dna
import words_dna_population
import matplotlib.pyplot as plt
import time

#10 random strings length 10
targetIncreasingLength = ["a"*x for x in range(1,40)]
mutationRate = [x*.01 for x in range(21)]
numGens = [x*25 for x in range(13)]
totalPop = [x*500 for x in range(1,11)]

gentoSolve = []
#avgFit = []
#poolSize = []
#best = []
#bestFit = []
runTime = []
init = time.time()

#iterate through targets in targetIncreasingLength
for x in targetIncreasingLength:

    #initialize population
    popul = words_dna_population.pop(totalPop[2], len(x), mutationRate[2])
    start = time.time()

    #run for n number generations
    for i in range(numGens[5]):
        popul.draw(x)

        #if target found handler
        if popul.targetFound:
            gentoSolve.append(i)
            break

    end = time.time()
    runTime.append(end-start)

    #if target not found handler
    if not popul.targetFound:
        gentoSolve.append(0)
        break

    # store other values
    # avgFit.append(popul.averageFitness)
    # poolSize.append(len(popul.matingPool))
    # best.append(repr(popul.bestSoln.getPhrase()))
    # bestFit.append(popul.bestFitness)


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

print("Runtime = ", fin-init)
