def show_matrix(matrix):
    for row in matrix:
        print(('{:<3}' * len(row)).format(*row))

def create_matrix(length):
    fill = iter(range(length ** 2 + 1))
    return [
        [next(fill) for i in range(length)]
        for i in range(length)
    ]

def rotate_matrix(m):
    print('Before:')
    show_matrix(m)
    
    side = len(m[0])
    zones = side // 2
    
    print('')

    for i in range(zones):
        the_side = range(i, side - i)

        # Save each side
        top   = [m[i][r] for r in the_side]
        left  = [m[side - r - 1][i] for r in the_side]
        bot   = [m[side - i - 1][side - r - 1] for r in the_side]
        right = [m[r][side - i - 1] for r in the_side]
        
        # Swap them
        for buf_index, r in enumerate(the_side):
            m[side - r - 1][i]            = top  [buf_index]  # Left = Top
            m[side - i - 1][side - r - 1] = left [buf_index]  # Bot = Left
            m[r][side - i - 1]            = bot  [buf_index]  # Right = Bot
            m[i][r]                       = right[buf_index]  # Top = Right
            
    print('After:')
    show_matrix(m)


rotate_matrix(create_matrix(4))
