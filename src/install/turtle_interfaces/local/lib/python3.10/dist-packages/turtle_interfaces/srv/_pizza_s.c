// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from turtle_interfaces:srv/Pizza.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "turtle_interfaces/srv/detail/pizza__struct.h"
#include "turtle_interfaces/srv/detail/pizza__functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__bool__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__bool__convert_to_py(void * raw_ros_message);
ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__bool__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__bool__convert_to_py(void * raw_ros_message);
ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__bool__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__bool__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool turtle_interfaces__srv__pizza__request__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[43];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("turtle_interfaces.srv._pizza.Pizza_Request", full_classname_dest, 42) == 0);
  }
  turtle_interfaces__srv__Pizza_Request * ros_message = _ros_message;
  {  // pizza_spawn
    PyObject * field = PyObject_GetAttrString(_pymsg, "pizza_spawn");
    if (!field) {
      return false;
    }
    if (!std_msgs__msg__bool__convert_from_py(field, &ros_message->pizza_spawn)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // pizza_save
    PyObject * field = PyObject_GetAttrString(_pymsg, "pizza_save");
    if (!field) {
      return false;
    }
    if (!std_msgs__msg__bool__convert_from_py(field, &ros_message->pizza_save)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // pizza_clear
    PyObject * field = PyObject_GetAttrString(_pymsg, "pizza_clear");
    if (!field) {
      return false;
    }
    if (!std_msgs__msg__bool__convert_from_py(field, &ros_message->pizza_clear)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * turtle_interfaces__srv__pizza__request__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Pizza_Request */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("turtle_interfaces.srv._pizza");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Pizza_Request");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  turtle_interfaces__srv__Pizza_Request * ros_message = (turtle_interfaces__srv__Pizza_Request *)raw_ros_message;
  {  // pizza_spawn
    PyObject * field = NULL;
    field = std_msgs__msg__bool__convert_to_py(&ros_message->pizza_spawn);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "pizza_spawn", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // pizza_save
    PyObject * field = NULL;
    field = std_msgs__msg__bool__convert_to_py(&ros_message->pizza_save);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "pizza_save", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // pizza_clear
    PyObject * field = NULL;
    field = std_msgs__msg__bool__convert_to_py(&ros_message->pizza_clear);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "pizza_clear", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
// already included above
// #include <Python.h>
// already included above
// #include <stdbool.h>
// already included above
// #include "numpy/ndarrayobject.h"
// already included above
// #include "rosidl_runtime_c/visibility_control.h"
// already included above
// #include "turtle_interfaces/srv/detail/pizza__struct.h"
// already included above
// #include "turtle_interfaces/srv/detail/pizza__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool turtle_interfaces__srv__pizza__response__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[44];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("turtle_interfaces.srv._pizza.Pizza_Response", full_classname_dest, 43) == 0);
  }
  turtle_interfaces__srv__Pizza_Response * ros_message = _ros_message;
  ros_message->structure_needs_at_least_one_member = 0;

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * turtle_interfaces__srv__pizza__response__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Pizza_Response */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("turtle_interfaces.srv._pizza");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Pizza_Response");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  (void)raw_ros_message;

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
