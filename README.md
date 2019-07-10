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
MACHINE LEARNING | OPTIMIZATION | TOY PROBLEM

- [x] **Random Board Generator for Battleship Game**<br>
- [x] **Implementation of Genetic Algorithm**<br>
- [x] **Genetic Selector: Elitism**<br>
The fittest chromosomes from the former generation that are selected to be parents of all of the chromosomes in a new generation.
- [x] **Genetic Operator: Crossover**<br>
Two chromosomes can be spliced at a random crossover gene and recombined to create two children, sharing gene chains from both parents.
- [x] **Genetic Operator: Mutation**<br>
Random genes of one chromosome can be inverted with bit flips to create a single child that exhibits a small genetic variation from its parent.

## Source Code
PYTHON | NUMPY | PANDAS

**[The Battleship Module](/src/battleship.py)**

* Random board generator for Battleship game
  1. Position the head of the ship with a random two-dimensional tuple.
  2. Orient the heading of the ship with a random cardinal direction.
  3. Locate the tail of the ship based on its head position, direction and length.
  4. Check that the tail of the ship remains within the boundaries of the board.
  5. Check that the ship does not overlap with any previously positioned ships.
  6. Repeat the process if the ship fails either of the two assertion tests.
* Genetic representation of the board solution as binary list
* Fitness function evaluator of a candidate solution based on accuracy

**[The Genetic Algorithm Module](/src/genetic_algorithm.py)**
* Random solution generator for first generation
* Assignment of elite chromos within a generation
* Selection of elite parents to populate new generation
* Creation of mutant descendents
* Creation of splice pair descendents
* Filling of generation with random descendents
* Creation of descendent generation
* Evaluation of fitness of generation

## Output Results
SEABORN | MATPLOTLIB

**[Genetic Algorithm Demon](/src/genetic_algorithm_battleship.ipynb)**

**Binary Representation of Battleship Board with 5 Ships Occupying 17 Squares (Red 1)**
0000111000000000000000000111100000000000000001000000010100000001010000000101000010000100001000000000
![01 Board Solution](/img/01_Battleship_Board_Solution.png)

**Random Chromosome with 51 Occupied Squares (Red) and 49 Unoccupied Squares (Blue)**
![02 Random Guess](/img/02_Battleship_Random_Guess_51.png)

**Accuracy Rate of Random Chromosome with 52 Matches (Green) and 48 Mismatches (Red)**
![03 Random Accuracy](/img/03_Random_Accuracy_53.png)

**Fitness of 10 Random Chromosomes in Generation 1**
![04 Generation 001](/img/04_Generation_001.png)

**Fitness of 2 Elitism, 2 Splice Pair and 6 Mutation Chromosomes in Generation 2**
![05 Generation 002](/img/05_Generation_002.png)

**Fitness of 2 Elitism, 2 Splice Pair and 6 Mutation Chromosomes in Generation 155**
![06 Generation 003](/img/06_Generation_155.png)

**Fitness Distribution Statistics for Generations 1 to 10**
![07 Statistics 010](/img/07_Stats_10.png)

**Fitness Distribution Statistics for Generations 146 to 155**
![08 Statistics 155](/img/08_Stats_155.png)

**Convergence of the Gene Pool Towards the Optimal Solution Over 155 Generations**
![09 Convergence](/img/09_Convergence.png)

**Performance Metric of a Genetic Algorithm with Fixed Model Parameters Over 1,000 Samples**
![10 Performance](/img/10_Performance.png)

## Contribute

**Contact**
* [Email](mailto:adam.c.dick@gmail.com)
* [LinkedIn](https://www.linkedin.com/in/adamcdick/)
* [Medium](https://medium.com/@adam.c.dick)
* [Scholar](https://scholar.google.com/citations?user=eMO88ogAAAAJ&hl=en)

**License**
* [MIT License](https://github.com/acdick/understanding_genetic_algorithms/blob/master/LICENSE)
