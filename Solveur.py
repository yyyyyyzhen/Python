class Solveur :
    def __init__( self, f, precision = 1e-5 ) :
        """ tous les attributs sont privees """
        self.__f = f
        self.__precision = precision # 1e-5 par defaut
    # end __init__

    @property
    def f( self ) :
        return self.__f
    # end getter f
    @f.setter
    def f( self, fonction ) :
        self.__f = fonction
    # end setter p

    @property
    def precision( self ) :
        return self.__precision
    # end getter precision
    @precision.setter
    def precision( self, eps ) :
        self.__precision = eps
    # end setter precision

    def newton( self, x0 ) :
        x = x0
        uN = self.precision + 1
        while self.f.getValeur( x ) != 0 and abs( uN ) > self.precision :
            uN = self.f.getValeur( x ) / self.f.getDerivee( x )
            x -= uN
        # end while
        return x
    # end newton

    def dichotomie( self, xMin, xMax ) :
        c, pC = 1, 1
        pA = self.f.getValeur( xMin )
        pB = self.f.getValeur( xMax )
        if pA == 0 :
            return xMin
        elif pB == 0 :
            return xMax
        # end if
        while pC != 0 and ( xMax - xMin ) > self.precision :
            c = ( xMin + xMax ) / 2
            pC = self.f.getValeur( c )
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
# end Solveur