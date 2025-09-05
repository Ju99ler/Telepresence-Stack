#include <chrono>
#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"

using namespace std::chrono_literals;

class CmdSub : public rclcpp::Node {
public:
  CmdSub() : Node("tp_cmd_sub") {
    auto qos = rclcpp::QoS(rclcpp::KeepLast(10))
      .reliability(RMW_QOS_POLICY_RELIABILITY_BEST_EFFORT)
      .durability(RMW_QOS_POLICY_DURABILITY_VOLATILE);
    sub_ = create_subscription<geometry_msgs::msg::Twist>(
      "/cmd_vel", qos, [this](geometry_msgs::msg::Twist::SharedPtr msg){
        last_msg_time_ = now();
        // TODO: send to motor driver. For now, log:
        RCLCPP_INFO_THROTTLE(get_logger(), *get_clock(), 1000,
                             "vx=%.2f wz=%.2f", msg->linear.x, msg->angular.z);
      });
    timer_ = create_wall_timer(100ms, [this](){
      // Hook: if you need periodic checks, put here.
    });
  }
private:
  rclcpp::Time last_msg_time_;
  rclcpp::Subscription<geometry_msgs::msg::Twist>::SharedPtr sub_;
  rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char** argv){
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<CmdSub>());
  rclcpp::shutdown();
  return 0;
}
