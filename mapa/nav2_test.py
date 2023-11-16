#! /usr/bin/env python3
import rclpy
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped
from tf_transformations import quaternion_from_euler
from math import pi
import time

def create_pose_stamped(navigator, pos_x, pos_y, rot_z):
    q_x, q_y, q_z, q_w = tf_transformations.quaternion_from_euler(0.0, 0.0, rot_z)
    pose = PoseStamped()
    pose.header.frame_id = 'map'
    pose.header.stamp = nav.get_clock().now().to_msg()
    pose.pose.position.x = pos_x
    pose.pose.position.y = pos_y
    pose.pose.position.z = pos_x
    pose.pose.orientation.x = q_x
    pose.pose.orientation.y = q_y
    pose.pose.orientation.z = q_z
    pose.pose.orientation.w = q_w
    return pose

def main():
    rclpy.init()
    global nav
    nav = BasicNavigator()

    # Envia a pose inicial apenas na primeira execução
    initial_pose_sent = False

    while True:
        if not initial_pose_sent:
            q_x, q_y, q_z, q_w = quaternion_from_euler(0.0, 0.0, 0.0)
            initial_pose = PoseStamped()
            initial_pose.header.frame_id = 'map'
            initial_pose.header.stamp = nav.get_clock().now().to_msg()
            initial_pose.pose.position.x = 0.0
            initial_pose.pose.position.y = 0.0
            initial_pose.pose.position.z = 0.0
            initial_pose.pose.orientation.x = q_x
            initial_pose.pose.orientation.y = q_y
            initial_pose.pose.orientation.z = q_z
            initial_pose.pose.orientation.w = q_w

            nav.setInitialPose(initial_pose)
            nav.waitUntilNav2Active()
            initial_pose_sent = True

        # Defina pontos de destino dinamicamente
        goal_pose = create_pose_stamped(nav, 1.0, 0.0, pi/2)
        obstacle_avoidance_goal_pose = create_pose_stamped(nav, 1.5, 0.0, pi/2)

        # Envia o ponto de destino com desvio de obstáculos
        nav.goToPoseWithDynamicObstacleAvoidance(goal_pose, obstacle_avoidance_goal_pose)
        
        while not nav.isTaskComplete():
            print(nav.getFeedback())
            time.sleep(1)  # Adiciona um pequeno atraso para evitar loop muito rápido

    rclpy.shutdown()

if __name__ == '__main__':
    main()
