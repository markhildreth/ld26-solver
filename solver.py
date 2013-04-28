MAP_WIDTH = 20

def make_map(level):
    height = len(level)
    width = len(level[0])

    m = {}
    m['devices_remaining'] = 0
    m['path'] = []
    data = m['data'] = {}

    for yIndex, yLevel in enumerate(level):
        y = height - yIndex - 1
        for x, xLevel in enumerate(yLevel):
            coord = (x, y)
            if xLevel == '*':
                m['player'] = coord
                data[coord] = '_'
            elif xLevel == '_' or xLevel == ' ':
                data[coord] = xLevel
            else:
                data[coord] = xLevel
                m['devices_remaining'] += 1
            

    return m
            
def _copy(g):
    return {
        'player' : g['player'],
        'data' : g['data'].copy(),
        'devices_remaining' : g['devices_remaining'],
        'path' : g['path'][:],
    }

def _handle_effect(g, dest):
    data = g['data']

    while True:
        tile = data[dest]
        
        if tile == '_':
            break
        if tile == ' ':
            dest = dest[0], dest[1] - 1
        if tile == 'S':
            g['devices_remaining'] -= 1
            data[dest] = '_'
            if g['facing'] == 'left':
                dest = dest[0] - 1, dest[1] + 2
            else:
                dest = dest[0] + 1, dest[1] + 2

    g['player'] = dest
    g['path'].append('Effect to {0}'.format(dest))
    return g

def _move_left(g):
    data = g['data']
    playerX = g['player'][0]
    playerY = g['player'][1]
    g['facing'] = 'left'

    newX = playerX
    while newX > 1:
        newX -= 1
        dest = (newX, playerY)
        if data[dest] != '_':
            g['path'].append('left to {0}'.format(dest))
            return _handle_effect(g, dest)

    return None

def _move_right(g):
    data = g['data']
    playerX = g['player'][0]
    playerY = g['player'][1]
    g['facing'] = 'right'

    newX = playerX
    while newX < MAP_WIDTH - 1:
        newX += 1
        dest = (newX, playerY)
        if data[dest] != '_':
            g['path'].append('right to {0}'.format(dest))
            return _handle_effect(g, dest)

    return None

def solve(g):
    winning_solutions = 0
    losing_solutions = 0

    if g['devices_remaining'] == 0:
        print 'Winner: {0}'.format(g['path'])
        return 1, 0

    newG = _move_left(_copy(g))
    if not newG:
        #print '{0}: Moving left loses'.format(g['path'])
        losing_solutions += 1
    else:
        w, l = solve(newG)
        winning_solutions += w
        losing_solutions += l

    newG = _move_right(_copy(g))
    if not newG:
        #print '{0}: Moving right loses'.format(g['path'])
        losing_solutions += 1
    else:
        w, l = solve(newG)
        winning_solutions += w
        losing_solutions += l

    return winning_solutions, losing_solutions

    

