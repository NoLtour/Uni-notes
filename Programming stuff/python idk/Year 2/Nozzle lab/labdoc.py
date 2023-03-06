import numpy as np
import matplotlib.pyplot as plot


pressure_atm_bar = 1.028
temp_atm = 291
temp_0 = temp_atm
temp_r = 293.15
pressure_r_bar = 1.013
k = np.sqrt( temp_r*pressure_atm_bar/(temp_atm*pressure_r_bar) )

pressure_0_bar_guage = 4
pressure_0_bar_abs   = pressure_0_bar_guage + pressure_atm_bar

gamma = 1.4
R = 287
cP = 1005

def TABLE_2():
    pressure_out_abs = np.array( [5.028,4.778,4.528,4.278,4.028,3.528,3.028,2.028] )
    pressure_2_absCor = np.array( [5.128,4.728,4.328,3.928,3.528,2.928,2.928,2.928] )
    mass_flow_cor = np.array( [0,1.415527546,2.42661865,2.831055092,3.134382423,3.336600644,3.437709755,3.437709755] )

    p_out_l_p_0 = pressure_out_abs/pressure_0_bar_abs
    p_2_l_p_0 = pressure_2_absCor/pressure_0_bar_abs

    linPressures = 100000*( 5.028 - np.arange( 0, 3, 0.1 ) )

    rho_0 = pressure_0_bar_abs*100000/(R * temp_0 )

    T_out = temp_0/( (pressure_0_bar_abs*100000/linPressures)**( (gamma-1)/gamma ) )
    rho_out = rho_0/( (temp_0/T_out)**(1/(gamma-1)) )
    area_throat = np.pi*(1/1000)**2
    vel = np.sqrt( 2*cP * ( temp_0 - T_out ) )

    mass_flow_calc = vel*area_throat*rho_out*1000 # g/s
 
    plot.figure( 69 );

    plot.plot( mass_flow_cor, p_out_l_p_0, "ro-.", label="p_out/p_0" );
    plot.plot( mass_flow_cor, p_2_l_p_0, "bx--", label="p_2/p_0" );
    plot.plot( mass_flow_calc, linPressures/(pressure_0_bar_abs*100000), "g-", label="ee" );

    plot.ylabel("p/p_0")
    plot.xlabel("mass flow rate (g/s)")

    plot.legend()

    plot.show();

TABLE_2()

