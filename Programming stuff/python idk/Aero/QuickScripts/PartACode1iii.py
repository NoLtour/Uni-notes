

import numpy as np
import matplotlib.pyplot as plot 

def getBLThickness( distances, velocities ):
    FS_Vel = max( velocities );
    return np.interp( FS_Vel*0.99, velocities, distances )

# importing data
turbulantVels  = np.array([ 0,8.435,9.199,9.677,10.031,10.939,11.508,11.732,11.929,12.266,12.549,12.793,13.009,13.202,13.377,13.755,14.072,14.346,14.587,14.804,15,15,15,15 ]) # in m/s
turbulantDists = np.array([ 0,0.238,0.476,0.715,0.953,1.906,2.858,3.335,3.811,4.764,5.717,6.67,7.623,8.575,9.528,11.91,14.292,16.674,19.057,21.439,23.821,26.203,28.585,30.967 ]) # in mm

yturb = turbulantDists
uturb = turbulantVels
delta_turb = getBLThickness(yturb, uturb)

Uinf_turb = max( uturb )

from scipy.optimize import curve_fit

def func( yd,n):
    return yd**(1/n)

idx = np.where( yturb/delta_turb > 1 )[0]
bl_idx = idx[0]

popt, pcov = curve_fit( func, yturb[0:bl_idx]/delta_turb, uturb[0:bl_idx]/Uinf_turb )

n = popt[0]

print( "The value of n=", np.round(n,2) )

plot.plot( uturb/Uinf_turb, yturb/delta_turb, "o" )
plot.plot( (yturb[0:bl_idx]/delta_turb)**(1/n), yturb[0:bl_idx]/delta_turb, "k-" )
plot.xlabel("Velocity (U/U_inf)")
plot.ylabel("Displacement (y/delta_99)")
plot.show()













