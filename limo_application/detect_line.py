import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from std_msgs.msg import Int32

import cv2
import numpy as np
from cv_bridge import CvBridge

class DetectLine(Node):
    def __init__(self):
        super().__init__('detect_line')
        self.br_ = CvBridge()

        self.image_sub_ = self.create_subscription(Image, 
                                                   'camera/image/image_color',
                                                   self.imageCallback,
                                                   10)
        
        self.error_pub_ = self.create_publisher(Int32,
                                                'gap',
                                                10)
        
        lane_h_l = 0 
        lane_l_l = 0 
        lane_s_l = 0 

        lane_h_h = 60 
        lane_l_h = 220 
        lane_s_h = 255

        self.yellow_lane_low = np.array([lane_h_l,
                                        lane_l_l,
                                        lane_s_l])
        

        self.yellow_lane_high = np.array([lane_h_h,
                                        lane_l_h,
                                        lane_s_h])

        
    def imageCallback(self, msg):
        _image = self.br_.imgmsg_to_cv2(msg, 'bgr8')

        _roi = _image[400:480, 0:320]
        _hls = cv2.cvtColor(_roi, cv2.COLOR_BGR2HLS)
        _mask_yellow =cv2.inRange(_hls, self.yellow_lane_low, self.yellow_lane_high)

        M = cv2.moments(_mask_yellow)
        if M['m00'] > 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cy = 400 + cy
            _image = cv2.circle(_image, (cx, cy), 10, (255, 0, 0), -1)
            _image = cv2.line(_image, (170, 0), (170, 480), (0, 255, 0), 5)
            gap = 170 - cx
        else:
            gap = 0
        
        msg = Int32()
        msg.data = gap
        self.error_pub_.publish(msg)
        cv2.imshow('original_image', _image)
        cv2.imshow('roi_image', _roi)
        cv2.imshow('masked_image', _mask_yellow)
        cv2.waitKey(2)

def main(args=None):
    rclpy.init(args=args)
    detect_line = DetectLine()
    rclpy.spin(detect_line)
    detect_line.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()