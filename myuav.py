import time
from flyt_python import api

UAV = api.navigation(timeout=120000)
time.sleep(3)

#takeoff
UAV.take_off(5.0)
 
#waypoint
i=1
while i<5:
        UAV.position_set(6.5, 0, 0, 1.57079632679, 0, False, False, True, True)
        time.sleep(2)
        i=i+1

#land
UAV.land(async=False)

UAV.disconnect()

