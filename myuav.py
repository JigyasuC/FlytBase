#importing_useful_libraries
import time
from flyt_python import api

#initializing
UAV = api.navigation(timeout=120000)
time.sleep(3)

#initializing_takeoff_to_5.0_meters
UAV.take_off(5.0)
 
#waypoint_navigation_for_a_square_path_(side_=_6.5_meters)
i=1
while i<5:
        UAV.position_set(6.5, 0, 0, 1.57079632679, 0, False, False, True, True) #command_to_make_the_vehicle_go_6.5meters_in_x-direction_(NED_coordinate_system),_and_yawing_90_degrees_(1.57079632679_in_radians)
        time.sleep(2) #for_a_better_trajectory (smoother_square_path)
        i=i+1

#initializing_landing
UAV.land(async=False)

#terminating
UAV.disconnect()
