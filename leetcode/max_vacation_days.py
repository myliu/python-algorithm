# Longest valid flight time
MAX_DISTANCE = 6

def max_vacation(dists, vacs_week_office):
    # Calculate valid neighbours
    valid_neighbours = []
    for offices in dists:
        valid_neighbours += [i for i in range(len(offices)) if offices[i] <= MAX_DISTANCE],
    # print valid_neighbours

    # Build the dynamic programming board (table)
    board = []
    board += [[-1, v] for v in vacs_week_office[0]], # first week
    for week in range(1, len(vacs_week_office)): # rest of the weeks
        this_week = []
        for office in range(len(vacs_week_office[week])):
            max_vacs = 0
            max_source = -1
            for neighbour in valid_neighbours[office]:
                if board[week-1][neighbour][1] > max_vacs:
                    max_source = neighbour
                    max_vacs = board[week-1][neighbour][1]
            this_week += [max_source, max_vacs + vacs_week_office[week][office]],
        board += this_week,

    for row in board:
        print row

    # Find the max, and iterate backwards
    index = 0
    max_vacs = board[-1][0][1]
    for office in range(len(board[-1])):
        if board[-1][office][1] > max_vacs:
            max_vacs = board[-1][office][1]
            index = office

    solution = [-1] * len(vacs_week_office)
    week = len(solution) - 1
    while week >= 0:
        solution[week] = index
        index = board[week][index][0]
        week -= 1

    # Done
    return solution

dists = [[0, 5, 9],
         [5, 0, 5],
         [9, 5, 0]]

vacs_week_office = [[2, 0, 1],
                    [0, 3, 2],
                    [2, 0, 0]]

print max_vacation(dists, vacs_week_office)