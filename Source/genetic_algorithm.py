import pandas as pd
import numpy as np

def random_generation(generation_size, genes):

    # create dataframe for gene pool
    generation = pd.DataFrame(columns=['Sequence','Chromosome','Generation','Birth','Fitness','Parents'])

    # for each chromosome
    for i in range(generation_size):

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
    n_elites = generation['Elite'].count()
    
    # for each mutant
    for i in range(mutants):
        
        # create mutant pheontype
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
        for i in range(len(bits_to_flip)):
            if not int(bits_to_flip[i]):
                mutant += parent[i]
            else:
                mutant += str(abs(int(parent[i]) - 1))
                
        chromosome['Chromosome'] = mutant
                
        # check for uniqueness and add to gene pool
        if chromosome['Chromosome'] not in generation['Chromosome']:
            generation = generation.append(chromosome, ignore_index=True)
            
    # return the generation
    return generation