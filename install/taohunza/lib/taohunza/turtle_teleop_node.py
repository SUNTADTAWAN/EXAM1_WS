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
from std_msgs.msg import Bool
import numpy as np


class TeleopTurtleNode(Node):
    def __init__(self):
        super().__init__('turtle_teleop_node')
        self.create_subscription(Twist,'cmd_vel',self.vel_callback,10)
        self.create_subscription(Pose,'pose',self.pose_callback,10)
        self.create_subscription(Bool,'spawn_pizza_sub',self.spawn_pizza_callback,10)
        self.create_subscription(Bool,'save_pizza',self.save_pizza_callback,10)
        self.create_subscription(Bool,'clear_pizza',self.clear_pizza_callback,10)
        # self.piazz_server = self.create_service(Pizza,'pizza_action',self.pizza_callback)
        self.spawn_pizza_client = self.create_client(GivePosition,'/spawn_pizza')
        self.eat_pizza_client = self.create_client(Empty,'eat')
        self.robot_pose = np.array([0.0,0.0,0.0])
        self.target_x = 5.44
        self.target_y = 5.44
        self.eaten = 0
        self.spawn = False
        self.save = False
        self.clear = False
        self.pizza_amount = 100
        self.now_pizza = 0

        self.kp_linear = 0.0
        self.kp_angular = 0.0
        self.kp = 0.8
        self.kp_a = 20.0
        self.set_param = np.array([0.8,20.0])

        self.declare_parameter('frequency', 10.0)
        self.declare_parameter('pizza amount', 50.0)
        self.frequency = self.get_parameter('frequency').get_parameter_value().double_value
        self.pizza_amount = self.get_parameter('pizza amount').get_parameter_value().double_value
        self.tim = 1.0/self.frequency
        self.create_timer(self.tim,self.timer_callback)

        self.get_logger().info(f'Starting {self.get_namespace()} / {self.get_name()} with thedefault parameter,  kp_linear:{self.kp_linear}, kp_angular:{self.kp_angular}')
    
    def spawn_pizza_callback(self,msg):
        self.pizza_amount = self.get_parameter('pizza amount').get_parameter_value().double_value
        self.get_logger().info(f'State {msg}')
        if msg.data and self.now_pizza < self.pizza_amount:
            self.spawn_pizza(self.robot_pose[0],self.robot_pose[1])
            self.now_pizza += 1
            self.get_logger().info(f'now pizza {self.now_pizza} robot pose {self.robot_pose}')
        else:
            pass
    def save_pizza_callback(self,msg):
        pass
    def clear_pizza_callback(self,msg):
        pass

    # def pizza_callback(self, request:Pizza , response:Pizza):
    #     self.spawn = request.Request.pizza_spawn
    #     self.save = request.Request.pizza_save
    #     self.clear = request.Request.pizza_clear

    def vel_callback(self,msg):
        pass
    # def cpizza_pose_callback(self,msg):
    #     self.cpizza_pose[0] = msg.x
    #     self.cpizza_pose[1] = msg.y
    #     self.spawn_pizza(self.cpizza_pose[0],self.cpizza_pose[1])
    #     # print(msg)
    #     print(self.cpizza_pose)


    def eat_pizza(self):
        eat_request = Empty.Request()
        self.eat_pizza_client.call_async(eat_request)

    def  spawn_turtle(self):
        position_re = Spawn.Request()
        position_re.x = 0.5
        position_re.y = 0.5
        self.spawn_turtle2_client.call_async(position_re)


    def  spawn_pizza(self,x,y):
        position_request = GivePosition.Request()
        position_request.x = x
        position_request.y = y
        self.get_logger().info(f'x {x} y {y}')
        self.spawn_pizza_client.call_async(position_request)

        
    # def cmdvel(self,v,w):
    #     msg =  Twist()
    #     msg.linear.x = v
    #     msg.angular.z = w
    #     self.cmd_vel_pub.publish(msg)
        

    def pose_callback(self,msg):
        self.robot_pose[0] = msg.x
        self.robot_pose[1] = msg.y
        self.robot_pose[2] = msg.theta

    def timer_callback(self):
        now_x = self.robot_pose[0]
        now_y = self.robot_pose[1]
        diff_x = self.target_x - now_x 
        diff_y = self.target_y - now_y 
        distance = np.sqrt((diff_x**2)+(diff_y**2))
        diff_theta = np.arctan(diff_y/diff_x) - self.robot_pose[2]
        # use_theta = np.arctan2(np.sin(diff_theta),np.cos(diff_theta))
        use_theta = np.arctan2(diff_y,diff_x)  - self.robot_pose[2]
        # print(self.robot_pose)
        # print(self.mouse_pose)
        # print(diff_x)
        # print(diff_y)
        # print(np.arctan(diff_y/diff_x))
        # print(diff_theta)
        # print(distance)
        # print(use_theta)
        # vx = 0.2*distance
        # vx = 0.8*distance
        # wz = 20*use_theta
        wz = self.kp_a*use_theta
        # if(diff_x < 0):
        #     wz = -2*use_theta
        # else:
        #     wz = 2*use_theta
        # wz = 0.2*diff_theta
        # if(distance < 1):
        #     self.eat_pizza()
        #     self.eaten = 0
        #     vx = 0.0
        # else:
        #     self.eaten = 1
        #     vx = self.kp*distance
        # self.cmdvel(vx,wz)

def main(args=None):
    rclpy.init(args=args)
    node = TeleopTurtleNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
