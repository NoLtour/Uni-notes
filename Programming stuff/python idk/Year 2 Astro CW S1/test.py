import numpy as np
import matplotlib.pyplot as plot 

JUPITER_MU = 1.26687*(10**8)*(10**9)
JUPITER_RAD = 69173000

JUPITER_ORB_PERIOD = 4332.589*24*60*60

INIT_Z_PHASE2 = 2*np.pi*((2*365*24*60*60)/JUPITER_ORB_PERIOD)

PROBE_PERIGEE_2YEAR = 73323380 
PROBE_APOGEE_2YEAR  = 622557000

PROBE_PERIGEE_3YEAR = PROBE_PERIGEE_2YEAR
PROBE_APOGEE_3YEAR  = 424821500

class Environment:
    moonCount    = 0
    moonRadii    = [] # all in meters
    moonOrbRadii = []
    moonOrbFreqs = []

    probeSemiMajor = 0
    probeSemiMinor = 0
    probeEccentrisity = 0
    probeSOAnglerMom = 0
    probeTheta = 0
    probeZ = 0
    probeR = 0

    currentTime = 0

    timesHist = []
    moonElcipseHist = []
    JupElcipseHist = []

    probeOrbitPeriod = 0
    

    def __init__(this, initSolarAngle, probeOrbitPerigee, probeOrbitApogee ): 
        
        this.probeSemiMajor = (probeOrbitPerigee+probeOrbitApogee)/2
        this.probeSemiMinor = ( (this.probeSemiMajor**2) - ( this.probeSemiMajor - probeOrbitPerigee )**2 )**0.5
        this.probeEccentrisity = (1-(this.probeSemiMinor**2/this.probeSemiMajor**2))**0.5

        this.probeSOAnglerMom = ( JUPITER_MU * this.probeSemiMajor * ( 1 - (this.probeEccentrisity**2) ) )**0.5

        this.dzdt = 2*np.pi/JUPITER_ORB_PERIOD
        this.A = (JUPITER_MU/this.probeSOAnglerMom) + this.dzdt
        this.B = (JUPITER_MU/this.probeSOAnglerMom)*this.probeEccentrisity
        this.hhomu = this.probeSOAnglerMom*this.probeSOAnglerMom/JUPITER_MU

        this.probeR = this.hhomu/( 1 + (this.probeEccentrisity * np.cos( this.probeTheta )) )

        this.currentTime = initSolarAngle/this.dzdt

        this.probeOrbitPeriod = np.pi*2*np.sqrt((this.probeSemiMajor**3) / JUPITER_MU)

        #this.addMoon( 1882700, 4820.6 ) # Callisto
        #this.addMoon( 1070400, 5268.2 ) # Ganymede
        #this.addMoon( 671100,  3121.6 ) # Europa
        this.addMoon( 421800,  1821.5*2 ) # IO

        #this.addMoon( JUPITER_RAD/1000, 0 )
        this.incrementTime(0)
        return;

    def addMoon(this, orbitalRadiusKM, moonDiameterKM):
        this.moonRadii.append( moonDiameterKM*1000 )
        
        this.moonOrbRadii.append( orbitalRadiusKM*1000 )

        this.moonOrbFreqs.append( 2*np.pi/(2*np.pi*np.sqrt( (orbitalRadiusKM*1000)**3 / JUPITER_MU )) )

        this.moonCount += 1

    def getMoonPos( this, moonIndex ):
        moonXAxisAngle = this.probeZ + (this.moonOrbFreqs[moonIndex]*this.currentTime)
        moonOrbRadius = this.moonOrbRadii[moonIndex]

        x = moonOrbRadius * np.cos( moonXAxisAngle )
        y = moonOrbRadius * np.sin( moonXAxisAngle )

        return x, y
        
    dzdt = 0
    A = 0
    B = 0
    hhomu = 0
        
    def incrementTime(this, timeChange):
        # update probe position
        angularVel = this.probeSOAnglerMom/(this.probeR**2) 

        this.probeTheta += angularVel*timeChange
        
        this.probeR = this.hhomu/( 1 + (this.probeEccentrisity * np.cos( this.probeTheta  )) )

        this.currentTime += timeChange
        this.probeZ = this.dzdt*this.currentTime

    def getProbePosition( this ):
        
        x = np.cos(this.probeTheta + this.probeZ) * this.probeR
        y = np.sin(this.probeTheta + this.probeZ) * this.probeR

        return x,y

    def inMoonEclipse( this, probePosition ):
        for mIndex in range(0, this.moonCount):
            moonPos = this.getMoonPos( mIndex )
            moonRadius = this.moonRadii[mIndex]

            if ( (moonPos[0]<probePosition[0]) and (abs(moonPos[1]-probePosition[1])<moonRadius) ):
                return True
            
        return False
    
    def inJupiterEclipse( this, probePosition ):
        if ( (0<probePosition[0]) and (abs(probePosition[1] ) < JUPITER_RAD) ):
            return True
        
        return False

    def getProbeConditions( this ):
        probePos = this.getProbePosition()
        
        moonEclipse = this.inMoonEclipse( probePos )
        jupEclipse = this.inJupiterEclipse( probePos )

        this.timesHist.append( this.currentTime )
        this.moonElcipseHist.append( moonEclipse )
        this.JupElcipseHist.append( jupEclipse )

        return probePos, jupEclipse, moonEclipse 


def displayOrbits():
    initEnv = Environment( 0, PROBE_PERIGEE_3YEAR, PROBE_APOGEE_3YEAR )
    initEnv.incrementTime( 0 )

    X = []
    Y = []

    moonsXs = [ [],[],[],[],[] ]
    moonsYs = [ [],[],[],[],[] ]

    for i in range(0, int((19.25)*60)):
        initEnv.incrementTime( 60 )
        cPos = initEnv.getProbePosition()

        X.append( cPos[0] )
        Y.append( cPos[1] )

        for mIndx in range(0, initEnv.moonCount):
            cMoonPos = initEnv.getMoonPos( mIndx )

            moonsXs[mIndx].append( cMoonPos[0] )
            moonsYs[mIndx].append( cMoonPos[1] )

    plot.figure( 69 );

    plot.plot( X, Y  );

    plot.ylabel("Y")
    plot.xlabel("X")


    for mIndx in range(0, initEnv.moonCount):
        plot.plot( moonsXs[mIndx], moonsYs[mIndx]  )
 
def displayEclipses():
    initEnv = Environment( 0, 73323380, 622557000 )
    initEnv.incrementTime( 0 )

    inEclipse = []
    time      = []

    for cMin in range(0, 50 * 24*60):
        initEnv.incrementTime( 60 )
        probeState = initEnv.getProbeConditions( )

        if ( probeState[1] ):
            inEclipse.append( 0 )
        elif ( probeState[2] ):
            inEclipse.append( 1 )
        else:
            inEclipse.append( 0 )

        time.append( cMin )

    plot.figure( 21 );

    plot.plot( time, inEclipse  );

    plot.ylabel("in eclipse")
    plot.xlabel("time (mins)") 
    return

ecCharts = 2231

def getLongestEclipse( freshEnvSim, days, dt, plotting=False ):
    global ecCharts 

    longestTotalEclipse = 0
    startEcTime = 0

    ecTimes = []
    ecLens  = []
    ecCharts += 1

    for i in range(0, int((days*24*60*60)/dt) ):
        freshEnvSim.incrementTime( dt )
        cState = freshEnvSim.getProbeConditions()
        
        if ( cState[1] or cState[2] ):
            if ( startEcTime == 0 ):
                startEcTime = freshEnvSim.currentTime
        elif ( startEcTime != 0 ):
            newTotalTime = freshEnvSim.currentTime - startEcTime

            if ( plotting ):
                period = freshEnvSim.probeOrbitPeriod
                ecLens.append( newTotalTime/(period)  )
                ecTimes.append( freshEnvSim.currentTime/(60*60*24) )

            longestTotalEclipse = max( newTotalTime, longestTotalEclipse )
            startEcTime = 0

    #print( "longestTimeInEclipse: ",longestTotalEclipse/60, "mins" )
    if ( plotting ):
        #plot.figure( ecCharts )
        plot.figure( 53642 )
        if ( ecCharts%2==0 ):
            plot.plot( ecTimes, ecLens, "bx"  )
        else:
            plot.plot( ecTimes, ecLens, "rx"  )
        plot.ylabel("eclipse RaTiO")
        plot.xlabel("time (days)")
            
    return longestTotalEclipse

dt = 120

envSim2Years = Environment( 0, PROBE_PERIGEE_2YEAR, PROBE_APOGEE_2YEAR )
print("2 year (phase 1) longest eclipse", getLongestEclipse( envSim2Years, 365*5 , dt, True )) 

envSim3Years = Environment( 0, PROBE_PERIGEE_3YEAR, PROBE_APOGEE_3YEAR )
print("3 year (phase 2) longest eclipse", getLongestEclipse( envSim3Years, 365*5, dt, True )) 

displayOrbits()

plot.show();
input("")