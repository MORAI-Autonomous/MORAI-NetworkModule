from lib.define.type import *
from lib.define.base import Base

class EgoTrajectoryTrackingCmd(Base):
    _fields_ = [
        ("header", _char * 23),
        ("data_length", _int),
        ("aux_data", _int * 3),
        ("timestamp_sec", _int),
        ("timestamp_nanosec", _int),
        ("sequence", _byte),
        ("trajectory_count", _uint8),
        ("trajectories", _float * 4 * 30),
        ("tail", _char * 2)
    ]

    def __init__(self):
        self.header = '#TrajectoryTrackingCmd$'.encode()
        self.data_length = 490
        self.aux_data = (0,0,0)
        self.timestamp_sec = 0
        self.timestamp_nanosec = 0
        self.sequence = 0
        self.trajectory_count = 30
        self.trajectories = tuple((0.0, 0.0, 0.0, 0.0) for _ in range(30))
        self.tail = '\r\n'.encode()  
