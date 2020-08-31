from Polynome import *
from Solveur import *

tab1 = [0.8571, -0.0714, -0.9286, 0.0714, 0.0714]
tab2 = [1, 2, 3, 0, 5, 6, 7]
tab3 = [0.8571, -0.0714, -0.9286, 0.0714, 0.0714]
"""
print('{:+.4f}x^{}'.format(.5,2))
print('{:+.4f}x^{}'.format(-.5001,2))
"""
""" test pour classe Polynome """
p1 = Polynome( tab1 )
p2 = Polynome( tab2 )
p3 = Polynome( tab3 )

# test Polynome.__str__
print( "Afficher les polynomes p1 et p2: " )
print( p1 )
print( p2 ) 

# test Polynome.__eq__
print( "Comparer polynome p1 avec p2 et p3: " )
print( p1 == p2 ) # True
print( p1 == p3 ) # False

# test Polynome.__add__
print( "Faire de l'addition entre p1 et p2: " )
print( p1 + p2 )

# test Polynome.getDegre
print( "Le degre de polynome p1: " )
print( str( p1.getDegre( ) ) ) # 4

# test Polynome.getValeur
print( "Calucler les valeurs dans points 1.0, 3.0 et 4.0: " )
print( "%.5f %.5f %.5f" %( p1.getValeur( 1.0 ), p1.getValeur( 3.0 ), p1.getValeur( 4.0 ) ) )

# test Polynome.getDerivee
print( "Calculer les valeurs de derivation dans points 1.0, 3.0 et 4.0: " )
print( "%.5f %.5f %.5f" %( p1.getDerivee( 1.0 ), p1.getDerivee( 3.0 ), p1.getDerivee( 4.0 ) ) )

""" test pour classe Solveur """
sol = Solveur( p1 ) # precision: 1e-5 par defaut 

# test methode Newton
racine1 = sol.newton( 2.0 )
print( "La racine d'equation p1 = 0 par methode Newton est: " )
print( str( racine1 ) )

# test methode Dichotomie
racine2 = sol.dichotomie( 0.0, 5.0 )
print( "La racine d'equation p1 = 0 par methode Dichotomie est: " )
print( str( racine2 ) )
#print( str( p1.getValeur( racine1 ) ) )
#print( str( p1.getValeur( racine2 ) ) )



