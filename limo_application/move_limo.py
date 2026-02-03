import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
import math

class MoveLimo(Node):
    def __init__(self):
        super().__init__('move_limo')

        self.pub_ = self.create_publisher(Twist, 'cmd_vel', 10)

        self.timer_ = self.create_timer(0.1, self.timerCallback)
        self.t_ = 0.0
    
    def timerCallback(self):
        _cmd = Twist()
        _cmd.linear.x = 1.0*math.sin(2*math.pi*0.5*self.t_)
        self.t_+=0.1
        self.pub_.publish(_cmd)

def main(args=None):
    rclpy.init(args=args)
    move_limo = MoveLimo()
    rclpy.spin(move_limo)
    move_limo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()