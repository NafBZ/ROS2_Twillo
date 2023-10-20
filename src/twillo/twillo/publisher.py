#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimplePublisher(Node):
    def __init__(self):
        super().__init__(node_name="simple_publisher")
        self.pub_ = self.create_publisher(String, topic="chatter", qos_profile=10)
        self.counter_ = 0
        self.frequency_ = 1.0
        
        self.get_logger().info(f"Publishing at {self.frequency_} Hz")
        self.timer_ = self.create_timer(timer_period_sec= self.frequency_, callback=self.timerCallback)
        
    def timerCallback(self):
        msg = String()
        msg.data = f"I am learning ROS2 in {self.counter_} seconds"
        
        self.pub_.publish(msg)
        self.counter_ += 1
        

def main():
    rclpy.init()
    simple_publisher = SimplePublisher()
    rclpy.spin(simple_publisher)
    simple_publisher.destroy_node()
    rclpy.shutdown()


        
if __name__ == 'main':
    main()
    