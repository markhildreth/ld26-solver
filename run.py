import solver

level = [
    '       _            ',
    '                    ',
    '     _S             ',
    '                    ',
    '   _S               ',
    '                    ',
    '*_S_________________'
]

m = solver.make_map(level)
wins, losses = solver.solve(m)

print '{0} Wins'.format(wins)
print '{0} Losses'.format(losses)
print '{0}% Win Prcnt'.format(wins * 100.0 / losses)
