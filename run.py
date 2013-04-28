import solver

def do(l):
    print '\n'.join(l)
    m = solver.make_map(l)

    wins, losses = solver.solve(m)
    wins, losses = solver.prune_paths(wins, losses)
    print 'WINS:'
    print '\n'.join([str(x) for x in wins])
    print 'LOSSES:'
    print '\n'.join([str(x) for x in losses])

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
#do(level1)

level2 = [
    '                    ',
    '                    ',
    '            _S      ',
    '        S_*         ',
    '___________S________',
]
#do(level2)

level3 = [
    "                    ",
    "                    ",
    "    _S              ",
    "   _S_S             ",
    "*__S________________",
]
#do(level3)

level4 = [
    "                    ",
    "                    ",
    " _RR_RRR*RRR____    ",
    "                    ",
    "  __RRR_RRRS        ",
    "                    ",
    "____________________",
]
#do(level4)

level5 = [
    "                    ",
    "                    ",
    "      S_            ",
    "  _RR_ _            ",
    "      S              ",
    "___S_*S_____________",

]
#do(level5)

level6 = [
    "                    ",
    "                    ",
    " *RRRRRRRRRRRRRR    ",
    "                    ",
    "  SRRRRRRRRRRRRR_   ",
    "                    ",
    "   _RRRRRRRRRRRS    ",
    "    SRRRRRRRRRRRRRR_",
    "__________________S_",

]
#do(level6)

level7 = [
    "                    ",
    "                    ",
    "                    ",
    "    _*_T_T_RR_      ",
    " ___   _____        ",
    "______S_S___________",
]
#do(level7)

level8 = [
    "                    ",
    "                    ",
    "  *_T_R_T_          ",
    " _ S_S_S_S          ",
    "  __T_RR___         ",
    "____________________",
]
#do(level8)

level9 = [
    "                    ",
    "                    ",
    "  _RR_              ",
    "  *RRR_             ",
    " _SS S _RRR         ",
    "______S_____________",
]
#do(level9)

level10 = [
    '     _RRR_          ',
    ' E                  ',
    '   _ST__*           ',
    '                    ',
    '__S____S______E_____'
]
do(level10)
