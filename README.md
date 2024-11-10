##Humbot Files for MTRN4068

All ROS2 files required for the simulation and ROS2 setup are found here, the general structure is as follows:

- description - files describing behaviour and structure of robot, sensors and controls.
- config - configuration of ros2 controller (unused for demonstration).
-launch - Contains launch files for quick deployment of robot and simulation.
- other - Other files generated during development, such as through graph generator for the pdf, or rviz setup when opening rviz2.
- CMakeLists.txt - show ROS2 where to find directories of our package, and other functionalities.
- package.xml - Tells ROS2 what dependencies our package has.
