import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node



def generate_launch_description():

    package_name='autonom_rover'
    #Get Robot State Publisher from rsp.launch file
    #launch robot state publisher from its launch file
    rsp = IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(
                get_package_share_directory(package_name), 'launch', 'rsp.launch.py'
            )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    #Launch Gazebo
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')])
        )

     #Load robot into Gazebo World
    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                    arguments=['-topic', 'robot_description',
                                '-entity', 'my_bot'],
                    output='screen')
    #Start Differential Drive Controller
    diff_drive_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["diff_cont"],
    )
    #Start Differential Drive State Broadcaster
    joint_broad_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_broad"],
    )


    # Run the Nodes and Related Scripts
    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity,
        # diff_drive_spawner,   ##Manual Control Done Without Ros2 Control
        # joint_broad_spawner   ##Manual Control Done Without Ros2 Control
    ])