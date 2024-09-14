// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from turtle_interfaces:srv/Pizza.idl
// generated code does not contain a copyright notice

#ifndef TURTLE_INTERFACES__SRV__DETAIL__PIZZA__STRUCT_H_
#define TURTLE_INTERFACES__SRV__DETAIL__PIZZA__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'pizza_spawn'
// Member 'pizza_save'
// Member 'pizza_clear'
#include "std_msgs/msg/detail/bool__struct.h"

/// Struct defined in srv/Pizza in the package turtle_interfaces.
typedef struct turtle_interfaces__srv__Pizza_Request
{
  std_msgs__msg__Bool pizza_spawn;
  std_msgs__msg__Bool pizza_save;
  std_msgs__msg__Bool pizza_clear;
} turtle_interfaces__srv__Pizza_Request;

// Struct for a sequence of turtle_interfaces__srv__Pizza_Request.
typedef struct turtle_interfaces__srv__Pizza_Request__Sequence
{
  turtle_interfaces__srv__Pizza_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} turtle_interfaces__srv__Pizza_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/Pizza in the package turtle_interfaces.
typedef struct turtle_interfaces__srv__Pizza_Response
{
  uint8_t structure_needs_at_least_one_member;
} turtle_interfaces__srv__Pizza_Response;

// Struct for a sequence of turtle_interfaces__srv__Pizza_Response.
typedef struct turtle_interfaces__srv__Pizza_Response__Sequence
{
  turtle_interfaces__srv__Pizza_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} turtle_interfaces__srv__Pizza_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TURTLE_INTERFACES__SRV__DETAIL__PIZZA__STRUCT_H_
