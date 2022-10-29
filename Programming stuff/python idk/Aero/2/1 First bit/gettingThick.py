
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import os

directory_path = "C:\\uni stuff\\Uni notes\\Programming stuff\\python idk\Aero\\2\\1 First bit"

laminarSet = pd.read_csv( directory_path+"\\laminar_profile.csv" )
turbulantSet = pd.read_csv( directory_path+"\\turbulent_profile.csv" )


def getBLThickness( distances, velocities ):
    FS_Vel = max( velocities );

    return np.interp( FS_Vel*0.9, distances, velocities )

laminarVels  = laminarSet[ laminarSet.columns[0] ]
laminarDists = laminarSet[ laminarSet.columns[1] ]

turbulantVels  = turbulantSet[ turbulantSet.columns[0] ]
turbulantDists = turbulantSet[ turbulantSet.columns[1] ]

print( "laminar thickness:", getBLThickness( laminarVels, laminarDists ), "mm"  )

print( "turbulant thickness:", getBLThickness( turbulantVels, turbulantDists ), "mm"  )


plot.figure( 69 );

plot.plot( laminarVels, laminarDists, "k" );
plot.plot( max( laminarVels )*0.9, getBLThickness( laminarVels, laminarDists ), "kx" );

plot.plot( turbulantVels, turbulantDists, "r" );
plot.plot( max( turbulantVels )*0.9, getBLThickness( turbulantVels, turbulantDists ), "rx" );

plot.show();














