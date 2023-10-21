#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import SetParametersResult
from rclpy.parameter import Parameter

class SimpleParameters(Node):
    def __init__(self):
        super().__init__("simple_parameter")
        
        self.declare_parameter(name="wheel_radius", value= 5.0)
        self.declare_parameter(name="model_name", value = "twillo")
        
        self.wheel_radius = self.get_parameter('wheel_radius').value
        self.model_name = self.get_parameter('model_name').value
        
        self.add_on_set_parameters_callback(self.paramChangeCallback)
    
    def paramChangeCallback(self, params): 
        result = SetParametersResult()
        
        for param in params:          
            if param.name == 'model_name' and param.type_ == Parameter.Type.STRING:
                self.model_name = param.value
                self.get_logger().info(f"Robot's model is changed to {param.value}")
                self.wheel_radius = 8.0
                self.get_logger().info(f"Wheel radius is changed to {self.wheel_radius} cm")
                result.successful = True
                
            if param.name == 'wheel_radius' and param.type_ == Parameter.Type.DOUBLE:
                self.get_logger().info(f"Wheel radius is changed to {param.value} cm")
                result.successful = True
                
        return result
    
    
def main():
    rclpy.init()
    simple_parameters = SimpleParameters()
    try:
        rclpy.spin(simple_parameters)
    except KeyboardInterrupt:
        print("\nTerminating Node")
        simple_parameters.destroy_node()
    #rclpy.shutdown()


        
if __name__ == 'main':
    try:
        main()
    except KeyboardInterrupt:
        print("Terminating the Node")