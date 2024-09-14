# FRA501 EXAM 6531 6562

## Information
1. Architecture

    1.1.taohunza package :
    ![Alt text](architecture.png)
    This package have input from teleop_twist_keyboard package.

    This package have 3 Node :

        copy_turtle_node : This node for control copy turtle.
   
        pizza_memory_node : This node for collect position data of pizza from turtle. 

        turtle_teleop_node : This node for control turtle.

        Melodic_turtle_node : This node for control Melodic turtle.



## How to run

### 1. Setup the Environment
1. Clone the repository :
    ```sh
    git clone https://github.com/SUNTADTAWAN/EXAM1_WS.git
    ```
2. Navigate to the project directory :
    ```sh
    cd EXAM1_WS
    ```
3. Install pynput :
    ```sh
    pip install pynput
    ```
### 2. Build the Firmware
1. Build :
    ```sh
    colon build
    ``` 
2. Source workspace :
    ```sh
    source ~/EXAM1_WS/install/setup.bash 
    ```
### 3. Run
1. Run teleop_twist_keyboard with namespace :
    ```sh
    ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r __ns:=/field1/nongtao1
    ```

2. Run launch file :
   ```sh
   ros2 launch taohunza turtle_launch.py
   ```
3. Run rqt :
   ```sh
   rqt
   ```


## How to Use

1. Use keyboard for control turtle
2. Use keyboard for spawn / clear / save a Pizza
3. Use rqt to config parameter of gain and pizza amount
   ```sh
   ros2 run rqt_reconfigure rqt_reconfigure
   ```
    (field1-->nongtao1-->controller)
   For adjust Pizza amount and Controller gain.

## How to Fix when Bug
1. If it cannot run teleop_twist_keyboard :
   
    1.1. Restart your terminal
   
    2.2. Rebuild & source
    ```sh
    colon build
    source install/setup.bash
    ```
2. Something else :
   
   2.1. Kill all node
   
   2.2. Restart your computer
   
   2.3. Ask chatGPT and let's fix it

   



