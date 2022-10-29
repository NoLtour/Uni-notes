
import pandas as pd
import numpy as np
import os

directory_path = "C:\\uni stuff\\Uni notes\\Programming stuff\\python idk\Aero\\2\\1 First bit"

laminarSet = pd.read_csv( directory_path+"\\laminar_profile.csv" )
turbulantSet = pd.read_csv( directory_path+"\\turbulent_profile.csv" )


def getBLThickness( distances, velocities ):
    FS_Vel = max( velocities );

    return np.interp( distances, velocities, FS_Vel )


print( "laminar thickness:", getBLThickness( laminarSet.columns[0][1:], laminarSet.columns[1][1:] )  )


print( "turbulant thickness:", getBLThickness( turbulantSet.columns[0][1:], turbulantSet.columns[1][1:] )  )
















