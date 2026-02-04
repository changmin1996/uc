import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32, Bool
from geometry_msgs.msg import Twist

class LimoControl(Node):
    def __init__(self):
        super().__init__('limo_control')
        self.stop_sub_ = self.create_subscription(Bool, 
                                                  'stop',
                                                  self.stopCallback,
                                                  10)
        self.error_sub_ = self.create_subscription(Int32,
                                                   'gap',
                                                   self.errorCallback,
                                                   10)
        self.cmd_pub_ = self.create_publisher(Twist,
                                              'cmd_vel',
                                              10)
        self.stop_flag_ = True

    def stopCallback(self, msg):
        self.stop_flag_ = msg.data

    def errorCallback(self, msg):
        _cmd = Twist()

        _cmd.linear.x = 0.3
        _cmd.angular.z = 0.0055 * msg.data

        if self.stop_flag_:
            _cmd.linear.x = 0.0
            _cmd.angular.z = 0.0
        
        self.cmd_pub_.publish(_cmd)

def main(args=None):
    rclpy.init(args=args)
    limo_control = LimoControl()
    rclpy.spin(limo_control)
    limo_control.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()