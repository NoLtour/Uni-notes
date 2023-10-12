 
import numpy as np
import matplotlib.pyplot as plot 


def getBLThickness( distances, velocities ):
    FS_Vel = max( velocities );
    return np.interp( FS_Vel*0.99, velocities, distances )

def getDisplacementThickness( dists, vels ):
    FS_Vel = max( vels );
    return np.trapz( 1-(vels/FS_Vel), dists )

def getMomentumThickness( dists, vels ):
    dists = np.array(dists)/1000
    vels = np.array(vels)

    FS_Vel = max( vels );
    return np.trapz( (1-(vels/FS_Vel))*(vels/FS_Vel), dists )

def getShapeFactor( dists, vels ):
    return getDisplacementThickness( dists, vels )/getMomentumThickness( dists, vels )

# importing data
 
boundaryLabData = {
    "100k_half":{
        "positions": [0.2, 0.6, 1, 1.4, 1.8, 2, 3, 4, 5, 6, 7, 8, 10],
        "vels": [ 5.713984666,9.034603029,9.896911754,10.68988647,11.42796933,11.42796933,11.42796933,11.42796933,11.42796933,11.42796933,11.42796933,11.42796933,11.42796933 ]
    },
    "200k_half":{
        "positions": [0.2, 0.6, 1, 1.4, 1.8, 2, 3, 4, 5, 6, 7, 8, 10],
        "vels": [ 17.141954,20.6020647,21.75820537,22.13016745,22.13016745,22.49598012,22.49598012,22.85593866,22.85593866,22.85593866,22.85593866,22.85593866,22.85593866 ]
    },
    "400k_full":{
        "positions": [0.2, 0.6, 1, 1.4, 1.8, 2, 3, 4, 5, 6, 7, 8, 10],
        "vels": [ 15.11778242,17.141954,18.06920606,19.37706476,19.79382351,20.6020647,21.37977293,21.75820537,21.75820537,22.13016745,22.13016745,22.85593866,22.85593866 ]
    },
    "200k_full":{
        "positions": [0.2, 0.6, 1, 1.4, 1.8, 2, 3, 4, 5, 6, 7, 8, 10],
        "vels": [ 5.713984666,8.080794609,9.034603029,9.896911754,9.896911754,10.68988647,10.68988647,11.42796933,11.42796933,11.42796933,11.42796933,11.42796933,11.42796933 ]
    }
}

"""laminarVels  = []
laminarDists = []

turbulantVels  = []
turbulantDists = []

print( "dthick: ", getDisplacementThickness( laminarDists, laminarVels ) );
print( "mthick: ", getMomentumThickness( laminarDists, laminarVels ) );
print( "L sFact: ", getShapeFactor( laminarDists, laminarVels ) );
 
print( "T sFact: ", getShapeFactor( turbulantDists, turbulantVels ) );

print( "laminar thickness:", getBLThickness( laminarDists, laminarVels ), "mm"  )
#print( "turbulant thickness:", getBLThickness( turbulantDists, turbulantVels ), "mm"  )
"""
# plotting data

"""plot.figure( 6159 );


plot.plot( boundaryLabData["100k_half"]["vels"], boundaryLabData["100k_half"]["positions"], "rx", label="Re 100k, halfplate" )
plot.plot( [0]+boundaryLabData["100k_half"]["vels"], [0]+boundaryLabData["100k_half"]["positions"], "r" )
plot.plot( boundaryLabData["200k_half"]["vels"], boundaryLabData["200k_half"]["positions"], "bo", label="Re 200k, halfplate" )
plot.plot( [0]+boundaryLabData["200k_half"]["vels"], [0]+boundaryLabData["200k_half"]["positions"], "b" )


plot.legend()"""

plot.figure( 26159 );

plot.title("Boundary layer profile fullplate Re 400k")

Vinf = max(boundaryLabData["400k_full"]["vels"])
dispThick = getBLThickness( np.array([0]+boundaryLabData["400k_full"]["positions"]), np.array([0]+boundaryLabData["400k_full"]["vels"])/Vinf )

velArr = np.array(boundaryLabData["400k_full"]["vels"])
velFilt = velArr<Vinf
velArr = velArr[velFilt]

disArr = np.array(boundaryLabData["400k_full"]["positions"])[velFilt]

m = np.polyfit( np.log(disArr/dispThick), np.log(velArr/Vinf), 1 )[0]
cRange = np.arange(0, 1.005, 0.005)
curve = np.power(cRange, (1/m))

filt   = (np.array(boundaryLabData["400k_full"]["positions"])/dispThick) < 1
filt0  = (np.array([0]+boundaryLabData["400k_full"]["positions"])/dispThick) < 1

plot.plot(  np.array(boundaryLabData["400k_full"]["positions"])[filt]/dispThick, np.array(boundaryLabData["400k_full"]["vels"])[filt]/Vinf,"rx", label="experiment data" )
plot.plot(  curve, cRange, "r", label="(y/δ)^"+str(m)[0:6] )

"""print( "100k disp: ",dispThick )

dispThick = getBLThickness( np.array([0]+boundaryLabData["200k_full"]["positions"]), np.array([0]+boundaryLabData["200k_full"]["vels"])/Vinf )

print( "200k disp: ",dispThick )

filt   = (np.array(boundaryLabData["200k_full"]["positions"])/dispThick) < 2
filt0  = (np.array([0]+boundaryLabData["200k_full"]["positions"])/dispThick) < 2
plot.plot(  np.array(boundaryLabData["200k_full"]["positions"])[filt]/dispThick, np.array(boundaryLabData["200k_full"]["vels"])[filt]/Vinf,"bx", label="Re 200k, fullplate δ="+str(dispThick)[0:4]+"mm" )
plot.plot( np.array([0]+boundaryLabData["200k_full"]["positions"])[filt0]/dispThick, np.array([0]+boundaryLabData["200k_full"]["vels"])[filt0]/Vinf, "b,--" )"""
 
#plot.plot( boundaryLabData["200k_full"]["positions"], boundaryLabData["200k_full"]["vels"], "rx", label="Re 200k" )
#plot.plot(  [0]+boundaryLabData["200k_full"]["positions"], [0]+boundaryLabData["200k_full"]["vels"],"r" )
#plot.plot( boundaryLabData["400k_full"]["positions"],boundaryLabData["400k_full"]["vels"],  "bo", label="Re 400k" )
#plot.plot( [0]+boundaryLabData["400k_full"]["positions"], [0]+boundaryLabData["400k_full"]["vels"], "b" )

plot.grid()

plot.legend()
plot.xlabel("y/δ")
plot.ylabel("V/V∞")

print( "boundary layer 400:", getMomentumThickness( [0]+boundaryLabData["400k_full"]["positions"], [0]+boundaryLabData["400k_full"]["vels"] ) )
print( "boundary layer 400c:", getMomentumThickness(cRange*(dispThick),curve*Vinf ) )
print(  "200:", getMomentumThickness([0]+boundaryLabData["200k_full"]["positions"], [0]+boundaryLabData["200k_full"]["vels"] ) )

plot.show();













