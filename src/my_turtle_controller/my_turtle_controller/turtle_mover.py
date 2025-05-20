#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class TurtleMover(Node):
    def __init__(self):
        super().__init__('turtle_mover')

        # Паблишер в топик /turtle1/cmd_vel с типом Twist
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        # Таймер (0,5 с)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.move_turtle)

        # Готовое сообщение Twist
        self.twist_msg = Twist()
        self.twist_msg.linear.x = 2.0   # линейная скорость
        self.twist_msg.angular.z = 1.0  # угловая скорость

    def move_turtle(self):
        # Публикуем сообщение
        self.publisher_.publish(self.twist_msg)
        self.get_logger().info(
            f'Publishing turtle velocity: linear={self.twist_msg.linear.x}, '
            f'angular={self.twist_msg.angular.z}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = TurtleMover()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
