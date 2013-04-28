import random

MAP_WIDTH = 20

def make_map(level):
    height = len(level)
    width = len(level[0])

    m = {}
    m['devices_remaining'] = 0
    m['path'] = []
    m['device_path'] = []
    m['teleporters'] = []
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
            elif xLevel == 'E':
                data[coord] = xLevel
                m['teleporters'].append(coord)
                m['devices_remaining'] += 1
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
        'device_path' : g['device_path'][:],
        'teleporters' : g['teleporters'][:],
    }

def _handle_effect(g, dest):
    data = g['data']

    while True:
        tile = data[dest]
        
        if tile == '_':
            break
        elif tile == ' ':
            dest = dest[0], dest[1] - 1
        else:
            g['device_path'].append(dest)
            if tile == 'S':
                g['devices_remaining'] -= 1
                data[dest] = '_'
                if g['facing'] == 'left':
                    dest = dest[0] - 1, dest[1] + 2
                else:
                    dest = dest[0] + 1, dest[1] + 2
            elif tile == 'R':
                g['devices_remaining'] -= 1
                data[dest] = ' '
                if g['facing'] == 'left':
                    dest = dest[0] - 1, dest[1]
                else:
                    dest = dest[0] + 1, dest[1]
            elif tile == 'T':
                g['devices_remaining'] -= 1
                data[dest] = '_'
                dest = dest[0], dest[1] - 1
            elif tile == 'E':
                g['devices_remaining'] -= 2
                newDest = [x for x in g['teleporters'] if x != dest][0]
                data[dest] = '_'
                data[newDest] = '_'
                dest = newDest

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
    if g['devices_remaining'] == 0:
        return [g['device_path']], []

    winning_solutions = []
    losing_solutions = []

    leftG = _move_left(_copy(g))
    rightG = _move_right(_copy(g))

    if leftG:
        w, l = solve(leftG)
        winning_solutions += w
        losing_solutions += l

    if rightG:
        w, l = solve(rightG)
        winning_solutions += w
        losing_solutions += l

    if len(winning_solutions) == 0:
        losing_solutions += [g['device_path']]
    return winning_solutions, losing_solutions

    
def prune_paths(win_paths, loss_paths):
    real_losses = []

    for loss_path in loss_paths:
        found_match = False
        for win_path in win_paths:
            if win_path[:len(loss_path)] == loss_path:
                found_match = True
                break

        if not found_match:
            real_losses.append(loss_path)

    # Remove duplicate win scenarios
    real_wins = list(set([tuple(x) for x in win_paths]))
    # Remove duplicate loss scenarios
    real_losses = list(set([tuple(x) for x in real_losses]))

    # Now go through losses that are really just the start
    # to other losses and remove those
    real_losses_2 = []

    for loss_path1 in real_losses:
        found_parent = False
        for loss_path2 in real_losses:
            if loss_path1 == loss_path2:
                continue

            if loss_path1[:len(loss_path2)] == loss_path2:
                found_parent = True
                break

        if not found_parent:
            real_losses_2.append(loss_path1)

    return real_wins, real_losses_2
        

def create_random(m):
    results = []
    for yIndex, y in enumerate(m):
        result = ''
        for xIndex, x in enumerate(y):
            if x == '?':
                result = result + random.choice(['R', 'T', 'S'])
            else:
                result = result + x
        results.append(result)

    
    return results
