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
from std_msgs.msg import Bool,Float64MultiArray,Int16,Int16MultiArray
import numpy as np
import yaml


class CopyTurtleNode(Node):
    def __init__(self):
        super().__init__('copy_turtle_node')
        self.declare_parameter('pizza_positionX',[0.0,0.0])
        self.declare_parameter('pizza_positionY',[0.0,0.0])
        self.cmd_vel = self.create_publisher(Twist,'cmd_vel',10)
        self.spawn_pizza_client = self.create_client(GivePosition,'/field2'+'/spawn_pizza')
        # self.end_spawn_client = self.create_client(Pizza,'/field1'+'/finish_status')
        self.create_subscription(Pose,'pose',self.pose_callback,10)
        self.create_subscription(Bool,'start_spawn',self.spawn_pizza_callback,10)
        self.create_subscription(Bool,'/end_spawn',self.end_pizza_callback,10)
        self.finish_status = self.create_publisher(Int16,'/finish_status',10)
        self.yaml_file_path = 'src/taohunza/config/pizza_memory.yaml'
        
        self.robot_pose = np.array([0.0,0.0,0.0])
        self.target_x = 5.44
        self.target_y = 5.44
        self.positionX = []
        self.positionY = []
        # self.pizza_position3 = []
        # self.pizza_position4 = []
        self.state = 0
        self.start_spawn = 0 

        self.kp_linear = 0.0
        self.kp_angular = 0.0
        self.kp = 1
        self.kp_a = 10
        self.set_param = np.array([0.8,20.0])
        self.frequency = 100.0

        self.declare_parameter('frequency', 10.0)
        # self.declare_parameter('pizza amount', 50.0)
        # self.frequency = self.get_parameter('frequency').get_parameter_value().double_value
        # self.pizza_amount = self.get_parameter('pizza amount').get_parameter_value().double_value
        self.tim = 1.0/self.frequency
        self.create_timer(self.tim,self.timer_callback)

        # self.get_logger().info(f'Starting {self.get_namespace()} / {self.get_name()} with thedefault parameter,  kp_linear:{self.kp_linear}, kp_angular:{self.kp_angular}')
    def end_pizza_callback(self,msg):
        if msg.data:
            self.positionX = [10.0]
            self.positionY = [10.0]
            self.target_x = self.positionX[0]
            self.target_y = self.positionY[0]
    def spawn_pizza_callback(self,msg):    
        # self.positionX = self.get_parameter('pizza_positionX').value
        # self.positionY = self.get_parameter('pizza_positionY').value
        # self.target_x = self.positionX[0]
        # self.target_y = self.positionY[0]
        # self.declare_parameter('pizza_positionX')
        # # self.declare_parameter('pizza_positionY')
        # self.update_yaml_file(f'copy_node', 'pizza_positionX', )
        with open(self.yaml_file_path, 'r') as file:
            yaml_data = yaml.safe_load(file)
        valueX = yaml_data[self.get_namespace()+'/copy_node']['ros__parameters']['pizza_positionX']
        valueY = yaml_data[self.get_namespace()+'/copy_node']['ros__parameters']['pizza_positionY']
        self.positionX = self.get_parameter('pizza_positionX').value
        self.positionY = self.get_parameter('pizza_positionY').value
        self.get_logger().info(f'getX {valueX} getY {valueY}')
        self.get_logger().info(f'selfX {self.positionX} selfY {self.positionX}')
        # self.get_logger().info(f'Namespace: {self.get_namespace()[8]}')
        if msg.data and len(self.positionX) != 0:
            self.target_x = self.positionX[0]
            self.target_y = self.positionY[0]
        
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
        with open(self.yaml_file_path_new, 'w') as file:
            yaml.dump(yaml_data, file, default_flow_style=False)

        self.get_logger().info(f"Updated {param_name} to {param_value} in {self.yaml_file_path}")

        # if msg.data and self.now_pizza < self.pizza_amount:
        #     self.spawn_pizza(self.robot_pose[0],self.robot_pose[1])
        #     if self.state < 4:
        #         self.pizza_positionX.append(self.robot_pose[0])
        #         self.pizza_positionY.append(self.robot_pose[1])
        #         self.get_logger().info(f'pos {self.pizza_positionX} {self.pizza_positionY}')
        #     else:
        #         self.get_logger().info(f'Pls Reset')    
        #     self.now_pizza += 1
        #     self.get_logger().info(f'now pizza {self.now_pizza} robot pose {self.robot_pose}')
        # else:
        #     pass

    # def clear_pizza_callback(self,msg):
    #     if msg.data and len(self.pizza_positionX) != 0:
    #         self.start_eat = len(self.pizza_positionX)
    #         self.target_x = self.pizza_positionX[0]
    #         self.target_y = self.pizza_positionY[0]
        # self.clear = msg.data
        # pass

    # def pizza_callback(self, request:Pizza , response:Pizza):
    #     self.spawn = request.Request.pizza_spawn
    #     self.save = request.Request.pizza_save
    #     self.clear = request.Request.pizza_clear


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
        self.start_spawn = len(self.positionX)
        # self.declare_parameter('pizza_positionX')
        # self.declare_parameter('pizza_positionY')
        # self.pizza_positionX = self.get_parameter('pizza_positionX').value
        # self.pizza_positionY = self.get_parameter('pizza_positionY').value
        # self.get_logger().info(f'getX {self.pizza_positionX} getY {self.pizza_positionY}')
        # if self.clear:
        #     self.start_eat = len(self.pizza_positionX)
        if self.start_spawn > 0:
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
                self.spawn_pizza(self.positionX[0],self.positionY[0])
                self.eaten = 0
                vx = 0.0
                self.positionX.pop(0)
                self.positionY.pop(0)
                self.start_spawn = len(self.positionX)
                if self.start_spawn > 0:
                    self.target_x = self.positionX[0]
                    self.target_y = self.positionY[0]
                else:
                    msg = Int16()
                    # msg = Pizza.Request()
                    if self.get_namespace()[8] == 'F':
                        msg.data = 1
                        # self.end_spawn_client.call_async(msg)
                    elif self.get_namespace()[8] == 'N':
                        msg.data = 2
                        # self.end_spawn_client.call_async(msg)
                    elif self.get_namespace()[8] == 'H':
                        msg.data = 3
                        # self.end_spawn_client.call_async(msg)
                    elif self.get_namespace()[8] == 'I':
                        msg.data = 4
                        # self.end_spawn_client.call_async(msg)
                    self.finish_status.publish(msg)
                
                # self.get_logger().info(f'afterclear {self.positionY}')
            else:
                self.eaten = 1
                vx = (self.kp*distance)+0.6
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
