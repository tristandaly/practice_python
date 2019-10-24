#Conway's Game of Life
import random
import time
import copy

WIDTH = 211
HEIGHT = 50

#Create a list of lists for the cells:
next_cells = []
for x in range(WIDTH):
    column = [] #Create a new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('.') # Add a living cell.
        else:
            column.append(' ') # Add a dead cell.
    next_cells.append(column) # next_cells is a list of column lists

while True: # Main program loop.
    print('\n\n\n\n\n') # Separate each step with newlines.
    current_cells = copy.deepcopy(next_cells)

    # Print current_cells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(current_cells[x][y], end='') # Print the # or space.
        print()

    # Calculate the next step's cells based on the current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coordinates:
            # '% WIDTH' ensures left_coord is always between 0 and WIDTH - 1
            left_coord = (x - 1) % WIDTH
            right_coord = (x + 1) % WIDTH
            up_coord = (y - 1) % HEIGHT
            down_coord = (y + 1) % HEIGHT

            # Count number of living neighbors:
            num_neighbors = 0
            if current_cells[left_coord][up_coord] is '.':
                num_neighbors += 1 # Top-left neighbor is alive.
            if current_cells[x][up_coord] is '.':
                num_neighbors += 1 # Up neighbor
            if current_cells[right_coord][up_coord] is '.':
                num_neighbors += 1
            if current_cells[left_coord][y] is '.':
                num_neighbors += 1
            if current_cells[right_coord][y] is '.':
                num_neighbors += 1
            if current_cells[left_coord][down_coord] is '.':
                num_neighbors += 1
            if current_cells[x][down_coord] is '.':
                num_neighbors += 1
            if current_cells[right_coord][down_coord] is '.':
                num_neighbors += 1

            # Set cell based on Conway's Game of Life rules:
            if current_cells[x][y] is '.' and (num_neighbors is 2 or num_neighbors is 3):
                # Living cells with 2 or 3 neigbors stay alive:
                next_cells[x][y] = '.'
            elif current_cells[x][y] is ' ' and num_neighbors is 3:
                # Dead cells with 3 neighbors become alive:
                next_cells[x][y] = '.'
            else:
                # Everything else dies or stays dead:
                next_cells[x][y] = ' '
    time.sleep(0.1) # Add pause to reduce flickering.
