// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from turtle_interfaces:srv/Pizza.idl
// generated code does not contain a copyright notice

#ifndef TURTLE_INTERFACES__SRV__DETAIL__PIZZA__STRUCT_HPP_
#define TURTLE_INTERFACES__SRV__DETAIL__PIZZA__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'tao1'
// Member 'tao2'
// Member 'tao3'
// Member 'tao4'
#include "std_msgs/msg/detail/int16__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__turtle_interfaces__srv__Pizza_Request __attribute__((deprecated))
#else
# define DEPRECATED__turtle_interfaces__srv__Pizza_Request __declspec(deprecated)
#endif

namespace turtle_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Pizza_Request_
{
  using Type = Pizza_Request_<ContainerAllocator>;

  explicit Pizza_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : tao1(_init),
    tao2(_init),
    tao3(_init),
    tao4(_init)
  {
    (void)_init;
  }

  explicit Pizza_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : tao1(_alloc, _init),
    tao2(_alloc, _init),
    tao3(_alloc, _init),
    tao4(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _tao1_type =
    std_msgs::msg::Int16_<ContainerAllocator>;
  _tao1_type tao1;
  using _tao2_type =
    std_msgs::msg::Int16_<ContainerAllocator>;
  _tao2_type tao2;
  using _tao3_type =
    std_msgs::msg::Int16_<ContainerAllocator>;
  _tao3_type tao3;
  using _tao4_type =
    std_msgs::msg::Int16_<ContainerAllocator>;
  _tao4_type tao4;

  // setters for named parameter idiom
  Type & set__tao1(
    const std_msgs::msg::Int16_<ContainerAllocator> & _arg)
  {
    this->tao1 = _arg;
    return *this;
  }
  Type & set__tao2(
    const std_msgs::msg::Int16_<ContainerAllocator> & _arg)
  {
    this->tao2 = _arg;
    return *this;
  }
  Type & set__tao3(
    const std_msgs::msg::Int16_<ContainerAllocator> & _arg)
  {
    this->tao3 = _arg;
    return *this;
  }
  Type & set__tao4(
    const std_msgs::msg::Int16_<ContainerAllocator> & _arg)
  {
    this->tao4 = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    turtle_interfaces::srv::Pizza_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const turtle_interfaces::srv::Pizza_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<turtle_interfaces::srv::Pizza_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<turtle_interfaces::srv::Pizza_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      turtle_interfaces::srv::Pizza_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<turtle_interfaces::srv::Pizza_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      turtle_interfaces::srv::Pizza_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<turtle_interfaces::srv::Pizza_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<turtle_interfaces::srv::Pizza_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<turtle_interfaces::srv::Pizza_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__turtle_interfaces__srv__Pizza_Request
    std::shared_ptr<turtle_interfaces::srv::Pizza_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__turtle_interfaces__srv__Pizza_Request
    std::shared_ptr<turtle_interfaces::srv::Pizza_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Pizza_Request_ & other) const
  {
    if (this->tao1 != other.tao1) {
      return false;
    }
    if (this->tao2 != other.tao2) {
      return false;
    }
    if (this->tao3 != other.tao3) {
      return false;
    }
    if (this->tao4 != other.tao4) {
      return false;
    }
    return true;
  }
  bool operator!=(const Pizza_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Pizza_Request_

// alias to use template instance with default allocator
using Pizza_Request =
  turtle_interfaces::srv::Pizza_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace turtle_interfaces


#ifndef _WIN32
# define DEPRECATED__turtle_interfaces__srv__Pizza_Response __attribute__((deprecated))
#else
# define DEPRECATED__turtle_interfaces__srv__Pizza_Response __declspec(deprecated)
#endif

namespace turtle_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Pizza_Response_
{
  using Type = Pizza_Response_<ContainerAllocator>;

  explicit Pizza_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  explicit Pizza_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  // field types and members
  using _structure_needs_at_least_one_member_type =
    uint8_t;
  _structure_needs_at_least_one_member_type structure_needs_at_least_one_member;


  // constant declarations

  // pointer types
  using RawPtr =
    turtle_interfaces::srv::Pizza_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const turtle_interfaces::srv::Pizza_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<turtle_interfaces::srv::Pizza_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<turtle_interfaces::srv::Pizza_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      turtle_interfaces::srv::Pizza_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<turtle_interfaces::srv::Pizza_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      turtle_interfaces::srv::Pizza_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<turtle_interfaces::srv::Pizza_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<turtle_interfaces::srv::Pizza_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<turtle_interfaces::srv::Pizza_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__turtle_interfaces__srv__Pizza_Response
    std::shared_ptr<turtle_interfaces::srv::Pizza_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__turtle_interfaces__srv__Pizza_Response
    std::shared_ptr<turtle_interfaces::srv::Pizza_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Pizza_Response_ & other) const
  {
    if (this->structure_needs_at_least_one_member != other.structure_needs_at_least_one_member) {
      return false;
    }
    return true;
  }
  bool operator!=(const Pizza_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Pizza_Response_

// alias to use template instance with default allocator
using Pizza_Response =
  turtle_interfaces::srv::Pizza_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace turtle_interfaces

namespace turtle_interfaces
{

namespace srv
{

struct Pizza
{
  using Request = turtle_interfaces::srv::Pizza_Request;
  using Response = turtle_interfaces::srv::Pizza_Response;
};

}  // namespace srv

}  // namespace turtle_interfaces

#endif  // TURTLE_INTERFACES__SRV__DETAIL__PIZZA__STRUCT_HPP_
