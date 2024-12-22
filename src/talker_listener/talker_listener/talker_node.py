import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class TalkerNode(Node):

    def __init__(self):
        super().__init__("talker_node")
        self.publisher = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5
        self.create_timer(timer_period, self.timer_callback)
        self.count = 0


    def timer_callback(self):
        msg = String()
        msg.data = f"Ciao a tutti {self.count}"
        self.publisher.publish(msg)
        self.count += 1
        self.get_logger().info(f"Sto pubblicando {msg.data}")


def main(args=None):
    rclpy.init(args=args)

    # crea il nodo
    talkerNode = TalkerNode()

    # usa/spin il nodo
    rclpy.spin(talkerNode)

    #  distrugge il nodo
    talkerNode.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()