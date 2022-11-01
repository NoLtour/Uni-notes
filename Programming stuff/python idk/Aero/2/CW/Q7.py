
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import os

directory_path = "C:\\uni stuff\\Uni notes\\Programming stuff\\python idk\Aero\\2\\CW"


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

laminarSet = pd.read_excel( directory_path+"\\LBLdata1.xlsx" ) 

laminarDists = laminarSet[ laminarSet.columns[0] ]/1000 
laminarVels  = laminarSet[ laminarSet.columns[1] ]


print( "dthick: ", getDisplacementThickness( laminarDists, laminarVels ) );
print( "mthick: ", getMomentumThickness( laminarDists, laminarVels ) );
print( "L sFact: ", getShapeFactor( laminarDists, laminarVels ) );

print( "laminar thickness:", getBLThickness( laminarDists, laminarVels ), "mm"  )
#print( "turbulant thickness:", getBLThickness( turbulantDists, turbulantVels ), "mm"  )

# plotting data

plot.figure( 69 );

plot.plot( laminarDists, laminarVels, "b" );
plot.plot( getDisplacementThickness( laminarDists, laminarVels ), max(laminarVels)*0.99 , "bx" );

 
plot.ylabel("veloicty ")
plot.xlabel("surface distance ")

plot.show();














