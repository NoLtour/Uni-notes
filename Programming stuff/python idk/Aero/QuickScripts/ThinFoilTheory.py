
import numpy as np
import matplotlib.pyplot as plot 

degToRad = np.pi/180

# Settings
cIncrement = 0.0001
nCount = 10

# Inputs (radians)

AOA = 0

def dzdxFunction( chordFrac ):
    return 0.1 * ( 1 - 2 * chordFrac )


# Working parts

# Fraction along chord
cFraction = np.arange( 0, 1+cIncrement, cIncrement )

# Generates the dz/dx values for the chord points
dzdx = dzdxFunction( cFraction )

cTheta_0 = np.arccos( 1 - 2*cFraction )

# Uses trapizium version of integration to get A0
A0 = AOA - (1/np.pi) * np.trapz( dzdx, cTheta_0 )

An  = []

# Uses trapizium version of integration to get An upto nCount
for n in range( 1, nCount+1 ):
    An.append( (2/np.pi) * np.trapz( dzdx * np.cos( cTheta_0 * n ), cTheta_0 ) )

An = np.array( [A0] + An )

print( "A0:",An[0],"\tA1:",An[1],"\tA2:",An[2],"\tA3:",An[3],"\tA4:",An[4] )

# Gets zero lift angle using trapizium version of integration
zeroLiftAngle = (1/np.pi) * np.trapz( dzdx * ( 1 - np.cos( cTheta_0 ) ), cTheta_0 )
print("Calculated zeroLiftAngle:", zeroLiftAngle, "rad\t", zeroLiftAngle/degToRad, "degrees")

# Gets quater chord moment 
quaterChordMoment = (np.pi/4) * ( An[2] - An[1] )
print("Calculated quaterChordMomentCoeff:", quaterChordMoment, "\t or: ", quaterChordMoment/np.pi, "pi")

# gets leading edge moment
leadingEdgeMoment = (-np.pi/2) * ( A0 + An[1] + An[2]/2 )
print("Calculated leadingEdgeMomentCoeff:", leadingEdgeMoment, "\t or: ", leadingEdgeMoment/np.pi, "pi")

# gets lift coefficient
Cl = 2*np.pi*( AOA - zeroLiftAngle )
print("Calculated Cl:", Cl)


print("done.")












