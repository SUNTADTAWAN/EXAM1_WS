import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/tadtawan/EXAM1_WS/install/teleop_keyboard'
