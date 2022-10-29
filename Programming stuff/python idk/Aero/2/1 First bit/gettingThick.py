
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import os

directory_path = "C:\\uni stuff\\Uni notes\\Programming stuff\\python idk\Aero\\2\\1 First bit"

laminarSet = pd.read_csv( directory_path+"\\laminar_profile.csv" )
turbulantSet = pd.read_csv( directory_path+"\\turbulent_profile.csv" )


def getBLThickness( distances, velocities ):
    FS_Vel = max( velocities );

    return np.interp( FS_Vel*0.99, velocities, distances )

laminarVels  = laminarSet[ laminarSet.columns[1] ] 
laminarDists = laminarSet[ laminarSet.columns[0] ]

turbulantVels  = turbulantSet[ turbulantSet.columns[1] ]
turbulantDists = turbulantSet[ turbulantSet.columns[0] ]


print( "laminar thickness:", getBLThickness( laminarDists, laminarVels ), "mm"  )
print( "turbulant thickness:", getBLThickness( turbulantDists, turbulantVels ), "mm"  )


plot.figure( 69 );

plot.plot( laminarDists, laminarVels, "b" );
plot.plot( getBLThickness( laminarDists, laminarVels ), max(laminarVels)*0.99 , "bx" );

plot.plot( turbulantDists, turbulantVels, "r" );
plot.plot( getBLThickness( turbulantDists, turbulantVels ), max(turbulantVels)*0.99 , "rx" );
 
plot.ylabel("veloicty (m/s)")
plot.xlabel("surface distance (mm)")

plot.show();














