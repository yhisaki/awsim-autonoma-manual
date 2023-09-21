from launch import LaunchDescription

from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package="joy",
                executable="joy_node",
                name="joy_node",
                output="screen",
            ),
            Node(
                package="awsim_autonoma_manual",
                executable="awsim_autonoma_manual",
                name="awsim_autonoma_manual",
                output="screen",
            ),
        ]
    )
