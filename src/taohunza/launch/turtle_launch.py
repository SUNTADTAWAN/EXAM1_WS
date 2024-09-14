from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess,DeclareLaunchArgument

def generate_launch_description():
    package_name = 'taohunza'
    namespace = ['nongtao1','Foxy','Noetic','Humble','Iron']
    field = ['field1/','field2/']
    return LaunchDescription([
        Node(
            package='turtlesim_plus',
            namespace='field1',
            executable='turtlesim_plus_node.py',
            name='turtlesim'
        ),
        ExecuteProcess(
            cmd = [[
                'ros2 service call /field1/remove_turtle turtlesim/srv/Kill "name: \'turtle1\'" ',
            ]],
            shell =True
        ),
        ExecuteProcess(
            cmd = [[
                'ros2 service call /field1/spawn_turtle turtlesim/srv/Spawn "{x: -5.0, y: -5.0, theta: 0.5, name: \''+namespace[0]+'\'}"',
            ]],
            shell =True
        ),
        Node(
            package='turtlesim_plus',
            namespace='field2',
            executable='turtlesim_plus_node.py',
            name='turtlesim'
        ),
        ExecuteProcess(
            cmd = [[
                'ros2 service call /field2/remove_turtle turtlesim/srv/Kill "name: \'turtle1\'" ',
            ]],
            shell =True
        ),
        ExecuteProcess(
            cmd = [[
                'ros2 service call /field2/spawn_turtle turtlesim/srv/Spawn "{x: -5.0, y: -5.0, theta: 0.5, name: \''+namespace[1]+'\'}"',
            ]],
            shell =True
        ),
        ExecuteProcess(
            cmd = [[
                'ros2 service call /field2/spawn_turtle turtlesim/srv/Spawn "{x: -5.0, y: -5.0, theta: 0.5, name: \''+namespace[2]+'\'}"',
            ]],
            shell =True
        ),
        ExecuteProcess(
            cmd = [[
                'ros2 service call /field2/spawn_turtle turtlesim/srv/Spawn "{x: -5.0, y: -5.0, theta: 0.5, name: \''+namespace[3]+'\'}"',
            ]],
            shell =True
        ),
        ExecuteProcess(
            cmd = [[
                'ros2 service call /field2/spawn_turtle turtlesim/srv/Spawn "{x: -5.0, y: -5.0, theta: 0.5, name: \''+namespace[4]+'\'}"',
            ]],
            shell =True
        ),
        Node(
            package=package_name,
            namespace= field[0]+namespace[0],
            executable='turtle_teleop_node.py',
            name='controller'
        ),
        Node(
            package=package_name,
            namespace= field[0]+namespace[0],
            executable='pizza_memory_node.py',
            name='pizza_memory'
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