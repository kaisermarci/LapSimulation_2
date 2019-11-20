from TwoDimLookup_motor import TwoDimLookup_motor as motor_TDL
from GG_ESB import GG_ESB_OneDim
from sliceable import Sliceable
import numpy as np


class vehicleOneDimLookup_2:
    def __init__(self,car_data,car_name, upper_max_speed=50):
        self.C_F = car_data(0)  #Cornering stiffnes front [N/rad]
        self.C_R = car_data(1)  #Cornering stiffnes rear [N/rad]
        self.m = car_data(2)      #Weight [kg]
        self.CoG_X = car_data(3) #Center of gravity (0 at front axis, 1 at rear axis)
        self.mu = car_data(4)    #Friciton coefficient between tire gum and street
        self.CoP_X = car_data(6)
        self.alpha = car_data(5)  #Slip angle as optimum value [deg]
        self.C_la = car_data(7)
        self.rho=car_data(8)
        self.DriveType = car_data(9)  #2WD or 4WD
        self.gearRatio = car_data(10)
        self.tireRadius = car_data(11)
        self.fr = car_data(12)  # Friction coefficient
        self.Lift2Drag = car_data(13)
        self.Pmax = car_data(14)
        self.CarName = car_name
        self.DrivingRes = None


        ggMap = GG_ESB_OneDim(self.C_F, self.C_R, self.m, self.CoG_X, self.mu, self.alpha, self.DriveType)
        
        self.ay_max = ggMap.GG_ESB_ay_Max() 
        self.ax_max = ggMap.GG_ESB_ax_Max()
        
        ##ggMap.Plot_gg(self.ay_max, self.ax_max)  # Plot gg map
        
        self.upper_max_speed = upper_max_speed
        self.min_curvature = self.ay_max / upper_max_speed**2
        
        self.DriveType = car_data(8)

    def create_state(self, ls):
        n = ls.trackmap.curvature.shape[0]
        return State(n, maxspeed=self.upper_max_speed)

    def max_speed_calc(self, ls):
        k = np.fabs(ls.trackmap.curvature)
        corner = k > self.min_curvature

        ls.state_max.speed[corner] = np.transpose([np.sqrt(self.ay_max/np.fabs(k[corner]))])

    def lim_accel(self, ls, state):
        k = ls.trackmap.curvature[[ls.counter]]
        cp = ls.counter in ls.critical_points
        ay = np.abs(state.speed**2*k)
        if (ay <= self.ay_max) | cp:
            if cp:
                ay = self.ay_max

            if ls.dir == 1:
                ax = ((1-(ay**2 / self.ay_max**2)) * self.ax_max**2)**0.5
            else:
                if self.DriveType == '2WD':
                    ax = (-2) * ((1-(ay**2 / self.ay_max**2)) * self.ax_max**2)**0.5
                if self.DriveType == '4WD':
                    ax = (-1) * ((1-(ay**2 / self.ay_max**2)) * self.ax_max**2)**0.5
            
            ls.run = True

        else:
            ax = 0
            ls.run = False

        state.speed = np.sqrt(state.speed**2 + 2 * ax * ls.trackmap.ds * ls.dir)
        state.AccelX = ax
        
        #Initialize motor
        Motor = motor_TDL(self.gearRatio, self.tireRadius, self.CoG_X, self.m, self.CoP_X, self.C_la, self.rho, self.fr, self.Lift2Drag, self.DriveType)
        self.DrivingRes = Motor.Driving_Resistances(state.speed)    #calculate driving resistances
        
        return state


class State(Sliceable):
    def __init__(self, n, maxspeed=100):
        self.speed = np.ones((n, 1)) * maxspeed
        self.AccelX = np.zeros((n, 1))
