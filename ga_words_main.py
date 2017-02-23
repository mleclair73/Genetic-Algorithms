import random
import ga_words
import ga_words_population

mutationRate = .1
totalPop = 5000

target = "aaaaa"
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

popul = ga_words_population.pop(totalPop, tLength, mutationRate)
count = 0
# while(True):
#     for dna in popul.population:
#         if (dna.getPhrase() == target):
#             break
#     else:
#         popul.draw(target)
# #
for i in range(50):
    popul.draw(target)
    print(len(popul.population))
    print(len(popul.matingPool))

    print(popul.averageFitness)
    if popul.targetFound(target):
        break
    print("best ", repr(popul.bestSoln.getPhrase()))
    print("best " , popul.bestFitness)
