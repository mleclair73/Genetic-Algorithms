# Word Guessing Genetic Algorithm

## Overview
This project showcases a simple implementation of a genetic algorithm used to guess a string. The algorithm first generates a number of random guesses the length of the target. These guesses are then scored and given a chance to reproduce (randomly cross with another guess) proportional to their score. During the crossover, each position has a small chance of random mutation, to help the algorithm converge if the correct letter any position is not present in the initial random sample.

## Future Improvements
* Creating a more general dna and population class definition to guess different types of data such as images, or an encoded behavior for a virtual creature.
* Further evaluation of performance, and optimization of search using population size and mutation rate
* Capped mating pool size or more efficient system for mating pool to improve performance

## Plot 1
!(/Plots/Population Size v Generations to Solve 100-1000 Population.png)

## Plot 2
!(/Plots/Population Size v Time to Solve.png)

## Plot 3
!(/Plots/String Length v Generations to Solve (pop 1000).png)

## Plot 4
### Log Scale
!(/Plots/String Length v Generations to Solve.png)
