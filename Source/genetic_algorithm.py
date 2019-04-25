import pandas as pd
import numpy as np

def random_generation(phenotypes, genes):

    # create dataframe for gene pool
    generation = pd.DataFrame(columns=['Phenotype','Generation','Birth','Elite','Fitness'])

    # for each phenotype
    for i in range(phenotypes):

        # create random pheontype
        phenotype = {}
        phenotype['Phenotype'] = ''.join(str(x) for x in list(np.random.randint(2, size=genes)))
        phenotype['Generation'] = 1
        phenotype['Birth'] = 'Random'
        phenotype['Elite'] = False

        # check for uniqueness and add to gene pool
        if phenotype['Phenotype'] not in generation['Phenotype']:
            generation = generation.append(phenotype, ignore_index=True)

    # print the generation
    return generation