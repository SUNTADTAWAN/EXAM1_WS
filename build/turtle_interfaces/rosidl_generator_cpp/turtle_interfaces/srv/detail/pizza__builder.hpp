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

class Init_Pizza_Request_tao4
{
public:
  explicit Init_Pizza_Request_tao4(::turtle_interfaces::srv::Pizza_Request & msg)
  : msg_(msg)
  {}
  ::turtle_interfaces::srv::Pizza_Request tao4(::turtle_interfaces::srv::Pizza_Request::_tao4_type arg)
  {
    msg_.tao4 = std::move(arg);
    return std::move(msg_);
  }

private:
  ::turtle_interfaces::srv::Pizza_Request msg_;
};

class Init_Pizza_Request_tao3
{
public:
  explicit Init_Pizza_Request_tao3(::turtle_interfaces::srv::Pizza_Request & msg)
  : msg_(msg)
  {}
  Init_Pizza_Request_tao4 tao3(::turtle_interfaces::srv::Pizza_Request::_tao3_type arg)
  {
    msg_.tao3 = std::move(arg);
    return Init_Pizza_Request_tao4(msg_);
  }

private:
  ::turtle_interfaces::srv::Pizza_Request msg_;
};

class Init_Pizza_Request_tao2
{
public:
  explicit Init_Pizza_Request_tao2(::turtle_interfaces::srv::Pizza_Request & msg)
  : msg_(msg)
  {}
  Init_Pizza_Request_tao3 tao2(::turtle_interfaces::srv::Pizza_Request::_tao2_type arg)
  {
    msg_.tao2 = std::move(arg);
    return Init_Pizza_Request_tao3(msg_);
  }

private:
  ::turtle_interfaces::srv::Pizza_Request msg_;
};

class Init_Pizza_Request_tao1
{
public:
  Init_Pizza_Request_tao1()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Pizza_Request_tao2 tao1(::turtle_interfaces::srv::Pizza_Request::_tao1_type arg)
  {
    msg_.tao1 = std::move(arg);
    return Init_Pizza_Request_tao2(msg_);
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
  return turtle_interfaces::srv::builder::Init_Pizza_Request_tao1();
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
