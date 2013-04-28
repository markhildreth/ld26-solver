def make_map(level):
    height = len(level)
    width = len(level[0])

    m = {}
    data = m['data'] = {}

    for yIndex, yLevel in enumerate(level):
        y = height - yIndex - 1
        for x, xLevel in enumerate(yLevel):
            coord = (x, y)
            if xLevel == '*':
                m['start'] = coord
                data[coord] = '_'
            else:
                data[coord] = xLevel
            

    return m
            
def solve(g):
    pass
    

