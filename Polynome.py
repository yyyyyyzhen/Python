import fonction.Fonction as f

class Polynome( f.Fonction ) :
    def __init__( self, coefficients ) :
        self.__coefficients = coefficients # attribut privee
    # end __init__

    @property
    def coefficients( self ) :
        return self.__coefficients
    # end getter
    @coefficients.setter
    def coefficients( self, tab ) :
        self.__coefficients = tab.copy( )
    # end setter

    def __str__( self, x = "x" ) :
        l = len( self.coefficients )
        tabInverse = self.coefficients[l - 1 : : -1]
        tabExp = [i for i in range( l - 1, -1, -1 )]
        strPoly = "-" if tabInverse[0] < 0 else ""
        for i in range( l ) :
            if tabExp[i] == 1 :
                strX = "*" + x
            elif tabExp[i] == 0 :
                strX = ""
            else :
                strX = "*" + x +"^" + str( tabExp[i] )
            # end if
            if i < l - 1 :
                strOp = "+" if tabInverse[i + 1] >= 0 else "-"
            # end if
            strPoly += str( abs( tabInverse[i] ) ) + strX + strOp if tabInverse[i] != 0 else ""
        # end for
        strPoly = strPoly[: len( strPoly ) - 1]
        return strPoly
    # end __str__

    def __eq__( self, other ) :
        if not isinstance( other, Polynome ) :
            return False
        if self is other :
            return True
        if self.coefficients != other.coefficients :
            return False
        return True
    # end __eq__

    def __add__( self, other ) :
        lSelf = len( self.coefficients )
        lOther = len( other.coefficients )
        sTab = lSelf if lSelf > lOther else lOther
        res = [0] * sTab
        for i in range( lSelf ) :
            res[i] += self.coefficients[i]
        # end for
        for i in range( lOther ) :
            res[i] += other.coefficients[i]
        # end for
        return Polynome( res )
    # end __add__

    def getDegre( self ) :
        return len( self.coefficients ) - 1
    # end getDegre

    def getValeur( self, x ) :
        res, x0 = 0, 1
        for i in range( len( self.coefficients ) ) :
            res += self.coefficients[i] * x0
            x0 *= x
        # end for
        return res
    # end getValeur

    def getDerivee( self, x ) :
        res, x0 = 0, 1
        for i in range( 1, len( self.coefficients ) ) :
            res += i * self.coefficients[i] * x0
            x0 *= x
        # end for
        return res
    # end getDerivee
# end Polynome