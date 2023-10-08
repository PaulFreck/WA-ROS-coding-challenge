import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32MultiArray

class MinimalSubscriber(Node):
    array1 = None
    array2 = None
    def __init__(self):
        super().__init__('merge_arrays')
        self.publisher_ = self.create_publisher(Int32MultiArray, '/output/array', 10)
        self.subscription = self.create_subscription(Int32MultiArray, '/input/array1', self.array_one_listener_callback, 10)
        self.subscription = self.create_subscription(Int32MultiArray, '/input/array2', self.array_two_listener_callback, 10)
        self.subscription #here to prevent unused var warning

    def array_one_listener_callback(self, msg):
        i = 0
        j = 0
        self.array1 = msg.data
        self.get_logger().info('hearing: "%s"' % self.array1)
        if (self.array2 is not None and self.array1 is not None):
            outputArray = [None] * (len(self.array2)+len(self.array1))
            while(i < len(self.array1) and j < len(self.array2)):
                if(self.array1[i] < self.array2[j]):
                    outputArray[i+j] = self.array1[i]
                    i += 1
                else:
                    outputArray[i+j] = self.array2[j]
                    j += 1
            if (i == len(self.array1)):
                for k in range(j, len(self.array2)):
                    outputArray[i+k] = self.array2[k]
            if (j == len(self.array2)):
                for l in range(i, len(self.array1)):
                    outputArray[j+l] = self.array1[l]
            msg = Int32MultiArray()
            msg.data = outputArray
            self.publisher_.publish(msg)
            self.get_logger().info('Publishing: "%s"' % outputArray)
            
        
    def array_two_listener_callback(self, msg):
        i = 0
        j = 0
        self.array2 = msg.data
        self.get_logger().info('hearing: "%s"' % self.array2)
        if (self.array2 is not None and self.array1 is not None):
            outputArray = [None] * (len(self.array2)+len(self.array1))
            while(i < len(self.array1) and j < len(self.array2)):
                if(self.array1[i] < self.array2[j]):
                    outputArray[i+j] = self.array1[i]
                    i += 1
                else:
                    outputArray[i+j] = self.array2[j]
                    j += 1
            if (i == len(self.array1)):
                for k in range(j, len(self.array2)):
                    outputArray[i+k] = self.array2[k]
            if (j == len(self.array2)):
                for l in range(i, len(self.array1)):
                    outputArray[j+l] = self.array1[l]
            msg = Int32MultiArray()
            msg.data = outputArray
            self.publisher_.publish(msg)
            self.get_logger().info('Publishing: "%s"' % outputArray)
        

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
