import random
import ga_words
import ga_words_population
import matplotlib.pyplot as plt

mutationRate = .01
totalPop = 300

target = "The mountains"
tLength = len(target)
#print(tLength)
# def setup():
#     population = [ga_words.DNA(tLength) for i in range(totalPop)]
#         #print(repr(population[i].getPhrase()))
#     return population

#def draw():
    #print(population)
    #for element in population:
    #    print(repr(element))
    # for dna in population:      #sets fitness
    #     dna.fitness(target)
    #
    # for dna in population:
    #     for x in range(int(dna.fitness*100)):
    #         matingPool.append(dna)
    #
    # for i, d in enumerate(matingPool):
    #     print(i)
    #     print(d)
    # # for dna in population:
    # #     partnerA = matingPool[random.randint(0, len(matingPool)-1)]
    # #     partnerB = matingPool[random.randint(0, len(matingPool)-1)]
    # #     child = partnerA.crossover(partnerB)
    # #     child.mutate()
    # #     dna = child
#
# population = setup()
# draw()

# while(True):
#     for dna in popul.population:
#         if (dna.getPhrase() == target):
#             break
#     else:
#         popul.draw(target)
# #
for x in range(5):
    popul = ga_words_population.pop(totalPop, tLength, mutationRate)
    print(x)
    for i in range(100):
        popul.draw(target)
        #print(i)
        #print(len(popul.matingPool) / len(popul.population))
        #print(len(popul.matingPool))

        #print(popul.averageFitness)
        if popul.targetFound(target):
            print("Target found in ", i ," generations")
            break
    print("avg", popul.averageFitness)
    print("MatingPool Size: ", len(popul.matingPool))
    print("best ", repr(popul.bestSoln.getPhrase()))
    print("best " , popul.bestFitness)
