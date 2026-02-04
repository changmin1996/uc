import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan
from std_msgs.msg import Bool
import math

class LimoStop(Node):
    def __init__(self):
        super().__init__('limo_stop')

        self.stop_pub_ = self.create_publisher(Bool, 'stop', 10)
        self.laser_sub_ = self.create_subscription(LaserScan, 
                                                   'scan',
                                                    10,
                                                    self.laserCallback)
    
    def laserCallback(self, msg):
        _stop = Bool()
        _stop.data = False
        for index, data in enumerate(msg.ranges):
            _theta = msg.angle_min + msg.angle_increment * index
            _x = data * math.cos(_theta)
            _y = data * math.sin(_theta)
            if 0.05 < _x < 0.25 and -0.1 < _y < 0.1:
                _stop.data = True
                break

        self.stop_pub_.publish(_stop)
        
def main(args=None):
    rclpy.init(args=args)
    limo_stop = LimoStop()
    rclpy.spin(limo_stop)
    limo_stop.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()