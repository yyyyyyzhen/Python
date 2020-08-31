from abc import ABC, abstractmethod

class Fonction( ABC ) :
    def __init__( self ) :
        pass
    # end __init__

    def __str__( self ) :
        pass
    # end __str__

    @abstractmethod
    def getValeur( self, x ) :
        pass
    # end getValeur

    @abstractmethod
    def getDerivee( self, x ) :
        pass
    # end getDerivee

    def getValeurCompose( self, g, x ) :
        return self.getValeur( g.getValeur( x ) )
    # end getValeurCompose

    def getDeriveeCompose( self, g, x ) :
        return g.getDerivee( x ) * self.getDerivee( g.getValeur( x ) )
    # end getDeriveeCompose
# end Fonction