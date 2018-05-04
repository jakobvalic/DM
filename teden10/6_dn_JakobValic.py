# 6. domača naloga pri predmetu Diskretno modeliranje
# študent Jakob Valič


# Najprej izgotovimo 3 pomožne funkcije: za vse možne razpostavitve oklepajev, za dodajanje veznikov in izračun vrednosti.
# Sledi krovna funkcija, ki se poslužuje pomožnih.

def razpostaviOklepaje(izraz):
    '''Vrne vse možne razpostavitve oklepajev.'''
    razpostavitve = []
    if len(izraz) == 1:
        razpostavitve.append(izraz[0]) # Ker nočemo oklepajev pri enem členu
    if len(izraz) == 2:
        razpostavitve.append(izraz) # Med dvema členoma je vedno zgolj ena možnost postavitve členov
    else:
        for ind in range(len(izraz) - 1):
            glava = izraz[:ind + 1]
            rep = izraz[ind + 1:]
            for razpostavitveGlava in razpostaviOklepaje(glava):
                for razpostavitveRep in razpostaviOklepaje(rep):
                    razpostavitve.append((razpostavitveGlava, razpostavitveRep))
    return razpostavitve

def dodajVeznike(razpostavitve, vezniki):
    '''V vse možne razpostavitve doda veznike.'''
    return [str(razpostavitev).replace(',', ' {} ').format(*vezniki) for razpostavitev in razpostavitve]

def izracunajVrednosti(razpostavitve):
    '''Izračuna, koliko razpostavitev se izvrednoti v resnično vrenost in vrne te kombinacije.'''
    stResnicnih = 0
    resnicneRazpostavitve = []
    for razpostavitev in razpostavitve:
        if eval(razpostavitev):
            stResnicnih += 1
            resnicneRazpostavitve.append(razpostavitev)
    return stResnicnih, resnicneRazpostavitve

def krovnaFunkcija(izraz, vezniki):
    '''Poveže pomožne funkcije in izpiše razultat.'''
    zOklepaji = razpostaviOklepaje(izraz)
    zVezniki = dodajVeznike(zOklepaji, vezniki)
    stResnicnih, resnicneRazpostavitve = izracunajVrednosti(zVezniki)
    print('Število resničnih razpostavitev je: {}'.format(stResnicnih))
    for razpostavitev in resnicneRazpostavitve:
        print(razpostavitev, '-> True')

# Podatke dobimo v obliki dveh seznamov: v prvem so logične vrednosti, v drugem pa vezniki.
izraz = (True, False, True, True)
vezniki = ('and', 'and', 'or')

krovnaFunkcija(izraz, vezniki)


