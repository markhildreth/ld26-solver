import solver

def show(results):
    print '\n'.join([repr(x) + ',' for x in results['map']])
    print 'WINS:'
    print '\n'.join([str(x) for x in results['wins']])
    #print 'LOSSES:'
    #print '\n'.join([str(x) for x in results['losses']])

    total_wins = len(results['wins'])
    total_losses = len(results['losses'])
    print '{0} Wins'.format(total_wins)
    print '{0} Losses'.format(total_losses)

    print '{0}% Win Prcnt'.format(total_wins * 100 / (total_wins + total_losses))

def do(l):
    m = solver.make_map(l)

    wins, losses = solver.solve(m)
    wins, losses = solver.prune_paths(wins, losses)
    return {
        'map' : l,
        'wins' : wins,
        'losses' : losses
    }

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
    " _RR_RRR*RRR____    ",
    "                    ",
    "  __RRR_RRRS        ",
    "                    ",
    "____________________",
]

level5 = [
    "                    ",
    "                    ",
    "      S_            ",
    "  _RR_ _            ",
    "      S              ",
    "___S_*S_____________",

]

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

level7 = [
    "_RR_                ",
    "                    ",
    "   *S_T__           ",
    "  __S__S            ",
    "                    ",
    "                    ",
    "____________________",
]

level8 = [
    "                    ",
    "                    ",
    "                    ",
    "    _*_T_T_RR_      ",
    " ___   _____        ",
    "______S_S___________",
]

level9 = [
    "                    ",
    "                    ",
    "  *_T_R_T_          ",
    " _ S_S_S_S          ",
    "  __T_RR___         ",
    "____________________",
]

level10 = [
    "                    ",
    "                    ",
    "  _RR_              ",
    "  *RRR_             ",
    " _SS S _RRR         ",
    "______S_____________",
]

level11 = [
    '                    ',
    '                    ',
    '         E_S        ',
    '_____E_*____________'

]

level12 = [
    '     _RRR_          ',
    ' E                  ',
    '   _ST__*           ',
    '                    ',
    '__S____S______E_____'
]

level13 = [
    '                    ',
    '     E              ',
    '           ___      ',
    '__T_RR_TT_          ',
    '_RRRR_ _S_          ',
    '______SS*_____E_____',

]

level14 = [
    "                    ",
    "                    ",
    "     S              ",
    " __RE_S__T_         ",
    "   SRT*S_           ",
    "____________E_______",
]

level15 = [
    '                    ',
    '                    ',
    '       RRTRR_       ',
    '    _E_SS__TRT__    ',
    '        ST*__       ',
    '__________E_________',
]

level16 = [
    '                    ',
    '                    ',
    '     _S_R_          ',
    ' E_S_S*S__S_____    ',
    '____S____E__________',
]

level17 = [
    '                    ',
    '      _RR_          ',
    '    SR_S_T___       ',
    '   __R_RR_RR_R__    ',
    '_______S*S__________',
]

level18 = [
    '                    ',
    '                    ',
    '    _SRSE           ',
    '   _T_TT_T_         ',
    '   SSR_R___TSR_     ',
    '  _S___SR*_R        ',
    '________E___________',
]

level19 = [
    '                    ',
    '                    ',
    '       E            ',
    '    _SST_           ',
    '    ____T           ',
    '  _STS__R           ',
    '   ___T___T_        ',
    '*S_E________________',
]

level20 = [
    '                    ',
    '      _RR_          ',
    '    SR_S_T___       ',
    '   __R_RR_RR_R__    ',
    '_______S*S__________',
]

level21 = [
    '                    ',
    '                    ',
    ' E___S_RRR_T__R_    ',
    '  __R__R* __R___S   ',
    '  _S___R___S___E_   ',
    '                    ',
    '                    ',
    '____________________',
]

level22 = [
    '                    ',
    '                    ',
    '  __R__R__S__R_     ',
    '  __S__T__R__T__    ',
    '  __T__S__T__R_     ',
    '  __R_R_*_TR_S_     ',
    '  __S_____S__T_     ',
    '____________________',
]


new_level = [
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    '____________________',
]


show(do(level10))
show(do(level11))
show(do(level12))
show(do(level13))
show(do(level14))
show(do(level15))
show(do(level16))
show(do(level17))
show(do(level18))
show(do(level19))
show(do(level20))
show(do(level21))
show(do(level22))

def do_random():
    while True:
        r = solver.create_random(new_level)
        results = do(r)
        print len(results['wins'])
        if len(results['wins']) == 1:
            show(results)
            break

#do_random()


            
