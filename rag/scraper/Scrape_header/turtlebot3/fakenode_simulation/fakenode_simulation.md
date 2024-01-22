
[Edit on GitHub](https://github.com/ROBOTIS-GIT/emanual/blob/master/docs/en/platform/turtlebot3/simulation/fakenode_simulation.md "https://github.com/ROBOTIS-GIT/emanual/blob/master/docs/en/platform/turtlebot3/simulation/fakenode_simulation.md") 

Kinetic 
Melodic
Noetic
Dashing
Foxy
Humble
Windows

## [Fake Node Simulation](#fake-node-simulation "#fake-node-simulation")

The contents in e-Manual are subject to be updated without a prior notice. Therefore, some video may differ from the contents in e-Manual.

To use `turtlebot3_fake_node`, you need the `turtlebot3_simulation` metapackage. Install the package as shown in the following command.

**TIP**: The terminal application can be found with the Ubuntu search icon on the top left corner of the screen. The shortcut key for running the terminal is `Ctrl`-`Alt`-`T`.

**NOTE**: The `turtlebot3_simulation` metapackage requires `turtlebot3` metapackage and `turtlebot3_msgs` package as a prerequisite. If you didn’t install it in the [Install Dependent ROS Packages of PC Setup](/docs/en/platform/turtlebot3/quick-start/#install-dependent-ros-1-packages-1 "/docs/en/platform/turtlebot3/quick-start/#install-dependent-ros-1-packages-1") section, install it first.

```
$ cd ~/catkin_ws/src/
$ git clone -b kinetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
$ cd ~/catkin_ws && catkin_make

```

To launch the virtual robot, execute the `turtlebot3_fake.launch` file in the `turtlebot3_fake` package as shown below. The `turtlebot3_fake` is a very simple simulation node that can be run without having an actual robot. You can even control the virtual TurtleBot3 in RViz with a teleoperation node.

Please use the proper keyword among `burger`, `waffle`, `waffle_pi` for the `TURTLEBOT3_MODEL` parameter.

```
$ export TURTLEBOT3\_MODEL=burger
$ roslaunch turtlebot3_fake turtlebot3_fake.launch

```

```
$ export TURTLEBOT3\_MODEL=burger
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

```

The contents in e-Manual are subject to be updated without a prior notice. Therefore, some video may differ from the contents in e-Manual.

To use `turtlebot3_fake_node`, you need the `turtlebot3_simulation` metapackage. Install the package as shown in the following command.

**TIP**: The terminal application can be found with the Ubuntu search icon on the top left corner of the screen. The shortcut key for running the terminal is `Ctrl`-`Alt`-`T`.

**NOTE**: The `turtlebot3_simulation` metapackage requires `turtlebot3` metapackage and `turtlebot3_msgs` package as a prerequisite. If you didn’t install it in the [Install Dependent ROS Packages of PC Setup](/docs/en/platform/turtlebot3/quick-start/#install-dependent-ros-1-packages-1 "/docs/en/platform/turtlebot3/quick-start/#install-dependent-ros-1-packages-1") section, install it first.

```
$ cd ~/catkin_ws/src/
$ git clone -b melodic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
$ cd ~/catkin_ws && catkin_make

```

To launch the virtual robot, execute the `turtlebot3_fake.launch` file in the `turtlebot3_fake` package as shown below. The `turtlebot3_fake` is a very simple simulation node that can be run without having an actual robot. You can even control the virtual TurtleBot3 in RViz with a teleoperation node.

Please use the proper keyword among `burger`, `waffle`, `waffle_pi` for the `TURTLEBOT3_MODEL` parameter.

```
$ export TURTLEBOT3\_MODEL=burger
$ roslaunch turtlebot3_fake turtlebot3_fake.launch

```

```
$ export TURTLEBOT3\_MODEL=burger
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

```

The contents in e-Manual are subject to be updated without a prior notice. Therefore, some video may differ from the contents in e-Manual.

To use `turtlebot3_fake_node`, you need the `turtlebot3_simulation` metapackage. Install the package as shown in the following command.

**TIP**: The terminal application can be found with the Ubuntu search icon on the top left corner of the screen. The shortcut key for running the terminal is `Ctrl`-`Alt`-`T`.

**NOTE**: The `turtlebot3_simulation` metapackage requires `turtlebot3` metapackage and `turtlebot3_msgs` package as a prerequisite. If you didn’t install it in the [Install Dependent ROS Packages of PC Setup](/docs/en/platform/turtlebot3/quick-start/#install-dependent-ros-1-packages-1 "/docs/en/platform/turtlebot3/quick-start/#install-dependent-ros-1-packages-1") section, install it first.

```
$ cd ~/catkin_ws/src/
$ git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
$ cd ~/catkin_ws && catkin_make

```

To launch the virtual robot, execute the `turtlebot3_fake.launch` file in the `turtlebot3_fake` package as shown below. The `turtlebot3_fake` is a very simple simulation node that can be run without having an actual robot. You can even control the virtual TurtleBot3 in RViz with a teleoperation node.

Please use the proper keyword among `burger`, `waffle`, `waffle_pi` for the `TURTLEBOT3_MODEL` parameter.

```
$ export TURTLEBOT3\_MODEL=burger
$ roslaunch turtlebot3_fake turtlebot3_fake.launch

```

```
$ export TURTLEBOT3\_MODEL=burger
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

```

The contents in e-Manual are subject to be updated without a prior notice. Therefore, some video may differ from the contents in e-Manual.

To use a virtual TurtleBot3, execute `turtlebot3_fake_node.launch.py` in a `turtlebot3_fake_node` package that is simple simulation node.
Follow the instructions to bring TurtleBot3 into the virtual world using Fake Node.

1. Execute `turtlebot3_fake_node.launch.py` file.  

 Please use the proper keyword among `burger`, `waffle`, `waffle_pi` for the `TURTLEBOT3_MODEL` parameter.

```
$ export TURTLEBOT3\_MODEL=burger
$ ros2 launch turtlebot3_fake_node turtlebot3_fake_node.launch.py

```
2. You can control the virtual TurtleBot3 by using [Teleoperation](/docs/en/platform/turtlebot3/ros2_basic_operation/#basic_operation/#teleoperation "/docs/en/platform/turtlebot3/ros2_basic_operation/#basic_operation/#teleoperation")

```
$ export TURTLEBOT3\_MODEL=burger
$ ros2 run turtlebot3_teleop teleop_keyboard

```

The contents in e-Manual are subject to be updated without a prior notice. Therefore, some video may differ from the contents in e-Manual.

To use a virtual TurtleBot3, execute `turtlebot3_fake_node.launch.py` in a `turtlebot3_fake_node` package that is simple simulation node.
Follow the instructions to bring TurtleBot3 into the virtual world using Fake Node.

1. Execute `turtlebot3_fake_node.launch.py` file.  

 Please use the proper keyword among `burger`, `waffle`, `waffle_pi` for the `TURTLEBOT3_MODEL` parameter.

```
$ export TURTLEBOT3\_MODEL=burger
$ ros2 launch turtlebot3_fake_node turtlebot3_fake_node.launch.py

```
2. You can control the virtual TurtleBot3 by using [Teleoperation](/docs/en/platform/turtlebot3/basic_operation/#teleoperation "/docs/en/platform/turtlebot3/basic_operation/#teleoperation")

```
$ export TURTLEBOT3\_MODEL=burger
$ ros2 run turtlebot3_teleop teleop_keyboard

```

The contents in e-Manual are subject to be updated without a prior notice. Therefore, some video may differ from the contents in e-Manual.

To use a virtual TurtleBot3, execute `turtlebot3_fake_node.launch.py` in a `turtlebot3_fake_node` package that is simple simulation node.
Follow the instructions to bring TurtleBot3 into the virtual world using Fake Node.

1. Execute `turtlebot3_fake_node.launch.py` file.  

 Please use the proper keyword among `burger`, `waffle`, `waffle_pi` for the `TURTLEBOT3_MODEL` parameter.

```
$ export TURTLEBOT3\_MODEL=burger
$ ros2 launch turtlebot3_fake_node turtlebot3_fake_node.launch.py

```
2. You can control the virtual TurtleBot3 by using [Teleoperation](/docs/en/platform/turtlebot3/basic_operation/#teleoperation "/docs/en/platform/turtlebot3/basic_operation/#teleoperation")

```
$ export TURTLEBOT3\_MODEL=burger
$ ros2 run turtlebot3_teleop teleop_keyboard

```

**NOTE**: This feature is availabe for Kinetic, Noetic, Dashing, Foxy.

 Previous Page
Next Page 