import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='joy',
            executable='joy_node',
            name='joystick'),

        launch_ros.actions.Node(
            package='my_teleop_joy',
            executable='my_teleop_joy_node',
            remappings=[("/cmd_vel", "turtle1/cmd_vel")],
            name='teleop'),

        launch_ros.actions.Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtle'),
    ])
