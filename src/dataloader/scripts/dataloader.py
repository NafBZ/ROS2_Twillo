#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import pandas as pd

class BagDataToCSV(Node):
    def __init__(self):
        super().__init__('bag_to_csv')
        self.subscription_rpm = self.create_subscription(
            Float32,
            '/current_rpm',
            self.callback_rpm,
            10 
        )
        self.subscription_avg_spindle = self.create_subscription(
            Float32,
            '/current_avg_spindle',
            self.callback_avg_spindle,
            10 
        )

        self.rpm_data = []
        self.avg_spindle_data = []

    def callback_rpm(self, msg):
        self.rpm_data.append(msg.data)

    def callback_avg_spindle(self, msg):
        self.avg_spindle_data.append(msg.data)

    def save_to_dataframe(self):
        df_rpm = pd.DataFrame({'rpm': self.rpm_data})
        df_avg_spindle = pd.DataFrame({'avg_spindle': self.avg_spindle_data})

        merged_df = pd.concat([df_rpm, df_avg_spindle], axis=1)

        merged_df.to_csv('./rosbag_data.csv', index=False)


def main(args=None):
    rclpy.init(args=args)
    node = BagDataToCSV()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('\nData retrieval complete. Saved in rosbag_data.csv. Terminating Node')
    
    node.save_to_dataframe()
    node.destroy_node()

if __name__ == '__main__':
    main()
