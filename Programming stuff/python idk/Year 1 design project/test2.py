import airfoilsim

import scipy.optimize as sp
import splineLibs as sl
import numpy as np


tester = sl.Optimiser()


def testVars( values ):
    foil = sl.AirFoil( values )

    return 100/np.max(0.001, tester.testFoil( foil ))

#, bounds = [ [ 0, 0, 0.1, 0, 0.3, 0, 0.1, 0, 0.3, 0 ], [ 0.4, 0.4, 0.5, 0.5, 0.7, 0.5, 0.5, 0.5, 0.7, 0.5 ] ], options={'eps':0.001}

#print( sp.minimize( fun = testVars, x0 = [ 0.05, 0.05, 0.2, 0.1, 0.2, 0.05, 0.66, 0.04, 0.66, 0.04 ], method='Nelder-Mead', options={'eps':0.001} ) )

foil = tester.createAirfoil( [ 0.05, 0.05, 0.2, 0.1, 0.2, 0.05, 0.66, 0.04, 0.66, 0.04 ] )


foil.render()

print( tester.testFoil( foil ) )