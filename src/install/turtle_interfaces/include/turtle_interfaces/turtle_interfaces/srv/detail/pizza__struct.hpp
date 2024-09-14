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
// Member 'pizza_spawn'
// Member 'pizza_save'
// Member 'pizza_clear'
#include "std_msgs/msg/detail/bool__struct.hpp"

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
  : pizza_spawn(_init),
    pizza_save(_init),
    pizza_clear(_init)
  {
    (void)_init;
  }

  explicit Pizza_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : pizza_spawn(_alloc, _init),
    pizza_save(_alloc, _init),
    pizza_clear(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _pizza_spawn_type =
    std_msgs::msg::Bool_<ContainerAllocator>;
  _pizza_spawn_type pizza_spawn;
  using _pizza_save_type =
    std_msgs::msg::Bool_<ContainerAllocator>;
  _pizza_save_type pizza_save;
  using _pizza_clear_type =
    std_msgs::msg::Bool_<ContainerAllocator>;
  _pizza_clear_type pizza_clear;

  // setters for named parameter idiom
  Type & set__pizza_spawn(
    const std_msgs::msg::Bool_<ContainerAllocator> & _arg)
  {
    this->pizza_spawn = _arg;
    return *this;
  }
  Type & set__pizza_save(
    const std_msgs::msg::Bool_<ContainerAllocator> & _arg)
  {
    this->pizza_save = _arg;
    return *this;
  }
  Type & set__pizza_clear(
    const std_msgs::msg::Bool_<ContainerAllocator> & _arg)
  {
    this->pizza_clear = _arg;
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
    if (this->pizza_spawn != other.pizza_spawn) {
      return false;
    }
    if (this->pizza_save != other.pizza_save) {
      return false;
    }
    if (this->pizza_clear != other.pizza_clear) {
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
