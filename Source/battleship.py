import numpy as np

# generate battleship board and solution
def new_board():
    
    # create a clear board
    dim = 10
    board = np.zeros((dim, dim), dtype=int)

    # randomly place ships on the board
    ship_lengths = [5, 4, 3, 3, 2]

    # for each ship
    for ship_length in ship_lengths:
        is_ship_placed = False

        while not is_ship_placed:
            # seed a coordinate for the head of a ship
            head = tuple(np.random.randint(dim, size=2))

            # choose a direction for the ship to be laid out
            # N=0, S=1, E=2, W=3
            heading = np.random.randint(4)

            # check that the ship does not hang off the edge of the board
            if heading == 0:
                tail = (head[0] - ship_length + 1, head[1])
            elif heading == 1:
                tail = (head[0] + ship_length - 1, head[1])
            elif heading == 2:
                tail = (head[0], head[1] + ship_length - 1)
            elif heading == 3:
                tail = (head[0], head[1] - ship_length + 1)

            if not ((0 <= tail[0] <= dim-1) and (0 <= tail[1] <= dim-1)):
                continue

            # check that the ship does not overlap with any others
            NS_min = min(head[0],tail[0])
            NS_max = max(head[0],tail[0])
            EW_min = min(head[1],tail[1])
            EW_max = max(head[1],tail[1])

            if sum(sum(board[NS_min:NS_max+1,EW_min:EW_max+1])) != 0:
                continue

            # place the ship
            board[NS_min:NS_max+1,EW_min:EW_max+1] = 1
            is_ship_placed = True
            
    #check number of pieces on the board
    if sum(ship_lengths) == sum(sum(board)):
        print('Correct number of pieces on board')
    else:
        print('Incorrect number of pieces on board')

    # represent board solution in genetic form
    genetic_solution = ''.join(str(x) for x in list(board.flatten()))
    
    return board, genetic_solution

# fitness function
def accuracy(solution, candidate):
    n_gene_matches = 0
    
    for i in range(len(solution)):
        if solution[i] == candidate[i]:
            n_gene_matches += 1
            
    return n_gene_matches / len(solution)