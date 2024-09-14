// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from turtle_interfaces:srv/Pizza.idl
// generated code does not contain a copyright notice

#ifndef TURTLE_INTERFACES__SRV__DETAIL__PIZZA__BUILDER_HPP_
#define TURTLE_INTERFACES__SRV__DETAIL__PIZZA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "turtle_interfaces/srv/detail/pizza__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace turtle_interfaces
{

namespace srv
{

namespace builder
{

class Init_Pizza_Request_pizza_clear
{
public:
  explicit Init_Pizza_Request_pizza_clear(::turtle_interfaces::srv::Pizza_Request & msg)
  : msg_(msg)
  {}
  ::turtle_interfaces::srv::Pizza_Request pizza_clear(::turtle_interfaces::srv::Pizza_Request::_pizza_clear_type arg)
  {
    msg_.pizza_clear = std::move(arg);
    return std::move(msg_);
  }

private:
  ::turtle_interfaces::srv::Pizza_Request msg_;
};

class Init_Pizza_Request_pizza_save
{
public:
  explicit Init_Pizza_Request_pizza_save(::turtle_interfaces::srv::Pizza_Request & msg)
  : msg_(msg)
  {}
  Init_Pizza_Request_pizza_clear pizza_save(::turtle_interfaces::srv::Pizza_Request::_pizza_save_type arg)
  {
    msg_.pizza_save = std::move(arg);
    return Init_Pizza_Request_pizza_clear(msg_);
  }

private:
  ::turtle_interfaces::srv::Pizza_Request msg_;
};

class Init_Pizza_Request_pizza_spawn
{
public:
  Init_Pizza_Request_pizza_spawn()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Pizza_Request_pizza_save pizza_spawn(::turtle_interfaces::srv::Pizza_Request::_pizza_spawn_type arg)
  {
    msg_.pizza_spawn = std::move(arg);
    return Init_Pizza_Request_pizza_save(msg_);
  }

private:
  ::turtle_interfaces::srv::Pizza_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::turtle_interfaces::srv::Pizza_Request>()
{
  return turtle_interfaces::srv::builder::Init_Pizza_Request_pizza_spawn();
}

}  // namespace turtle_interfaces


namespace turtle_interfaces
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::turtle_interfaces::srv::Pizza_Response>()
{
  return ::turtle_interfaces::srv::Pizza_Response(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace turtle_interfaces

#endif  // TURTLE_INTERFACES__SRV__DETAIL__PIZZA__BUILDER_HPP_
