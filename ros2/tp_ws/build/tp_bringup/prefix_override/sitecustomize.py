import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/yiyo/Telepresence/Telepresence-Stack/ros2/tp_ws/install/tp_bringup'
