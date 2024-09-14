# FRA501 EXAM 6531 6562

## Information
1. Architecture
    <img src="/home/tadtawan/Pictures/Screenshots/Screenshot from 2024-09-15 00-29-15.png" alt="Alt text" title="Optional title">




## How to run

### 1. Setup the Environment
1. Clone the repository:
    ```sh
    git clone https://github.com/SUNTADTAWAN/EXAM1_WS.git
    ```
2. Navigate to the project directory:
    ```sh
    cd EXAM1_WS
    ```
3. Install pynput
    ```sh
    pip install pynput
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
### 3. Run
1. Run teleop_twist_keyboard with namespace 
    ```sh
    ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r __ns:=/your_namespace
    ```

2. Run launch file
   ```sh
   ros2 launch taohunza turtle_launch.py
   ```



## How to Fix when Bug
1. If it cannot run teleop_twist_keyboard
   
    1.1. Restart your terminal
   
    2.2. Rebuild & source
    ```sh
    colon build
    source install/setup.bash
    ```




