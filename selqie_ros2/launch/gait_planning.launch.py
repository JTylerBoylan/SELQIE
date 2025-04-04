from launch import LaunchDescription
from launch_ros.actions import Node

from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
def UseSimTime():
    launch_arg = DeclareLaunchArgument(
        'use_sim_time', default_value='false', description='Use simulation clock'
    )
    use_sim_time = LaunchConfiguration('use_sim_time')
    return launch_arg, use_sim_time

import os
from ament_index_python.packages import get_package_share_directory
PACKAGE_NAME = 'selqie_ros2'
CONFIG_FOLDER = os.path.join(get_package_share_directory(PACKAGE_NAME), 'config')
    
def GaitPlanningNode(use_sim_time : str):
    return Node(
        package='gait_planning',
        executable='gait_planning_node',
        name='gait_planning_node',
        parameters=[os.path.join(CONFIG_FOLDER, 'gait_planning_config.yaml'),
                    {'use_sim_time': use_sim_time}],
        # prefix=['xterm -e gdb -ex run --args']
    )

def generate_launch_description():
    launch_args, use_sim_time = UseSimTime()
    return LaunchDescription([
        launch_args,
        GaitPlanningNode(use_sim_time)
    ])