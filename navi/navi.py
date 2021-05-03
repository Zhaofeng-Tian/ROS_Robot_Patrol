#!/usr/bin/env python
import rospy
import actionlib
# move_base is the package that takes goals for navigation
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
# coordinates of the map are required. This was used turtlebot3_stage_4
# map from Turtlebot3. The first array is x,y,z location. The second one# is a "quaternion" defining an orientation. Quaternions are a different# mathematical represetnation for "euler angles", yaw, pitch and roll.
# Setting goal: Frame:map, Position(-1.091, -0.832, 0.000), Orientation(0.000, 0.000, 0.917, -0.399) = Angle: -2.320
# Setting goal: Frame:map, Position(-2.228, -0.762, 0.000), Orientation(0.000, 0.000, 0.935, 0.354) = Angle: 2.418
# Setting goal: Frame:map, Position(-5.057, 1.758, 0.000), Orientation(0.000, 0.000, 0.937, 0.349) = Angle: 2.428
# Setting goal: Frame:map, Position(-1.455, 1.854, 0.000), Orientation(0.000, 0.000, -0.327, 0.945) = Angle: -0.667
# Setting goal: Frame:map, Position(-2.564, -0.574, 0.000), Orientation(0.000, 0.000, 0.919, -0.393) = Angle: -2.333
# Setting goal: Frame:map, Position(-1.512, -1.349, 0.000), Orientation(0.000, 0.000, -0.323, 0.947) = Angle: -0.657
# Setting goal: Frame:map, Position(-0.216, -0.097, 0.000), Orientation(0.000, 0.000, 0.926, -0.378) = Angle: -2.365

waypoints = [ [(-5.260, 1.938, 0.000), (0.000, 0.000, 0.362, -0.932)], [(-3.723, 3.561, 0.000), (0.000, 0.000, 0.374, 0.928)], [(-1.247, 2.272, 0.000), (0.000, 0.000, -0.421, 0.907)]]
# Function to use MoveBaseGoal() from a two dimensional array
# containing a location and a rotation. 

def goal_pose(pose):
    goal_pose = MoveBaseGoal()
    goal_pose.target_pose.header.frame_id = 'map'
    goal_pose.target_pose.pose.position.x = pose[0][0]
    goal_pose.target_pose.pose.position.y = pose[0][1]
    goal_pose.target_pose.pose.position.z = pose[0][2]
    goal_pose.target_pose.pose.orientation.x = pose[1][0]
    goal_pose.target_pose.pose.orientation.y = pose[1][1]
    goal_pose.target_pose.pose.orientation.z = pose[1][2]
    goal_pose.target_pose.pose.orientation.w = pose[1][3]

    return goal_pose

# Main program starts here

if __name__ == '__main__':
    # A node called 'patrol' which is an action client to move_base
    rospy.init_node('patrol')
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    # wait for action server to be ready
    client.wait_for_server()
    # Loop until ^c
    while not rospy.is_shutdown():
        # repeat the waypoints over and over again
        for pose in waypoints:
            goal = goal_pose(pose)
            print("Going for goal: ", goal)
            client.send_goal(goal)
            client.wait_for_result()
