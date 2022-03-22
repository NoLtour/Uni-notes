




import math


class Setting:

    def __init__( this, angle, power ):

        this.range = 0;
        this.angle = angle;
        this.power = power;

        this.calcRange();

    def calcRange( this ):
        #                   angle adjustment                |      range at 45 degrees
        this.range = math.sin( this.angle * 2 * 3.142/180 ) * ( 6.808-(this.power*0.3672) )



settings = []

for P in range( 0, 16 ):
    for A in range( 45, 56 ):
        settings.append( Setting( A, P ) )


#print( settings )

def getSettings( desRange, setCount ):
    desRange = float(desRange)
    setCount = int(setCount)

    
    lowests = []
    resSets = []

    for i in range(0, setCount):
        cLowest = 1000000000000000
        resSets.append(0)

        for z in range(0, len(settings)):
            cSet = settings[z]
            cInacc = abs(cSet.range - desRange)
            if ( cInacc < cLowest and not ( cSet in resSets ) ):
                cLowest = cInacc
                resSets[i] = cSet
        
        lowests.append( abs(resSets[i].range - desRange) )
    
    for i in range(0, setCount):
        cSet = resSets[i]
        print( "---------" )
        print( "Inacc:", (cSet.range - desRange) )
        print( "Angle:", (cSet.angle) )
        print( "Power:", (cSet.power) )

    #print( lowests )
    return resSets;

tmp = getSettings( input("desired range: "), input("search count: ") )

#print(tmp)

input("\n\n\npress enter to exit")

