from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='tp_safety',
            executable='estop_mux',
            name='estop_mux',
            parameters=[{'timeout_ms': 200}]
        ),
        Node(
            package='tp_cmd_sub',
            executable='cmd_sub',
            name='cmd_sub'
        ),
        # Optional later:
        # Node(package='rosbridge_server', executable='rosbridge_websocket', name='rosbridge'),
        # Node(package='image_transport', executable='republish',
        #      arguments=['raw', 'in:=/camera/image', 'compressed', 'out:=/camera/image/compressed'],
        #      name='img_compress'),
    ])
