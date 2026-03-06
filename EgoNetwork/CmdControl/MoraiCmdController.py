import time
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from lib.network.UDP import Sender
from lib.define.EgoCtrlCmd import EgoCtrlCmd

IP = '127.0.0.1' 
PORT = 9095

#Protocol정보
#https://help-morai-sim.scrollhelp.site/ko/morai-sim-drive/24.R2/ros-1#id-(24.R2-ko)통신메시지프로토콜-EgoCtrlCmd.1

def main():
    ego_ctrl = Sender(IP, PORT)

    data = EgoCtrlCmd()    
    import ctypes 
    print(ctypes.sizeof(EgoCtrlCmd()))

    data.ctrl_mode = 2 # 1 : Keyboard   2 : AutoMode
    data.gear = 4  
    """
    index   0   1   2   3   4   5
    Gear    M   P   R   N   D   L
    """
    
    """
    1: Throttle(accel,brake,steer) 
    2: Velocity(velocity,steer)
    3: Acceleration(acceleration,steer)
    """
    data.cmd_type = 1
    data.accel = 0.5
    data.brake = 0.1

    # data.cmd_type = 2
    # data.velocity = 30 #km

    # data.cmd_type = 3
    # data.acceleration = 5 #m/s2
    
    data.front_steer = 0.1 # -1 ~ 1  
    while 1:
        ego_ctrl.send(data)
        time.sleep(0.1)

        

if __name__ == '__main__':
    main()