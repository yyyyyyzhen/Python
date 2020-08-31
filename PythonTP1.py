""" TP 1 """
""" 4.1.d """
def exponentielle(x, esp):
    uN, N, i, exp, xInit = 1, 1, 1, 1, 1
    exp = 0
    while (uN > esp):
        uN = xInit / N
        N *= i
        xInit *= x
        i += 1
        exp += uN
    #end while
    print("exp(%d) = %.9f" %(x, exp))
    return exp
#end exponentielle

""" test pour ex1 """
#exponentielle(2, 1e-9)

""" Exercice 2 """

""" Exercice 3 """

""" Exercice 4 """
""" 4.1.a """
def sommeN(N):
    res = 0
    for i in range(N + 1):
        res += i
    #end for
    return res
#end sommeN

""" test pour 4.1.a """
N = 100
#print("1+2+...+%d = %d" %(N, sommeN(N)))

""" 4.1.b """
def factorielle(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    #end for
    print("fact(%d) = %d" %(n, res))
    return res
#end factorielle

""" test pour ex4.1.b """
#factorielle(5)

""" 4.1.c """
def xExponent(x, n):
    res, i = 1, 0
    for i in range(0, n):
        res *= x
    #end for
    return res
#end xExponent

""" test pour ex4.1.c """
x, n = 2, 3
res = xExponent(x, n)
#print("%d^%d = %d" %(x, n, res))

""" 4.1.e """
def calculPi(eps):
    uN, d, n, res = 1, 1, 0, 0
    while abs(uN) > eps:
        uN = d / (2 * n + 1)
        d *= (-1)
        n += 1
        res += uN
    #end while
    return res * 4
#end calculPi

""" test pour 4.1.e """
#print("Pi = %.5f" %calculPi(1e-5))

""" Exercice 5.1 """
Echi = [[" ", "X", " ", "X"],
        ["X", " ", "X", " "],
        [" ", "X", " ", "X"],
        ["X", " ", "X", " "]]

def afficherAxis():
    print("+---+---+---+---+")
#end afficherAxis

def afficherEchiquier(tab):
    afficherAxis()
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            print("| %c " %tab[i][j], end = "")
        #end for
        print("|")
        afficherAxis()
    #end for
#end afficherEchiquier

""" test pour ex5.1 """
#afficherEchiquier(Echi)

""" Exercice 5.2 """
""" 5.2.a """
def droiteTriangle(n):
    for i in range(1, n + 1):
        for j in range(0, i):
            print("*", end = '')
        #end for
        print("")
    #end for
#end droiteTriangle

""" test pour 5.2.a """
#droiteTriangle(4)

""" 5.2.b """
def centreeTriangle(n):
    n -= 1
    for i in range(1, n + 2):
        for j in range(0, n + i):
            if j > (n - i):
                print("*", end = '')
            else:
                print(" ", end = '')
            #end if
        #end for
        print("")
    #end for
#end centreeTriangle

""" test pour 5.2.b """
#centreeTriangle(4)

""" 5.2.c """
def centreeVideTriangle(n):
    n -= 1
    for i in range(1, n + 2):
        for j in range(0, n + i):
            if j > (n - i):
                if i == n + 1:
                    print("*", end = '')
                elif (j == (n - i + 1)) or (j == (n + i -1)):
                    print("*", end = '')
                else:
                    print(" ", end = '')
                #end if
            else:
                print(" ", end = '')
            #end if
        #end for
        print("")
    #end for
#end centreeVideTriangle

""" test pour 5.2.c """
centreeVideTriangle(6)

""" 5.2.d """
def charTriangle(char, n):
    n -= 1
    for i in range(1, n + 2):
        for j in range(0, n + i):
            if j > (n - i):
                print("%c" %char, end = '')
            else:
                print(" ", end = '')
            #end if
        #end for
        print("")
    #end for
#end charTriangle

""" test pour 5.2.d """
c = "h"
#charTriangle(c, 4)

""" Exercice 6 """
tab = [12, 1, 5, 26, 7, 14, 3, 7, 2]

""" 6.1.a """
def echangePositions(t, i, j):
    temp = t[i]
    t[i] = t[j]
    t[j] = temp
#end echangePositions

""" 6.1.b """
def positionPlusPetit(t, p):
    index = p
    min = t[p]
    for i in range(p, len(t)):
        if t[i] < min:
            min = t[i]
            index = i
        #end if
    #end for
    return index
#end postionPlusPetit

""" test pour 6.1.b """
#print(positionPlusPetit(tab, 3))

""" 6.1.c """
def algorithme1(t):
    for i in range(len(t)):
        minIndex = positionPlusPetit(t, i)
        echangePositions(t, i, minIndex)
    #end for
#end algorithme1

""" test pour algorithme1 """
#algorithme1(tab)
#print(tab)

""" 6.2 """
def algorithme2(t):
    flag = 1
    while flag:
        flag = 0
        for i in range(len(t) - 1):
            if t[i] > t[i + 1]:
                echangePositions(t, i, i + 1)
                flag = 1
            #end if
        #end for
    #end while
#end algorithme2

""" test pour algorithme2 """
#algorithme2(tab)
#print(tab)

""" 6.3 """
def QuickSort(t):
    if len(t) >= 2:
        mid = t[len(t) // 2]
        gauche, droite = [], []
        t.remove(mid)
        for num in t:
            if num >= mid:
                droite.append(num)
            else:
                gauche.append(num)
            #end if
        #end for
        return QuickSort(gauche) + [mid] + QuickSort(droite)
    else:
        return t
    #end if
#end QuickSort

""" test pour 6.3 """
#print(QuickSort(tab))

""" Exercice 7 """
import string
str1 = "Ceci est une test"
str2 = "et"
char1 = 'e'

""" 7.1 """
def combienDeFoisLaLettre(str, char):
    count = 0
    for i in range(len(str)):
        if char == str[i]:
            count += 1
        #end if
    #end for
    return count
#end combienDeFoisLaLettre

""" test pour 7.1 """
#print(combienDeFoisLaLettre(str1, char1))

""" 7.2 """
def supprCar(str, char):
    return str.replace(char, '')
#end supprCar

""" test pour 7.2 """
#print(supprCar(str1, char1))

""" 7.3 """
def supprDoublons(str, strSuppr):
    transTab = str.maketrans(strSuppr, len(strSuppr) * strSuppr[0])
    s = str.translate(transTab)
    return supprCar(s, strSuppr[0])
#end supprDoublons

""" test pour 7.3 """
#print(supprDoublons(str1, str2))

""" 7.4 """
def combienDeMots(str):
    count = 0
    for i in range(len(str)):
        if str[i] == " ":
            count += 1
        #end if
    #end for
    return count + 1
#end combienDeMots

""" test pour 7.4 """
#print(combienDeMots(str1))