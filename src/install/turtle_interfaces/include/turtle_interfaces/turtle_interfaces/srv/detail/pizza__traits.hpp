// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from turtle_interfaces:srv/Pizza.idl
// generated code does not contain a copyright notice

#ifndef TURTLE_INTERFACES__SRV__DETAIL__PIZZA__TRAITS_HPP_
#define TURTLE_INTERFACES__SRV__DETAIL__PIZZA__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "turtle_interfaces/srv/detail/pizza__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'pizza_spawn'
// Member 'pizza_save'
// Member 'pizza_clear'
#include "std_msgs/msg/detail/bool__traits.hpp"

namespace turtle_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const Pizza_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: pizza_spawn
  {
    out << "pizza_spawn: ";
    to_flow_style_yaml(msg.pizza_spawn, out);
    out << ", ";
  }

  // member: pizza_save
  {
    out << "pizza_save: ";
    to_flow_style_yaml(msg.pizza_save, out);
    out << ", ";
  }

  // member: pizza_clear
  {
    out << "pizza_clear: ";
    to_flow_style_yaml(msg.pizza_clear, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Pizza_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: pizza_spawn
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pizza_spawn:\n";
    to_block_style_yaml(msg.pizza_spawn, out, indentation + 2);
  }

  // member: pizza_save
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pizza_save:\n";
    to_block_style_yaml(msg.pizza_save, out, indentation + 2);
  }

  // member: pizza_clear
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pizza_clear:\n";
    to_block_style_yaml(msg.pizza_clear, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Pizza_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace turtle_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use turtle_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const turtle_interfaces::srv::Pizza_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  turtle_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use turtle_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const turtle_interfaces::srv::Pizza_Request & msg)
{
  return turtle_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<turtle_interfaces::srv::Pizza_Request>()
{
  return "turtle_interfaces::srv::Pizza_Request";
}

template<>
inline const char * name<turtle_interfaces::srv::Pizza_Request>()
{
  return "turtle_interfaces/srv/Pizza_Request";
}

template<>
struct has_fixed_size<turtle_interfaces::srv::Pizza_Request>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Bool>::value> {};

template<>
struct has_bounded_size<turtle_interfaces::srv::Pizza_Request>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Bool>::value> {};

template<>
struct is_message<turtle_interfaces::srv::Pizza_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace turtle_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const Pizza_Response & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Pizza_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Pizza_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace turtle_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use turtle_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const turtle_interfaces::srv::Pizza_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  turtle_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use turtle_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const turtle_interfaces::srv::Pizza_Response & msg)
{
  return turtle_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<turtle_interfaces::srv::Pizza_Response>()
{
  return "turtle_interfaces::srv::Pizza_Response";
}

template<>
inline const char * name<turtle_interfaces::srv::Pizza_Response>()
{
  return "turtle_interfaces/srv/Pizza_Response";
}

template<>
struct has_fixed_size<turtle_interfaces::srv::Pizza_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<turtle_interfaces::srv::Pizza_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<turtle_interfaces::srv::Pizza_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<turtle_interfaces::srv::Pizza>()
{
  return "turtle_interfaces::srv::Pizza";
}

template<>
inline const char * name<turtle_interfaces::srv::Pizza>()
{
  return "turtle_interfaces/srv/Pizza";
}

template<>
struct has_fixed_size<turtle_interfaces::srv::Pizza>
  : std::integral_constant<
    bool,
    has_fixed_size<turtle_interfaces::srv::Pizza_Request>::value &&
    has_fixed_size<turtle_interfaces::srv::Pizza_Response>::value
  >
{
};

template<>
struct has_bounded_size<turtle_interfaces::srv::Pizza>
  : std::integral_constant<
    bool,
    has_bounded_size<turtle_interfaces::srv::Pizza_Request>::value &&
    has_bounded_size<turtle_interfaces::srv::Pizza_Response>::value
  >
{
};

template<>
struct is_service<turtle_interfaces::srv::Pizza>
  : std::true_type
{
};

template<>
struct is_service_request<turtle_interfaces::srv::Pizza_Request>
  : std::true_type
{
};

template<>
struct is_service_response<turtle_interfaces::srv::Pizza_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // TURTLE_INTERFACES__SRV__DETAIL__PIZZA__TRAITS_HPP_
