import random
import words_dna
import words_dna_population
import matplotlib.pyplot as plt

mutationRate = .01
target = "The mountains"
tLength = len(target)
totalPop = tLength * 26
num_gens = tLength * 10
trials = 5


for x in range(trials):
    popul = words_dna_population.pop(totalPop, tLength, mutationRate)
    print(x)
    for i in range(num_gens):
        popul.draw(target)
        #print(i)
        #print(len(popul.matingPool) / len(popul.population))
        #print(len(popul.matingPool))

        #print(popul.averageFitness)
        if popul.targetFound:
            print("Target found in ", i ," generations")
            break
    if not popul.targetFound:
        print("Target not found")
    print("avg", popul.averageFitness)
    print("MatingPool Size: ", len(popul.matingPool))
    print("best ", repr(popul.bestSoln.getPhrase()))
    print("best " , popul.bestFitness)
