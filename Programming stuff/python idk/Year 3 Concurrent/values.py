

import matplotlib.pyplot as plt
import numpy as np

BOLTZ_CONST = 0.00000005670367

def calculateSurfaceTemp( lunarIncidentPM, solarIncidentPM, lunarArea, solarArea, internalEnergyDissipation,
                         surfaceEmissivity:np.ndarray, surfaceAbsorbtance:np.ndarray, surfaceArea ):
    
    heatIn = (lunarIncidentPM*lunarArea + solarIncidentPM*solarArea)*surfaceAbsorbtance + internalEnergyDissipation
    
    surfaceTemp = (heatIn/(BOLTZ_CONST*surfaceEmissivity*surfaceArea))**0.25
    
    return surfaceTemp
  
def calculateInputPower( lunarIncidentPM, solarIncidentPM, lunarArea, solarArea, internalEnergyDissipation,
                        surfaceAbsorbtance:np.ndarray ):
    
    heatIn = (lunarIncidentPM*lunarArea + solarIncidentPM*solarArea)*surfaceAbsorbtance + internalEnergyDissipation
  
    return heatIn
  
lunarEmissionPMMax = 390 # W/m^2
lunarEmissionPMMin = 0 # W/m^2
solarEmissionPMMax = 1426 # W/m^2
solarEmissionPMMin = 0 # W/m^2

internalDissipationMax = 8 # W
internalDissipationMin = 3 # W


sunFacingCrossSection  = 0.1*0.2 # m^2
moonFacingCrossSection = 0.1*0.2 # m^2
totalSurfaceArea       = 0.1*0.1*( 2*1 + 2*3 + 3*1 )*2

emVals = np.linspace(0, 1, 1000)
abVals = 1-np.linspace(0, 1, 1000)

emGrid, abGrid = np.meshgrid(emVals, abVals)

def plotSurfaceTemps():
    plt.figure(1)
    plt.title("")
    plt.xlabel("Emissivity")
    plt.ylabel("Absobtivity")
    plt.imshow( calculateSurfaceTemp( lunarEmissionPMMin, solarEmissionPMMin, sunFacingCrossSection, moonFacingCrossSection, internalDissipationMin, emGrid, abGrid ) ) 
    plt.colorbar()
    plt.xticks( np.linspace(0, 99, 5), ['0.0', '0.25', '0.5', '0.75', '1.0'] )
    plt.yticks( np.linspace(0, 99, 5), ['1.0', '0.75', '0.5', '0.25', '0.0'] )

    plt.show()
    

def plotHeaterRequirements():
    minAcceptableTemp = 275
    maxAcceptableTemp = 315
    
    naturalInputPower_peakHeating = calculateInputPower( lunarEmissionPMMax, solarEmissionPMMax, sunFacingCrossSection, moonFacingCrossSection, internalDissipationMax, abGrid )
    naturalInputPower_peakCold    = calculateInputPower( lunarEmissionPMMin, solarEmissionPMMin, sunFacingCrossSection, moonFacingCrossSection, internalDissipationMin, abGrid )
    
    totalHeatInpRequired_peakHeating = maxAcceptableTemp**4 * BOLTZ_CONST * emGrid * totalSurfaceArea
    totalHeatInpRequired_peakCold    = minAcceptableTemp**4 * BOLTZ_CONST * emGrid * totalSurfaceArea 
    
    heatingRequired_peakHeating = totalHeatInpRequired_peakHeating - naturalInputPower_peakHeating
    heatingRequired_peakCold    = totalHeatInpRequired_peakCold    - naturalInputPower_peakCold
    
    validConfigs = (heatingRequired_peakHeating > 0) * (heatingRequired_peakCold > 0)
    
    plt.figure(1)
    plt.title("Max heating required for valid configurations (cubesat core)")
    plt.xlabel("Emissivity")
    plt.ylabel("Absobtivity")
    plt.imshow( np.where(validConfigs, heatingRequired_peakCold, np.inf ) ) 
    plt.colorbar()
    plt.xticks( np.linspace(0, 1000, 5), ['0.0', '0.25', '0.5', '0.75', '1.0'] )
    plt.yticks( np.linspace(0, 1000, 5), ['1.0', '0.75', '0.5', '0.25', '0.0'] )

    plt.show()

plotHeaterRequirements()
