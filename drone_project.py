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
        
        self.gt_pose_sub = self.create_subscription(Pose, '/drone/gt_pose',
            self.pose_callback, 1)

        self.gt_pose = None
        self.current_point_index = 0
        self.next_point_index = 1

        self.command_pub = self.create_publisher(Twist, '/drone/cmd_vel', 10)

        timer_period = 1
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.points = [(0.0, 2.0), (0.0, 12.0), (0.0, 7.0), (5.0, 7.0), (5.0, 12.0), (5.0, 2.0), (5.0, 7.0), (0.0, 2.0)] # Punkty do wykonania litery H

    def pose_callback(self, data):
        self.gt_pose = data
        print(f"{data}")

    def timer_callback(self):
        msg = Twist()
        msg.linear.z = 2.0
        self.command_pub.publish(msg)
        
        if self.gt_pose is not None:
            x = self.gt_pose.position.x
            y = self.gt_pose.position.y
            
        current_point = self.points[self.current_point_index]
        next_point = self.points[self.next_point_index]

        X = abs(x - next_point[0])
        Y = abs(y - next_point[1])

        if X < 1 and Y < 1:
                self.current_point_index = self.next_point_index
                self.next_point_index = (self.current_point_index + 1) % len(self.points)
      

            
def main(args=None):
    rclpy.init(args=args)

    node = DroneController()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if _name_ == '_main_':
    main()
