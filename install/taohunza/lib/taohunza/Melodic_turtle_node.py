#!/usr/bin/python3

from taohunza.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim_plus_interfaces.srv import GivePosition
from turtlesim.srv import Spawn
from std_srvs.srv import Empty
from turtle_interfaces.srv import Pizza
from std_msgs.msg import Float64MultiArray,Int16,Bool
import numpy as np
import yaml


class CopyTurtleNode(Node):
    def __init__(self):
        super().__init__('copy_turtle_node')
        self.declare_parameter('pizza_positionX',[0.0,0.0])
        self.declare_parameter('pizza_positionY',[0.0,0.0])
        self.cmd_vel = self.create_publisher(Twist,'cmd_vel',10)
        self.create_subscription(Pose,'pose',self.pose_callback,10)
        self.eat_pizza_client = self.create_client(Empty,'eat')
        self.create_subscription(Float64MultiArray,'/last_position',self.finish_callback,10)
        self.create_subscription(Bool,'/eat_all',self.eat_all_callback,10)
        
        self.robot_pose = np.array([0.0,0.0,0.0])
        self.target_x = 5.44
        self.target_y = 5.44
        self.positionX = []
        self.positionY = []
        self.state = 0
        self.start_eat = 0 

        self.kp_linear = 0.0
        self.kp_angular = 0.0
        self.kp = 0.8
        self.kp_a = 10.0
        self.set_param = np.array([0.8,20.0])
        self.frequency = 100.0

        self.declare_parameter('frequency', 10.0)
        self.tim = 1.0/self.frequency
        self.create_timer(self.tim,self.timer_callback)

        # self.get_logger().info(f'Starting {self.get_namespace()} / {self.get_name()} with thedefault parameter,  kp_linear:{self.kp_linear}, kp_angular:{self.kp_angular}')
    def finish_callback(self,msg:Float64MultiArray):
        self.positionX.append(msg.data[0])
        self.positionY.append(msg.data[1])
        self.start_eat = len(self.positionX)
    def eat_all_callback(self,msg):
        self.positionX = self.get_parameter('pizza_positionX').value
        self.positionY = self.get_parameter('pizza_positionY').value
        if msg.data and len(self.positionX) != 0:
            self.target_x = self.positionX[0]
            self.target_y = self.positionY[0]

    def eat_pizza(self):
        eat_request = Empty.Request()
        self.eat_pizza_client.call_async(eat_request)

    def  spawn_turtle(self):
        position_re = Spawn.Request()
        position_re.x = 0.5
        position_re.y = 0.5
        self.spawn_turtle2_client.call_async(position_re)
        
    def cmdvel(self,v,w):
        msg =  Twist()
        msg.linear.x = v
        msg.angular.z = w
        self.cmd_vel.publish(msg)
        
    def pose_callback(self,msg):
        self.robot_pose[0] = msg.x
        self.robot_pose[1] = msg.y
        self.robot_pose[2] = msg.theta

    def timer_callback(self):
        if self.start_eat > 0:
            self.eat_pizza()
            now_x = self.robot_pose[0]
            now_y = self.robot_pose[1]
            diff_x = self.target_x - now_x 
            diff_y = self.target_y - now_y 
            distance = np.sqrt((diff_x**2)+(diff_y**2))
            diff_theta = np.arctan(diff_y/diff_x) - self.robot_pose[2]
            # use_theta = np.arctan2(np.sin(diff_theta),np.cos(diff_theta))
            use_theta = np.arctan2(diff_y,diff_x)  - self.robot_pose[2]
            use_theta = np.arctan2(np.sin(use_theta), np.cos(use_theta))
            wz = self.kp_a*use_theta
            if(distance < 0.1):
                self.eaten = 0
                vx = 0.0
                self.positionX.pop(0)
                self.positionY.pop(0)
                self.start_eat = len(self.positionX)
                if self.start_eat > 0:
                    self.target_x = self.positionX[0]
                    self.target_y = self.positionY[0]
                else:
                    pass
                
                # self.get_logger().info(f'afterclear {self.positionY}')
            else:
                self.eaten = 1
                vx = (self.kp*distance)+0.8
            self.cmdvel(vx,wz)
        else:
            pass
        # vx = 0.2*distance
        # vx = 0.8*distance
        # wz = 20*use_theta
        
        # if(diff_x < 0):
        #     wz = -2*use_theta
        # else:
        #     wz = 2*use_theta
        # wz = 0.2*diff_theta
        # if(distance < 0.5):
        #     self.eat_pizza()
        #     self.eaten = 0
        #     vx = 0.0
        # else:
        #     self.eaten = 1
        #     vx = self.kp*distance
        # self.cmdvel(vx,wz)

def main(args=None):
    rclpy.init(args=args)
    node = CopyTurtleNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
