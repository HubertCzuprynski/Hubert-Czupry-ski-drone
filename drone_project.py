import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Pose

"""
Wybrany znak: H
Petla: tak
Plaszczyzna: x, y
"""

class DroneController(Node):
    def __init__(self):
        super().__init__('drone_controller')
        
        self.gt_pose_sub = self.create_subscription( Pose, '/drone/gt_pose',
            self.pose_callback, 1)

        self.gt_pose = None

        self.command_pub = self.create_publisher(Twist, '/drone/cmd_vel', 10)

        timer_period = 1
        self.timer = self.create_timer(timer_period, self.timer_callback)


    def pose_callback(self, data):
        self.gt_pose = data
        print(f"{data}")

    
    def timer_callback(self):
        msg = Twist()
        msg.linear.z = 2.0
        self.command_pub.publish(msg)

    #Punkty do wykonania litery H
points = [(0.0, 2.0), (0.0, 12.0), (0.0, 7.0), (5.0, 7.0), (5.0, 12.0), (5.0, 2.0), (5.0, 7.0), (0.0, 2.0)]

    
    if True:
        x = self.gt_pose.position.x
        y = self.gt_pose.position.y
        self.x, self.y = points[self.next_point_index]

        X = abs(x - points[next_point_index][0])
        Y = abs(y - points[next_point_index][1])

    if X < 1 and Y < 1:
        current_point_index = next_point_index
        next_point_index = (current_point_index + 1) % len(points)

    self.command_pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    node = DroneController()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '_main_':
    main()
