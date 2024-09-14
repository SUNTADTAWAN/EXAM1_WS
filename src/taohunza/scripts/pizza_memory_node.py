#!/usr/bin/python3

from taohunza.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray,Int16
import numpy as np
import yaml
from array import array

class pizza_memory_node(Node):
    def __init__(self):
        super().__init__('pizza_memory_node')
        # self.declare_parameter('pizza_positionX',[0.0])
        # self.declare_parameter('pizza_positionY',[0.0])
        self.yaml_file_path = 'src/taohunza/config/Pizza_memory.yaml'
        self.create_subscription(Float64MultiArray,'pizza_posX',self.pizza_positionX_callback,10)
        self.create_subscription(Float64MultiArray,'pizza_posY',self.pizza_positionY_callback,10)
        self.create_subscription(Int16,'now_state',self.state_callback,10)
        self.state = 0
        self.tim = 1.0/100.0
        self.create_timer(self.tim ,self.timer_callback)
        self.flag = 0

    def state_callback(self,msg):
        self.state = msg.data

    def pizza_positionX_callback(self,msg):
        self.get_logger().info(f'posX {self.state}')
        if self.state == 0:
            # self.positonX_1 = msg.data
            self.update_yaml_file(f'Foxy'+'/pizza_memory', 'pizza_positionX', msg.data.tolist())
        elif self.state == 1:
            # self.positonX_2 = msg.data
            self.update_yaml_file(f'Noetic'+'/pizza_memory', 'pizza_positionX', msg.data.tolist())
        elif self.state == 2:
            # self.positonX_3 = msg.data
            self.update_yaml_file(f'Humble'+'/pizza_memory', 'pizza_positionX', msg.data.tolist())
        elif self.state == 3:
            # self.positonX_4 = msg.data
            self.update_yaml_file(f'Iron'+'/pizza_memory', 'pizza_positionX', msg.data.tolist())
    def pizza_positionY_callback(self,msg):
        self.get_logger().info(f'posY {msg.data.tolist()}')
        if self.state == 0:
            # self.positonY_1 = msg.data
            self.update_yaml_file(f'Foxy'+'/pizza_memory', 'pizza_positionY', msg.data.tolist())
        elif self.state == 1:
            # self.positonY_2 = msg.data
            self.update_yaml_file(f'Noetic'+'/pizza_memory', 'pizza_positionY', msg.data.tolist())
        elif self.state == 2:
            # self.positonY_3 = msg.data
            self.update_yaml_file(f'Humble'+'/pizza_memory', 'pizza_positionY', msg.data.tolist())
        elif self.state == 3:
            # self.positonY_4 = msg.data
            self.update_yaml_file(f'Iron'+'/pizza_memory', 'pizza_positionY', msg.data.tolist())

        


    def update_yaml_file(self, node_name, param_name, param_value):
        # Load the YAML file
        with open(self.yaml_file_path, 'r') as file:
            yaml_data = yaml.safe_load(file)

        # Update the parameter value
        if node_name in yaml_data:
            yaml_data[node_name]['ros__parameters'][param_name] = param_value
        else:
            # If the node doesn't exist, create it
            yaml_data[node_name] = {
                'ros__parameters': {
                    param_name: param_value
                }
            }

        # Write the updated YAML data back to the file
        with open(self.yaml_file_path, 'w') as file:
            yaml.dump(yaml_data, file, default_flow_style=False)

        # self.get_logger().info(f"Updated {param_name} to {param_value} in {self.yaml_file_path}")

    # def timer_callback(self):
    #     self.random_position = np.random.normal(10.0,4.5)
    #     self.update_yaml_file(f'{self.get_namespace()}'+'/scheduler_node', 'position', self.random_position)
    def timer_callback(self):
        pass

def main(args=None):
    rclpy.init(args=args)
    node = pizza_memory_node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
