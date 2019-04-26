import pandas as pd
import numpy as np

def random_generation(generation_size, genes):

    # create dataframe for gene pool
    generation = pd.DataFrame(columns=['Sequence','Phenotype','Generation','Birth','Fitness','Parent'])

    # for each phenotype
    for i in range(generation_size):

        # create random pheontype
        phenotype = {}
        phenotype['Sequence'] = i+1
        phenotype['Phenotype'] = ''.join(str(x) for x in list(np.random.randint(2, size=genes)))
        phenotype['Generation'] = 1
        phenotype['Birth'] = 'Random'
        phenotype['Parent'] = 'None'

        # check for uniqueness and add to gene pool
        if phenotype['Phenotype'] not in generation['Phenotype']:
            generation = generation.append(phenotype, ignore_index=True)

    # return the generation
    return generation

def assign_elites(generation, elite_rate):
    
    # determine number of elites
    generation_size = generation.shape[0]
    elites = elite_rate * generation_size
    
    # assign elite status to most fit phenotypes
    generation['Elite'] = False
    generation = generation.sort_values(by='Fitness', ascending=False)
    generation.iloc[0:int(elites),6:7] = True
    
    # return the generation
    return generation

def select_elites(generation):
    elites = generation.loc[generation['Elite'] == True].copy()
    
    pool_size = generation['Sequence'].max()
    elites['Parent'] = elites['Sequence']
    elites['Sequence'] = range(pool_size + 1, pool_size + elites.shape[0] + 1)
    elites.loc[:,'Birth'] = 'Elitism'
    
    return elites