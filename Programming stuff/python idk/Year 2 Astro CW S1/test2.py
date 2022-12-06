import numpy as np
import matplotlib.pyplot as plot 
import scipy.optimize as sp

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

    timesHist       = []
    moonElcipseHist = []
    jupElcipseHist  = []
    seperationHist  = []
    

    probeOrbitPeriod = 0
    

    def __init__(this, initSolarAngle, probeOrbitPerigee, probeOrbitApogee ): 
        this.changeOrbit( probeOrbitApogee, probeOrbitPerigee )

        this.currentTime = initSolarAngle/this.dzdt 
        this.addMoon( 421800,  1821.5*2 ) # IO
 
        this.incrementTime(0) 

    def getTimeIndex( this, time ):
        for i in range(0, len(this.timesHist)):
            if ( this.timesHist[i]>=time ):
                return i
        return -1

    def trimStoredData( this, savedRangesYears ):
        timesHist       = []
        moonElcipseHist = []
        jupElcipseHist  = []
        seperationHist  = []

        for cSample in savedRangesYears:
            minTimeIndex = this.getTimeIndex( cSample[0]*(60*60*24*365) )
            maxTimeIndex = this.getTimeIndex( cSample[1]*(60*60*24*365) )

            timesHist += this.timesHist[ minTimeIndex:maxTimeIndex ]
            moonElcipseHist += this.moonElcipseHist[ minTimeIndex:maxTimeIndex ]
            jupElcipseHist += this.jupElcipseHist[ minTimeIndex:maxTimeIndex ]
            seperationHist += this.seperationHist[ minTimeIndex:maxTimeIndex ]

        this.timesHist = timesHist
        this.moonElcipseHist = moonElcipseHist
        this.jupElcipseHist = jupElcipseHist
        this.seperationHist = seperationHist


    def changeOrbit( this, probeOrbitPerigee, probeOrbitApogee ):
        this.probeSemiMajor = (probeOrbitPerigee+probeOrbitApogee)/2
        this.probeSemiMinor = ( (this.probeSemiMajor**2) - ( this.probeSemiMajor - probeOrbitPerigee )**2 )**0.5
        this.probeEccentrisity = (1-(this.probeSemiMinor**2/this.probeSemiMajor**2))**0.5

        this.probeSOAnglerMom = ( JUPITER_MU * this.probeSemiMajor * ( 1 - (this.probeEccentrisity**2) ) )**0.5

        this.dzdt = 2*np.pi/JUPITER_ORB_PERIOD
        this.A = (JUPITER_MU/this.probeSOAnglerMom) + this.dzdt
        this.B = (JUPITER_MU/this.probeSOAnglerMom)*this.probeEccentrisity
        this.hhomu = this.probeSOAnglerMom*this.probeSOAnglerMom/JUPITER_MU

        this.probeR = this.hhomu/( 1 + (this.probeEccentrisity * np.cos( this.probeTheta )) ) 

        this.probeOrbitPeriod = np.pi*2*np.sqrt((this.probeSemiMajor**3) / JUPITER_MU)

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
        this.jupElcipseHist.append( jupEclipse )
        this.seperationHist.append( this.probeR )

        return probePos, jupEclipse, moonEclipse 

JUPITER_SOLAR_MULTIPLIER = 0.035462

FIBRE_GYRO = 15.8
REACTION_WHEEL = 5
SENSORS_LIGHT = 6.7 + 7.6 + 4.2 + 7.8
SENSORS_DARK  = 6.7 + 4.2 + 7.8
COMS_POWER    = 25
POWER_CONTROL = 28

def exampleConsumptionFunction( inSolarEclipse, inJupiterEclipse, jupiterSeperation ):
    baseLoad = FIBRE_GYRO + REACTION_WHEEL*2 + COMS_POWER + POWER_CONTROL

    if ( inJupiterEclipse or inSolarEclipse ):
        baseLoad += 10

    baseLoad *= 3.3 # SETTINGS ARE GOOD FOR DEBUGGING (opt mass 64.09)

    if ( inJupiterEclipse ):
        return baseLoad + SENSORS_DARK
    else:
        return baseLoad + SENSORS_LIGHT

RTG_OUTPUT = 5.2 * 57 
BATTERY_CAPACITY_PER_KG = 110*(60*60)

class ProbeState:

    init_solar_output = 0
    init_RTG_output = 0
    init_battery_capacity = 0 # Watt seconds
    energyConsumtionFunction = exampleConsumptionFunction

    def __init__(this, RTG_count, solarMass, batteryMass, energyConsumtionFunction):

        this.init_RTG_output = RTG_count * RTG_OUTPUT
        this.init_solar_output = solarMass * 50 * JUPITER_SOLAR_MULTIPLIER
        this.init_battery_capacity = batteryMass*BATTERY_CAPACITY_PER_KG
        this.energyConsumtionFunction = energyConsumtionFunction

    def genPowerData( this, envSim ):
        energyStates = []

        pTime = 0
        currentEnergy = this.init_battery_capacity
        pEnergy = currentEnergy
        lowestCapacity = 10000000000000
        overCharge = 0
        underCharge = 0

        prevDt = 1000000000000

        avRecChange = 0
        
        TIME_SINCE_START = 365*60*60*24*( 2.7 ) # TODO GET CORRECT VALUE!

        for i in range(0, len(envSim.timesHist)):
            cTime = envSim.timesHist[i]
            cMoonEclipse = envSim.moonElcipseHist[i]
            cJupEc  = envSim.jupElcipseHist[i]
            cSep = envSim.seperationHist[i]
            RTG_efficiency = 1-(0.00787*(TIME_SINCE_START+cTime)/(365*60*60*24))

            dt = cTime - pTime

            if ( dt > prevDt*30 ):
                if ( currentEnergy/this.init_battery_capacity < 0.99999 ):
                    # clear data jump AND it didn't end prev iteration at max power
                    currentEnergy += dt * avRecChange

            else:
                if ( cJupEc or cMoonEclipse ):
                    currentEnergy += dt * ( this.init_RTG_output * RTG_efficiency )
                else:
                    currentEnergy += dt * ( (this.init_RTG_output * RTG_efficiency) + this.init_solar_output )

                currentEnergy -= dt * ( this.energyConsumtionFunction( cMoonEclipse, cJupEc, cSep ) )

            if ( currentEnergy > this.init_battery_capacity ):
                overCharge += currentEnergy - this.init_battery_capacity
                currentEnergy = this.init_battery_capacity

            if ( currentEnergy < 0 ):
                underCharge -= currentEnergy
                currentEnergy = 0

            avRecChange = (100000*avRecChange + (currentEnergy-pEnergy))/(dt+100000)

            pTime = cTime
            energyStates.append( currentEnergy )
            lowestCapacity = min( currentEnergy, lowestCapacity )
            prevDt = dt
            pEnergy = currentEnergy

        overCharge /= pTime - envSim.timesHist[1] 

        return np.array( envSim.timesHist ), np.array( energyStates ), lowestCapacity, overCharge, underCharge




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
                ecLens.append( newTotalTime/(60)  )
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
        plot.ylabel("eclipse time (mins)")
        plot.xlabel("time (days)")
            
    return longestTotalEclipse

def getPowerData( envSim, probeSim ):
    plot.figure( 420 );
    times, powers, ignore, ignore2, ignore3 = probeSim.genPowerData( envSim )

    plot.plot( times/(60*60*24*365), powers/(60*60)   );

    plot.ylabel("current power stored (Wh)")
    plot.xlabel("time (years)")

class PowerOptamiser:
    envSim = 0
    consumptionFunction = exampleConsumptionFunction

    lastScore = -1

    def __init__(this, envSim, consumptionFunction):
        this.consumptionFunction = consumptionFunction
        this.envSim = envSim

    def powerScoringFunction( this, inputs ):
        batteryMass, rtgCount, solarMass = inputs
        rtgCount = int( rtgCount )

        powerMass = batteryMass + rtgCount*54 + solarMass

        probeSim = ProbeState( rtgCount, solarMass, batteryMass, this.consumptionFunction )
         
        times, powers, lowestCapacity, overCharge, underCharge = probeSim.genPowerData( this.envSim )
        
        trashness = 0

        if( lowestCapacity/(batteryMass*BATTERY_CAPACITY_PER_KG) >= 0.9999 ):
            trashness += (overCharge * 50/(batteryMass*BATTERY_CAPACITY_PER_KG)) + 10000
        elif ( lowestCapacity <= 0 ): 
            trashness += 100000000

        trashness += underCharge

        if ( batteryMass<0 or solarMass<0 ):
            trashness += 1000000000000
        
        trashness += powerMass + ( abs(lowestCapacity-80000)/20 )

       # print( "S:",solarMass, "\tB:", batteryMass, "\tR:",rtgCount, "\tL:",lowestCapacity, "\tO:",overCharge , "\tM:",powerMass , "\tt:",trashness )

        this.lastScore = trashness
        return trashness

    def getOptimalValues( this ):
        maxDraw = max(this.consumptionFunction( True, True, JUPITER_RAD*1.3 ), this.consumptionFunction( False, False, JUPITER_RAD*1.3 ))

        initBMass  = 5
        initRTGs   = int( 0.8 + (maxDraw/(RTG_OUTPUT*(1-0.060599))) )
        initSMass  = 5

        outs = sp.minimize( this.powerScoringFunction, [initBMass, initRTGs, initSMass],  bounds=[ [0, 50], [0, 5], [0, 50] ], method="Powell", options={ } ).x 
        pOutMass = outs[0] + outs[2] + (54*int(outs[1]))
        bRTGCount = int(outs[1]) 
        outs2 = sp.minimize( this.powerScoringFunction, [initBMass, bRTGCount-1, initSMass],  bounds=[ [0, 50], [bRTGCount-1, bRTGCount-1], [0, 50] ], method="Powell", options={ } ).x 
        nOutMass = outs2[0] + outs2[2] + (54*int(outs2[1]))

        if ( nOutMass < pOutMass ):
            print("switching Outs!!!!!!!!!!!!!!!!!!!!!")
            outs = outs2
        elif ( bRTGCount == initRTGs ):
            print("init assumption correct")
        print( "bestMass: ", pOutMass )

        bBatMass  = outs[0]
        bSolMass  = outs[2]
        bRTGCount = int(outs[1]) 

        return bBatMass, bSolMass, bRTGCount

class MultiConfigurationOptamiser:
    sampleCount = 0
    inSunPowerDemands     = []
    inEclipsePowerDemands = []
    optimalMasses         = []
    optimalRTGCounts      = []
    optimalBatteryMasses  = []
    optimalSolarMasses    = []
    fianlLowestBatStates  = []

    inSunPowerRange = []
    inEclPowerRange = []

    cIndex = 0

    def __init__(this, minInSunPower, maxInSunPower, minInEclipsePower, maxInEclipsePower, sampleCount ):

        inSunRange = maxInSunPower - minInSunPower # 5
        inEclipseRange = maxInEclipsePower - minInEclipsePower # 4

        sampleConstant = np.sqrt( sampleCount/(inSunRange*inEclipseRange) )

        sunSampleCount     = int(inSunRange*sampleConstant)
        eclipseSampleCount = int(inEclipseRange*sampleConstant)

        for sunIndex in range(0, sunSampleCount):
            cSunPower = minInSunPower + (sunIndex*inSunRange/sunSampleCount)
            this.inSunPowerRange.append( cSunPower )

            for eclipseIndex in range(0, eclipseSampleCount):
                cEclipsePower = minInEclipsePower + (eclipseIndex*inEclipseRange/eclipseSampleCount)
                this.inSunPowerDemands.append( cSunPower )
                this.inEclipsePowerDemands.append( cEclipsePower )

                if ( len(this.inEclPowerRange) < eclipseSampleCount ):
                    this.inEclPowerRange.append( cEclipsePower )

        this.sampleCount = sunSampleCount*eclipseSampleCount

    def findOptimalAmounts( this, envSim ): 
        for i in range(0, this.sampleCount ):
            this.cIndex = i
            optamiser = PowerOptamiser( envSim, this.consumptionFunction )
            bBatMass, bSolMass, bRTGCount = optamiser.getOptimalValues()

            this.optimalMasses.append( bBatMass + bSolMass + (bRTGCount*54) )
            this.optimalRTGCounts.append( bRTGCount )
            this.optimalBatteryMasses.append( bBatMass )
            this.optimalSolarMasses.append( bSolMass )

            lowestCapacity = ProbeState( bRTGCount, bSolMass, bBatMass, this.consumptionFunction ).genPowerData( envSim )[2]
            this.fianlLowestBatStates.append( lowestCapacity )

        return

    def plotOptimals( this ):
        inEclPowerRange = np.array( this.inEclPowerRange ) # xaxis
        inSunPowerRange = np.array( this.inSunPowerRange ) # yaxis

        ecP, suP = np.meshgrid( inEclPowerRange, inSunPowerRange )
        
        gridShape = ecP.shape

        massGrid    = np.array( this.optimalMasses ).reshape( gridShape )
        rtgCGrid    = np.array( this.optimalRTGCounts ).reshape( gridShape )
        solarGrid   = np.array( this.optimalSolarMasses ).reshape( gridShape )
        batteryGrid = np.array( this.optimalBatteryMasses ).reshape( gridShape )

        plot.figure( 5409 )
        plot.title("Minimum mass for power requirements")
        plot.xlabel("Power consumption in eclipse (Watts)")
        plot.ylabel("Power consumption in light (Watts)")
        plot.colorbar( plot.contourf( ecP, suP, massGrid, 60 ) )

        plot.figure( 54029 )
        plot.title("RTG count at power requirements")
        plot.xlabel("Power consumption in eclipse (Watts)")
        plot.ylabel("Power consumption in light (Watts)")
        plot.colorbar( plot.contourf( ecP, suP, rtgCGrid, max(this.optimalRTGCounts)-min(this.optimalRTGCounts) ) ) 

        plot.figure( 54039 )
        plot.title("Solar panel mass at power requirements (kg)")
        plot.xlabel("Power consumption in eclipse (Watts)")
        plot.ylabel("Power consumption in light (Watts)")
        plot.colorbar( plot.contourf( ecP, suP, solarGrid, 60 ) )

        plot.figure( 54409 )
        plot.title("Battery mass at power requirements (kg)")
        plot.xlabel("Power consumption in eclipse (Watts)")
        plot.ylabel("Power consumption in light (Watts)")
        plot.colorbar( plot.contourf( ecP, suP, batteryGrid, 60 ) )
        

    def consumptionFunction( this, inSolarEclipse, inJupiterEclipse, jupiterSeperation ):
        if ( inSolarEclipse or inJupiterEclipse ):
            return this.inSunPowerDemands[ this.cIndex ]
        else:
            return this.inEclipsePowerDemands[ this.cIndex ]


dt = 1200




envSim = Environment( 0, PROBE_PERIGEE_2YEAR, PROBE_APOGEE_2YEAR )
print("2 year (phase 1) longest eclipse", getLongestEclipse( envSim, 365*2 , dt, True )) 

envSim.changeOrbit( PROBE_PERIGEE_3YEAR, PROBE_APOGEE_3YEAR )
print("3 year (phase 2) longest eclipse", getLongestEclipse( envSim, 365*3, dt, True )) 
 
"""probeOpt = PowerOptamiser( envSim, exampleConsumptionFunction )

bBatMass, bSolMass, bRTGCount = 1.7635247134412746, 46.08615988524932, 1 # probeOpt.getOptimalValues()

probeSim = ProbeState( bRTGCount, bSolMass, bBatMass, exampleConsumptionFunction )
print(bBatMass, bSolMass, bRTGCount)

getPowerData( envSim, probeSim ) """

envSim.trimStoredData( [ [3.34109, 3.34742], [4.94825, 4.9552] ] )

#configOpt = MultiConfigurationOptamiser( 60, 600, 60, 900, 600 )
configOpt = MultiConfigurationOptamiser( 50, 240, 50, 600, 200 )
configOpt.findOptimalAmounts( envSim )
configOpt.plotOptimals()



#displayOrbits()
print("with IO")
plot.show();
input("")
