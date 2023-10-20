#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimpleSubscriber(Node):
    def __init__(self):
        super().__init__(node_name="simple_subscriber")
        self.sub_ = self.create_subscription(String, topic="chatter", callback=self.msgCallback, qos_profile=10)

        
    def msgCallback(self, msg):
        self.get_logger().info(f"Yahoo!!! {msg.data}")
        

def main():
    rclpy.init()
    simple_subscriber = SimpleSubscriber()
    rclpy.spin(simple_subscriber)
    simple_subscriber.destroy_node()
    rclpy.shutdown()

        
if __name__ == 'main':
    main()