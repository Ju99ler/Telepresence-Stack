import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool

class EstopMux(Node):
    def __init__(self):
        super().__init__('estop_mux')
        self.declare_parameter('timeout_ms', 200)
        self.timeout = self.get_parameter('timeout_ms').value / 1000.0
        self.e_stop = False
        self.last_msg_time = self.get_clock().now()

        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.sub_cmd = self.create_subscription(Twist, '/cmd_vel_raw', self.on_cmd, 10)
        self.sub_estop = self.create_subscription(Bool, '/e_stop', self.on_estop, 10)

        self.timer = self.create_timer(0.02, self.tick)  # 50 Hz

    def on_cmd(self, msg: Twist):
        self.last_msg_time = self.get_clock().now()
        if not self.e_stop:
            self.pub.publish(msg)

    def on_estop(self, msg: Bool):
        self.e_stop = msg.data
        if self.e_stop:
            self.pub.publish(Twist())  # immediate stop

    def tick(self):
        # if silent too long, enforce zero
        if (self.get_clock().now() - self.last_msg_time).nanoseconds/1e9 > self.timeout:
            self.pub.publish(Twist())

def main():
    rclpy.init()
    rclpy.spin(EstopMux())
    rclpy.shutdown()
