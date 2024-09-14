import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/aitthikit/Documents/GitHub/EXAM1_WS/install/teleop_twist_keyboard'
