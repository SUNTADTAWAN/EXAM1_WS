# FRA501 EXAM 6531 6562
## How To Run
### 1. Setup the Environment
1. Clone the repository:
    ```sh
    git clone https://github.com/SUNTADTAWAN/EXAM1_WS.git
    ```
2. Navigate to the project directory:
    ```sh
    cd EXAM1_WS
    ```
### 2. Build the Firmware
1. Build
    ```sh
    colon build
    ``` 
2. Source workspace
    ```sh
    source ~/EXAM1_WS/install/setup.bash 
    ```
### 3. Run launch file


## How To  Use
### 1. teleop_twist_keyboard
1. Run teleop_twist_keyboard with namespace
    ```sh
    ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r __ns:=/your_namespace
    ```
