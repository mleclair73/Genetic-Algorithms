import ga_words
import random

class pop:
    matingPool = []
    averageFitness = 0
    bestFitness = 0
    bestSoln = ga_words.DNA()
    def __init__(self, totalPopSize, tLength, mRate):
        self.population = [ga_words.DNA(tLength) for i in range(totalPopSize)]
        self.mutationRate = mRate

    def targetFound (self, target):
        if self.bestSoln.getPhrase == target:
            return True
        return False

    def draw(self, target):
        self.averageFitness = 0
        for dna in self.population:                                #sets fitness
            dna.setFitness(target)                                 #set dna fit
            self.averageFitness += dna.fitness                     #inc. avg fit
            if (dna.fitness > self.bestFitness):                   #if this fit is largest make best
                self.bestSoln = dna
                self.bestFitness = dna.fitness
        self.averageFitness /= len(self.population)

        for dna in self.population:
            for x in range(int(dna.fitness * (1000))):
                self.matingPool.append(dna)

        # for i, d in enumerate(self.matingPool):
        #     print(i)
        #     print(d)

        for i, dna in enumerate(self.population):
            if(len(self.matingPool) > 0):
                partnerA = self.matingPool[random.randint(0, len(self.matingPool)-1)]
                partnerB = self.matingPool[random.randint(0, len(self.matingPool)-1)]
                child = partnerA.crossover(partnerB)
                child.mutate(self.mutationRate)
                self.population[i] = child
