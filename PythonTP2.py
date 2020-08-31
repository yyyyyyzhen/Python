""" TP2 """
""" Exercice 1 """
tab = [0.8571, -0.0714, -0.9286, 0.0714, 0.0714]

class Polynome :
    def __init__( self, strNom, tab ) :
        self.nom = strNom
        self.tabCoeff = tab.copy( )
    # end __init__

    def __genererStrPolynome( self ) :
        l = len( self.tabCoeff )
        tabInverse = self.tabCoeff[l - 1 : : -1]
        tabExp = [i for i in range( l - 1, -1, -1 )]
        strPoly = "-" if tabInverse[0] < 0 else ""
        for i in range( l ) :
            if tabExp[i] == 1 :
                strX = "*x"
            elif tabExp[i] == 0 :
                strX = ""
            else :
                strX = "*x^" + str( tabExp[i] )
            # end if
            if i < l - 1 :
                strOp = " + " if tabInverse[i + 1] >= 0 else " - "
            # end if
            strPoly += str( abs( tabInverse[i] ) ) + strX + strOp
        # end for
        strPoly = strPoly[: len( strPoly ) - 2]
        return strPoly
    # end genererStrPolynome

    def afficherPolynome( self ) :
        strPoly = self.__genererStrPolynome( )
        print( "Le polynome", self.nom, "est:", strPoly )
    # end afficherPolynome

    def comparerPolynome( self, p ) :
        strPoly1 = self.__genererStrPolynome( )
        strPoly2 = p.__genererStrPolynome( )
        if strPoly1 == strPoly2 :
            print( "Ces deux polynomes sont equivalent." )
        else :
            print( "Ces deux polynomes ne sont pas equivalent." )
        # end if
    # end comparerPolynome
    
    def getValeur( self, x ) :
        res, x0 = 0, 1
        for i in range( len( self.tabCoeff ) ) :
            res += self.tabCoeff[i] * x0
            x0 *= x
        # end for
        return res
    # end getValeur

    def getDerivee( self, x ) :
        res, x0 = 0, 1
        for i in range( 1, len( self.tabCoeff ) ) :
            res += i * self.tabCoeff[i] * x0
            x0 *= x
        # end for
        return res
    # end getDerivee
# end class Polynome

p = Polynome("P1", tab)
x = 3.0

""" test pour getValeur( ) 
print( "Valeur du polynome au point", x, end = "" )
print( "est: %.5f" %p.getValeur( x ) )
"""

""" test pour getDerivee( ) 
print( "Valeur de la derivee du polynome au point", x, end = "" )
print( "est: %.5f" %p.getDerivee( x ) )
"""

""" Exercice 2 """
def dichotomie( p, xMin, xMax, eps ) :
    c, pC = 1, 1
    pA = p.getValeur( xMin )
    pB = p.getValeur( xMax )
    if pA == 0 :
        return xMin
    elif pB == 0 :
        return xMax
    # end if
    while ( pC != 0 ) and ( ( xMax - xMin ) > eps ) :
        c = ( xMin + xMax ) / 2
        pC = p.getValeur( c )
        if pA * pC < 0 :
            xMax = c
            pB = pC
        else :
            xMin = c
            pA = pC
        # end if
    # end while
    return c
# end dichotomie

def newton( p, x0, eps ) :
    x = x0
    uN = eps + 1
    while ( p.getValeur( x ) != 0 ) and ( abs( uN ) > eps ) :
        uN = p.getValeur( x ) / p.getDerivee( x )
        x -= uN
    # end while
    return x
# end newton

""" test pour Exercice 2 
a, b, x0, eps = 2.0, 4.0, 2.0, 1e-5
print( "La racine du polynome par dichotomie est: %.5f" %dichotomie( p, a, b, eps ) )
print( "La racine du polynome par newton est: %.5f" %newton( p, x0, eps ) )
"""

""" test pour Exercice 3 """
tab2 = [-1.0, 2.0, -3.0, 4.0, -5.0, 6.0, -7.0]

p.afficherPolynome( )
p2 = Polynome( "P2", tab2 )
p2.afficherPolynome( )
p.comparerPolynome( p2 )

