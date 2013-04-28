import solver

def do(l):
    print '\n'.join(l)
    m = solver.make_map(l)

    wins, losses = solver.solve(m)
    losses = solver.prune_losses(wins, losses)
    #print 'WINS:'
    #print '\n'.join([str(x) for x in wins])
    #print 'LOSSES:'
    #print '\n'.join([str(x) for x in losses])

    total_wins = len(wins)
    total_losses = len(losses)
    print '{0} Wins'.format(total_wins)
    print '{0} Losses'.format(total_losses)

    if losses == 0:
        print '100% Win Prcnt'
    else:
        print '{0}% Win Prcnt'.format(total_wins * 100 / (total_wins + total_losses))


level1 = [
    '       _            ',
    '                    ',
    '     _S             ',
    '                    ',
    '   _S               ',
    '                    ',
    '*_S_________________'
]

level2 = [
    '                    ',
    '                    ',
    '            _S      ',
    '        S_*         ',
    '___________S________',
]
level3 = [
    "                    ",
    "                    ",
    "    _S              ",
    "   _S_S             ",
    "*__S________________",
]

level4 = [
    "                    ",
    "                    ",
    "      _S_ _         ",
    "       _S_S         ",
    "_______S*___________",
]

do(level1)
do(level2)
do(level3)
do(level4)
