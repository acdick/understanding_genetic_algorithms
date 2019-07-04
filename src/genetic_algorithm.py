import battleship as ship
import pandas as pd
import numpy as np

def random_generation(generation_size, genes):

    # create dataframe for gene pool
    generation = pd.DataFrame(columns=['Sequence','Chromosome','Generation','Birth','Fitness','Parents'])

    # for each chromosome
    i = 0
    while i < generation_size:

        # create random chromosome
        chromosome = {}
        chromosome['Sequence'] = i+1
        chromosome['Chromosome'] = ''.join(str(x) for x in list(np.random.randint(2, size=genes)))
        chromosome['Generation'] = 1
        chromosome['Birth'] = 'Random'
        chromosome['Parents'] = 0

        # check for uniqueness and add to gene pool
        if chromosome['Chromosome'] not in generation['Chromosome']:
            generation = generation.append(chromosome, ignore_index=True)
            i += 1

    # return the generation
    return generation

def assign_elites(generation, elite_rate):
    
    # determine number of elites
    generation_size = generation.shape[0]
    elites = elite_rate * generation_size
    
    # assign elite status to most fit chromosomes
    generation['Elite'] = False
    generation = generation.sort_values(by='Fitness', ascending=False)
    generation.iloc[0:int(elites),6:7] = True
    
    # return the generation
    return generation

def select_elites(generation):
    
    # copy elites from old generation
    elites = generation.loc[generation['Elite'] == True].copy()
    
    # update attributes of new generation
    pool_size = generation['Sequence'].max()
    elites['Parents'] = elites['Sequence']
    elites['Sequence'] = range(pool_size + 1, pool_size + elites.shape[0] + 1)
    elites.loc[:,'Birth'] = 'Elitism'
    elites['Elite'] = False
    elites['Generation'] = generation['Generation'].max() + 1
    
    return elites

def create_mutants(generation, mutants, bit_flip_rate):
    
    # get generation attributes
    last_generation = generation['Generation'].max()
    last_sequence = generation['Sequence'].max()
    n_elites = generation['Birth'].value_counts()['Elitism']
    
    # for each mutant
    i = 0
    while i < mutants:
        
        # create mutant chromosome
        chromosome = {}
        chromosome['Sequence'] = last_sequence + i + 1
        chromosome['Generation'] = last_generation
        chromosome['Birth'] = 'Mutation'
        chromosome['Elite'] = False
        
        # select random elite as new parent
        parent_index = np.random.choice(n_elites)
        chromosome['Parents'] = list(generation['Sequence'].values)[parent_index]
        parent = list(generation['Chromosome'].values)[parent_index]

        # create array of random bit flips
        bit_flip_array = np.random.choice(2, len(parent), p=[1 - bit_flip_rate, bit_flip_rate])
        bits_to_flip = ''.join(str(x) for x in list(bit_flip_array.flatten()))

        # create mutant child from parent and flip bits from array
        mutant = ''
        for j in range(len(bits_to_flip)):
            if not int(bits_to_flip[j]):
                mutant += parent[j]
            else:
                mutant += str(abs(int(parent[j]) - 1))
        
        # check for uniqueness and add to gene pool
        chromosome['Chromosome'] = mutant
        if chromosome['Chromosome'] not in generation['Chromosome']:
            generation = generation.append(chromosome, ignore_index=True)
            i += 1
            
    # return the generation
    return generation

def create_splices(generation, n_splice_pairs):
    
    # get generation attributes
    last_generation = generation['Generation'].max()
    last_sequence = generation['Sequence'].max()
    n_elites = generation['Birth'].value_counts()['Elitism']
    
    # for each splice pair
    i = 0
    while i < n_splice_pairs:
        
        # create splice pair chromosome
        chromosome = {}
        chromosome['Generation'] = last_generation
        chromosome['Birth'] = 'Splice Pair'
        chromosome['Elite'] = False
        
        # select random elite pair as new parents
        parent_indices = np.random.choice(n_elites, 2, replace=False)
        chromosome['Parents'] = np.array(generation['Sequence'].values)[parent_indices]
        parents = np.array(generation['Chromosome'].values)[parent_indices]

        # create random splice bit
        splice_bit = np.random.randint(len(parents[0]))

        # create splice pair children from parent and cross over bits
        splices = []
        splices.append(parents[0][0:splice_bit] + parents[1][splice_bit:len(parents[1])])
        splices.append(parents[1][0:splice_bit] + parents[0][splice_bit:len(parents[0])])
        
        # add splices to gene pool
        chromosome['Chromosome'] = splices[0]
        chromosome['Sequence'] = last_sequence + i + 1
        generation = generation.append(chromosome, ignore_index=True)
        
        chromosome['Chromosome'] = splices[1]
        chromosome['Sequence'] = last_sequence + i + 2
        generation = generation.append(chromosome, ignore_index=True)
            
        i += 1
            
    # return the generation
    return generation

def fill_random(generation, generation_size, genes):
    
    # get generation attributes
    last_generation = generation['Generation'].max()
    last_sequence = generation['Sequence'].max()
    
    # for each random chromosome
    i = generation.shape[0]
    while i < generation_size:
        
        # create random chromosome
        chromosome = {}
        chromosome['Sequence'] = last_sequence + i + 1
        chromosome['Chromosome'] = ''.join(str(x) for x in list(np.random.randint(2, size=genes)))
        chromosome['Generation'] = last_generation
        chromosome['Birth'] = 'Random'
        chromosome['Parents'] = 0
        chromosome['Elite'] = False

        # check for uniqueness and add to gene pool
        if chromosome['Chromosome'] not in generation['Chromosome']:
            generation = generation.append(chromosome, ignore_index=True)
            i += 1
            
    # return the generation
    return generation

def create_descendents(gene_pool, elite_rate, solution, stop_limit):
    
    # copy initial generation
    next_generation = gene_pool.copy()
    generation_size = next_generation.shape[0]
    
    # create generations until fitness criteria is achieved
    while gene_pool['Fitness'].max() < stop_limit:
        
        # print current generation
        # print(str(gene_pool['Generation'].max()) + ': ' + str(gene_pool['Fitness'].max()))
        
        # select elites with elite rate
        next_generation = select_elites(next_generation)

        # add splice pairs to generation
        splice_pair_rate = elite_rate / 2
        n_splice_pairs = int(splice_pair_rate * generation_size)
        next_generation = create_splices(next_generation, n_splice_pairs)

        # add mutants to generation
        mutant_rate = 0.60
        bit_flip_rate = 0.01
        n_mutants = int(mutant_rate * generation_size)
        next_generation = create_mutants(next_generation, n_mutants, bit_flip_rate)

        # fill the rest of the generation with random chromosomes for diversity
        next_generation = fill_random(next_generation, generation_size, 100)

        # compare fitness
        next_generation['Fitness'] = next_generation.apply(lambda row: ship.accuracy(row.Chromosome, solution), axis=1)

        # assign elites with elite rate
        elite_rate = 0.20
        next_generation = assign_elites(next_generation, elite_rate)
        next_generation

        # add generation to gene pool
        gene_pool = gene_pool.append(next_generation)

    return gene_pool

def solve(solution, generation_size):
    # initialize the first random generation
    gene_pool = random_generation(generation_size, 100)

    # compare fitness
    gene_pool['Fitness'] = gene_pool.apply(lambda row: ship.accuracy(row.Chromosome, solution), axis=1)

    # assign elites with elite rate
    elite_rate = 0.20
    gene_pool = assign_elites(gene_pool, elite_rate)

    # create successive generations until termination criteria is met
    gene_pool = create_descendents(gene_pool, elite_rate, solution, 1.0)
    gene_pool = gene_pool.set_index('Sequence')
    
    return gene_pool