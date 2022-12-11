import math
#préfonction non présent dans le menu

def pgcd_n(a, b):
    #retourne le plus grand diviseur commun de a et b
    if a == 0 or b == 0:
        return 0
    lst = []
    for j in range(1, min(a, b)+1):
        if a % j == 0 and b % j == 0:
            lst.append(j)
    return max(lst)

def inverse_n(a,b,n):
    #retourne true si a est il'inverse de b modulo n
    if a*b % n == 1:
        return True
    else:
        return False

def est_premier(a):
    #retourne True si a est premier
    if a == 0 or a == 1:
        return False
    for j in range(2, a):
        if a % j == 0:
            return False
    return True


def ppd_n(a, b):
    #retourne le plus petit diviseur commun de a et b
    if a == 0 or b == 0:
        return 0
    lst = []
    for j in range(1, min(a, b)+1):
        if a % j == 0 and b % j == 0:
            lst.append(j)
    return min(lst)

def est_premier_avecx(a,b):
    #retourne True si a est premier avec b
    if pgcd_n(a,b) == 1:
        return True
    else:
        return False

def entrer_nombre():
    a = int(input("Entrez le premier nombre: "))
    b = int(input("Entrez le deuxième nombre: "))
    return a,b
#listes des fonctions
def division():
    a,b = entrer_nombre()
    return a/b

def quotient():
    a,b = entrer_nombre()
    return a//b

def reste():
    a,b = entrer_nombre()
    return a%b

def multiplication():
    a,b = entrer_nombre()
    return a*b

def addition():
    a,b = entrer_nombre()
    return a+b

def soustraction():
    a,b = entrer_nombre()
    return a-b

def modulo():
    a,b = entrer_nombre()
    return a%b

def puissance():
    a,b = entrer_nombre()
    return a**b

def racine():
    a = int(input("Entrez le premier nombre: "))
    return a**0.5

def inverse():
    a = int(input("Entrez le premier nombre: "))
    return 1/a

def exponentielle():
    a = int(input("Entrez le premier nombre: "))
    return math.exp(a)

def factorielle():
    a = int(input("Entrez le premier nombre: "))
    return math.factorial(a)

def verification_modulo():
    nombre = int(input("Entrez le nombre: "))
    modulo = int(input("Entrez le modulo: "))
    reste = int(input("Entrez le reste: "))
    if nombre % modulo == reste:
        return True
    else:
        return False

def pgcd_diviseur_list():
    #retourne la liste d'une taille n des plus grand diviseurs communs de nbr1 et nbr2
    lst = []
    n = int(input("Entrez la taille de la liste: "))
    nbr1 = int(input("Entrez le premier nombre: "))
    nbr2 = int(input("Entrez le deuxième nombre: "))
    ordre = int(input("Plus grand : 1, plus petit : 2: "))

    for j in range(1, min(nbr1, nbr2)+1):
        if nbr1 % j == 0 and nbr2 % j == 0:
            lst.append(j)

    if ordre == 1:
        lst.sort(reverse=True)
        #on retire les éléments en trop
        lst = lst[:n]
    elif ordre == 2:
        lst.sort()
        #on retire les éléments en trop
        lst = lst[:n]
    return lst

def pgcd():
    a,b = entrer_nombre()
    #retourne le plus grand diviseur commun de a et b
    lst = []
    for j in range(1, min(a, b)+1):
        if a % j == 0 and b % j == 0:
            lst.append(j)
    return max(lst)

def ppd():
    a,b = entrer_nombre()
    #retourne le plus petit diviseur commun de a et b
    lst = []
    for j in range(1, min(a, b)+1):
        if a % j == 0 and b % j == 0:
            lst.append(j)
    return min(lst)

def euclide_pgcd_methode():
   return "Ainsi, l'algorithme d'Euclide opère ainsi : on remplace le plus grand des deux nombres par le reste de la division euclidienne du plus grand nombre par le plus petit. On recommence jusqu'à ce que le reste soit nul. Le plus grand diviseur commun est alors le plus petit des deux nombres."

def entiers_entre_deux_nombres():
    a = int(input("Entrez la borne de début: "))
    b = int(input("Entrez la borne de fin: "))
    indicateur = int(input("Premier entre quelle borne: debut->1 ou fin->2: "))
    lst = []
    if indicateur == 2:
        #on renvoye la liste des entier qui est premier entre a et b
        for i in range(a, b+1):
            if est_premier_avecx(i,b):
                lst.append(i)
    elif indicateur == 1:
        #on renvoye la liste des entier qui est premier entre a et b
        for i in range(b, a+1):
            if est_premier_avecx(i,a):
                lst.append(i)
    print(len(lst),"entiers premiers entre",a,"et",b)
    return lst

def entiers_inconnus_avec_pgcd_et_somme():
    print("la liste retournera les nombres qui sont premier entre eux sous ce format [a,b]")
    print("entrez la range des nombres que vous voulez tester")
    a,b = entrer_nombre()
    somme = int(input("Entrez la somme: "))
    pgcd_nbr = int(input("Entrez le pgcd: "))
    lst = []
    for i in range(a, b+1):
        for j in range(a, b+1):
            if i+j == somme and pgcd_n(i,j) == pgcd_nbr:
                lst.append([(i),(j)])
    return lst

def entiers_inconnus_avec_pgcd_et_ppd():
    print("la liste retournera les nombres qui sont premier entre eux sous ce format [a,b]")
    print("entrez la range des nombres que vous voulez tester")
    a,b = entrer_nombre()
    ppd_nbr = int(input("Entrez le ppd: "))
    pgcd_nbr = int(input("Entrez le pgcd: "))
    lst = []
    for i in range(a, b+1):
        for j in range(a, b+1):
            if pgcd_n(i,j) == pgcd_nbr and ppd_n(i,j) == ppd_nbr:
                lst.append([(i),(j)])
    return lst

def cherche_entiers_format_nbr1xu_nbr2xv():
    print("la liste retournera les nombres qui sont premier entre eux sous ce format [u,v]")
    print("entrez les bornes de recherche")
    a,b = entrer_nombre()
    print("entrez les deux nombres associés à u et v")
    nbr1,nbr2 = entrer_nombre()
    resultat = int(input("Entrez le resultat: "))
    lst = []
    for i in range(a, b+1):
        for j in range(a, b+1):
            if nbr1*i + nbr2*j == resultat:
                lst.append([(i),(j)])
    return lst

def cherche_entiers_format_au_plus_bv_egual_pgcd_ab():
    print("la liste retournera les nombres qui sont premier entre eux sous ce format [u,v]")
    print("entrez les bornes de recherche")
    a,b = entrer_nombre()
    print("entrez les deux nombres associés à u et v")
    nbr1,nbr2 = entrer_nombre()
    egual = pgcd_n(nbr1,nbr2)
    lst = []
    for i in range(a, b+1):
        for j in range(a, b+1):
            if nbr1*i + nbr2*j == egual:
                lst.append([(i),(j)])
    return lst

def nbr_premier_entre_deux_nombres():
    a,b = entrer_nombre()
    lst = []
    for i in range(a, b+1):
        if est_premier(i):
            lst.append(i)
    print(len(lst),"entiers premiers entre",a,"et",b)
    return lst

def nbr_premier():
    #vérifie si un nombre est premier
    nbr = int(input("Entrez un nombre: "))
    return est_premier(nbr)

def decomposition_nombre_en_nombre_premier():
    #décompose un nombre en multiplication de nombres premier
    nbr = int(input("Entrez un nombre: "))
    lst = []
    for i in range(2, nbr+1):
        if est_premier(i):
            while nbr%i == 0:
                lst.append(i)
                nbr = nbr/i
    dellst = []
    lst2 = []
    for i in lst:
        if i not in lst2:
            lst2.append(i)
        elif i in lst2:
            dellst.append(i)
            nbr_de_fois = 0
            for j in lst:
                if i == j:
                    nbr_de_fois += 1
            if nbr_de_fois > 1:
                lst2.append(str(i)+"^"+str(nbr_de_fois))
    for i in dellst:
        if i in lst2:
            lst2.remove(i)
    lst2 = list(dict.fromkeys(lst2))
    return lst2

def nombre_diviseurs():
    nbr = int(input("Entrez un nombre: "))
    lst = []
    for i in range(1, nbr+1):
        if nbr%i == 0:
            lst.append(i)
    print(len(lst),"diviseurs")
    return lst

def est_inverse():
    nbr1,nbr2 = entrer_nombre()
    modul = int(input("Entrez le modulo: "))
    return inverse_n(nbr1,nbr2,modul)

def calcul_inverse_modulo():
    nbr = int(input("Entrez un nombre: "))
    modul = int(input("Entrez le modulo: "))
    print("entrez les bornes de recherche")
    a,b = entrer_nombre()
    #calcul de l'inverse de nbr modulo modul entre a et b
    for i in range(a, b+1):
        if nbr*i%modul == 1:
            return i

def resolveur_equation():
    #equation = 7x congru a 3 modulo 13
    premierchiffre = int(input("Entrez le premier chiffre: "))
    deuxiemechiffre = int(input("Entrez le deuxieme chiffre: "))
    modulo = int(input("Entrez le modulo: "))
    print("entrez les bornes de recherche")
    a,b = entrer_nombre()

    for i in range(a, b+1):
        if premierchiffre*i%modulo == deuxiemechiffre:
            return i
    
def rsa():
    print("entrez la clé publique attention entrez en premier e puis n")
    a,b = entrer_nombre()
    message = int(input("Entrez le message: "))
    return message**a%b

def calcul_clee_privee():
    print("entrez e et n")
    e,n = entrer_nombre()
    print("entrez p et q")
    p,q = entrer_nombre()
    phi = (p-1)*(q-1)
    return e%phi

def menu():
    actions = {
        1: division,
        2: quotient,
        3: reste,
        4: multiplication,
        5: addition,
        6: soustraction,
        7: modulo,
        8: puissance,
        9: racine,
        10: inverse,
        11: exponentielle,
        12: factorielle,
        13: verification_modulo,
        14: pgcd_diviseur_list,
        15: pgcd,
        16: ppd,
        17: euclide_pgcd_methode,
        18: entiers_entre_deux_nombres,
        19 : entiers_inconnus_avec_pgcd_et_somme,
        20 : entiers_inconnus_avec_pgcd_et_ppd,
        21 : cherche_entiers_format_nbr1xu_nbr2xv,
        22 : cherche_entiers_format_au_plus_bv_egual_pgcd_ab,
        23 : nbr_premier_entre_deux_nombres,
        24 : nbr_premier,
        25 : decomposition_nombre_en_nombre_premier,
        26 : nombre_diviseurs,
        27 : est_inverse,
        28 : calcul_inverse_modulo,
        29 : resolveur_equation,
        30 : rsa,
        31 : calcul_clee_privee
    }
    fin = False
    print("Bienvenue dans le menu de calculs mathématiques")
    while fin == False:
        for i in range(1, len(actions)+1):
            print(str(i)+" : "+str(actions[i])[10:-23])
        print("0 : Quitter")
        choix = int(input("Entrez votre choix: "))
        #on lance la fonction qui se trouve dans le dictionnaire avec comme clé le choix de l'utilisateur
        if choix == 0:
            fin = True
            print("Au revoir")
        else:
            print(actions[choix]())
    
menu()