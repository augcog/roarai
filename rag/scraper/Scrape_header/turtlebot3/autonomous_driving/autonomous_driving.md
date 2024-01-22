
[Edit on GitHub](https://github.com/ROBOTIS-GIT/emanual/blob/master/docs/en/platform/turtlebot3/autonomous_driving/autonomous_driving.md "https://github.com/ROBOTIS-GIT/emanual/blob/master/docs/en/platform/turtlebot3/autonomous_driving/autonomous_driving.md") 

Kinetic 
Melodic
Noetic
Dashing
Foxy
Humble
Windows

![](/assets/images/platform/turtlebot3/autonomous_driving/autorace_rbiz_challenge_2017_robots_1.png)

# [Autonomous Driving](#autonomous-driving "#autonomous-driving")

**NOTE**: TurtleBot3 Autorace is only officially supported in ROS Kinetic and Noetic

**NOTE**: TurtleBot3 Autorace is only officially supported in ROS Kinetic and Noetic

**NOTE**: TurtleBot3 Autorace is only officially supported in ROS Kinetic and Noetic

**NOTE**: TurtleBot3 Autorace is only officially supported in ROS Kinetic and Noetic

**NOTE**: TurtleBot3 Autorace is only officially supported in ROS Kinetic and Noetic

## Getting Started

**NOTE**: This instructions were tested on `Ubuntu 16.04` and `ROS Kinetic Kame`.

The contents in e-Manual are subject to be updated without a prior notice. Therefore, some video may differ from the contents in e-Manual.

The following instruction describes how to build the autonomous driving TurtleBot3 on ROS by using AutoRace packages.

### [What you need for Autonomous Driving](#what-you-need-for-autonomous-driving "#what-you-need-for-autonomous-driving")

`TurtleBot3 Burger`

* It is the basic model to use AutoRace packages for the autonomous driving on ROS.
* Provided source codes, AutoRace Packages, are made based on TurtleBot3 Burger.

`Remote PC`

* It communicates with an single board computer (SBC) on Turtlebot3.
* Laptop, desktop, or other devices with ROS 1.

`Raspberry Pi camera module with a camera mount`

* You can use a different module if ROS supports it.
* Source codes provided to calibrate the camera are created based on ([Fisheye Lens](https://www.waveshare.com/rpi-camera-g.htm "https://www.waveshare.com/rpi-camera-g.htm")) module.

`AutoRace tracks and objects`

* Download 3D CAD files for AutoRace tracks, Traffic signs, traffic lights and other objects at [ROBOTIS\_GIT/autorace](https://github.com/ROBOTIS-GIT/autorace_track "https://github.com/ROBOTIS-GIT/autorace_track").
* Download a refree system at [ROBOTIS-GIT/autorace\_referee](https://github.com/ROBOTIS-GIT/autorace_referee "https://github.com/ROBOTIS-GIT/autorace_referee")

### [Install Autorace Packages](#install-autorace-packages "#install-autorace-packages")

The following instructions describes how to install packages and to calibrate camera.

1. Install AutoRace package on both `Remote PC` and `SBC`.

```
$ cd ~/catkin_ws/src/
$ git clone -b kinetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_autorace_2020.git
$ cd ~/catkin_ws && catkin_make

```
2. Install additional dependent packages on `Remote PC`.

```
$ sudo apt-get install ros-kinetic-image-transport ros-kinetic-cv-bridge ros-kinetic-vision-opencv python-opencv libopencv-dev ros-kinetic-image-proc

```
3. You need to [Calibrate a Camera on SBC](#calibrate-a-camera-on-sbc "#calibrate-a-camera-on-sbc").

## Getting Started

**NOTE**

* Autorace package is mainly developed on `Ubuntu 20.04` with `ROS1 Noetic Ninjemys`.
* Autorace package is mainly tested under the Gazebo simulation.
* To simulate given examples properly, complete [Simulation](/docs/en/platform/turtlebot3/simulation/ "/docs/en/platform/turtlebot3/simulation/").

**Tip**: If you have actual TurtleBot3, you can perform up to **[Lane Detection](#lane-detection "#lane-detection")** from our Autonomus Driving package. For more details, clcik expansion note (![](/assets/images/icon_unfold.png)**Click to expand:** ) at the end of content in each sub section.

The contents in e-Manual are subject to be updated without a prior notice. Therefore, some video may differ from the contents in e-Manual.

### [Prerequisites](#prerequisites "#prerequisites")

`Remote PC`

* ROS 1 Noetic installed Laptop or desktop PC.
* This instruction is based on Gazebo simulation, but can be ported to the actual robot later.

![](/assets/images/icon_unfold.png) **Click to expand : Prerequisites for use of actual TurtleBot3**

### [What you need for Autonomous Driving](#what-you-need-for-autonomous-driving "#what-you-need-for-autonomous-driving")

`TurtleBot3 Burger`

* It is the basic model to use AutoRace packages for the autonomous driving on ROS.
* Provided source codes, AutoRace Packages, are made based on TurtleBot3 Burger.

`Remote PC`

* It communicates with an single board computer (SBC) on Turtlebot3.
* Laptop, desktop, or other devices with ROS 1.

`Raspberry Pi camera module with a camera mount`

* You can use a different module if ROS supports it.
* Source codes provided to calibrate the camera are created based on ([Fisheye Lens](https://www.waveshare.com/rpi-camera-g.htm "https://www.waveshare.com/rpi-camera-g.htm")) module.

`AutoRace tracks and objects`

* Download 3D CAD files for AutoRace tracks, Traffic signs, traffic lights and other objects at [ROBOTIS\_GIT/autorace](https://github.com/ROBOTIS-GIT/autorace_track "https://github.com/ROBOTIS-GIT/autorace_track").
* Download a refree system at [ROBOTIS-GIT/autorace\_referee](https://github.com/ROBOTIS-GIT/autorace_referee "https://github.com/ROBOTIS-GIT/autorace_referee")

### [Install Autorace Packages](#install-autorace-packages "#install-autorace-packages")

1. Install the AutoRace 2020 meta package on `Remote PC`.

```
$ cd ~/catkin_ws/src/
$ git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_autorace_2020.git
$ cd ~/catkin_ws && catkin_make

```
2. Install additional dependent packages on `Remote PC`.

```
$ sudo apt install ros-noetic-image-transport ros-noetic-cv-bridge ros-noetic-vision-opencv python3-opencv libopencv-dev ros-noetic-image-proc

```

![](/assets/images/icon_unfold.png) **Click to expand : Autorace Package Installation for an actual TurtleBot3**

The following instructions describes how to install packages and to calibrate camera.

1. Install AutoRace package on both `Remote PC` and `SBC`.

```
$ cd ~/catkin_ws/src/
$ git clone -b feature-raspicam https://github.com/ROBOTIS-GIT/turtlebot3_autorace_2020.git
$ cd ~/catkin_ws && catkin_make

```
2. Install additional dependent packages on `SBC`.
	* Create a swap file to prevent lack of memory in building OpenCV.

```
	  $ sudo fallocate -l 4G /swapfile
	  $ sudo chmod 600 /swapfile
	  $ sudo mkswap /swapfile
	  $ sudo swapon /swapfile

```
	* Install required dependencies.

```
	  $ sudo apt-get update
	  $ sudo apt-get install build-essential cmake gcc g++ git unzip pkg-config
	  $ sudo apt-get install libjpeg-dev libpng-dev libtiff-dev libavcodec-dev libavformat-dev libswscale-dev libgtk2.0-dev libcanberra-gtk\* libxvidcore-dev libx264-dev python3-dev python3-numpy python3-pip libtbb2 libtbb-dev libdc1394-22-dev libv4l-dev v4l-utils libopenblas-dev libatlas-base-dev libblas-dev liblapack-dev gfortran libhdf5-dev libprotobuf-dev libgoogle-glog-dev libgflags-dev protobuf-compiler

```
	* Build with opencv & opencv\_contrib

```
	  $ cd ~
	  $ wget -O opencv.zip https://github.com/opencv/opencv/archive/4.5.0.zip
	  $ wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.5.0.zip

	  $ unzip opencv.zip
	  $ unzip opencv_contrib.zip

	  $ mv opencv-4.5.0 opencv
	  $ mv opencv_contrib-4.5.0 opencv_contrib

```
	* Create cmake file.

```
	  $ cd opencv
	  $ mkdir build
	  $ cd build
	  $ cmake -D CMAKE\_BUILD\_TYPE=RELEASE \
	          -D CMAKE\_INSTALL\_PREFIX=/usr/local \
	          -D OPENCV\_EXTRA\_MODULES\_PATH=~/opencv_contrib/modules \
	          -D ENABLE\_NEON=ON \
	          -D BUILD\_TIFF=ON \
	          -D WITH\_FFMPEG=ON \
	          -D WITH\_GSTREAMER=ON \
	          -D WITH\_TBB=ON \
	          -D BUILD\_TBB=ON \
	          -D BUILD\_TESTS=OFF \
	          -D WITH\_EIGEN=OFF \
	          -D WITH\_V4L=ON \
	          -D WITH\_LIBV4L=ON \
	          -D WITH\_VTK=OFF \
	          -D OPENCV\_ENABLE\_NONFREE=ON \
	          -D INSTALL\_C\_EXAMPLES=OFF \
	          -D INSTALL\_PYTHON\_EXAMPLES=OFF \
	          -D BUILD\_NEW\_PYTHON\_SUPPORT=ON \
	          -D BUILD\_opencv\_python3=TRUE \
	          -D OPENCV\_GENERATE\_PKGCONFIG=ON \
	          -D BUILD\_EXAMPLES=OFF ..

```
	* It will take an hour or two to build.

```
	  $ cd ~/opencv/build
	  $ make -j4
	  $ sudo make install
	  $ sudo ldconfig
	  $ make clean
	  $ sudo apt-get update

```
	* Turn off Raspberry Pi, take out the microSD card and edit the config.txt in system-boot section. add start\_x=1 before the enable\_uart=1 line.

```
	  $ sudo apt install ffmpeg
	  $ ffmpeg -f video4linux2 -s 640x480 -i /dev/video0 -ss 0:0:2 -frames 1 capture_test.jpg

```
	* Install additional dependent packages

```
	  $ sudo apt install ros-noetic-cv-camera

```
3. Install additional dependent packages on `Remote PC`.

```
$ sudo apt install ros-noetic-image-transport ros-noetic-image-transport-plugins ros-noetic-cv-bridge ros-noetic-vision-opencv python3-opencv libopencv-dev ros-noetic-image-proc ros-noetic-cv-camera ros-noetic-camera-calibration 

```

## [Camera Calibration](#camera-calibration "#camera-calibration")

Calibrating the camera is very important for autonomous driving. The following describes how to simply calibrate the camera step by step.

## [Camera Calibration](#camera-calibration "#camera-calibration")

Calibrating the camera is very important for autonomous driving. The following describes how to simply calibrate the camera step by step.

### [Camera Imaging Calibration](#camera-imaging-calibration "#camera-imaging-calibration")

1. Launch roscore on `Remote PC`.

```
$ roscore

```
2. Trigger the camera on `SBC`.

```
$ roslaunch turtlebot3_autorace_${Autorace\_Misson}_camera turtlebot3_autorace_camera_pi.launch

```

**WARNING**: Be sure to specify `${Autorace_Misson}` (i.e, **roslaunch turtlebot3\_autorace\_traffic\_light\_camera turtlebot3\_autorace\_camera\_pi.launch**)
3. Execute rqt\_image\_view on `Remote PC`.

```
$ rqt_image_view

```
4. Select **/camera/image/compressed** (or **/camera/image/**) topic on the check box.

![](/assets/images/platform/turtlebot3/autonomous_driving/tb3_click_compressed.png)
5. Excute rqt\_reconfigure on `Remote PC`.

```
$ rosrun rqt_reconfigure rqt_reconfigure

```
6. Click **camera**, and modify parameter value in order to see clear images from the camera.

![](/assets/images/platform/turtlebot3/autonomous_driving/rqt_reconfigure_camera_yaml_edit_01.png)
7. Open **camera.yaml** file located in **turtlebot3*autorace*[Autorace Misson]\_camera/calibration/camera\_calibration** folder.
8. Write modified values to the file.

![](/assets/images/platform/turtlebot3/autonomous_driving/rqt_reconfigure_camera_yaml_edit_02.png)

### [Camera Imaging Calibration](#camera-imaging-calibration "#camera-imaging-calibration")

Camera image calibration is not required in Gazebo Simulation.

![](/assets/images/icon_unfold.png) **Click to expand : Camera Imaging Calibration with an actual TurtleBot3**

1. Launch roscore on `Remote PC`.

```
$ roscore

```
2. Trigger the camera on `SBC`.

```
$ roslaunch turtlebot3_autorace_camera raspberry_pi_camera_publish.launch

```
3. Execute rqt\_image\_view on `Remote PC`.

```
$ rqt_image_view

```

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_rpi_rqt_image_view.png)

> 
> rqt\_image view
> 
> 
>

### [Intrinsic Camera Calibration](#intrinsic-camera-calibration "#intrinsic-camera-calibration")

Print a checkerboard on A4 size paper. The checkerboard is used for Intrinsic Camera Calibration.

* The checkerboard is stored at **turtlebot3\_autorace\_camera/data/checkerboard\_for\_calibration.pdf**
* Modify value of parameters in **turtlebot3\_autorace\_camera/launch/turtlebot3\_autorace\_intrinsic\_camera\_calibration.launch**
* For detailed information on the camera calibration, see [Camera Calibration manual](http://wiki.ros.org/camera_calibration "http://wiki.ros.org/camera_calibration") from ROS Wiki.

![](/assets/images/platform/turtlebot3/autonomous_driving/autorace_checkerboard.png)

> 
> Checkerboard
> 
> 
>

1. Launch roscore on `Remote PC`.

```
$ roscore

```
2. Trigger the camera on `SBC`.

```
$ roslaunch turtlebot3_autorace_${Autorace\_Misson}_camera turtlebot3_autorace_camera_pi.launch

```

**WARNING**: Be sure to specify `${Autorace_Misson}` (i.e, **roslaunch turtlebot3\_autorace\_traffic\_light\_camera turtlebot3\_autorace\_camera\_pi.launch**)
3. Run a intrinsic camera calibration launch file on `Remote PC`.

```
$ export AUTO\_IN\_CALIB=calibration
$ export GAZEBO\_MODE=false
$ roslaunch turtlebot3_autorace_${Autorace\_Misson}_camera turtlebot3_autorace_intrinsic_camera_calibration.launch

```
4. Use the checkerboard to calibrate the camera, and click **CALIBRATE**.

![](/assets/images/platform/turtlebot3/autonomous_driving/intrinsic_camera_calibration_test.png)
5. Click **Save** to save the intrinsic calibration data.

![](/assets/images/platform/turtlebot3/autonomous_driving/intrinsic_camera_calibration_capture.png)
6. **calibrationdata.tar.gz** folder will be created at **/tmp** folder.

![](/assets/images/platform/turtlebot3/autonomous_driving/camera_320_240_saved_path_01.png)
7. Extract **calibrationdata.tar.gz** folder, and open **ost.yaml**.

![](/assets/images/platform/turtlebot3/autonomous_driving/open_ost_yaml.png)

> 
> ost.yaml
> 
> 
> 

![](/assets/images/platform/turtlebot3/autonomous_driving/ost_yaml.png)

> 
> Intrinsic Calibration Data in ost.yaml
> 
> 
>
8. Copy and paste the data from **ost.yaml** to **camerav2\_320x240\_30fps.yaml**.

![](/assets/images/platform/turtlebot3/autonomous_driving/open_320_240_30fps.png)

> 
> camerav2\_320x240\_30fps.yaml
> 
> 
> 

![](/assets/images/platform/turtlebot3/autonomous_driving/camerav2_320_240_30fps.png)

> 
> Intrinsic Calibration Data in camerav2\_320x240\_30fps.yaml
> 
> 
>

### [Intrinsic Camera Calibration](#intrinsic-camera-calibration "#intrinsic-camera-calibration")

Intrinsic Camera Calibration is not required in Gazebo simulation.

![](/assets/images/icon_unfold.png) **Click to expand : Intrinsic Camera Calibration with an actual TurtleBot3**

Print a checkerboard on A4 size paper. The checkerboard is used for Intrinsic Camera Calibration.

* The checkerboard is stored at **turtlebot3\_autorace\_camera/data/checkerboard\_for\_calibration.pdf**
* Modify value of parameters in **turtlebot3\_autorace\_camera/launch/intrinsic\_camera\_calibration.launch**
* For detailed information on the camera calibration, see [Camera Calibration manual](http://wiki.ros.org/camera_calibration "http://wiki.ros.org/camera_calibration") from ROS Wiki.

![](/assets/images/platform/turtlebot3/autonomous_driving/autorace_checkerboard.png)

> 
> Checkerboard
> 
> 
>

1. Launch roscore on `Remote PC`.

```
$ roscore

```
2. Trigger the camera on `SBC`.

```
$ roslaunch turtlebot3_autorace_camera raspberry_pi_camera_publish.launch

```
3. Run a intrinsic camera calibration launch file on `Remote PC`.

```
$ roslaunch turtlebot3_autorace_camera intrinsic_camera_calibration.launch mode:=calibration

```
4. Use the checkerboard to calibrate the camera, and click **CALIBRATE**.

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_rpi_before_intrinsic_calibration.png)
5. Click **Save** to save the intrinsic calibration data.

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_rpi_after_intrinsic_calibration.png)
6. **calibrationdata.tar.gz** folder will be created at **/tmp** folder.

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_rpi_calibration_data_tar_gz.png)
7. Extract **calibrationdata.tar.gz** folder, and open **ost.yaml**.

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_rpi_ost_yaml_file.png)

> 
> ost.yaml
> 
> 
> 

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_rpi_ost_yaml.png)

> 
> Intrinsic Calibration Data in ost.yaml
> 
> 
>
8. Copy and paste the data from **ost.yaml** to **camerav2\_320x240\_30fps.yaml**.

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_rpi_camerav2_yaml.png)

> 
> camerav2\_320x240\_30fps.yaml
> 
> 
> 

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_rpi_camerav2_320x240.png)

> 
> Intrinsic Calibration Data in camerav2\_320x240\_30fps.yaml
> 
> 
>

### [Extrinsic Camera Calibration](#extrinsic-camera-calibration "#extrinsic-camera-calibration")

1. Launch roscore on `Remote PC`.

```
$ roscore

```
2. Trigger the camera on `SBC`.

```
$ roslaunch turtlebot3_autorace_${Autorace\_Misson}_camera turtlebot3_autorace_camera_pi.launch

```

**WARNING**: Be sure to specify `${Autorace_Misson}` (i.e, **roslaunch turtlebot3\_autorace\_traffic\_light\_camera turtlebot3\_autorace\_camera\_pi.launch**)
3. Use the command on `Remote PC`.

```
$ export AUTO\_IN\_CALIB=action
$ export GAZEBO\_MODE=false
$ roslaunch turtlebot3_autorace_${Autorace\_Misson}_camera turtlebot3_autorace_intrinsic_camera_calibration.launch

```
4. Run the extrinsic camera calibration launch file on `Remote PC`.

```
$ export AUTO\_EX\_CALIB=calibration
$ roslaunch turtlebot3_autorace_${Autorace\_Misson}_camera turtlebot3_autorace_extrinsic_camera_calibration.launch

```
5. Execute rqt on `Remote PC`.

```
$ rqt

```
6. Click **plugins** > **visualization** > **Image view**; Multiple windows will be present.
7. Select `/camera/image_extrinsic_calib/compressed` and `/camera/image_projected_compensated` topics on each monitors.

* One of two screens will show an image with a red rectangle box. The other one shows the ground projected view (Bird’s eye view).

![](/assets/images/platform/turtlebot3/autonomous_driving/camera_image_extrinsic_calib_compressed.png)

> 
> `/camera/image_extrinsic_calib/compressed` topic
> 
> 
> 

![](/assets/images/platform/turtlebot3/autonomous_driving/camera_image_projected_compensated.png)

> 
> `/camera/image_projected_compensated` topic
> 
> 
>

1. Excute rqt\_reconfigure on `Remote PC`.

```
$ rosrun rqt_reconfigure rqt_reconfigure

```
2. Adjust parameters in `/camera/image_projection` and `/camera/image_compensation_projection`.

* Change `/camera/image_projection` parameter value. It affects `/camera/image_extrinsic_calib/compressed` topic.
* Intrinsic camera calibration will transform the image surrounded by the red rectangle, and will show the image that looks from over the lane.

![](/assets/images/platform/turtlebot3/autonomous_driving/camera_image_projection_compensation_projection.png)

> 
> rqt\_reconfigure
> 
> 
> 

![](/assets/images/platform/turtlebot3/autonomous_driving/modify_image_projection_image_extrinsic_calib.png)

> 
> Result from parameter modification.
> 
> 
>

### [Extrinsic Camera Calibration](#extrinsic-camera-calibration "#extrinsic-camera-calibration")

1. Open a new terminal on `Remote PC` and launch Gazebo.

```
$ roslaunch turtlebot3_gazebo turtlebot3_autorace_2020.launch

```
2. Open a new terminal and launch the intrinsic camera calibration node.

```
$ roslaunch turtlebot3_autorace_camera intrinsic_camera_calibration.launch

```
3. Open a new terminal and launch the extrinsic camera calibration node.

```
$ roslaunch turtlebot3_autorace_camera extrinsic_camera_calibration.launch mode:=calibration

```
4. Execute rqt on `Remote PC`.

```
$ rqt

```
5. Select **plugins** > **visualization** > **Image view**. Create two image view windows.
6. Select `/camera/image_extrinsic_calib/compressed` topic on one window and `/camera/image_projected_compensated` on the other.
	* The first topic shows an image with a red trapezoidal shape and the latter shows the ground projected view (Bird’s eye view).

	![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_extrinsic_calibration.png)

	> 
	> `/camera/image_extrinsic_calib/compressed` (Left) and `/camera/image_projected_compensated` (Right)
	> 
	> 
	>
7. Excute rqt\_reconfigure on `Remote PC`.

```
$ rosrun rqt_reconfigure rqt_reconfigure

```
8. Adjust parameters in `/camera/image_projection` and `/camera/image_compensation_projection`.
	* Change `/camera/image_projection` parameter value. It affects `/camera/image_extrinsic_calib/compressed` topic.
	* Intrinsic camera calibration modifies the perspective of the image in the red trapezoid.

	![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_extrinsic_calibration_reconfigure.png)

	> 
	> rqt\_reconfigure
	> 
	> 
	>
9. After that, overwrite each values on to the yaml files in **turtlebot3\_autorace\_camera/calibration/extrinsic\_calibration/.** This will save the current calibration parameters so that they can be loaded later.

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_compensation_yaml.png)

> 
> turtlebot3\_autorace\_camera/calibration/extrinsic\_calibration/`compensation.yaml`
> 
> 
> 

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_projection_yaml.png)

> 
> turtlebot3\_autorace\_camera/calibration/extrinsic\_calibration/`projection.yaml`
> 
> 
>

![](/assets/images/icon_unfold.png) **Click to expand : Extrinsic Camera Calibration with an actual TurtleBot3**

1. Launch roscore on `Remote PC`.

```
$ roscore

```
2. Trigger the camera on `SBC`.

```
$ roslaunch turtlebot3_autorace_camera raspberry_pi_camera_publish.launch

```
3. Use the command on `Remote PC`.

```
$ roslaunch turtlebot3_autorace_camera intrinsic_camera_calibration.launch mode:=action

```
4. Run the extrinsic camera calibration launch file on `Remote PC`.

```
$ roslaunch turtlebot3_autorace_camera extrinsic_camera_calibration.launch mode:=calibration

```
5. Execute rqt on `Remote PC`.

```
$ rqt

```
6. Click **plugins** > **visualization** > **Image view**; Multiple windows will be present.
7. Select `/camera/image_extrinsic_calib/compressed` and `/camera/image_projected_compensated` topics on each monitors.

* One of two screens will show an image with a red rectangle box. The other one shows the ground projected view (Bird’s eye view).

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_rpi_before_extrinsic_calibration.png)

> 
> `/camera/image_extrinsic_calib/compressed` topic `/camera/image_projected_compensated` topic
> 
> 
>

1. Excute rqt\_reconfigure on `Remote PC`.

```
$ rosrun rqt_reconfigure rqt_reconfigure

```
2. Adjust parameters in `/camera/image_projection` and `/camera/image_compensation_projection`.

* Change `/camera/image_projection` parameter value. It affects `/camera/image_extrinsic_calib/compressed` topic.
* Intrinsic camera calibration will transform the image surrounded by the red rectangle, and will show the image that looks from over the lane.

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_rpi_extrinsic_calibration_param.png)

> 
> rqt\_reconfigure
> 
> 
> 

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_rpi_after_extrinsic_calibration.png)

> 
> Result from parameter modification.
> 
> 
>

### [Check Calibration Result](#check-calibration-result "#check-calibration-result")

When you complete all the camera calibration (Camera Imaging Calibration, Intrinsic Calibration, Extrinsic Calibration), be sure that the calibration is successfully applied to the camera.  

The following instruction describes settings for recognition.

1. Launch roscore on `Remote PC`.

```
$ roscore

```
2. Trigger the camera on `SBC`.

```
$ roslaunch turtlebot3_autorace_${Autorace\_Misson}_camera turtlebot3_autorace_camera_pi.launch

```

**WARNING**: Be sure to specify `${Autorace_Misson}` (i.e, **roslaunch turtlebot3\_autorace\_traffic\_light\_camera turtlebot3\_autorace\_camera\_pi.launch**)
3. Run a intrinsic camera calibration launch file on `Remote PC`.

```
$ export AUTO\_IN\_CALIB=action
$ roslaunch turtlebot3_autorace_${Autorace\_Misson}_camera turtlebot3_autorace_intrinsic_camera_calibration.launch

```
4. Open terminal and use the command on `Remote PC`.

```
$ export AUTO\_EX\_CALIB=action
$ roslaunch turtlebot3_autorace_${Autorace\_Misson}_camera turtlebot3_autorace_extrinsic_camera_calibration.launch

```

From now, the following descriptions will mainly adjust `feature detector / color filter` for object recognition. Every adjustment after here is independent to each other’s process. However, if you want to adjust each parameters in series, complete every adjustment perfectly, then continue to next.

### [Check Calibration Result](#check-calibration-result "#check-calibration-result")

After completing calibrations, run the step by step instructions below on `Remote PC` to check the calibration result.

1. Close all of terminal.
2. Open a new terminal and launch Autorace Gazebo simulation. The `roscore` will be automatically launched with the **roslaunch** command.

```
$ roslaunch turtlebot3_gazebo turtlebot3_autorace_2020.launch

```
3. Open a new terminal and launch the intrinsic calibration node.

```
$ roslaunch turtlebot3_autorace_camera intrinsic_camera_calibration.launch

```
4. Open a new terminal and launch the extrinsic calibration node.

```
$ roslaunch turtlebot3_autorace_camera extrinsic_camera_calibration.launch

```
5. Open a new terminal and launch the rqt image viewer.

```
$ rqt_image_view

```
6. With successful calibration settings, the bird eye view image should appear as below when the `/camera/image_projected_compensated` topic is selected.
![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_camera_calibration_rqt_image_view.png)

![](/assets/images/icon_unfold.png) **Click to expand : Extrinsic Camera Calibration for use of actual TurtleBot3**

When you complete all the camera calibration (Camera Imaging Calibration, Intrinsic Calibration, Extrinsic Calibration), be sure that the calibration is successfully applied to the camera.  

The following instruction describes settings for recognition.

1. Launch roscore on `Remote PC`.

```
$ roscore

```
2. Trigger the camera on `SBC`.

```
$ roslaunch turtlebot3_autorace_camera raspberry_pi_camera_publish.launch

```
3. Run a intrinsic camera calibration launch file on `Remote PC`.

```
$ roslaunch turtlebot3_autorace_camera intrinsic_camera_calibration.launch mode:=action

```
4. Open terminal and use the command on `Remote PC`.

```
$ roslaunch turtlebot3_autorace_camera extrinsic_camera_calibration.launch mode:=action

```
5. Execute rqt on `Remote PC`.

```
$ rqt

```

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_rpi_extrinsic_calibration_rqt.png)

> 
> rqt\_reconfigure
> 
> 
>

From now, the following descriptions will mainly adjust `feature detector / color filter` for object recognition. Every adjustment after here is independent to each other’s process. However, if you want to adjust each parameters in series, complete every adjustment perfectly, then continue to next.

## [Lane Detection](#lane-detection "#lane-detection")

Lane detection package allows Turtlebot3 to drive between two lanes without external influence.

The following instructions describe how to use the lane detection feature and to calibrate camera via rqt.

1. Place TurtleBot3 between yellow and white lanes.

**NOTE**: Be sure that yellow lane is placed left side of the robot and White lane is placed right side of the robot.
2. Launch roscore on `Remote PC`.

```
$ roscore

```
3. Trigger the camera on `SBC`.

```
$ roslaunch turtlebot3_autorace_${Autorace\_Misson}_camera turtlebot3_autorace_camera_pi.launch

```

**WARNING**: Be sure to specify `${Autorace_Misson}` (i.e, **roslaunch turtlebot3\_autorace\_traffic\_light\_camera turtlebot3\_autorace\_camera\_pi.launch**)
4. Run a intrinsic camera calibration launch file on `Remote PC`.

```
$ export AUTO\_IN\_CALIB=action
$ export GAZEBO\_MODE=false
$ roslaunch turtlebot3_autorace_${Autorace\_Misson}_camera turtlebot3_autorace_intrinsic_camera_calibration.launch

```
5. Run a extrinsic camera calibration launch file on `Remote PC`.

```
$ export AUTO\_EX\_CALIB=action
$ roslaunch turtlebot3_autorace_${Autorace\_Misson}_camera turtlebot3_autorace_extrinsic_camera_calibration.launch

```
6. Run a lane detection launch file on `Remote PC`

```
$ export AUTO\_DT\_CALIB=calibration
$ roslaunch turtlebot3_autorace_${Autorace\_Misson}_detect turtlebot3_autorace_detect_lane.launch

```
7. Execute rqt on `Remote PC`.

```
$ rqt

```
8. Click **plugins** > **visualization** > **Image view**; Multiple windows will be present.
9. Select three topics at each image view: `/detect/image_yellow_lane_marker/compressed`, `/detect/image_lane/compressed`, `/detect/image_white_lane_marker/compressed`

	* Left (Yellow line) and Right (White line) screen show a filtered image.  

	![](/assets/images/platform/turtlebot3/autonomous_driving/rqt_yellow_lane_detection.png)

	> 
	> Image view of `/detect/image_yellow_lane_marker/compressed` topic
	> 
	> 
	>![](/assets/images/platform/turtlebot3/autonomous_driving/rqt_white_lane_detection.png)

> 
> Image view of `/detect/image_white_lane_marker/compressed` topic
> 
> 
> 

	* Center screen is the view of the camera from TurtleBot3.  

	![](/assets/images/platform/turtlebot3/autonomous_driving/rqt_image_lane.png)

	> 
	> Image view of `/detect/image_lane/compressed` topic
	> 
	> 
	>
10. Execute rqt\_reconfigure on `Remote PC`.

```
$ rosrun rqt_reconfigure rqt_reconfigure

```
11. Click **Detect Lane** then adjust parameters to do line color filtering.

![](/assets/images/platform/turtlebot3/autonomous_driving/result_of_ybw_configuration_01.png)

> 
> List of Detect Lane Parameters
> 
> 
> 

![](/assets/images/platform/turtlebot3/autonomous_driving/result_of_ybw_configuration_02.png)

> 
> Filtered Image resulted from adjusting parameters at rqt\_reconfigure
> 
> 
> 

**TIP**: Calibration process of line color filtering is sometimes difficult due to physical environment, such as the luminance of light in the room and etc. To make everything quickly, put the value of **lane.yaml** file located in **turtlebot3*autorace*[Autorace\_Misson]\_detect/param/lane/** on the reconfiguration parameter, then start calibration. Calibrate hue low - high value at first. (1) Hue value means the color, and every colors, like `yellow`, `white`, have their own region of hue value (refer to hsv map). Then calibrate saturation low - high value. (2) Every colors have also their own field of saturation. Finally, calibrate the lightness low - high value. (3) In the source code, however, have auto-adjustment function, so calibrating lightness low value is meaningless. Just put the lightness high value to 255. Clearly filtered line image will give you clear result of the lane.
12. Open **lane.yaml** file located in **turtlebot3*autorace*[Autorace\_Misson]\_detect/param/lane/**. You need to write modified values to the file. This will make the camera set its parameters as you set here from next launching.

![](/assets/images/platform/turtlebot3/autonomous_driving/write_lane_yaml.png)
13. Close both **rqt\_rconfigure** and **turtlebot3\_autorace\_detect\_lane**.
14. Open terminal and use the command on `Remote PC`.

```
$ export AUTO\_DT\_CALIB=action
$ roslaunch turtlebot3_autorace_${Autorace\_Misson}_detect turtlebot3_autorace_detect_lane.launch

```
15. Check if the results come out correctly.

	* Open terminal and use the command on `Remote PC`.
```
$ roslaunch turtlebot3_autorace_${Autorace\_Misson}_control turtlebot3_autorace_control_lane.launch

```

	* Open terminal and use the command on `Remote PC`.
```
$ roslaunch turtlebot3_bringup turtlebot3_robot.launch

```
16. After using the commands, TurtleBot3 will start to run.

## [Lane Detection](#lane-detection "#lane-detection")

Lane detection package that runs on the `Remote PC` receives camera images either from TurtleBot3 or Gazebo simulation to detect driving lanes and to drive the Turtlebot3 along them.  

The following instructions describe how to use and calibrate the lane detection feature via rqt.

1. Place the TurtleBot3 inbetween yellow and white lanes.

**NOTE**: The lane detection filters yellow on the left side while filters white on the right side. Be sure that the yellow lane is on the left side of the robot.
2. Open a new terminal and launch Autorace Gazebo simulation. The `roscore` will be automatically launched with the **roslaunch** command.

```
$ roslaunch turtlebot3_gazebo turtlebot3_autorace_2020.launch

```
3. Open a new terminal and launch the intrinsic calibration node.

```
$ roslaunch turtlebot3_autorace_camera intrinsic_camera_calibration.launch

```
4. Open a new terminal and launch the extrinsic calibration node.

```
$ roslaunch turtlebot3_autorace_camera extrinsic_camera_calibration.launch

```
5. Open a new terminal and launch the lane detection calibration node.

```
$ roslaunch turtlebot3_autorace_detect detect_lane.launch mode:=calibration

```
6. Open a new terminal and launch the rqt.

```
$ rqt

```
7. Launch the rqt image viewer by selecting **Plugins** > **Cisualization** > **Image view**.  

 Multiple rqt plugins can be run.
8. Display three topics at each image viewer
	* `/detect/image_lane/compressed`  

	![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_detect_image_lane.png)
	* `/detect/image_yellow_lane_marker/compressed` : a yellow range color filtered image.  

	![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_detect_yellow_lane.png)
	* `/detect/image_white_lane_marker/compressed` : a white range color filtered image.  

	![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_detect_white_lane.png)
9. Open a new terminal and execute rqt\_reconfigure.

```
$ rosrun rqt_reconfigure rqt_reconfigure

```
10. Click **detect\_lane** then adjust parameters so that yellow and white colors can be filtered properly.

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_lane_reconfigure.png)

**TIP**: Calibration process of line color filtering is sometimes difficult due to physical environment, such as the luminance of light in the room and etc.  

To make everything quickly, put the value of **lane.yaml** file located in **turtlebot3\_auatorace\_detect/param/lane/** on the reconfiguration parameter, then start calibration.  

Calibrate hue low - high value at first. (1) Hue value means the color, and every colors, like `yellow`, `white`, have their own region of hue value (refer to hsv map).  

Then calibrate saturation low - high value. (2) Every colors have also their own field of saturation.  

Finally, calibrate the lightness low - high value. (3) In the source code, however, have auto-adjustment function, so calibrating lightness low value is meaningless. Just put the lightness high value to 255.  

Clearly filtered line image will give you clear result of the lane.
11. Open **lane.yaml** file located in **turtlebot3\_autorace\_detect/param/lane/**. You need to write modified values to the file. This will make the camera set its parameters as you set here from next launching.

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_lane_yaml.png)

> 
> Modified lane.yaml file
> 
> 
>
12. Close the terminal or terminate with `Ctrl` + `C` on **rqt\_reconfigure** and **detect\_lane** terminals.
13. Open a new terminal and launch the lane detect node without the calibration option.

```
$ roslaunch turtlebot3_autorace_detect detect_lane.launch

```
14. Open a new terminal and launch the node below to start the lane following operation.

```
$ roslaunch turtlebot3_autorace_driving turtlebot3_autorace_control_lane.launch

```

![](/assets/images/icon_unfold.png) **Click to expand : How to Perform Lane Detection with Actual TurtleBot3?**

Lane detection package allows Turtlebot3 to drive between two lanes without external influence.

The following instructions describe how to use the lane detection feature and to calibrate camera via rqt.

1. Place TurtleBot3 between yellow and white lanes.

**NOTE**: Be sure that yellow lane is placed left side of the robot and White lane is placed right side of the robot.
2. Launch roscore on `Remote PC`.

```
$ roscore

```
3. Trigger the camera on `SBC`.

```
$ roslaunch turtlebot3_autorace_camera raspberry_pi_camera_publish.launch

```
4. Run a intrinsic camera calibration launch file on `Remote PC`.

```
$ roslaunch turtlebot3_autorace_camera intrinsic_camera_calibration.launch mode:=action

```
5. Run a extrinsic camera calibration launch file on `Remote PC`.

```
$ roslaunch turtlebot3_autorace_camera extrinsic_camera_calibration.launch mode:=action

```
6. Run a lane detection launch file on `Remote PC`

```
$ roslaunch turtlebot3_autorace_detect detect_lane.launch mode:=calibration

```
7. Execute rqt on `Remote PC`.

```
$ rqt

```
8. Click **plugins** > **visualization** > **Image view**; Multiple windows will be present.
9. Select three topics at each image view: `/detect/image_yellow_lane_marker/compressed`, `/detect/image_lane/compressed`, `/detect/image_white_lane_marker/compressed`

	* Left (Yellow line) and Right (White line) screen show a filtered image. Center screen is the view of the camera from TurtleBot3.
	![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_rpi_before_detect_lane.png)

	> 
	> Image view of `/detect/image_yellow_lane_marker/compressed` topic , `/detect/image_white_lane_marker/compressed` topic , `/detect/image_lane/compressed` topic
	> 
	> 
	>
10. Execute rqt\_reconfigure on `Remote PC`.

```
$ rosrun rqt_reconfigure rqt_reconfigure

```
11. Click **Detect Lane** then adjust parameters to do line color filtering.

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_rpi_detect_lane_param.png)

> 
> List of Detect Lane Parameters
> 
> 
> 

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_rpi_after_detect_lane.png)

> 
> Filtered Image resulted from adjusting parameters at rqt\_reconfigure
> 
> 
> 

**TIP**: Calibration process of line color filtering is sometimes difficult due to physical environment, such as the luminance of light in the room and etc. To make everything quickly, put the value of **lane.yaml** file located in **turtlebot3*autorace*\_detect/param/lane/** on the reconfiguration parameter, then start calibration. Calibrate hue low - high value at first. (1) Hue value means the color, and every colors, like `yellow`, `white`, have their own region of hue value (refer to hsv map). Then calibrate saturation low - high value. (2) Every colors have also their own field of saturation. Finally, calibrate the lightness low - high value. (3) In the source code, however, have auto-adjustment function, so calibrating lightness low value is meaningless. Just put the lightness high value to 255. Clearly filtered line image will give you clear result of the lane.
12. Open **lane.yaml** file located in **turtlebot3*\_autorace*\_detect/param/lane/**. You need to write modified values to the file. This will make the camera set its parameters as you set here from next launching.

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_rpi_lane_yaml.png)
13. Close both **rqt\_rconfigure** and **turtlebot3\_autorace\_detect\_lane**.
14. Open terminal and use the command on `Remote PC`.

```
$ roslaunch turtlebot3_autorace_detect detect_lane.launch mode:=action

```
15. Check if the results come out correctly.

	* Open terminal and use the command on `Remote PC`.
```
$ roslaunch turtlebot3_autorace_driving turtlebot3_autorace_control_lane.launch

```

	* Open terminal and use the command on `Remote PC`.
```
$ roslaunch turtlebot3_bringup turtlebot3_robot.launch

```
16. After using the commands, TurtleBot3 will start to run.

## [Traffic Sign Detection](#traffic-sign-detection "#traffic-sign-detection")

TurtleBot3 can detect traffic signs using a node with `SIFT algorithm`, and perform programmed tasks while it drives on a built track. Follow the provided instructions to use Traffic sign detection.

**NOTE**: More edges in the traffic sign increase recognition results from SIFT.

1. Take pictures of traffic signs by using TurtleBot3’s camera and `rqt_image_view` node.
2. Edit the pictures using a photo editor that can be used in Linux OS.
3. Put TurtleBot3 on the lane. Traffic signes should be placed where TurtleBot3 can see them easily.

**NOTE**: Do not have TurtleBot3 run on the lane yet.
4. Execute rqt\_image\_view on `Remote PC`.

```
$ rqt_image_view

```
5. Select `/camera/image_compensated` topic in the select box. A screen will show the view from TurtleBot3.
6. Capture the picture from `Remote PC`，and edit it with a photo editor.
7. Place the edited picture to turtlebot3\_autorace package you’ve placed **/turtlebot3\_autorace/turtlebot3\_autorace\_detect/file/detect\_sign/** and rename it as you want. (Although, you should change the file name written in the source **detect\_sign.py** file, if you want to change the default file names.)
8. Open terminal and use the command on `Remote PC`.

```
$ roslaunch turtlebot3_autorace_${Autorace\_Misson}_detect turtlebot3_autorace_detect_sign.launch

```
9. Open terminal and use the command on `Remote PC`.

```
$ rqt_image_view

```
10. Select `/detect/image_traffic_sign/compressed` topic in the select box. A screen will show the result of traffic sign detection.

## [Traffic Sign Detection](#traffic-sign-detection "#traffic-sign-detection")

TurtleBot3 can detect various signs with the `SIFT` algorithm which compares the source image and the camera image, and perform programmed tasks while it drives.  

Follow the instructions below to test the traffic sign detection.

**NOTE**: More edges in the traffic sign increase recognition results from the SIFT algorithm.  

Please refer to the link below for related information.  

[https://docs.opencv.org/master/da/df5/tutorial\_py\_sift\_intro.html](https://docs.opencv.org/master/da/df5/tutorial_py_sift_intro.html "https://docs.opencv.org/master/da/df5/tutorial_py_sift_intro.html")

1. Open a new terminal and launch Autorace Gazebo simulation. The `roscore` will be automatically launched with the **roslaunch** command.

```
$ roslaunch turtlebot3_gazebo turtlebot3_autorace_2020.launch

```
2. Open a new terminal and launch the teleoperation node. Drive the TurtleBot3 along the lane and stop where traffic signes can be clearly seen by the camera.

```
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

```
3. Open a new terminal and launch the rqt\_image\_view.

```
$ rqt_image_view

```
4. Select the `/camera/image_compensated` topic to display the camera image.
5. Capture each traffic sign from the `rqt_image_view` and crop unnecessary part of image. For the best performance, it is recommended to use original traffic sign images used in the track.
6. Save the images in the turtlebot3\_autorace\_detect package **/turtlebot3\_autorace\_2020/turtlebot3\_autorace\_detect/image/**. The file name should match with the name used in the source code.
	* `construction.png`, `intersection.png`, `left.png`, `right.png`, `parking.png`, `stop.png`, `tunnel.png` file names are used by default.
7. Open a new terminal and launch the intrinsic calibration node.

```
$ roslaunch turtlebot3_autorace_camera intrinsic_camera_calibration.launch

```
8. Open a new terminal and launch the extrinsic calibration node.

```
$ roslaunch turtlebot3_autorace_camera extrinsic_camera_calibration.launch

```
9. Open a new terminal and launch the traffic sign detection node.  

A specific mission for the ***mission*** argument must be selected among below.
	* `intersection`, `construction`, `parking`, `level_crossing`, `tunnel`

```
	$ roslaunch turtlebot3_autorace_detect detect_sign.launch mission:=SELECT_MISSION

```**NOTE**: Replace the `SELECT_MISSION` keyword with one of available options in the above.
10. Open a new terminal and launch the rqt image view plugin.

```
$ rqt_image_view

```
11. Select `/detect/image_traffic_sign/compressed` topic from the drop down list. A screen will display the result of traffic sign detection.

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_detect_intersection.png)

> 
> Detecting the Intersection sign when `mission:=intersection`
> 
> 
> 

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_detect_left.png)

> 
> Detecting the Left sign when `mission:=intersection`
> 
> 
> 

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_detect_right.png)

> 
> Detecting the Right sign when `mission:=intersection`
> 
> 
> 

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_detect_construction.png)

> 
> Detecting the Construction sign when `mission:=construction`
> 
> 
> 

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_detect_parking.png)

> 
> Detecting the Parking sign when `mission:=parking`
> 
> 
> 

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_detect_level_crossing.png)

> 
> Detecting the Level Crossing sign when `mission:=level_crossing`
> 
> 
> 

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_detect_tunnel.png)

> 
> Detecting the Tunnel sign when `mission:=tunnel`
> 
> 
>

## [Missions](#missions "#missions")

The AutoRace is a competition for autonomous driving robot platforms.  

To provide various conditions for a robot application development, the game provide structural regulation as less as possible. Provided open sources are based on ROS, and can be applied to this competition. The contents can be continually updated. Join the competition and show your skill.

**WARNING**: Be sure to read [Autonomous Driving](#autonomous-driving "#autonomous-driving") in order to start missions.

## [Missions](#missions "#missions")

The AutoRace is a competition for autonomous driving robot platforms.  

To provide various conditions for a robot application development, the game provide structural regulation as less as possible. Provided open sources are based on ROS, and can be applied to this competition. The contents can be continually updated. Join the competition and show your skill.

**WARNING**: Be sure to read [Autonomous Driving](#autonomous-driving "#autonomous-driving") in order to start missions.

### [Traffic Lights](#traffic-lights "#traffic-lights")

Traffic Light is the first mission of AutoRace. TurtleBot3 recognizes the traffic lights and starts the course.

#### [Traffic Lights Detection](#traffic-lights-detection "#traffic-lights-detection")

1. Open terminal and use the command on `Remote PC`.

```
$ export AUTO\_DT\_CALIB=calibration
$ roslaunch turtlebot3_autorace_traffic_light_detect turtlebot3_autorace_detect_traffic_light.launch

```
2. Excute rqt on `Remote PC`.

```
rqt

```
3. Select four topics: `/detect/image_red_light`, `/detect/image_yellow_light`, `/detect/image_green_light`, `/detect/image_traffic_light`.
4. Excute rqt\_reconfigure.

```
$ rosrun rqt_reconfigure rqt_reconfigure

```
5. Adjust parameters regarding traffic light topics to enhance the detection of traffic signs. The way of adjusting parameters is similar to step 5 at [Lane Detection](#lane-detection "#lane-detection").
6. Open **traffic\_light.yaml** file located at **turtlebot3\_autorace\_traffic\_light\_detect/param/traffic\_light/**.
7. Write modified values to the file and save.
8. Terminate both running rqt and rqt\_reconfigure in order to test, from the next step, the calibration whether or not it is successfully applied.
9. Use the command on `Remote PC`.

```
$ export AUTO\_DT\_CALIB=action
$ roslaunch turtlebot3_autorace_traffic_light_detect turtlebot3_autorace_detect_traffic_light.launch

```
10. Execute rqt\_image\_view.

```
$ rqt_image_view

```
11. See traffic light calibration is successfully applied.

#### [How to Run Traffic Light Mission](#how-to-run-traffic-light-mission "#how-to-run-traffic-light-mission")

**WARNING**: Be sure to read [Camera Calibration for Traffic Lights](#camera-calibration-for-traffic-lights "#camera-calibration-for-traffic-lights") before running the traffic light node.

1. Use the command on `Remote PC`.

```
$ export AUTO\_IN\_CALIB=action
$ export GAZEBO\_MODE=false
$ roslaunch turtlebot3_autorace_traffic_light_camera turtlebot3_autorace_intrinsic_camera_calibration.launch

```
2. Use the command on `Remote PC`.

```
$ export AUTO\_EX\_CALIB=action
$ export AUTO\_DT\_CALIB=action
$ roslaunch turtlebot3_autorace_traffic_light_core turtlebot3_autorace_core.launch

```
3. Use the command on `Remote PC`.

```
$ rostopic pub -1 /core/decided_mode std_msgs/UInt8 "data: 3"

```

### [Traffic Lights](#traffic-lights "#traffic-lights")

Traffic Light is the first mission of AutoRace. TurtleBot3 recognizes the traffic lights and starts the course.

##### [Traffic Lights Detection](#traffic-lights-detection "#traffic-lights-detection")

**NOTE**: In order to fix the traffic ligth to a specific color in Gazebo, you may modify the controlMission method in the `core_node_mission` file in the ***turtlebot3\_autorace\_2020/turtlebot3\_autorace\_core/nodes/*** directory.

1. Open a new terminal and launch Autorace Gazebo simulation. The `roscore` will be automatically launched with the **roslaunch** command.

```
$ roslaunch turtlebot3_gazebo turtlebot3_autorace_2020.launch

```
2. Open a new terminal and launch the intrinsic calibration node.

```
$ roslaunch turtlebot3_autorace_camera intrinsic_camera_calibration.launch

```
3. Open a new terminal and launch the extrinsic calibration node.

```
$ roslaunch turtlebot3_autorace_camera extrinsic_camera_calibration.launch

```
4. Open a new terminal and launch the traffic light detection node with a calibration option.

```
$ roslaunch turtlebot3_autorace_detect detect_traffic_light.launch mode:=calibration

```
5. Open a new terminal to execute the rqt. Open four `rqt_image_view` plugins.

```
$ rqt

```
6. Select four topics: `/detect/image_red_light`, `/detect/image_yellow_light`, `/detect/image_green_light`, `/detect/image_traffic_light`.

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_detect_traffic_light_green.png)

> 
> Detecting the Green light. The image on the right displays `/detect/image_green_light` topic.
> 
> 
> 

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_detect_traffic_light_yellow.png)

> 
> Detecting the Yellow light. The image on the right displays `/detect/image_yellow_light` topic.
> 
> 
> 

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_detect_traffic_light_red.png)

> 
> Detecting the Red light. The image on the right displays `/detect/image_red_light` topic.
> 
> 
>
7. Open a new terminal and excute rqt\_reconfigure.

```
$ rosrun rqt_reconfigure rqt_reconfigure

```
8. Select `detect_traffic_light` on the left column and adjust parameters properly so that the colors of the traffic light can be well detected.

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_traffic_light_reconfigure.png)

> 
> Traffic light reconfigure
> 
> 
>
9. Open the `traffic_light.yaml` file located at ***turtlebot3\_autorace\_detect/param/traffic\_light/***.

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_traffic_light_yaml.png)
10. Write modified values and save the file.

##### [Testing Traffic Light Detection](#testing-traffic-light-detection "#testing-traffic-light-detection")

1. Close all terminals or terminate them with `Ctrl` + `C`
2. Open a new terminal and launch Autorace Gazebo simulation. The `roscore` will be automatically launched with the **roslaunch** command.

```
$ roslaunch turtlebot3_gazebo turtlebot3_autorace_2020.launch

```
3. Open a new terminal and launch the intrinsic calibration node.

```
$ roslaunch turtlebot3_autorace_camera intrinsic_camera_calibration.launch

```
4. Open a new terminal and launch the extrinsic calibration node.

```
$ roslaunch turtlebot3_autorace_camera extrinsic_camera_calibration.launch

```
5. Open a new terminal and launch the traffic light detection node.

```
$ roslaunch turtlebot3_autorace_detect detect_traffic_light.launch

```
6. Open a new terminal and execute the rqt\_image\_view.

```
$ rqt_image_view

```
7. Check each topics: `/detect/image_red_light`, `/detect/image_yellow_light`, `/detect/image_green_light`.

##### [How to Run Traffic Light Mission](#how-to-run-traffic-light-mission "#how-to-run-traffic-light-mission")

**WARNING**: Please calibrate the color as described in the [Traffic Lights Detecion](#traffic-lights-detection "#traffic-lights-detection") section before running the traffic light mission.

1. Close all terminals or terminate them with `Ctrl` + `C`
2. Open a new terminal and launch Autorace Gazebo simulation. The `roscore` will be automatically launched with the **roslaunch** command.

```
$ roslaunch turtlebot3_gazebo turtlebot3_autorace_2020.launch

```
3. Open a new terminal and launch the intrinsic calibration node.

```
$ roslaunch turtlebot3_autorace_camera intrinsic_camera_calibration.launch

```
4. Open a new terminal and launch the autorace core node with a specific mission name.

```
$ roslaunch turtlebot3_autorace_core turtlebot3_autorace_core.launch mission:=traffic_light

```
5. Open a new terminal and enter the command below. This will prepare to run the traffic light mission by setting the `decided_mode` to `3`.

```
$ rostopic pub -1 /core/decided_mode std_msgs/UInt8 "data: 3"

```
6. Launch the Gazebo mission node.

```
$ roslaunch turtlebot3_autorace_core turtlebot3_autorace_mission.launch

```

### [Intersection](#intersection "#intersection")

Intersection is the second mission of AutoRace. TurtleBot3 detects a specific traffic sign (such as a curve sign) at the intersection course, and go to the given direction.

#### [How to Run Intersection Mission](#how-to-run-intersection-mission "#how-to-run-intersection-mission")

1. Use the command on `Remote PC`.

```
$ export AUTO\_IN\_CALIB=action
$ roslaunch turtlebot3_autorace_intersection_camera turtlebot3_autorace_intrinsic_camera_calibration.launch

```
2. Use the command on `Remote PC`.

```
$ export AUTO\_EX\_CALIB=action
$ export AUTO\_DT\_CALIB=action
$ roslaunch turtlebot3_autorace_intersection_core turtlebot3_autorace_core.launch

```
3. Use the command on `Remote PC`.

```
$ rostopic pub -1 /core/decided_mode std_msgs/UInt8 "data: 2"

```

### [Intersection](#intersection "#intersection")

Intersection is the second mission of AutoRace. TurtleBot3 must detect the directional sign at the intersection, and proceed to the directed path.

##### [How to Run Intersection Mission](#how-to-run-intersection-mission "#how-to-run-intersection-mission")

1. Close all terminals or terminate them with `Ctrl` + `C`
2. Open a new terminal and launch Autorace Gazebo simulation. The `roscore` will be automatically launched with the **roslaunch** command.

```
$ roslaunch turtlebot3_gazebo turtlebot3_autorace_2020.launch

```
3. Open a new terminal and launch the intrinsic calibration node.

```
$ roslaunch turtlebot3_autorace_camera intrinsic_camera_calibration.launch

```
4. Open a new terminal and launch the keyboard teleoperation node.  

Drive the TurtleBot3 along the lane and stop before the intersection traffic sign.

```
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

```
5. Open a new terminal and launch the autorace core node with a specific mission name.

```
$ roslaunch turtlebot3_autorace_core turtlebot3_autorace_core.launch mission:=intersection

```
6. Open a new terminal and launch the Gazebo mission node.

```
$ roslaunch turtlebot3_autorace_core turtlebot3_autorace_mission.launch

```
7. Open a new terminal and enter the command below. This will prepare to run the intersection mission by setting the `decided_mode` to `2`.

```
$ rostopic pub -1 /core/decided_mode std_msgs/UInt8 "data: 2"

```

### [Construction](#construction "#construction")

Construction is the third mission of AutoRace. TurtleBot3 avoids constructions on the track while it is driving.

#### [How to Run Construction Mission](#how-to-run-construction-mission "#how-to-run-construction-mission")

1. Use the command on `Remote PC`.

```
$ export AUTO\_IN\_CALIB=action
$ export GAZEBO\_MODE=false
$ roslaunch turtlebot3_autorace_construction_camera turtlebot3_autorace_intrinsic_camera_calibration.launch

```
2. Use the command on `Remote PC`.

```
$ export AUTO\_EX\_CALIB=action
$ export AUTO\_DT\_CALIB=action
$ roslaunch turtlebot3_autorace_construction_core turtlebot3_autorace_core.launch

```
3. Use the command on `Remote PC`.

```
$ rostopic pub -1 /core/decided_mode std_msgs/UInt8 "data: 2"

```

### [Construction](#construction "#construction")

Construction is the third mission of TurtleBot3 AutoRace 2020. TurtleBot3 must avoid obstacles in the construction area.

##### [How to Run Construction Mission](#how-to-run-construction-mission "#how-to-run-construction-mission")

1. Close all terminals or terminate them with `Ctrl` + `C`
2. Open a new terminal and launch Autorace Gazebo simulation. The `roscore` will be automatically launched with the **roslaunch** command.

```
$ roslaunch turtlebot3_gazebo turtlebot3_autorace_2020.launch

```
3. Open a new terminal and launch the intrinsic calibration node.

```
$ roslaunch turtlebot3_autorace_camera intrinsic_camera_calibration.launch

```
4. Open a new terminal and launch the keyboard teleoperation node.  

Drive the TurtleBot3 along the lane and stop before the construction traffic sign.

```
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

```
5. Open a new terminal and launch the autorace core node with a specific mission name.

```
$ roslaunch turtlebot3_autorace_core turtlebot3_autorace_core.launch mission:=construction

```
6. Open a new terminal and enter the command below. This will prepare to run the construction mission by setting the `decided_mode` to `2`.

```
$ rostopic pub -1 /core/decided_mode std_msgs/UInt8 "data: 2"

```

### [Parking](#parking "#parking")

Parking is the fourth mission of AutoRace. TurtleBot3 detects the parking sign, and park itself at a parking lot.

#### [How to Run Parking Mission](#how-to-run-parking-mission "#how-to-run-parking-mission")

1. Use the command on `Remote PC`.

```
$ export AUTO\_IN\_CALIB=action
$ export GAZEBO\_MODE=false
$ roslaunch turtlebot3_autorace_parking_camera turtlebot3_autorace_intrinsic_camera_calibration.launch

```
2. Use the command on `Remote PC`.

```
$ export AUTO\_EX\_CALIB=action
$ export AUTO\_DT\_CALIB=action
$ roslaunch turtlebot3_autorace_parking_core turtlebot3_autorace_core.launch

```
3. Use the command on `Remote PC`.

```
$ rostopic pub -1 /core/decided_mode std_msgs/UInt8 "data: 2"

```

### [Parking](#parking "#parking")

Parking is the fourth mission of TurtleBot3 AutoRace 2020. TurtleBot3 must detect the parking sign, and park at an empty parking spot.

##### [How to Run Parking Mission](#how-to-run-parking-mission "#how-to-run-parking-mission")

1. Close all terminals or terminate them with `Ctrl` + `C`
2. Open a new terminal and launch Autorace Gazebo simulation. The `roscore` will be automatically launched with the **roslaunch** command.

```
$ roslaunch turtlebot3_gazebo turtlebot3_autorace_2020.launch

```
3. Open a new terminal and launch the intrinsic calibration node.

```
$ roslaunch turtlebot3_autorace_camera intrinsic_camera_calibration.launch

```
4. Open a new terminal and launch the keyboard teleoperation node.  

Drive the TurtleBot3 along the lane and stop before the parking traffic sign.

```
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

```
5. Open a new terminal and launch the autorace core node with a specific mission name.

```
$ roslaunch turtlebot3_autorace_core turtlebot3_autorace_core.launch mission:=parking

```
6. Open a new terminal and launch the Gazebo mission node.

```
$ roslaunch turtlebot3_autorace_core turtlebot3_autorace_mission.launch

```
7. Open a new terminal and enter the command below. This will prepare to run the parking mission by setting the `decided_mode` to `2`.

```
$ rostopic pub -1 /core/decided_mode std_msgs/UInt8 "data: 2"

```

### [Level Crossing](#level-crossing "#level-crossing")

Level Crossing is the fifth mission of AutoRace. When TurtleBot3 encounters the level crossing, it stops driving, and wait until the level crossing opens.

#### [Level Crossing Detection](#level-crossing-detection "#level-crossing-detection")

1. Use the command on `Remote PC`.

```
$ export AUTO\_DT\_CALIB=calibration
$ roslaunch turtlebot3_autorace_level_crossing_detect turtlebot3_autorace_detect_level.launch

```
2. Execute rqt

```
$ rqt

```
3. Select two topics: `/detect/image_level_color_filtered`, `/detect/image_level`
4. Execute rqt\_reconfigure.

```
$ rosrun rqt_reconfigure rqt_reconfigure

```
5. Select `/detect_level` and adjust parameters regarding Level Crossing topics to enhance the detection of the level crossing object. The way of adjusting parameters is similar to step 5 at [Lane Detection](#lane-detection "#lane-detection").
6. Open **level.yaml** located at **turtlebot3\_autorace\_stop\_bar\_detect/param/level/**.
7. Write modified values to the file and save.
8. Run a detect level lanuch file.

```
$ export AUTO\_DT\_CALIB=action
$ roslaunch turtlebot3_autorace_detect turtlebot3_autorace_detect_level.launch

```

#### [How to Run Level Crossing Mission](#how-to-run-level-crossing-mission "#how-to-run-level-crossing-mission")
9. Use the command on `Remote PC`.

```
$ export AUTO\_IN\_CALIB=action
$ export GAZEBO\_MODE=false
$ roslaunch turtlebot3_autorace_level_crossing_camera turtlebot3_autorace_intrinsic_camera_calibration.launch

```
10. Use the command on `Remote PC`.

```
$ export AUTO\_EX\_CALIB=action
$ export AUTO\_DT\_CALIB=action
$ roslaunch turtlebot3_autorace_level_crossing_core turtlebot3_autorace_core.launch

```
11. Use the command on `Remote PC`.

```
$ rostopic pub -1 /core/decided_mode std_msgs/UInt8 "data: 2"

```

### [Level Crossing](#level-crossing "#level-crossing")

Level Crossing is the fifth mission of TurtleBot3 AutoRace 2020. TurtleBot3 must detect the stop sign and wait until the crossing gate is lifted.

##### [Level Crossing Detection](#level-crossing-detection "#level-crossing-detection")

1. Close all terminals or terminate them with `Ctrl` + `C`
2. Open a new terminal and launch Autorace Gazebo simulation. The `roscore` will be automatically launched with the **roslaunch** command.

```
$ roslaunch turtlebot3_gazebo turtlebot3_autorace_2020.launch

```
3. Open a new terminal and launch the intrinsic calibration node.

```
$ roslaunch turtlebot3_autorace_camera intrinsic_camera_calibration.launch

```
4. Open a new terminal and launch the extrinsic calibration node.

```
$ roslaunch turtlebot3_autorace_camera extrinsic_camera_calibration.launch

```
5. Open a new terminal and launch the level crossing detection node with a calibration option.

```
$ roslaunch turtlebot3_autorace_detect detect_level_crossing.launch mode:=calibration

```
6. Open a new terminal and execute rqt.

```
$ rqt

```
7. Select two topics: `/detect/image_level_color_filtered/compressed`, `/detect/image_level/compressed`.
 ![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_detect_level.png)
8. Excute rqt\_reconfigure.

```
$ rosrun rqt_reconfigure rqt_reconfigure

```
9. Adjust parameters in the `detect_level_crossing` in the left column to enhance the detection of crossing gate.
![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_level_reconfigure.png)
10. Open `level.yaml` file located at ***turtlebot3\_autorace\_detect/param/level/***.

![](/assets/images/platform/turtlebot3/autonomous_driving/noetic_level_yaml.png)
11. Write modified values to the file and save.

##### Testing Level Crossing Detection

1. Close all terminals or terminate them with `Ctrl` + `C`
2. Open a new terminal and launch Autorace Gazebo simulation. The `roscore` will be automatically launched with the **roslaunch** command.

```
$ roslaunch turtlebot3_gazebo turtlebot3_autorace_2020.launch

```
3. Open a new terminal and launch the intrinsic calibration node.

```
$ roslaunch turtlebot3_autorace_camera intrinsic_camera_calibration.launch

```
4. Open a new terminal and launch the extrinsic calibration node.

```
$ roslaunch turtlebot3_autorace_camera extrinsic_camera_calibration.launch

```
5. Open a new terminal and launch the level crossing detection node.

```
$ roslaunch turtlebot3_autorace_detect detect_level_crossing.launch

```
6. Open a new terminal and execute the rqt\_image\_view.

```
$ rqt_image_view

```
7. Check the image topic: `/detect/image_level/compressed`.

##### [How to Run Level Crossing Mission](#how-to-run-level-crossing-mission "#how-to-run-level-crossing-mission")

1. Close all terminals or terminate them with `Ctrl` + `C`
2. Open a new terminal and launch Autorace Gazebo simulation. The `roscore` will be automatically launched with the **roslaunch** command.

```
$ roslaunch turtlebot3_gazebo turtlebot3_autorace_2020.launch

```
3. Open a new terminal and launch the intrinsic calibration node.

```
$ roslaunch turtlebot3_autorace_camera intrinsic_camera_calibration.launch

```
4. Open a new terminal and launch the keyboard teleoperation node.  

Drive the TurtleBot3 along the lane and stop before the stop traffic sign.

```
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

```
5. Open a new terminal and launch the autorace core node with a specific mission name.

```
$ roslaunch turtlebot3_autorace_core turtlebot3_autorace_core.launch mission:=level_crossing

```
6. Open a new terminal and launch the Gazebo mission node.

```
$ roslaunch turtlebot3_autorace_core turtlebot3_autorace_mission.launch

```
7. Open a new terminal and enter the command below. This will prepare to run the level crossing mission by setting the `decided_mode` to `2`.

```
$ rostopic pub -1 /core/decided_mode std_msgs/UInt8 "data: 2"

```

### [Tunnel](#tunnel "#tunnel")

Tunnel is the sixth mission of AutoRace. TurtleBot3 passes the tunnel successfully.

#### [How to Run Tunnel Mission](#how-to-run-tunnel-mission "#how-to-run-tunnel-mission")

1. Use the command on `Remote PC`.

```
$ export AUTO\_IN\_CALIB=action
$ export GAZEBO\_MODE=false
$ roslaunch turtlebot3_autorace_tunnel_camera turtlebot3_autorace_intrinsic_camera_calibration.launch

```
2. Use the command on `Remote PC`.

```
$ export AUTO\_EX\_CALIB=action
$ export AUTO\_DT\_CALIB=action
$ export TURTLEBOT3\_MODEL=burger
$ roslaunch turtlebot3_autorace_tunnel_core turtlebot3_autorace_core.launch

```
3. Use the command on `Remote PC`.

```
$ rostopic pub -1 /core/decided_mode std_msgs/UInt8 "data: 2"

```

### [Tunnel](#tunnel "#tunnel")

Tunnel is the sixth mission of TurtleBot3 AutoRace 2020. TurtleBot3 must avoid obstacles in the unexplored tunnel and exit successfully.

##### [How to Run Tunnel Mission](#how-to-run-tunnel-mission "#how-to-run-tunnel-mission")

**NOTE**: Change the navigation parameters in the **turtlebot3/turtlebot3\_navigation/param/** file. If you slam and make a new map, Place the new map to turtlebot3\_autorace package you’ve placed **/turtlebot3\_autorace/turtlebot3\_autorace\_driving/maps/**.

1. Close all terminals or terminate them with `Ctrl` + `C`
2. Open a new terminal and launch Autorace Gazebo simulation. The `roscore` will be automatically launched with the **roslaunch** command.

```
$ roslaunch turtlebot3_gazebo turtlebot3_autorace_2020.launch

```
3. Open a new terminal and launch the intrinsic calibration node.

```
$ roslaunch turtlebot3_autorace_camera intrinsic_camera_calibration.launch

```
4. Open a new terminal and launch the keyboard teleoperation node.  

Drive the TurtleBot3 along the lane and stop before the tunnel traffic sign.

```
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

```
5. Open a new terminal and launch the autorace core node with a specific mission name.

```
$ roslaunch turtlebot3_autorace_core turtlebot3_autorace_core.launch mission:=tunnel

```
6. Open a new terminal and enter the command below. This will prepare to run the tunnel mission by setting the `decided_mode` to `2`.

```
$ rostopic pub -1 /core/decided_mode std_msgs/UInt8 "data: 2"

```

 Previous Page
Next Page 