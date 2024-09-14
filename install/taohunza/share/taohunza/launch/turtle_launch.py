from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    package_name = 'taohunza'
    namespace = ['turtle1','turtle2']
    return LaunchDescription([
        Node(
            package='turtlesim_plus',
            namespace='',
            executable='turtlesim_plus_node.py',
            name='turtlesim'
        ),
        Node(
            package=package_name,
            namespace= namespace[0],
            executable='turtle_teleop_node.py',
            name='controller'
        ),
        Node(
            package=package_name,
            namespace= namespace[0],
            executable='pizza_memory_node.py',
            name='controller'
        ),
        # Node(
        #     package='turtlesim',
        #     executable='mimic',
        #     name='mimic',
        #     remappings=[
        #         ('/input/pose', '/turtlesim1/turtle1/pose'),
        #         ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel'),
        #     ]
        # )
    ])  