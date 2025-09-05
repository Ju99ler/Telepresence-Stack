source /opt/ros/humble/setup.bash
cd "$(dirname "$BASH_SOURCE")/tp_ws"
colcon build --symlink-install
source install/setup.bash
