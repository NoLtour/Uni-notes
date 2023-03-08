import numpy as np
import matplotlib.pyplot as plot


pressure_atm_bar = 1.028
temp_atm = 18 + 273.15
temp_0 = temp_atm
temp_r = 293.15
pressure_r_bar = 1.013
k = np.sqrt( temp_r*pressure_atm_bar/(temp_atm*pressure_r_bar) )


gamma = 1.4
R = 287
cP = 1005

def TABLE_2():
    pressure_0_bar_guage = 4
    pressure_0_bar_abs   = pressure_0_bar_guage + pressure_atm_bar

    critical_pressure_bar = pressure_0_bar_abs*( 2/(gamma+1) )**(gamma/(gamma-1))
    print("Table 1, P*/P_0: ", critical_pressure_bar/pressure_0_bar_abs )

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

    #mass_flow_calc = vel*area_throat*rho_out*1000 # g/s

    mass_flow_calc = 1000*area_throat*rho_0*(linPressures/(pressure_0_bar_abs*100000))**(1/gamma) * np.sqrt( 2 * cP * temp_0 * ( 1 - ((linPressures/(pressure_0_bar_abs*100000)))**((gamma-1)/gamma) ) )
 
    plot.figure( 69 );
    plot.plot( p_2_l_p_0, mass_flow_cor, "bx--", label="p_2/p_0" );

    plot.plot( linPressures/(pressure_0_bar_abs*100000), mass_flow_calc, "g-", label="theoretical" );

    plot.xlabel("p_2/p_0")
    plot.ylabel("mass flow rate (g/s)")

    plot.legend()


    plot.figure( 269 );
    plot.plot( p_out_l_p_0,mass_flow_cor,  "ro--" );

    plot.xlabel("p_out/p_0")
    plot.ylabel("mass flow rate (g/s)")

    plot.legend()

TABLE_2()


def TABLE_3():

    P_0_abs_bar = pressure_atm_bar + np.array( [  0, 1, 1.5,  2,  2.5,   3, 3.5, 4,   4.5, 5 ] )

    mass_flow_correct =          k*np.array( [0, 1.4, 1.6, 1.9, 2.2, 2.6, 3,   3.3, 3.6, 4 ] );
    


    plot.figure( 1269 );
    plot.plot( P_0_abs_bar,  mass_flow_correct, "rx" );

    plot.xlabel("p_0")
    plot.ylabel("mass flow rate (g/s)")

    grad = (np.sqrt( 2 * cP * temp_0 )/(R * temp_0)) * np.pi*(1/1000)**2 * ( 2/(gamma+1) )**(gamma/(gamma-1)) * np.sqrt( (gamma-1)/(gamma+1) )
    
    m, c = np.polyfit(    P_0_abs_bar[1:],mass_flow_correct[1:], 1 )

    print( "T3, gradient of slope: ", m )
    print( "T3, theo gradient of slope: ", grad * 100000*1000 )

    plot.plot(  np.array([0, 6]), (np.array([0, 6]))*m + c, "r--" );

    plot.legend()

TABLE_3()

def TABLE_4():
    area_throat = np.pi*(1/1000)**2


    tapping_point      = np.array( [ 1,   2,    3,    4,  5,   6,   7,  8 ] )
    guage_p_bar_nCor   = np.array( [ 2.9, 1.8, 1.7, 1.3, 1.3, 0.2,  0, 0 ] )
    p_bar_abs_nC       = np.array( [ 3.928, 2.828, 2.728, 2.328, 2.328, 1.228,  1.028, 1.028 ] )
    p_bar              = np.array( [ 3.928, 2.928, 2.828, 2.328, 2.328, 1.328,  1.128, 1.028 ] )
    
    p_0_bar = 4 + pressure_atm_bar
    rho_0 = p_0_bar*100000/(R * temp_0 )


    p_0_ov_p = p_0_bar/p_bar

    A_ov_Ast          = np.array( [ 1.4, 1, 1.13, 1.28, 1.42, 1.59, 1.77, 1.94 ] )
    area_point = A_ov_Ast * area_throat;


    # pre shock calcs
    temps_preSh = temp_0/( p_0_ov_p**((gamma-1)/gamma) )
    speed_sound_prSh = np.sqrt( gamma * R * temps_preSh )
    rho_preSh = p_bar*100000/(R*temps_preSh)

    mass_flow_rate = rho_0 * np.sqrt( 2 * cP * temp_0 ) * area_throat * ( 2/(gamma+1) )**(1/(gamma-1)) * np.sqrt( (gamma-1)/(gamma+1) )
    pre_sh_V = mass_flow_rate/(rho_preSh*area_point)
    Ma_pre_sh = pre_sh_V/speed_sound_prSh

    # post shock calcs

    plot.figure( 13 )

TABLE_4()

plot.show();