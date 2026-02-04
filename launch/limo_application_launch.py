import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='limo_application',
            executable='limo_stop',
            name='limo_stop'),

        launch_ros.actions.Node(
            package='limo_appcliation',
            executable='limo_control',
            name='limo_control'),

        launch_ros.actions.Node(
            package='limo_application',
            executable='detect_line',
            name='detect_line'),
    ])