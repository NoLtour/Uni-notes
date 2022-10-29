
import pandas as pd
import numpy as np
import os

directory_path = os.getcwd()

laminarSet = pd.read_csv( directory_path+"\\laminar_profile.csv" )
turbulantSet = pd.read_csv( "//turbulent_profile.csv" )


def getBLThickness( distances, velocities ):
    FS_Vel = max( velocities );

    return np.interp( distances, velocities, FS_Vel )


print( "laminar thickness:", getBLThickness( laminarSet.columns[0], laminarSet.columns[1] )  )


print( "turbulant thickness:", getBLThickness( turbulantSet.columns[0], turbulantSet.columns[1] )  )
















