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
from std_msgs.msg import Bool,Float64MultiArray,Int16
import numpy as np


class TeleopTurtleNode(Node):
    def __init__(self):
        super().__init__('turtle_teleop_node')
        # self.create_subscription(Twist,'cmd_vel',self.vel_callback,10)
        self.create_subscription(Pose,'pose',self.pose_callback,10)
        self.create_subscription(Bool,'spawn_pizza_sub',self.spawn_pizza_callback,10)
        self.create_subscription(Bool,'save_pizza',self.save_pizza_callback,10)
        self.create_subscription(Bool,'clear_pizza',self.clear_pizza_callback,10)
        self.create_subscription(Int16,'/finish_status',self.finish_callback,10)
        self.cmd_vel = self.create_publisher(Twist,'cmd_vel',10)
        self.send_pizza_positionX = self.create_publisher(Float64MultiArray,'pizza_posX',10)
        self.send_pizza_positionY = self.create_publisher(Float64MultiArray,'pizza_posY',10)
        self.send_state = self.create_publisher(Int16,'now_state',10)
        # self.piazz_server = self.create_service(Pizza,'pizza_action',self.pizza_callback)
        self.spawn_pizza_client = self.create_client(GivePosition,'/field1'+'/spawn_pizza')
        self.send_end = self.create_publisher(Bool,'/end_spawn',10)
        self.eat_pizza_client = self.create_client(Empty,'eat')
        self.spawn_turtle_client = self.create_client(Spawn,'/field2/spawn_turtle')
        self.extra_position = self.create_publisher(Float64MultiArray,'/last_position',10)
        self.eat_all = self.create_publisher(Bool,'/eat_all',10)

        self.namespace = ['Foxy','Noetic','Humble','Iron']
        self.robot_pose = np.array([0.0,0.0,0.0])
        self.target_x = 5.44
        self.target_y = 5.44
        self.eaten = 0
        self.spawn = False
        self.save = False
        self.clear = False
        self.pizza_amount = 100
        self.now_pizza = 0
        self.pizza_positionX = []
        self.pizza_positionY = []
        self.set_finish = []
        self.state = 0
        self.start_eat = 0 
        self.isfinish = []

        self.kp_linear = 0.0
        self.kp_angular = 0.0
        self.kp = 1.0
        self.kp_angular = 10.0
        self.set_param = np.array([0.8,20.0])

        self.declare_parameter('frequency', 10.0)
        self.declare_parameter('pizza amount', 50.0)
        self.declare_parameter('kp', 2.0)
        self.declare_parameter('kp_angular', 2.0)
        self.frequency = self.get_parameter('frequency').get_parameter_value().double_value
        self.pizza_amount = self.get_parameter('pizza amount').get_parameter_value().double_value
        self.kp = self.get_parameter('kp').get_parameter_value().double_value
        self.kp_a = self.get_parameter('kp_angular').get_parameter_value().double_value
        self.tim = 1.0/self.frequency
        self.create_timer(self.tim,self.timer_callback)

        self.get_logger().info(f'Starting {self.get_namespace()} / {self.get_name()} with thedefault parameter,  kp_linear:{self.kp_linear}, kp_angular:{self.kp_angular}')
    
    def finish_callback(self,msg):
        if str(msg.data) not in self.set_finish:
            self.set_finish.append(str(msg.data))


    def spawn_pizza_callback(self,msg):
        self.pizza_amount = self.get_parameter('pizza amount').get_parameter_value().double_value
        self.get_logger().info(f'State {msg}')
        if msg.data and self.now_pizza < self.pizza_amount:
            self.spawn_pizza(self.robot_pose[0],self.robot_pose[1])
            if self.state < 5:
                self.pizza_positionX.append(self.robot_pose[0])
                self.pizza_positionY.append(self.robot_pose[1])
                # self.get_logger().info(f'pos {self.pizza_positionX} {self.pizza_positionY}')
            else:
                self.get_logger().info(f'Pls Reset')    
            self.now_pizza += 1
            # self.get_logger().info(f'now pizza {self.now_pizza} robot pose {self.robot_pose}')
        else:
            pass
    def save_pizza_callback(self,msg):
        if msg.data and self.state < 4 and self.clear == False:
            positionX = Float64MultiArray()
            positionY = Float64MultiArray()
            now_state = Int16()
            positionX.data = self.pizza_positionX
            positionY.data = self.pizza_positionY
            self.send_pizza_positionX.publish(positionX)
            self.send_pizza_positionY.publish(positionY)
            self.pizza_positionX.clear()
            self.pizza_positionY.clear()
            # self.get_logger().info(f'aefterclear {self.pizza_positionY}')
            self.state += 1
            now_state.data = self.state
            self.send_state.publish(now_state)
            if self.state == 4:
                for i in range(len(self.namespace)):
                    self.send_start = self.create_publisher(Bool,'/field2/'+self.namespace[i]+'/start_spawn',10)
                    msg = Bool()
                    msg.data = True
                    self.send_start.publish(msg)

        else:
            # self.get_logger().info(f'Pls Reset') 
            pass
    def clear_pizza_callback(self,msg):
        if msg.data and len(self.pizza_positionX) != 0:
            self.start_eat = len(self.pizza_positionX)
            self.target_x = self.pizza_positionX[0]
            self.target_y = self.pizza_positionY[0]


    def eat_pizza(self):
        eat_request = Empty.Request()
        self.eat_pizza_client.call_async(eat_request)

    def  spawn_turtle(self):
        position_re = Spawn.Request()
        position_re.x = -5.0
        position_re.y = -5.0
        position_re.name = 'Melodic'
        self.spawn_turtle_client.call_async(position_re)


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
        # self.get_logger().info(f'ENDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD{len(self.isfinish)}') 
        self.kp = self.get_parameter('kp').get_parameter_value().double_value
        self.kp_a = self.get_parameter('kp_angular').get_parameter_value().double_value
        if len(self.set_finish) == 4:
            msg = Bool()
            msg.data = True
            self.send_end.publish(msg)
            self.set_finish.append(1.0)
            self.spawn_turtle()
            self.eat_all.publish(msg)
            msg2 = Float64MultiArray()
            msg2.data = [10.0,10.0]
            self.extra_position.publish(msg2)

        if self.start_eat > 0:
            self.clear = True
            self.kp = self.get_parameter('kp').get_parameter_value().double_value
            self.kp_a = self.get_parameter('kp_angular').get_parameter_value().double_value
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
                self.eat_pizza()
                self.eaten = 0
                vx = 0.0
                self.pizza_positionX.pop(0)
                self.pizza_positionY.pop(0)
                self.start_eat = len(self.pizza_positionX)
                self.now_pizza -= 1
                if self.start_eat > 0:
                    self.target_x = self.pizza_positionX[0]
                    self.target_y = self.pizza_positionY[0]
                else:
                    pass
                
                # self.get_logger().info(f'afterclear {self.pizza_positionY}')
            else:
                self.eaten = 1
                vx = (self.kp*distance)+0.8
            self.cmdvel(vx,wz)
        else:
            self.clear = False
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
    node = TeleopTurtleNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
