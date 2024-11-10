## Humbot Files for MTRN4068

All ROS2 files required for the simulation and ROS2 setup are found here, the general structure is as follows:

- description - files describing behaviour and structure of robot, sensors and controls.
- config - configuration of ros2 controller (unused for demonstration).
-launch - Contains launch files for quick deployment of robot and simulation.
- other - Other files generated during development, such as through graph generator for the pdf, or rviz setup when opening rviz2.
- CMakeLists.txt - show ROS2 where to find directories of our package, and other functionalities.
- package.xml - Tells ROS2 what dependencies our package has.


## Arduino Motor Control
Files remained on the Arduino and the RPi that was handed into the university at the end of the demonstration, this inlcuded the PID tuning and custom pin values for the circuit, the files were based on [this repository] (https://github.com/joshnewans/serial_motor_demo.git).
Please Consult the final report for the detailed circuit schematic and PID tuning process and values used.