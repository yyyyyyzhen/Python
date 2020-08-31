import fonction.Fonction as f

class SommeFonction( f.Fonction ) :
    def __init__( self, fTab ):
        self.__fTab = fTab
    # end __init__

    @property
    def fTab( self ):
        return self.__fTab
    # end getter

    @fTab.setter
    def fTab( self, tab ) :
        if len( tab ) <= 10 :
            self.__fTab = tab
        else :
            print( "Le nombre maximal d'operant est 10!" )
            self.__fTab = tab[0 : 10]
        # end if
    # end setter

    def __str__( self, x = "x" ) :
        l = len( self.fTab )
        s = ""
        for i in range( l ) :
            if i < l - 1 :
                strOp = "" if self.fTab[i + 1].__str__( x )[0] == "-" else "+"
            # end if
            s += self.fTab[i].__str__( x ) + strOp
        # end for
        s = s[ : len( s ) - 1]
        return s
    # end __str__

    def getValeur( self, x ) :
        val = 0
        for i in self.fTab :
            val += i.getValeur( x )
        # end for
        return val
    # end getValeur

    def getDerivee( self, x ) :
        val = 0
        for i in self.fTab :
            val += i.getDerivee( x )
        # end for
        return val
    # end getDerivee
# end SommeFonction


