from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.actions import Node
from launch.actions import ExecuteProcess, IncludeLaunchDescription, TimerAction
from launch.substitutions import LaunchConfiguration
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.conditions import IfCondition

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=['ros2', 'launch', 'turtlebot3_gazebo', 'turtlebot3_world.launch.py'],
            output='screen',
        ),
        ExecuteProcess(
            cmd=['ros2', 'launch', 'turtlebot3_navigation2', 'navigation2.launch.py', 'use_sim_time:=True', 'map:=../meu_pacote/alysson-mapa.yaml'],
            output='screen',
        ),
        TimerAction(
            period=5.0,
            actions=[
                Node(
                    package='meu_pacote',
                    executable='inicio_pode',
                    name='incio_pose',
                    output='screen'
                ),
            ],
        ),
        TimerAction(
            period=10.0,
            actions=[
                Node(
                    package='meu_pacote',
                    executable='nav2_test',
                    name='nav2_test',
                    prefix='gnome-terminal --',
                    output='screen'
                ),
            ],
        ),
    ])

if __name__ == '__main__':
    generate_launch_description()