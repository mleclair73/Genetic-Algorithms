# Word Guessing Genetic Algorithm

## Overview
This project showcases a simple implementation of a genetic algorithm used to guess a string. The algorithm first generates a number of random guesses the length of the target. These guesses are then scored and given a chance to reproduce (randomly cross with another guess) proportional to their score. During the crossover, each position has a small chance of random mutation, to help the algorithm converge if the correct letter any position is not present in the initial random sample.

## Future Improvements
* Creating a more general dna and population class definition to guess different types of data such as images, or an encoded behavior for a virtual creature.
* Further evaluation of performance, and optimization of search using population size and mutation rate
* Capped mating pool size or more efficient system for mating pool to improve performance

## Plot 1

![](https://raw.githubusercontent.com/mleclair73/Genetic-Algorithms/blob/master/Plots/Population_Size_v_Generations_to_Solve_100-1000_Population.png)

## Plot 2
## Log Scale
![](https://raw.githubusercontent.com/mleclair73/Genetic-Algorithms/blob/master/Plots/Plots/Population_Size_v_Time_to_Solve.png)

## Plot 3
![](https://raw.githubusercontent.com/mleclair73/Genetic-Algorithms/blob/master/Plots/String_Length_v_Generations_to_Solve_1000_Population.png)

## Plot 4
### Log Scale
![](https://raw.githubusercontent.com/mleclair73/Genetic-Algorithms/blob/master/Plots/String_Length_v_Time_to_Solve.png)
