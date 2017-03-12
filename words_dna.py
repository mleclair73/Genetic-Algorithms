import random

class DNA:

    def __init__(self, tLength = 0, genes = None):
        if genes is None:
            self.genes = []
        for i in range(tLength):
            self.genes.append((chr(random.randint(32, 127))))
        self.fitness = 0


    def setFitness(self, target):
        self.length = len(target)
        score = 0
        for (i, letter) in enumerate(self.genes):
            if letter == target[i]:
                score = score + 1
        self.fitness = score/self.length * 100           #percent correct


    def crossover(self, partner):
        midpoint = random.randint(0,len(self.getPhrase()))
        child = DNA()
        for i, gene in enumerate(self.genes):
            if i > midpoint:
                child.genes.append(partner.genes[i])
            else:
                child.genes.append(self.genes[i])
        return child

    def mutate(self, mutationRate):
        for i in range(len(self.genes)):
            if(random.random() < mutationRate):
                self.genes[i] = chr(random.randint(32, 128))

    def getPhrase(self):
        return "".join(self.genes)
