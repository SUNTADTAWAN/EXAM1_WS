# generated from rosidl_generator_py/resource/_idl.py.em
# with input from turtle_interfaces:srv/Pizza.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Pizza_Request(type):
    """Metaclass of message 'Pizza_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('turtle_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'turtle_interfaces.srv.Pizza_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__pizza__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__pizza__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__pizza__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__pizza__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__pizza__request

            from std_msgs.msg import Int16
            if Int16.__class__._TYPE_SUPPORT is None:
                Int16.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Pizza_Request(metaclass=Metaclass_Pizza_Request):
    """Message class 'Pizza_Request'."""

    __slots__ = [
        '_tao1',
        '_tao2',
        '_tao3',
        '_tao4',
    ]

    _fields_and_field_types = {
        'tao1': 'std_msgs/Int16',
        'tao2': 'std_msgs/Int16',
        'tao3': 'std_msgs/Int16',
        'tao4': 'std_msgs/Int16',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Int16'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Int16'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Int16'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Int16'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Int16
        self.tao1 = kwargs.get('tao1', Int16())
        from std_msgs.msg import Int16
        self.tao2 = kwargs.get('tao2', Int16())
        from std_msgs.msg import Int16
        self.tao3 = kwargs.get('tao3', Int16())
        from std_msgs.msg import Int16
        self.tao4 = kwargs.get('tao4', Int16())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.tao1 != other.tao1:
            return False
        if self.tao2 != other.tao2:
            return False
        if self.tao3 != other.tao3:
            return False
        if self.tao4 != other.tao4:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def tao1(self):
        """Message field 'tao1'."""
        return self._tao1

    @tao1.setter
    def tao1(self, value):
        if __debug__:
            from std_msgs.msg import Int16
            assert \
                isinstance(value, Int16), \
                "The 'tao1' field must be a sub message of type 'Int16'"
        self._tao1 = value

    @builtins.property
    def tao2(self):
        """Message field 'tao2'."""
        return self._tao2

    @tao2.setter
    def tao2(self, value):
        if __debug__:
            from std_msgs.msg import Int16
            assert \
                isinstance(value, Int16), \
                "The 'tao2' field must be a sub message of type 'Int16'"
        self._tao2 = value

    @builtins.property
    def tao3(self):
        """Message field 'tao3'."""
        return self._tao3

    @tao3.setter
    def tao3(self, value):
        if __debug__:
            from std_msgs.msg import Int16
            assert \
                isinstance(value, Int16), \
                "The 'tao3' field must be a sub message of type 'Int16'"
        self._tao3 = value

    @builtins.property
    def tao4(self):
        """Message field 'tao4'."""
        return self._tao4

    @tao4.setter
    def tao4(self, value):
        if __debug__:
            from std_msgs.msg import Int16
            assert \
                isinstance(value, Int16), \
                "The 'tao4' field must be a sub message of type 'Int16'"
        self._tao4 = value


# Import statements for member types

# already imported above
# import rosidl_parser.definition


class Metaclass_Pizza_Response(type):
    """Metaclass of message 'Pizza_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('turtle_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'turtle_interfaces.srv.Pizza_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__pizza__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__pizza__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__pizza__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__pizza__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__pizza__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Pizza_Response(metaclass=Metaclass_Pizza_Response):
    """Message class 'Pizza_Response'."""

    __slots__ = [
    ]

    _fields_and_field_types = {
    }

    SLOT_TYPES = (
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)


class Metaclass_Pizza(type):
    """Metaclass of service 'Pizza'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('turtle_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'turtle_interfaces.srv.Pizza')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__pizza

            from turtle_interfaces.srv import _pizza
            if _pizza.Metaclass_Pizza_Request._TYPE_SUPPORT is None:
                _pizza.Metaclass_Pizza_Request.__import_type_support__()
            if _pizza.Metaclass_Pizza_Response._TYPE_SUPPORT is None:
                _pizza.Metaclass_Pizza_Response.__import_type_support__()


class Pizza(metaclass=Metaclass_Pizza):
    from turtle_interfaces.srv._pizza import Pizza_Request as Request
    from turtle_interfaces.srv._pizza import Pizza_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
