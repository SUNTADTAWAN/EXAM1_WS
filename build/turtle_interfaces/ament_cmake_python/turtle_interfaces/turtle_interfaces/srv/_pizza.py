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

            from std_msgs.msg import Bool
            if Bool.__class__._TYPE_SUPPORT is None:
                Bool.__class__.__import_type_support__()

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
        '_pizza_spawn',
        '_pizza_save',
        '_pizza_clear',
    ]

    _fields_and_field_types = {
        'pizza_spawn': 'std_msgs/Bool',
        'pizza_save': 'std_msgs/Bool',
        'pizza_clear': 'std_msgs/Bool',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Bool'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Bool'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Bool'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Bool
        self.pizza_spawn = kwargs.get('pizza_spawn', Bool())
        from std_msgs.msg import Bool
        self.pizza_save = kwargs.get('pizza_save', Bool())
        from std_msgs.msg import Bool
        self.pizza_clear = kwargs.get('pizza_clear', Bool())

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
        if self.pizza_spawn != other.pizza_spawn:
            return False
        if self.pizza_save != other.pizza_save:
            return False
        if self.pizza_clear != other.pizza_clear:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def pizza_spawn(self):
        """Message field 'pizza_spawn'."""
        return self._pizza_spawn

    @pizza_spawn.setter
    def pizza_spawn(self, value):
        if __debug__:
            from std_msgs.msg import Bool
            assert \
                isinstance(value, Bool), \
                "The 'pizza_spawn' field must be a sub message of type 'Bool'"
        self._pizza_spawn = value

    @builtins.property
    def pizza_save(self):
        """Message field 'pizza_save'."""
        return self._pizza_save

    @pizza_save.setter
    def pizza_save(self, value):
        if __debug__:
            from std_msgs.msg import Bool
            assert \
                isinstance(value, Bool), \
                "The 'pizza_save' field must be a sub message of type 'Bool'"
        self._pizza_save = value

    @builtins.property
    def pizza_clear(self):
        """Message field 'pizza_clear'."""
        return self._pizza_clear

    @pizza_clear.setter
    def pizza_clear(self, value):
        if __debug__:
            from std_msgs.msg import Bool
            assert \
                isinstance(value, Bool), \
                "The 'pizza_clear' field must be a sub message of type 'Bool'"
        self._pizza_clear = value


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
