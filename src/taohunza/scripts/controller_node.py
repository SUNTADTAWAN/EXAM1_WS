#!/usr/bin/python3

from taohunza.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node


class controller_node(Node):
    def __init__(self):
        super().__init__('controller_node')

def main(args=None):
    rclpy.init(args=args)
    node = controller_node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
