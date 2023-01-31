

import numpy as np
import matplotlib.pyplot as plot 

def getBLThickness( distances, velocities ):
    FS_Vel = max( velocities );
    return np.interp( FS_Vel*0.99, velocities, distances )

def getDisplacementThickness( dists, vels ):
    FS_Vel = max( vels );
    return np.trapz( 1-(vels/FS_Vel), dists )

def getMomentumThickness( dists, vels ):
    FS_Vel = max( vels );
    return np.trapz( (1-(vels/FS_Vel))*(vels/FS_Vel), dists )

def getShapeFactor( dists, vels ):
    return getDisplacementThickness( dists, vels )/getMomentumThickness( dists, vels )

# importing data
turbulantVels  = np.array([ 0,8.435,9.199,9.677,10.031,10.939,11.508,11.732,11.929,12.266,12.549,12.793,13.009,13.202,13.377,13.755,14.072,14.346,14.587,14.804,15,15,15,15 ]) # in m/s
turbulantDists = np.array([ 0,0.238,0.476,0.715,0.953,1.906,2.858,3.335,3.811,4.764,5.717,6.67,7.623,8.575,9.528,11.91,14.292,16.674,19.057,21.439,23.821,26.203,28.585,30.967 ])/1000 # in m

print( "displacement thickness: ", getDisplacementThickness( turbulantDists, turbulantVels ), "m" );
print( "Free stream Velocity: ", ( np.max(turbulantVels) ), "m/s" );
print( "mthick: ", getMomentumThickness( turbulantDists, turbulantVels ), "m" );
print( "shape Fact: ", getShapeFactor( turbulantDists, turbulantVels ) );
print( "Boundary layer thickness:", getBLThickness( turbulantDists, turbulantVels )*1000, "mm"  )











"""# plotting data

plot.figure( 69 );
plot.plot( turbulantDists, turbulantVels, "r" );
plot.plot( getBLThickness( turbulantDists, turbulantVels ), max(turbulantVels)*0.99 , "rx" );
 
plot.ylabel("veloicty ")
plot.xlabel("surface distance ")

plot.show();"""














