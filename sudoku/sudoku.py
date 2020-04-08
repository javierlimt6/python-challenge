# Do not modify these helper functions!


def generate():
    '''
    Generates a 3x3 Sudoku puzzle.
    
    Usage:
    puzzle = generate(n)
    
    Return:
    3×3 nested list with some values filled.
    Empty values are represented by None.
    '''
    puzzle = [[None, 9, None],
              [3, None, 7],
              [None, 1, None]
              ]
    return puzzle


def get_unused(puzzle):
    '''
    Generates a list of integers (1 - 9 inclusive) that have not
    been used in puzzle.
    '''
    try:
        used = set(puzzle[0] + puzzle[1] + puzzle[2]) - {None}
    except Exception:
        raise
    unused = list(set(range(1,10)) - used)
    return unused


def get_unfilled(puzzle):
    '''
    Generates a list of unfilled coordinates that are unfilled
    in puzzle.
    
    Each coordinate is a tuple (y, x), where x & y are
    0-2 inclusive.
    '''
    unfilled = []
    for y in range(3):
        for x in range(3):
            try:
                if puzzle[y][x] is None:
                    unfilled.append((y, x))
            except Exception:
                raise
    return unfilled


def is_complete(puzzle):
    '''
    Check if any values in puzzle are empty (None).
    
    Return:
    False if any values are None.
    True if all values are not None.
    '''
    for i in range(3):
        # Check rows
        # Make a copy of the row to avoid modifying original
        line = puzzle[i].copy()
        if None in line:
            return False

        # Check cols
        line = [puzzle[0][i], puzzle[1][i], puzzle[2][i]]
        if None in line:
            return False
    return True


def is_correct(puzzle):
    '''
    Check if sum of all rows, columns, or diagonals is 15.
    
    Return:
    False if any row, column, or diagonal sum is not 15.
    True if all row, column, or diagonal sums are not 15.
    
    Error:
    ValueError if any values are empty (None)
    '''
    def sum_is_15(line):
        if sum(line) == 15:
            return True
        else:
            return False


    for i in range(3):
        # Check rows
        # Make a copy of the row to avoid modifying original
        line = puzzle[i].copy()
        if None in line:
            import pdb; pdb.set_trace()
            raise ValueError('puzzle is not complete (has None values)')
        elif not sum_is_15(line):
            return False

        # Check cols
        line = [puzzle[0][i], puzzle[1][i], puzzle[2][i]]
        if None in line:
            import pdb; pdb.set_trace()
            raise ValueError('puzzle is not complete (has None values)')
        elif not sum_is_15(line):
            return False

    # Check diags
    # No need to check diags for None since row & col check is sufficient
    line = [puzzle[0][0], puzzle[1][1], puzzle[2][2]]
    if not sum_is_15(line):
        return False
    line = [puzzle[0][2], puzzle[1][1], puzzle[2][0]]
    if not sum_is_15(line):
        return False
    return True