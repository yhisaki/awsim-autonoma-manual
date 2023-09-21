import rclpy
from autonoma_msgs.msg import VehicleInputs
from rclpy.node import Node
from sensor_msgs.msg import Joy


class AutonomaManualNode(Node):
    def __init__(self):
        super().__init__("awsim_autonoma_manual")
        self.publisher_ = self.create_publisher(VehicleInputs, "vehicle_inputs", 10)
        self.joy_subscriber_ = self.create_subscription(
            Joy, "joy", self.joy_callback, 10
        )

    def joy_callback(self, msg: Joy):
        self.get_logger().info(f"Axis 0: {msg.axes[0]}, Axis 1: {msg.axes[1]}")
        # steering_left = (1 - msg.axes[2]) / 2
        # steering_right = (1 - msg.axes[5]) / 2
        # # self.get_logger().info(f"Steering Left: {steering_left}")
        # # self.get_logger().info(f"Steering Right: {steering_right}")
        # steering = steering_left - steering_right
        # # self.get_logger().info(f"Steering: {steering}")
        vehicle_inputs = VehicleInputs()
        # if msg.axes[1] >= 0:
        #     vehicle_inputs.throttle_cmd = msg.axes[1] * 50.0
        # else:
        #     vehicle_inputs.brake_cmd = - msg.axes[1] * 5000.0
        vehicle_inputs.throttle_cmd = msg.buttons[1] * 20.0
        if msg.buttons[0] == 1:
            vehicle_inputs.brake_cmd = 1000.0
        vehicle_inputs.steering_cmd = msg.axes[0] * 100.0


        self.publisher_.publish(vehicle_inputs)


def main():
    rclpy.init()
    node = AutonomaManualNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
