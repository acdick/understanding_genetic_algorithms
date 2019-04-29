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
        chromosome['Sequence'] = last_sequence + i + 1
        chromosome['Generation'] = last_generation
        chromosome['Birth'] = 'Splice Pair'
        chromosome['Elite'] = False
        
        # select random elite pair as new parents
        parent_indices = np.random.choice(n_elites, 2*n_splice_pairs, replace=False)
        chromosome['Parents'] = np.array(generation['Sequence'].values)[parent_indices]
        parents = np.array(generation['Chromosome'].values)[parent_indices]

        # create random splice bit
        splice_bit = np.random.randint(len(parents[0]))

        # create splice pair children from parent and cross over bits
        splices = []
        splices.append(parents[0][0:splice_bit] + parents[1][splice_bit:len(parents[1])])
        splices.append(parents[1][0:splice_bit] + parents[0][splice_bit:len(parents[0])])
        
        # check for uniqueness and add to gene pool
        for splice in splices:
            chromosome['Chromosome'] = splice
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