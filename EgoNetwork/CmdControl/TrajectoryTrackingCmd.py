import time
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
import pandas as pd

from lib.network.UDP import Sender
from lib.define.EgoTrajectoryTrackingCmd import EgoTrajectoryTrackingCmd

IP = '127.0.0.1' 
PORT = 9109

#Protocol정보
#https://help-morai-sim.scrollhelp.site/ko/morai-sim-drive/24.R2/udp-1
"""
Trajectory Tracking Mode를 사용하기 위해서 Network setting > Cmd Control을 TrajectoryTrackingCmd로 Connect 해야함.
'R_KR_PG_K-City' 맵에서 'I'를 눌러 초기 위치로 이동 후 'Q' 를 눌러 Ego Controller를 AV-ExternalCtrl로 설정한 뒤 코드를 실행해야 동작함.
아래 예제는 특정 path를 주행한 뒤 정지하지만
Log 파일이나, 다른 실시간 데이터를 받아 Trajectory를 업데이트하여 송신하면 계속 주행할 수 있음.
"""
def main():
    ego_traj = Sender(IP, PORT)

    data = EgoTrajectoryTrackingCmd()
    import ctypes 
    print(ctypes.sizeof(EgoTrajectoryTrackingCmd()))

    t = time.time()
    data.timestamp_sec = int(t)
    data.timestamp_nanosec = int((t - data.timestamp_sec) * 1e9)

    data.trajectory_count = 30

    path = pd.read_csv(str(Path(__file__).resolve().parents[2]) + '\\lib\\trajectory\\R_KR_PG_K-City\\path.csv')

    for i in range(30):
        data.trajectories[i][0] = path['x'][150 + i * 50]
        data.trajectories[i][1] = path['y'][150 + i * 50]
        data.trajectories[i][2] = path['z'][150 + i * 50]
        data.trajectories[i][3] = 2.0

    ego_traj.send(data)
   
if __name__ == '__main__':
    main()