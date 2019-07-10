DATA STRUCTURES AND ALGORITHMS
# Understanding Genetic Algorithms
SOLVING A BATTLESHIP BOARD GAME AS AN OPTIMIZATION PROBLEM

A genetic algorithm is a prime example of technology imitating nature to solve complex problems, in this case, by adopting the concept of natural selection in an evolutionary algorithm. Genetic algorithms, introduced in 1960 by John Holland, extend Alan Turing’s concept of a “learning machine” and are best-suited for solving optimization problems such as the traveling salesman.

To intuitively understand the practical implementation and fundamental requirements for employing genetic algorithms, we can set up a toy problem and solve the board of the classic guessing game, Battleship, first released by Milton Bradley in 1967. But rather than calling a sequence of individual shots, let’s ask our genetic algorithm to make a series of guesses of the entire board.

[Continue reading the full story curated by Towards Data Science, a Medium publication...](https://towardsdatascience.com/understanding-genetic-algorithms-cd556e9089cb?source=friends_link&sk=70e5b098ef167ff2d1132396ab441030)

## Repository Contents

* [Project Features](#project-features)
* [Source Code](#source-code)
* [Output Results](#output-results)
* [Contribute](#contribute)

## Project Features
ARTIFICIAL INTELLIGENCE | MACHINE LEARNING | OPTIMIZATION | EVOLUTIONARY ALGORITHMS | TOY PROBLEMS

<p align="center">
  <img src="/img/01_Battleship_Board_Solution.png" width="600" title="Board Solution">
</p>

- [x] **Random Board Generator for Battleship Game**<br>
Graphical and binary representation of a Battleship board game with 5 ships occupying 17 squares
- [x] **Implementation of Genetic Algorithm**<br>
Iterative solver that generates candidate solutions of an entire board of a random Battleship game, which converge to the genetic solution
- [x] **Genetic Selector: Elitism**<br>
The fittest chromosomes from the former generation that are selected to be parents of all of the chromosomes in a new generation.
- [x] **Genetic Operator: Crossover**<br>
Two chromosomes can be spliced at a random crossover gene and recombined to create two children, sharing gene chains from both parents.
- [x] **Genetic Operator: Mutation**<br>
Random genes of one chromosome can be inverted with bit flips to create a single child that exhibits a small genetic variation from its parent.

## Source Code
PYTHON | NUMPY | PANDAS

**[The Random Board Generator](https://gist.github.com/acdick/11d2bc2d3c046306a143fd5a0b24b6a9)**
1. Position the head of the ship with a random two-dimensional tuple
2. Orient the heading of the ship with a random cardinal direction
3. Locate the tail of the ship based on its head position, direction and length
4. Check that the tail of the ship remains within the boundaries of the board
5. Check that the ship does not overlap with any previously positioned ships
6. Repeat the process if the ship fails either of the two assertion tests

**[The Battleship Module](/src/battleship.py)**

* Random board generator for a new Battleship game
* Genetic representation of the board solution as binary representation
* Fitness function evaluator of a candidate solution based on accuracy

**[The Genetic Algorithm Module](/src/genetic_algorithm.py)**
* Random solution generator for first generation
* Assignment of elite chromosomes within a generation
* Selection of elite parents to populate a new generation with elite rate
* Creation of mutant descendents with bit flip rate
* Creation of splice pair descendents with number of splice pairs
* Filling of generation vacancies with random descendents
* Creation of descendent generations with specified population mix and termination criterion
* Solution driver to create generations until convergence to the genetic solution

## Output Results
SEABORN | MATPLOTLIB

**[Genetic Algorithm Demo](/src/genetic_algorithm_battleship.ipynb)**
1. Set up the board with random board generator
2. Generate candidate solution for the entire board
3. Determine fitness of candidate solution based on accuracy
4. Create descendent generations until convergence to the genetic solution
5. Describe fitness statistics of generations to inspect algorithm behavior
6. Solve 1,000 random board games to assess performance of model parameters of genetic algorithm

**Random Chromosome**
* 51 Occupied Squares (Solution: 1, Candidate: Red)
* 49 Unoccupied Squares (Solution: 0, Candidate: Blue)

<p align="center">
  <img src="/img/02_Battleship_Random_Guess_51.png" width="600" title="Random Guess">
</p>

**Accuracy Rate of Random Chromosome**
* 52% candidate accuracy
* 52 Matches (Green)
* 48 Mismatches (Red)

<p align="center">
  <img src="/img/03_Random_Accuracy_53.png" width="600" title="Random Accuracy">
</p>

**Fitness of Generation 1**<br>
* 10 Random chromosomes
* 2 top performers are 57% accurate
* Median fitness of generation is 52.5%

<p align="center">
  <img src="/img/04_Generation_001.png" width="600" title="Generation 001">
</p>

**Fitness of Generation 2**
* 10 total chromosomes
* 2 Elitism chromosomes (20% elite rate)
* 2 Splice Pair chromosomes (20% crossover rate)
* 6 Mutation chromosomes (60% mutation rate and 1% bit flip rate)
* 2 top performers improve fitness to be 60% and 58% accurate

<p align="center">
  <img src="/img/05_Generation_002.png" width="600" title="Generation 002">
</p>

**Fitness of Generation 155**
* 155 generations with 10 chromosomes per generation
* 1 Mutation chromosome converges to genetic solution

<p align="center">
  <img src="/img/06_Generation_155.png" width="600" title="Generation 155">
</p>

**Fitness Distribution Statistics for Generations 1 to 10**
* Natural selection gradually improves population fitness
* Dispersion is highest in the first random generation

<p align="center">
  <img src="/img/07_Stats_10.png" width="400" title="Statistics 010">
</p>

**Fitness Distribution Statistics for Generations 146 to 155**
* All generations are extremely fit with least fit chromosome having 95% accuracy
* Improved fitness is most likely to occur through mutation of a single gene
* High mutation rates and low bit flip rates give latter generations better chance to converge

<p align="center">
  <img src="/img/08_Stats_155.png" width="400" title="Statistics 155">
</p>

**Convergence of the Gene Pool Towards the Optimal Solution Over 155 Generations**
* First random generation will be 50% accurate
* Elitism guarantees that generational peak performance is monotonically increasing
* Crossover promotes substantial improvements to fitness in initial generations
* Mutation achieves convergence with genetic solution in latter generations

<p align="center">
  <img src="/img/09_Convergence.png" width="600" title="Convergence">
</p>

**Performance Metric of a Genetic Algorithm with Fixed Model Parameters Over 1,000 Samples**
* Genetic algoritm performance is influenced by nature of Battleship problem and the model parameters
* Performance can be measured by sampling and solving 1,000 random Battleship board games
* Model parameters can be tuned by using the performance distribution as an objective function

<p align="center">
  <img src="/img/10_Performance.png" width="600" title="Performance">
</p>

## Contribute

**Contact**
* [Email](mailto:adam.c.dick@gmail.com)
* [LinkedIn](https://www.linkedin.com/in/adamcdick/)
* [Medium](https://medium.com/@adam.c.dick)
* [Scholar](https://scholar.google.com/citations?user=eMO88ogAAAAJ&hl=en)

**License**
* [MIT License](https://github.com/acdick/understanding_genetic_algorithms/blob/master/LICENSE)
