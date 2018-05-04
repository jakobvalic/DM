# 4. naloga pri kolokviju 2, DISMOD
# študent Jakob Valič


# Pomožne funkcije

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

def implikacija(a, b):
    '''Vrne vrednost implikacije a => b.'''
    if a and not b: # Edino v tem primeru je implikacija neresnična
        return False
    return True

def izračunajVrednosti(izraz):
    '''Izračuna vrednosti zaporedja logičnih izrazov, med katerimi so implikacije.'''
    if isinstance(izraz, bool):
        return izraz
    prviDel = izraz[0]
    drugiDel = izraz[1]
    if isinstance(prviDel, bool) and isinstance(drugiDel, bool):
        return implikacija(prviDel, drugiDel)
    else:
        return implikacija(izračunajVrednosti(prviDel), izračunajVrednosti(drugiDel))

# Krovna funkcija

def steviloResnicnih(izraz):
    '''Krovna funkcija za grafični prikaz števila resničnih.'''
    zOklepaji = razpostaviOklepaje(izraz)
    kolikoResnicnih = 0
    for moznost in zOklepaji:
        print(str(moznost).replace(',', ' ==>'), ' se izvrednoti v ', izračunajVrednosti(moznost))
        if izračunajVrednosti(moznost):
            kolikoResnicnih += 1
    return kolikoResnicnih

# Test

izraz = (True, False, True, False)
print(steviloResnicnih(izraz))