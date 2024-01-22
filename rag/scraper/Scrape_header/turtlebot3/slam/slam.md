
[Edit on GitHub](https://github.com/ROBOTIS-GIT/emanual/blob/master/docs/en/platform/turtlebot3/slam.md "https://github.com/ROBOTIS-GIT/emanual/blob/master/docs/en/platform/turtlebot3/slam.md") 

Kinetic 
Melodic
Noetic
Dashing
Foxy
Humble
Windows

# [SLAM](#slam "#slam")

**NOTE**

* Please run the SLAM on **Remote PC**.
* Make sure to launch the [Bringup](/docs/en/platform/turtlebot3/bringup "/docs/en/platform/turtlebot3/bringup") from TurtleBot3 before executing any operation.

The **SLAM (Simultaneous Localization and Mapping)** is a technique to draw a map by estimating current location in an arbitrary space. The SLAM is a well-known feature of TurtleBot from its predecessors. The video here shows you how accurately TurtleBot3 can draw a map with its compact and affordable platform.

**NOTE**

* Please run the SLAM on **Remote PC**.
* Make sure to launch the [Bringup](/docs/en/platform/turtlebot3/bringup "/docs/en/platform/turtlebot3/bringup") from TurtleBot3 before executing any operation.

The **SLAM (Simultaneous Localization and Mapping)** is a technique to draw a map by estimating current location in an arbitrary space. The SLAM is a well-known feature of TurtleBot from its predecessors. The video here shows you how accurately TurtleBot3 can draw a map with its compact and affordable platform.

**NOTE**

* Please run the SLAM on **Remote PC**.
* Make sure to launch the [Bringup](/docs/en/platform/turtlebot3/bringup "/docs/en/platform/turtlebot3/bringup") from TurtleBot3 before executing any operation.

The **SLAM (Simultaneous Localization and Mapping)** is a technique to draw a map by estimating current location in an arbitrary space. The SLAM is a well-known feature of TurtleBot from its predecessors. The video here shows you how accurately TurtleBot3 can draw a map with its compact and affordable platform.

**NOTE**

* Please run the SLAM on **Remote PC**.
* Make sure to launch the [Bringup](/docs/en/platform/turtlebot3/bringup "/docs/en/platform/turtlebot3/bringup") from TurtleBot3 before executing any operation.

The **SLAM (Simultaneous Localization and Mapping)** is a technique to draw a map by estimating current location in an arbitrary space. The SLAM is a well-known feature of TurtleBot from its predecessors. The video here shows you how accurately TurtleBot3 can draw a map with its compact and affordable platform.

**NOTE**

* Please run the SLAM on **Remote PC**.
* Make sure to launch the [Bringup](/docs/en/platform/turtlebot3/bringup "/docs/en/platform/turtlebot3/bringup") from TurtleBot3 before executing any operation.

The **SLAM (Simultaneous Localization and Mapping)** is a technique to draw a map by estimating current location in an arbitrary space. The SLAM is a well-known feature of TurtleBot from its predecessors. The video here shows you how accurately TurtleBot3 can draw a map with its compact and affordable platform.

**NOTE**

* Please run the SLAM on **Remote PC**.
* Make sure to launch the [Bringup](/docs/en/platform/turtlebot3/bringup "/docs/en/platform/turtlebot3/bringup") from TurtleBot3 before executing any operation.

The **SLAM (Simultaneous Localization and Mapping)** is a technique to draw a map by estimating current location in an arbitrary space. The SLAM is a well-known feature of TurtleBot from its predecessors. The video here shows you how accurately TurtleBot3 can draw a map with its compact and affordable platform.

**NOTE**

* Please run the SLAM on **Remote PC**.
* Make sure to launch the [Bringup](/docs/en/platform/turtlebot3/bringup "/docs/en/platform/turtlebot3/bringup") from TurtleBot3 before executing any operation.

The **SLAM (Simultaneous Localization and Mapping)** is a technique to draw a map by estimating current location in an arbitrary space. The SLAM is a well-known feature of TurtleBot from its predecessors. The video here shows you how accurately TurtleBot3 can draw a map with its compact and affordable platform.

## [Run SLAM Node](#run-slam-node "#run-slam-node")

1. Run roscore from Remote PC.

```
$ roscore

```
2. If the `Bringup` is not running on the TurtleBot3 SBC, launch the Bringup. **Skip this step if you have launched bringup previously**.
	* Open a new terminal from Remote PC with `Ctrl` + `Alt` + `T` and connect to Raspberry Pi with its IP address.
	The default password is **turtlebot**.

```
	$ ssh pi@{IP_ADDRESS_OF_RASPBERRY_PI}
	$ roslaunch turtlebot3_bringup turtlebot3_robot.launch

```
3. Open a new terminal from Remote PC with `Ctrl` + `Alt` + `T` and launch the SLAM node. The Gmapping is used as a default SLAM method.
 Please use the proper keyword among `burger`, `waffle`, `waffle_pi` for the `TURTLEBOT3_MODEL` parameter.

```
$ export TURTLEBOT3\_MODEL=burger
$ roslaunch turtlebot3_slam turtlebot3_slam.launch

```

![](/assets/images/icon_unfold.png) **How to save the TURTLEBOT3\_MODEL parameter?**

The `$ export TURTLEBOT3_MODEL=${TB3_MODEL}` command can be omitted if the **TURTLEBOT3\_MODEL** parameter is predefined in the `.bashrc` file.  

The `.bashrc` file is automatically loaded when a terminal window is created.

* Example of defining `TurtlBot3 Burger` as a default model.

```
$ echo 'export TURTLEBOT3\_MODEL=burger' >> ~/.bashrc
$ source ~/.bashrc

```
* Example of defining `TurtlBot3 Waffle Pi` as a default model.

```
$ echo 'export TURTLEBOT3\_MODEL=waffle\_pi' >> ~/.bashrc
$ source ~/.bashrc

```

![](/assets/images/icon_unfold.png) Read more about **other SLAM methods**

* **Gmapping** ([ROS WIKI](http://wiki.ros.org/gmapping "http://wiki.ros.org/gmapping"), [Github](https://github.com/ros-perception/slam_gmapping "https://github.com/ros-perception/slam_gmapping"))
	1. Install dependent packages on PC.  

	 Packages related to Gmapping have already been installed on [PC Setup](/docs/en/platform/turtlebot3/quick-start "/docs/en/platform/turtlebot3/quick-start") section.
	2. Launch the Gmapping SLAM node.

```
	$ roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping

```
* **Cartographer** ([ROS WIKI](http://wiki.ros.org/cartographer "http://wiki.ros.org/cartographer"), [Github](https://github.com/googlecartographer/cartographer "https://github.com/googlecartographer/cartographer"))
	1. Download and build packages on PC.  

	The Cartographer package developed by Google supports ROS1 Kinetic with 0.2.0 version. So if you need to use Cartogrpher on Kinetic, you should download and build the source code as follows instead of installing with the binary packages. Please refer to [official wiki page](https://google-cartographer-ros.readthedocs.io/en/latest/#building-installation "https://google-cartographer-ros.readthedocs.io/en/latest/#building-installation") for more detailed installation instructions.

```
	$ sudo apt-get install ninja-build libceres-dev libprotobuf-dev protobuf-compiler libprotoc-dev
	$ cd ~/catkin_ws/src
	$ git clone https://github.com/googlecartographer/cartographer.git
	$ git clone https://github.com/googlecartographer/cartographer_ros.git
	$ cd ~/catkin_ws
	$ src/cartographer/scripts/install_proto3.sh
	$ rm -rf protobuf/
	$ rosdep install --from-paths src --ignore-src -r -y --os=ubuntu:xenial
	$ catkin_make_isolated --install --use-ninja

```
	2. Launch the Cartographer SLAM node.

```
	$ source ~/catkin_ws/install_isolated/setup.bash
	$ roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=cartographer

```
* **Hector** ([ROS WIKI](http://wiki.ros.org/hector_slam "http://wiki.ros.org/hector_slam"), [Github](https://github.com/tu-darmstadt-ros-pkg/hector_slam "https://github.com/tu-darmstadt-ros-pkg/hector_slam"))
	1. Install dependent packages on PC.

```
	$ sudo apt-get install ros-kinetic-hector-mapping

```
	2. Launch the Hector SLAM node.

```
	$ roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=hector

```
* **Karto** ([ROS WIKI](http://wiki.ros.org/slam_karto "http://wiki.ros.org/slam_karto"), [Github](https://github.com/ros-perception/slam_karto "https://github.com/ros-perception/slam_karto"))
	1. Install dependent packages on PC.

```
	$ sudo apt-get install ros-kinetic-slam-karto

```
	2. Launch the Karto SLAM node.

```
	$ roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=karto

```
* **Frontier Exploration** ([ROS WIKI](http://wiki.ros.org/frontier_exploration "http://wiki.ros.org/frontier_exploration"), [Github](https://github.com/paulbovbel/frontier_exploration "https://github.com/paulbovbel/frontier_exploration"))  

Frontier Exploration uses gmapping, and the following packages should be installed.
	1. Install dependent packages on PC.

```
	$ sudo apt-get install ros-kinetic-frontier-exploration ros-kinetic-navigation-stage

```
	2. Launch the Frontier Exploration SLAM node.

```
	$ roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=frontier_exploration

```

1. Run roscore from Remote PC.

```
$ roscore

```
2. If the `Bringup` is not running on the TurtleBot3 SBC, launch the Bringup. **Skip this step if you have launched bringup previously**.
	* Open a new terminal from Remote PC with `Ctrl` + `Alt` + `T` and connect to Raspberry Pi with its IP address.
	The default password is **turtlebot**.

```
	$ ssh pi@{IP_ADDRESS_OF_RASPBERRY_PI}
	$ roslaunch turtlebot3_bringup turtlebot3_robot.launch

```
3. Open a new terminal from Remote PC with `Ctrl` + `Alt` + `T` and launch the SLAM node. The Gmapping is used as a default SLAM method.

```
$ export TURTLEBOT3\_MODEL=${TB3\_MODEL}
$ roslaunch turtlebot3_slam turtlebot3_slam.launch

```

![](/assets/images/icon_unfold.png) **How to save the TURTLEBOT3\_MODEL parameter?**

The `$ export TURTLEBOT3_MODEL=${TB3_MODEL}` command can be omitted if the **TURTLEBOT3\_MODEL** parameter is predefined in the `.bashrc` file.  

The `.bashrc` file is automatically loaded when a terminal window is created.

* Example of defining `TurtlBot3 Burger` as a default model.

```
$ echo 'export TURTLEBOT3\_MODEL=burger' >> ~/.bashrc
$ source ~/.bashrc

```
* Example of defining `TurtlBot3 Waffle Pi` as a default model.

```
$ echo 'export TURTLEBOT3\_MODEL=waffle\_pi' >> ~/.bashrc
$ source ~/.bashrc

```

![](/assets/images/icon_unfold.png) Read more about **other SLAM methods**

* **Gmapping** ([ROS WIKI](http://wiki.ros.org/gmapping "http://wiki.ros.org/gmapping"), [Github](https://github.com/ros-perception/slam_gmapping "https://github.com/ros-perception/slam_gmapping"))
	1. Install dependent packages on PC.  

	 Packages related to Gmapping have already been installed on [PC Setup](/docs/en/platform/turtlebot3/quick-start "/docs/en/platform/turtlebot3/quick-start") section.
	2. Launch the Gmapping SLAM node.

```
	$ roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping

```
* **Cartographer** ([ROS WIKI](http://wiki.ros.org/cartographer "http://wiki.ros.org/cartographer"), [Github](https://github.com/googlecartographer/cartographer "https://github.com/googlecartographer/cartographer"))
	1. Download and build packages on PC.  

	Please refer to [official wiki page](https://google-cartographer-ros.readthedocs.io/en/latest/#building-installation "https://google-cartographer-ros.readthedocs.io/en/latest/#building-installation") for more detailed installation instructions.

```
	$ sudo apt-get update
	$ sudo apt-get install -y python-wstool python-rosdep ninja-build stow
	$ mkdir ~/catkin_ws && cd ~/catkin_ws
	$ wstool init src
	$ wstool merge -t src https://raw.githubusercontent.com/cartographer-project/cartographer_ros/master/cartographer_ros.rosinstall
	$ wstool update -t src
	$ sudo rosdep init
	$ rosdep update
	$ rosdep install --from-paths src --ignore-src --rosdistro=melodic -y
	$ src/cartographer/scripts/install_abseil.sh
	$ catkin_make_isolated --install --use-ninja

```
	2. Launch the Cartographer SLAM node.

```
	$ source ~/catkin_ws/install_isolated/setup.bash
	$ roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=cartographer

```
* **Hector** ([ROS WIKI](http://wiki.ros.org/hector_slam "http://wiki.ros.org/hector_slam"), [Github](https://github.com/tu-darmstadt-ros-pkg/hector_slam "https://github.com/tu-darmstadt-ros-pkg/hector_slam"))
	1. Install dependent packages on PC.

```
	$ sudo apt-get install ros-melodic-hector-mapping

```
	2. Launch the Hector SLAM node.

```
	$ roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=hector

```
* **Karto** ([ROS WIKI](http://wiki.ros.org/slam_karto "http://wiki.ros.org/slam_karto"), [Github](https://github.com/ros-perception/slam_karto "https://github.com/ros-perception/slam_karto"))
	1. Install dependent packages on PC.

```
	$ sudo apt-get install ros-melodic-slam-karto

```
	2. Launch the Karto SLAM node.

```
	$ roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=karto

```

1. Run roscore from Remote PC.

```
$ roscore

```
2. If the `Bringup` is not running on the TurtleBot3 SBC, launch the Bringup. **Skip this step if you have launched bringup previously**.
	* Open a new terminal from Remote PC with `Ctrl` + `Alt` + `T` and connect to Raspberry Pi with its IP address.
	The default password is **turtlebot**. Please use the proper keyword among `burger`, `waffle`, `waffle_pi` for the `TURTLEBOT3_MODEL` parameter.

```
	$ ssh pi@{IP_ADDRESS_OF_RASPBERRY_PI}
	$ export TURTLEBOT3\_MODEL=${TB3\_MODEL}
	$ roslaunch turtlebot3_bringup turtlebot3_robot.launch

```
3. Open a new terminal from Remote PC with `Ctrl` + `Alt` + `T` and launch the SLAM node. The Gmapping is used as a default SLAM method.
 Please use the proper keyword among `burger`, `waffle`, `waffle_pi` for the `TURTLEBOT3_MODEL` parameter.

```
$ export TURTLEBOT3\_MODEL=burger
$ roslaunch turtlebot3_slam turtlebot3_slam.launch

```

![](/assets/images/icon_unfold.png) **How to save the TURTLEBOT3\_MODEL parameter?**

The `$ export TURTLEBOT3_MODEL=${TB3_MODEL}` command can be omitted if the **TURTLEBOT3\_MODEL** parameter is predefined in the `.bashrc` file.  

The `.bashrc` file is automatically loaded when a terminal window is created.

* Example of defining `TurtlBot3 Burger` as a default model.

```
$ echo 'export TURTLEBOT3\_MODEL=burger' >> ~/.bashrc
$ source ~/.bashrc

```
* Example of defining `TurtlBot3 Waffle Pi` as a default model.

```
$ echo 'export TURTLEBOT3\_MODEL=waffle\_pi' >> ~/.bashrc
$ source ~/.bashrc

```

![](/assets/images/icon_unfold.png) Read more about **other SLAM methods**

* **Gmapping** ([ROS WIKI](http://wiki.ros.org/gmapping "http://wiki.ros.org/gmapping"), [Github](https://github.com/ros-perception/slam_gmapping "https://github.com/ros-perception/slam_gmapping"))
	1. Install dependent packages on PC.  

	 Packages related to Gmapping have already been installed on [PC Setup](/docs/en/platform/turtlebot3/quick-start "/docs/en/platform/turtlebot3/quick-start") section.
	2. Launch the Gmapping SLAM node.

```
	$ roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping

```
* **Cartographer** ([ROS WIKI](http://wiki.ros.org/cartographer "http://wiki.ros.org/cartographer"), [Github](https://github.com/googlecartographer/cartographer "https://github.com/googlecartographer/cartographer"))
	1. Download and build packages on PC.  

	The Cartographer currently does not provide the binary installation method for ROS1 Noetic. Please download and build the source code as follows. Please refer to [official wiki page](https://google-cartographer-ros.readthedocs.io/en/latest/#building-installation "https://google-cartographer-ros.readthedocs.io/en/latest/#building-installation") for more details.

```
	$ sudo apt update
	$ sudo apt install -y python3-wstool python3-rosdep ninja-build stow
	$ cd ~/catkin_ws/src
	$ wstool init src
	$ wstool merge -t src https://raw.githubusercontent.com/cartographer-project/cartographer_ros/master/cartographer_ros.rosinstall
	$ wstool update -t src
	$ sudo rosdep init
	$ rosdep update
	$ rosdep install --from-paths src --ignore-src --rosdistro=noetic -y
	$ src/cartographer/scripts/install_abseil.sh
	$ sudo apt remove ros-noetic-abseil-cpp
	$ catkin_make_isolated --install --use-ninja

```
	2. Launch the Cartographer SLAM node.

```
	$ source ~/catkin_ws/install_isolated/setup.bash
	$ roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=cartographer

```
* **Karto** ([ROS WIKI](http://wiki.ros.org/slam_karto "http://wiki.ros.org/slam_karto"), [Github](https://github.com/ros-perception/slam_karto "https://github.com/ros-perception/slam_karto"))
	1. Install dependent packages on PC.

```
	$ sudo apt install ros-noetic-slam-karto

```
	2. Launch the Karto SLAM node.

```
	$ roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=karto

```

1. If the `Bringup` is not running on the TurtleBot3 SBC, launch the Bringup first. **Skip this step if you have launched bringup previously**.
	* Open a new terminal from Remote PC with `Ctrl` + `Alt` + `T` and connect to Raspberry Pi with its IP address.
	The default password is **ubuntu**.

```
	$ ssh ubuntu@{IP_ADDRESS_OF_RASPBERRY_PI}
	$ export TURTLEBOT3\_MODEL=${TB3\_MODEL}
	$ ros2 launch turtlebot3_bringup robot.launch.py

```
2. Open a new terminal from Remote PC with `Ctrl` + `Alt` + `T` and launch the SLAM node. The Cartographer is used as a default SLAM method.

```
$ export TURTLEBOT3\_MODEL=${TB3\_MODEL}
$ ros2 launch turtlebot3_cartographer cartographer.launch.py

```

![](/assets/images/platform/turtlebot3/ros2/platform_cartographer.png)

![](/assets/images/icon_unfold.png) **How to save the TURTLEBOT3\_MODEL parameter?**

The `$ export TURTLEBOT3_MODEL=${TB3_MODEL}` command can be omitted if the **TURTLEBOT3\_MODEL** parameter is predefined in the `.bashrc` file.  

The `.bashrc` file is automatically loaded when a terminal window is created.

* Example of defining `TurtlBot3 Burger` as a default model.

```
$ echo 'export TURTLEBOT3\_MODEL=burger' >> ~/.bashrc
$ source ~/.bashrc

```
* Example of defining `TurtlBot3 Waffle Pi` as a default model.

```
$ echo 'export TURTLEBOT3\_MODEL=waffle\_pi' >> ~/.bashrc
$ source ~/.bashrc

```

1. If the `Bringup` is not running on the TurtleBot3 SBC, launch the Bringup first. **Skip this step if you have launched bringup previously**.
	* Open a new terminal from Remote PC with `Ctrl` + `Alt` + `T` and connect to Raspberry Pi with its IP address.
	The default password is **ubuntu**.

```
	$ ssh ubuntu@{IP_ADDRESS_OF_RASPBERRY_PI}

```

	Please use the proper keyword among `burger`, `waffle`, `waffle_pi` for the `TURTLEBOT3_MODEL` parameter.

```
	$ export TURTLEBOT3\_MODEL=burger
	$ ros2 launch turtlebot3_bringup robot.launch.py

```
2. Open a new terminal from Remote PC with `Ctrl` + `Alt` + `T` and launch the SLAM node. The Cartographer is used as a default SLAM method.

```
$ export TURTLEBOT3\_MODEL=burger
$ ros2 launch turtlebot3_cartographer cartographer.launch.py

```

![](/assets/images/platform/turtlebot3/ros2/platform_cartographer.png)

![](/assets/images/icon_unfold.png) **How to save the TURTLEBOT3\_MODEL parameter?**

The `$ export TURTLEBOT3_MODEL=${TB3_MODEL}` command can be omitted if the **TURTLEBOT3\_MODEL** parameter is predefined in the `.bashrc` file.  

The `.bashrc` file is automatically loaded when a terminal window is created.

* Example of defining `TurtlBot3 Burger` as a default model.

```
$ echo 'export TURTLEBOT3\_MODEL=burger' >> ~/.bashrc
$ source ~/.bashrc

```
* Example of defining `TurtlBot3 Waffle Pi` as a default model.

```
$ echo 'export TURTLEBOT3\_MODEL=waffle\_pi' >> ~/.bashrc
$ source ~/.bashrc

```

1. If the `Bringup` is not running on the TurtleBot3 SBC, launch the Bringup first. **Skip this step if you have launched bringup previously**.
	* Open a new terminal from Remote PC with `Ctrl` + `Alt` + `T` and connect to Raspberry Pi with its IP address.
	The default password is **ubuntu**.

```
	$ ssh ubuntu@{IP_ADDRESS_OF_RASPBERRY_PI}

```

	Please use the proper keyword among `burger`, `waffle`, `waffle_pi` for the `TURTLEBOT3_MODEL` parameter.

```
	$ export TURTLEBOT3\_MODEL=burger
	$ ros2 launch turtlebot3_bringup robot.launch.py

```
2. Open a new terminal from Remote PC with `Ctrl` + `Alt` + `T` and launch the SLAM node. The Cartographer is used as a default SLAM method.

```
$ export TURTLEBOT3\_MODEL=burger
$ ros2 launch turtlebot3_cartographer cartographer.launch.py

```

![](/assets/images/platform/turtlebot3/ros2/platform_cartographer.png)

![](/assets/images/icon_unfold.png) **How to save the TURTLEBOT3\_MODEL parameter?**

The `$ export TURTLEBOT3_MODEL=${TB3_MODEL}` command can be omitted if the **TURTLEBOT3\_MODEL** parameter is predefined in the `.bashrc` file.  

The `.bashrc` file is automatically loaded when a terminal window is created.

* Example of defining `TurtlBot3 Burger` as a default model.

```
$ echo 'export TURTLEBOT3\_MODEL=burger' >> ~/.bashrc
$ source ~/.bashrc

```
* Example of defining `TurtlBot3 Waffle Pi` as a default model.

```
$ echo 'export TURTLEBOT3\_MODEL=waffle\_pi' >> ~/.bashrc
$ source ~/.bashrc

```

1. If the `Bringup` is not running on the TurtleBot3, launch the Bringup. **Skip this step if you have launched bringup previously**.

```
> roslaunch turtlebot3_bringup turtlebot3_robot.launch

```
2. Open a new terminal from Remote PC and launch the SLAM node. The Gmapping is used as a default SLAM method.
 Please use the proper keyword among `burger`, `waffle`, `waffle_pi` for the `TURTLEBOT3_MODEL` parameter.

```
> set TURTLEBOT3\_MODEL=waffle
> roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping

```

![](/assets/images/icon_unfold.png) Read more about **other SLAM methods**

* **Cartographer** ([ROS WIKI](http://wiki.ros.org/cartographer "http://wiki.ros.org/cartographer"), [Github](https://github.com/googlecartographer/cartographer "https://github.com/googlecartographer/cartographer"))
	1. Install dependent packages on PC using choco.

```
	> choco upgrade ros-melodic-cartographer_ros -y

```
	2. Launch the Cartographer SLAM node.  

	Please use the proper keyword among `burger`, `waffle`, `waffle_pi` for the `TURTLEBOT3_MODEL` parameter.

```
	> c:\ws\turtlebot3\devel\setup.bat
	> set TURTLEBOT3_MODEL=waffle
	> roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=cartographer

```

## [Run Teleoperation Node](#run-teleoperation-node "#run-teleoperation-node")

Once SLAM node is successfully up and running, TurtleBot3 will be exploring unknown area of the map using teleoperation. It is important to avoid vigorous movements such as changing the linear and angular speed too quickly. When building a map using the TurtleBot3, it is a good practice to scan every corner of the map.

1. Open a new terminal and run the teleoperation node from the Remote PC.  

 Please use the proper keyword among `burger`, `waffle`, `waffle_pi` for the `TURTLEBOT3_MODEL` parameter.

```
$ export TURTLEBOT3\_MODEL=burger
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

 Control Your TurtleBot3!
 ---------------------------
 Moving around:
        w
   a    s    d
        x

 w/x : increase/decrease linear velocity
 a/d : increase/decrease angular velocity
 space key, s : force stop

 CTRL-C to quit

```
2. Start exploring and drawing the map.  

![](/assets/images/platform/turtlebot3/slam/slam_running_for_mapping.png)

Once SLAM node is successfully up and running, TurtleBot3 will be exploring unknown area of the map using teleoperation. It is important to avoid vigorous movements such as changing the linear and angular speed too quickly. When building a map using the TurtleBot3, it is a good practice to scan every corner of the map.

1. Open a new terminal and run the teleoperation node from the Remote PC.  

 Please use the proper keyword among `burger`, `waffle`, `waffle_pi` for the `TURTLEBOT3_MODEL` parameter.

```
$ export TURTLEBOT3\_MODEL=burger
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

 Control Your TurtleBot3!
 ---------------------------
 Moving around:
        w
   a    s    d
        x

 w/x : increase/decrease linear velocity
 a/d : increase/decrease angular velocity
 space key, s : force stop

 CTRL-C to quit

```
2. Start exploring and drawing the map.  

![](/assets/images/platform/turtlebot3/slam/slam_running_for_mapping.png)

Once SLAM node is successfully up and running, TurtleBot3 will be exploring unknown area of the map using teleoperation. It is important to avoid vigorous movements such as changing the linear and angular speed too quickly. When building a map using the TurtleBot3, it is a good practice to scan every corner of the map.

1. Open a new terminal and run the teleoperation node from the Remote PC.  

 Please use the proper keyword among `burger`, `waffle`, `waffle_pi` for the `TURTLEBOT3_MODEL` parameter.

```
$ export TURTLEBOT3\_MODEL=burger
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

 Control Your TurtleBot3!
 ---------------------------
 Moving around:
        w
   a    s    d
        x

 w/x : increase/decrease linear velocity
 a/d : increase/decrease angular velocity
 space key, s : force stop

 CTRL-C to quit

```
2. Start exploring and drawing the map.  

![](/assets/images/platform/turtlebot3/slam/slam_running_for_mapping.png)

Once SLAM node is successfully up and running, TurtleBot3 will be exploring unknown area of the map using teleoperation. It is important to avoid vigorous movements such as changing the linear and angular speed too quickly. When building a map using the TurtleBot3, it is a good practice to scan every corner of the map.

1. Open a new terminal and run the teleoperation node from the Remote PC.  

 Please use the proper keyword among `burger`, `waffle`, `waffle_pi` for the `TURTLEBOT3_MODEL` parameter.

```
$ export TURTLEBOT3\_MODEL=burger
$ ros2 run turtlebot3_teleop teleop_keyboard

Control Your TurtleBot3!
---------------------------
Moving around:
       w
  a    s    d
       x

w/x : increase/decrease linear velocity
a/d : increase/decrease angular velocity
space key, s : force stop

CTRL-C to quit

```
2. Start exploring and drawing the map.  

![](/assets/images/platform/turtlebot3/slam/slam_running_for_mapping.png)

Once SLAM node is successfully up and running, TurtleBot3 will be exploring unknown area of the map using teleoperation. It is important to avoid vigorous movements such as changing the linear and angular speed too quickly. When building a map using the TurtleBot3, it is a good practice to scan every corner of the map.

1. Open a new terminal and run the teleoperation node from the Remote PC.  

 Please use the proper keyword among `burger`, `waffle`, `waffle_pi` for the `TURTLEBOT3_MODEL` parameter.

```
$ export TURTLEBOT3\_MODEL=burger
$ ros2 run turtlebot3_teleop teleop_keyboard

Control Your TurtleBot3!
---------------------------
Moving around:
       w
  a    s    d
       x

w/x : increase/decrease linear velocity
a/d : increase/decrease angular velocity
space key, s : force stop

CTRL-C to quit

```
2. Start exploring and drawing the map.  

![](/assets/images/platform/turtlebot3/slam/slam_running_for_mapping.png)

Once SLAM node is successfully up and running, TurtleBot3 will be exploring unknown area of the map using teleoperation. It is important to avoid vigorous movements such as changing the linear and angular speed too quickly. When building a map using the TurtleBot3, it is a good practice to scan every corner of the map.

1. Open a new terminal and run the teleoperation node from the Remote PC.  

 Please use the proper keyword among `burger`, `waffle`, `waffle_pi` for the `TURTLEBOT3_MODEL` parameter.

```
$ export TURTLEBOT3\_MODEL=burger
$ ros2 run turtlebot3_teleop teleop_keyboard

Control Your TurtleBot3!
---------------------------
Moving around:
       w
  a    s    d
       x

w/x : increase/decrease linear velocity
a/d : increase/decrease angular velocity
space key, s : force stop

CTRL-C to quit

```
2. Start exploring and drawing the map.  

![](/assets/images/platform/turtlebot3/slam/slam_running_for_mapping.png)

Once SLAM node is successfully up and running, TurtleBot3 will be exploring unknown area of the map using teleoperation. It is important to avoid vigorous movements such as changing the linear and angular speed too quickly. When building a map using the TurtleBot3, it is a good practice to scan every corner of the map.

1. Open a new terminal and run the teleoperation node from the PC.  

 Please use the proper keyword among `burger`, `waffle`, `waffle_pi` for the `TURTLEBOT3_MODEL` parameter.

```
> set TURTLEBOT3\_MODEL=waffle
> roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

 Control Your TurtleBot3!
 ---------------------------
 Moving around:
        w
   a    s    d
        x

 w/x : increase/decrease linear velocity
 a/d : increase/decrease angular velocity
 space key, s : force stop

 CTRL-C to quit

```
2. Start exploring and drawing the map.  

![](/assets/images/platform/turtlebot3/slam/slam_running_for_mapping.png)

## [Tuning Guide](#tuning-guide "#tuning-guide")

Gmapping has many parameters to change performances for different environments. You can get an information about whole parameters in [ROS WiKi](http://wiki.ros.org/gmapping "http://wiki.ros.org/gmapping") or refer to the Chapter 11 of [ROS Robot Programming](https://community.robotsource.org/t/download-the-ros-robot-programming-book-for-free/51 "https://community.robotsource.org/t/download-the-ros-robot-programming-book-for-free/51").
This tuning guide provides tips when configuring gmapping parameters. If you want to optimize SLAM performances for your environments, this section might be helpful.

Below parameters are defined in `turtlebot3_slam/config/gmapping_params.yaml` file.

### maxUrange

This parameter is set the maximum usable range of the lidar sensor.

### map\_update\_interval

This parameter defines time between updating the map.  

The smaller the value, the more frequent the map is updated.  

However, setting this too small will be require more processing power for the map calculation. 
Set this parameter depending on the map environment.

![](/assets/images/platform/turtlebot3/slam/tuning_map_update_interval.png)

### minimumScore

This parameter sets the minimum score value that determines the success or failure of the sensor’s scan data matching test. 
This can reduce errors in the expected position of the robot in a large area. 
If the parameter is set properly, you will see information similar to one shown below.

```
Average Scan Matching Score=278.965
neff= 100
Registering Scans:Done
update frame 6
update ld=2.95935e-05 ad=0.000302522
Laser Pose= -0.0320253 -5.36882e-06 -3.14142

```

If set too high, you might see below warnings.

```
Scan Matching Failed, using odometry. Likelihood=0
lp:-0.0306155 5.75314e-06 -3.14151
op:-0.0306156 5.90277e-06 -3.14151

```

### linearUpdate

When the robot translates longer distance than this value, it will run the scan process.

### angularUpdate

When the robot rotates more than this value, it will run the scan process. It is recommended to
set this value less than linearUpdate.

Gmapping has many parameters to change performances for different environments. You can get an information about whole parameters in [ROS WiKi](http://wiki.ros.org/gmapping "http://wiki.ros.org/gmapping") or refer to the Chapter 11 of [ROS Robot Programming](https://community.robotsource.org/t/download-the-ros-robot-programming-book-for-free/51 "https://community.robotsource.org/t/download-the-ros-robot-programming-book-for-free/51").
This tuning guide provides tips when configuring gmapping parameters. If you want to optimize SLAM performances for your environments, this section might be helpful.

Below parameters are defined in `turtlebot3_slam/config/gmapping_params.yaml` file.

### maxUrange

This parameter is set the maximum usable range of the lidar sensor.

### map\_update\_interval

This parameter defines time between updating the map.  

The smaller the value, the more frequent the map is updated.  

However, setting this too small will be require more processing power for the map calculation. 
Set this parameter depending on the map environment.

![](/assets/images/platform/turtlebot3/slam/tuning_map_update_interval.png)

### minimumScore

This parameter sets the minimum score value that determines the success or failure of the sensor’s scan data matching test. 
This can reduce errors in the expected position of the robot in a large area. 
If the parameter is set properly, you will see information similar to one shown below.

```
Average Scan Matching Score=278.965
neff= 100
Registering Scans:Done
update frame 6
update ld=2.95935e-05 ad=0.000302522
Laser Pose= -0.0320253 -5.36882e-06 -3.14142

```

If set too high, you might see below warnings.

```
Scan Matching Failed, using odometry. Likelihood=0
lp:-0.0306155 5.75314e-06 -3.14151
op:-0.0306156 5.90277e-06 -3.14151

```

### linearUpdate

When the robot translates longer distance than this value, it will run the scan process.

### angularUpdate

When the robot rotates more than this value, it will run the scan process. It is recommended to
set this value less than linearUpdate.

Gmapping has many parameters to change performances for different environments. You can get an information about whole parameters in [ROS WiKi](http://wiki.ros.org/gmapping "http://wiki.ros.org/gmapping") or refer to the Chapter 11 of [ROS Robot Programming](https://community.robotsource.org/t/download-the-ros-robot-programming-book-for-free/51 "https://community.robotsource.org/t/download-the-ros-robot-programming-book-for-free/51").
This tuning guide provides tips when configuring gmapping parameters. If you want to optimize SLAM performances for your environments, this section might be helpful.

Below parameters are defined in `turtlebot3_slam/config/gmapping_params.yaml` file.

### maxUrange

This parameter is set the maximum usable range of the lidar sensor.

### map\_update\_interval

This parameter defines time between updating the map.  

The smaller the value, the more frequent the map is updated.  

However, setting this too small will be require more processing power for the map calculation. 
Set this parameter depending on the map environment.

![](/assets/images/platform/turtlebot3/slam/tuning_map_update_interval.png)

### minimumScore

This parameter sets the minimum score value that determines the success or failure of the sensor’s scan data matching test. 
This can reduce errors in the expected position of the robot in a large area. 
If the parameter is set properly, you will see information similar to one shown below.

```
Average Scan Matching Score=278.965
neff= 100
Registering Scans:Done
update frame 6
update ld=2.95935e-05 ad=0.000302522
Laser Pose= -0.0320253 -5.36882e-06 -3.14142

```

If set too high, you might see below warnings.

```
Scan Matching Failed, using odometry. Likelihood=0
lp:-0.0306155 5.75314e-06 -3.14151
op:-0.0306156 5.90277e-06 -3.14151

```

### linearUpdate

When the robot translates longer distance than this value, it will run the scan process.

### angularUpdate

When the robot rotates more than this value, it will run the scan process. It is recommended to
set this value less than linearUpdate.

The SLAM in ROS2 uses Cartographer ROS which provides configuration options via `Lua` file.

Below options are defined in `turtlebot3_cartographer/config/turtlebot3_lds_2d.lua` file.
For more details about each options, please refer to [the Cartographer ROS official documentation](https://google-cartographer-ros.readthedocs.io/en/latest/algo_walkthrough.html "https://google-cartographer-ros.readthedocs.io/en/latest/algo_walkthrough.html").

### MAP\_BUILDER.use\_trajectory\_builder\_2d

This option sets the type of SLAM.

### TRAJECTORY\_BUILDER\_2D.min\_range

This option sets the minimum usable range of the lidar sensor.

### TRAJECTORY\_BUILDER\_2D.max\_range

This option sets the maximum usable range of the lidar sensor.

### TRAJECTORY\_BUILDER\_2D.missing\_data\_ray\_length

In 2D, Cartographer replaces ranges further than max\_range with ***TRAJECTORY\_BUILDER\_2D.missing\_data\_ray\_length***.

### TRAJECTORY\_BUILDER\_2D.use\_imu\_data

If you use 2D SLAM, range data can be handled in real-time without an additional source of information so you can choose whether you’d like Cartographer to use an IMU or not.

### TRAJECTORY\_BUILDER\_2D.use\_online\_correlative\_scan\_matching

**Local SLAM** : The ***RealTimeCorrelativeScanMatcher*** can be toggled depending on the reliability of the sensor.

### TRAJECTORY\_BUILDER\_2D.motion\_filter.max\_angle\_radians

**Local SLAM** : To avoid inserting too many scans per submaps, A scan is dropped if the motion does not exceed a certain angle.

### POSE\_GRAPH.optimize\_every\_n\_nodes

**Global SLAM** : Setting POSE\_GRAPH.optimize\_every\_n\_nodes to 0 is a handy way to disable global SLAM and concentrate on the behavior of local SLAM.

### POSE\_GRAPH.constraint\_builder.min\_score

**Global SLAM** : Threshold for the scan match score below which a match is not considered. Low scores indicate that the scan and map do not look similar.

### POSE\_GRAPH.constraint\_builder.global\_localization\_min\_score

**Global SLAM** : Threshold below which global localizations are not trusted.

**NOTE**: Constraints can be visualized in RViz, it is very handy to tune global SLAM. One can also toggle POSE\_GRAPH.constraint\_builder.log\_matches to get regular reports of the constraints builder formatted as histograms.

The SLAM in ROS2 uses Cartographer ROS which provides configuration options via `Lua` file.

Below options are defined in `turtlebot3_cartographer/config/turtlebot3_lds_2d.lua` file.
For more details about each options, please refer to [the Cartographer ROS official documentation](https://google-cartographer-ros.readthedocs.io/en/latest/algo_walkthrough.html "https://google-cartographer-ros.readthedocs.io/en/latest/algo_walkthrough.html").

### MAP\_BUILDER.use\_trajectory\_builder\_2d

This option sets the type of SLAM.

### TRAJECTORY\_BUILDER\_2D.min\_range

This option sets the minimum usable range of the lidar sensor.

### TRAJECTORY\_BUILDER\_2D.max\_range

This option sets the maximum usable range of the lidar sensor.

### TRAJECTORY\_BUILDER\_2D.missing\_data\_ray\_length

In 2D, Cartographer replaces ranges further than max\_range with ***TRAJECTORY\_BUILDER\_2D.missing\_data\_ray\_length***.

### TRAJECTORY\_BUILDER\_2D.use\_imu\_data

If you use 2D SLAM, range data can be handled in real-time without an additional source of information so you can choose whether you’d like Cartographer to use an IMU or not.

### TRAJECTORY\_BUILDER\_2D.use\_online\_correlative\_scan\_matching

**Local SLAM** : The ***RealTimeCorrelativeScanMatcher*** can be toggled depending on the reliability of the sensor.

### TRAJECTORY\_BUILDER\_2D.motion\_filter.max\_angle\_radians

**Local SLAM** : To avoid inserting too many scans per submaps, A scan is dropped if the motion does not exceed a certain angle.

### POSE\_GRAPH.optimize\_every\_n\_nodes

**Global SLAM** : Setting POSE\_GRAPH.optimize\_every\_n\_nodes to 0 is a handy way to disable global SLAM and concentrate on the behavior of local SLAM.

### POSE\_GRAPH.constraint\_builder.min\_score

**Global SLAM** : Threshold for the scan match score below which a match is not considered. Low scores indicate that the scan and map do not look similar.

### POSE\_GRAPH.constraint\_builder.global\_localization\_min\_score

**Global SLAM** : Threshold below which global localizations are not trusted.

**NOTE**: Constraints can be visualized in RViz, it is very handy to tune global SLAM. One can also toggle POSE\_GRAPH.constraint\_builder.log\_matches to get regular reports of the constraints builder formatted as histograms.

The SLAM in ROS2 uses Cartographer ROS which provides configuration options via `Lua` file.

Below options are defined in `turtlebot3_cartographer/config/turtlebot3_lds_2d.lua` file.
For more details about each options, please refer to [the Cartographer ROS official documentation](https://google-cartographer-ros.readthedocs.io/en/latest/algo_walkthrough.html "https://google-cartographer-ros.readthedocs.io/en/latest/algo_walkthrough.html").

### MAP\_BUILDER.use\_trajectory\_builder\_2d

This option sets the type of SLAM.

### TRAJECTORY\_BUILDER\_2D.min\_range

This option sets the minimum usable range of the lidar sensor.

### TRAJECTORY\_BUILDER\_2D.max\_range

This option sets the maximum usable range of the lidar sensor.

### TRAJECTORY\_BUILDER\_2D.missing\_data\_ray\_length

In 2D, Cartographer replaces ranges further than max\_range with ***TRAJECTORY\_BUILDER\_2D.missing\_data\_ray\_length***.

### TRAJECTORY\_BUILDER\_2D.use\_imu\_data

If you use 2D SLAM, range data can be handled in real-time without an additional source of information so you can choose whether you’d like Cartographer to use an IMU or not.

### TRAJECTORY\_BUILDER\_2D.use\_online\_correlative\_scan\_matching

**Local SLAM** : The ***RealTimeCorrelativeScanMatcher*** can be toggled depending on the reliability of the sensor.

### TRAJECTORY\_BUILDER\_2D.motion\_filter.max\_angle\_radians

**Local SLAM** : To avoid inserting too many scans per submaps, A scan is dropped if the motion does not exceed a certain angle.

### POSE\_GRAPH.optimize\_every\_n\_nodes

**Global SLAM** : Setting POSE\_GRAPH.optimize\_every\_n\_nodes to 0 is a handy way to disable global SLAM and concentrate on the behavior of local SLAM.

### POSE\_GRAPH.constraint\_builder.min\_score

**Global SLAM** : Threshold for the scan match score below which a match is not considered. Low scores indicate that the scan and map do not look similar.

### POSE\_GRAPH.constraint\_builder.global\_localization\_min\_score

**Global SLAM** : Threshold below which global localizations are not trusted.

**NOTE**: Constraints can be visualized in RViz, it is very handy to tune global SLAM. One can also toggle POSE\_GRAPH.constraint\_builder.log\_matches to get regular reports of the constraints builder formatted as histograms.

Gmapping has many parameters to change performances for different environments. You can get an information about whole parameters in [ROS WiKi](http://wiki.ros.org/gmapping "http://wiki.ros.org/gmapping") or refer to the Chapter 11 of [ROS Robot Programming](https://community.robotsource.org/t/download-the-ros-robot-programming-book-for-free/51 "https://community.robotsource.org/t/download-the-ros-robot-programming-book-for-free/51").
This tuning guide provides tips when configuring gmapping parameters. If you want to optimize SLAM performances for your environments, this section might be helpful.

Below parameters are defined in `turtlebot3_slam/config/gmapping_params.yaml` file.

### maxUrange

This parameter is set the maximum usable range of the lidar sensor.

### map\_update\_interval

This parameter defines time between updating the map.  

The smaller the value, the more frequent the map is updated.  

However, setting this too small will be require more processing power for the map calculation. 
Set this parameter depending on the map environment.

![](/assets/images/platform/turtlebot3/slam/tuning_map_update_interval.png)

### minimumScore

This parameter sets the minimum score value that determines the success or failure of the sensor’s scan data matching test. 
This can reduce errors in the expected position of the robot in a large area. 
If the parameter is set properly, you will see information similar to one shown below.

```
Average Scan Matching Score=278.965
neff= 100
Registering Scans:Done
update frame 6
update ld=2.95935e-05 ad=0.000302522
Laser Pose= -0.0320253 -5.36882e-06 -3.14142

```

If set too high, you might see below warnings.

```
Scan Matching Failed, using odometry. Likelihood=0
lp:-0.0306155 5.75314e-06 -3.14151
op:-0.0306156 5.90277e-06 -3.14151

```

### linearUpdate

When the robot translates longer distance than this value, it will run the scan process.

### angularUpdate

When the robot rotates more than this value, it will run the scan process. It is recommended to
set this value less than linearUpdate.

## [Save Map](#save-map "#save-map")

The map is drawn based on the robot’s [odometry](https://en.wikipedia.org/wiki/Odometry "https://en.wikipedia.org/wiki/Odometry"), [tf](http://wiki.ros.org/tf "http://wiki.ros.org/tf") and scan information. 
These map data is drawn in the RViz window as the TurtleBot3 was traveling. 
After creating a complete map of desired area, save the map data to the local drive for the later use.

1. Launch the **map\_saver** node in the map\_server package to create map files.  

 The map file is saved in the directory where the map\_saver node is launched at.  

 Unless a specific file name is provided, `map` will be used as a default file name and create `map.pgm` and `map.yaml`.

```
$ rosrun map_server map_saver -f ~/map

```

The `-f` option specifies a folder location and a file name where files to be saved.  

With the above command, `map.pgm` and `map.yaml` will be saved in the home folder `~/`(/home/${username}).

The map is drawn based on the robot’s [odometry](https://en.wikipedia.org/wiki/Odometry "https://en.wikipedia.org/wiki/Odometry"), [tf](http://wiki.ros.org/tf "http://wiki.ros.org/tf") and scan information. 
These map data is drawn in the RViz window as the TurtleBot3 was traveling. 
After creating a complete map of desired area, save the map data to the local drive for the later use.

1. Launch the **map\_saver** node in the map\_server package to create map files.  

 The map file is saved in the directory where the map\_saver node is launched at.  

 Unless a specific file name is provided, `map` will be used as a default file name and create `map.pgm` and `map.yaml`.

```
$ rosrun map_server map_saver -f ~/map

```

The `-f` option specifies a folder location and a file name where files to be saved.  

With the above command, `map.pgm` and `map.yaml` will be saved in the home folder `~/`(/home/${username}).

The map is drawn based on the robot’s [odometry](https://en.wikipedia.org/wiki/Odometry "https://en.wikipedia.org/wiki/Odometry"), [tf](http://wiki.ros.org/tf "http://wiki.ros.org/tf") and scan information. 
These map data is drawn in the RViz window as the TurtleBot3 was traveling. 
After creating a complete map of desired area, save the map data to the local drive for the later use.

1. Launch the **map\_saver** node in the map\_server package to create map files.  

 The map file is saved in the directory where the map\_saver node is launched at.  

 Unless a specific file name is provided, `map` will be used as a default file name and create `map.pgm` and `map.yaml`.

```
$ rosrun map_server map_saver -f ~/map

```

The `-f` option specifies a folder location and a file name where files to be saved.  

With the above command, `map.pgm` and `map.yaml` will be saved in the home folder `~/`(/home/${username}).

The map is drawn based on the robot’s [odometry](https://en.wikipedia.org/wiki/Odometry "https://en.wikipedia.org/wiki/Odometry"), [tf](http://wiki.ros.org/tf "http://wiki.ros.org/tf") and scan information. 
These map data is drawn in the RViz window as the TurtleBot3 was traveling. 
After creating a complete map of desired area, save the map data to the local drive for the later use.

1. Launch the **map\_saver** node in the nav2\_map\_server package to create map files.  

 The map file is saved in the directory where the map\_saver node is launched at.  

 Unless a specific file name is provided, `map` will be used as a default file name and create `map.pgm` and `map.yaml`.

```
$ ros2 run nav2_map_server map_saver -f ~/map

```

The `-f` option specifies a folder location and a file name where files to be saved.  

With the above command, `map.pgm` and `map.yaml` will be saved in the home folder `~/`(/home/${username}).

The map is drawn based on the robot’s [odometry](https://en.wikipedia.org/wiki/Odometry "https://en.wikipedia.org/wiki/Odometry"), [tf](http://wiki.ros.org/tf "http://wiki.ros.org/tf") and scan information. 
These map data is drawn in the RViz window as the TurtleBot3 was traveling. 
After creating a complete map of desired area, save the map data to the local drive for the later use.

1. Launch the **map\_saver\_cli** node in the nav2\_map\_server package to create map files.  

 The map file is saved in the directory where the map\_saver\_cli node is launched at.  

 Unless a specific file name is provided, `map` will be used as a default file name and create `map.pgm` and `map.yaml`.

```
$ ros2 run nav2_map_server map_saver_cli -f ~/map

```

The `-f` option specifies a folder location and a file name where files to be saved.  

With the above command, `map.pgm` and `map.yaml` will be saved in the home folder `~/`(/home/${username}).

The map is drawn based on the robot’s [odometry](https://en.wikipedia.org/wiki/Odometry "https://en.wikipedia.org/wiki/Odometry"), [tf](http://wiki.ros.org/tf "http://wiki.ros.org/tf") and scan information. 
These map data is drawn in the RViz window as the TurtleBot3 was traveling. 
After creating a complete map of desired area, save the map data to the local drive for the later use.

1. Launch the **map\_saver\_cli** node in the nav2\_map\_server package to create map files.  

 The map file is saved in the directory where the map\_saver\_cli node is launched at.  

 Unless a specific file name is provided, `map` will be used as a default file name and create `map.pgm` and `map.yaml`.

```
$ ros2 run nav2_map_server map_saver_cli -f ~/map

```

The `-f` option specifies a folder location and a file name where files to be saved.  

With the above command, `map.pgm` and `map.yaml` will be saved in the home folder `~/`(/home/${username}).

The map is drawn based on the robot’s [odometry](https://en.wikipedia.org/wiki/Odometry "https://en.wikipedia.org/wiki/Odometry"), [tf](http://wiki.ros.org/tf "http://wiki.ros.org/tf") and scan information. 
These map data is drawn in the RViz window as the TurtleBot3 was traveling. 
After creating a complete map of desired area, save the map data to the local drive for the later use.

1. Launch the **map\_saver** node in the map\_server package to create map files.  

 The map file is saved in the directory where the map\_saver node is launched at.  

 Unless a specific file name is provided, `map` will be used as a default file name and create `map.pgm` and `map.yaml`.

```
> rosrun map_server map_saver -f %USERPROFILE%\map

```

The `-f` option specifies a folder location and a file name where files to be saved.  

With the above command, `map.pgm` and `map.yaml` will be saved in the user directory. The user directory is stored in an environment variable `%USERPROFILE%`

## [Map](#map "#map")

The map uses two-dimensional **Occupancy Grid Map (OGM)**, which is commonly used in ROS. 
The saved map will look like the figure below, where **white** area is collision free area while **black** area is occupied and inaccessible area, and **gray** area represents the unknown area. 
This map is used for the [Navigation](/docs/en/platform/turtlebot3/navigation/#navigation "/docs/en/platform/turtlebot3/navigation/#navigation").

![](/assets/images/platform/turtlebot3/slam/map.png)

The figure below shows the result of creating a large map using TurtleBot3. It took about an hour to create a map with a travel distance of about 350 meters.

![](/assets/images/platform/turtlebot3/slam/large_map.png)

The map uses two-dimensional **Occupancy Grid Map (OGM)**, which is commonly used in ROS. 
The saved map will look like the figure below, where **white** area is collision free area while **black** area is occupied and inaccessible area, and **gray** area represents the unknown area. 
This map is used for the [Navigation](/docs/en/platform/turtlebot3/navigation/#navigation "/docs/en/platform/turtlebot3/navigation/#navigation").

![](/assets/images/platform/turtlebot3/slam/map.png)

The figure below shows the result of creating a large map using TurtleBot3. It took about an hour to create a map with a travel distance of about 350 meters.

![](/assets/images/platform/turtlebot3/slam/large_map.png)

The map uses two-dimensional **Occupancy Grid Map (OGM)**, which is commonly used in ROS. 
The saved map will look like the figure below, where **white** area is collision free area while **black** area is occupied and inaccessible area, and **gray** area represents the unknown area. 
This map is used for the [Navigation](/docs/en/platform/turtlebot3/navigation/#navigation "/docs/en/platform/turtlebot3/navigation/#navigation").

![](/assets/images/platform/turtlebot3/slam/map.png)

The figure below shows the result of creating a large map using TurtleBot3. It took about an hour to create a map with a travel distance of about 350 meters.

The map uses two-dimensional **Occupancy Grid Map (OGM)**, which is commonly used in ROS. 
The saved map will look like the figure below, where **white** area is collision free area while **black** area is occupied and inaccessible area, and **gray** area represents the unknown area. 
This map is used for the [Navigation](/docs/en/platform/turtlebot3/navigation "/docs/en/platform/turtlebot3/navigation").

![](/assets/images/platform/turtlebot3/slam/map.png)

The figure below shows the result of creating a large map using TurtleBot3. It took about an hour to create a map with a travel distance of about 350 meters.

![](/assets/images/platform/turtlebot3/slam/large_map.png)

The map uses two-dimensional **Occupancy Grid Map (OGM)**, which is commonly used in ROS. 
The saved map will look like the figure below, where **white** area is collision free area while **black** area is occupied and inaccessible area, and **gray** area represents the unknown area. 
This map is used for the [Navigation](/docs/en/platform/turtlebot3/navigation "/docs/en/platform/turtlebot3/navigation").

![](/assets/images/platform/turtlebot3/slam/map.png)

The figure below shows the result of creating a large map using TurtleBot3. It took about an hour to create a map with a travel distance of about 350 meters.

![](/assets/images/platform/turtlebot3/slam/large_map.png)

The map uses two-dimensional **Occupancy Grid Map (OGM)**, which is commonly used in ROS. 
The saved map will look like the figure below, where **white** area is collision free area while **black** area is occupied and inaccessible area, and **gray** area represents the unknown area. 
This map is used for the [Navigation](/docs/en/platform/turtlebot3/navigation "/docs/en/platform/turtlebot3/navigation").

![](/assets/images/platform/turtlebot3/slam/map.png)

The figure below shows the result of creating a large map using TurtleBot3. It took about an hour to create a map with a travel distance of about 350 meters.

![](/assets/images/platform/turtlebot3/slam/large_map.png)

The map uses two-dimensional **Occupancy Grid Map (OGM)**, which is commonly used in ROS. 
The saved map will look like the figure below, where **white** area is collision free area while **black** area is occupied and inaccessible area, and **gray** area represents the unknown area. 
This map is used for the [Navigation](/docs/en/platform/turtlebot3/navigation/#navigation "/docs/en/platform/turtlebot3/navigation/#navigation").

![](/assets/images/platform/turtlebot3/slam/map.png)

The figure below shows the result of creating a large map using TurtleBot3. It took about an hour to create a map with a travel distance of about 350 meters.

![](/assets/images/platform/turtlebot3/slam/large_map.png)

 Previous Page
Next Page 