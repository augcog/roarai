

 var \_gaq = \_gaq || [];
 \_gaq.push(['\_setAccount', 'UA-17821189-2']);
 \_gaq.push(['\_setDomainName', 'wiki.ros.org']);
 \_gaq.push(['\_trackPageview']);

 (function() {
 var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
 ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
 var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
 })();

ROS/Tutorials/Packaging your ROS project as a snap - ROS Wiki

<!--
var search\_hint = "Search";
//-->

 window.dataLayer = window.dataLayer || [];
 function gtag(){dataLayer.push(arguments);}
 gtag('js', new Date());

 gtag('config', 'G-EVD5Z6G6NH');

<!--// Initialize search form
var f = document.getElementById('searchform');
if(f) f.getElementsByTagName('label')[0].style.display = 'none';
var e = document.getElementById('searchinput');
if(e) {
 searchChange(e);
 searchBlur(e);
}

function handleSubmit() {
 var f = document.getElementById('searchform');
 var t = document.getElementById('searchinput');
 var r = document.getElementById('real\_searchinput');

 //alert("handleSubmit "+ t.value);
 if(t.value.match(/review/)) {
 r.value = t.value;
 } else {
 //r.value = t.value + " -PackageReviewCategory -StackReviewCategory -M3Review -DocReview -ApiReview -HelpOn -BadContent -LocalSpellingWords";
 r.value = t.value + " -PackageReviewCategory -StackReviewCategory -DocReview -ApiReview";
 }
 //return validate(f);
}
//-->

|  |  |
| --- | --- |
| [ros.org](/ "/") | [About](http://www.ros.org/about-ros "http://www.ros.org/about-ros")
 |
 [Support](/Support "/Support")
 |
 [Discussion Forum](http://discourse.ros.org/ "http://discourse.ros.org/")
 |
 [Index](http://index.ros.org/ "http://index.ros.org/")
 |
 [Service Status](http://status.ros.org/ "http://status.ros.org/")
 |
 [Q&A answers.ros.org](http://answers.ros.org/ "http://answers.ros.org/") |
| [Documentation](/ "/")[Browse Software](https://index.ros.org/packages "https://index.ros.org/packages")[News](https://discourse.ros.org/c/general "https://discourse.ros.org/c/general")[Download](/ROS/Installation "/ROS/Installation") |

* [ROS](/ROS "/ROS")
* [Tutorials](/ROS/Tutorials "/ROS/Tutorials")
* [Packaging your ROS project as a snap](/ROS/Tutorials/Packaging%20your%20ROS%20project%20as%20a%20snap "/ROS/Tutorials/Packaging%20your%20ROS%20project%20as%20a%20snap")

#### ROS 2 Documentation

The ROS Wiki is for ROS 1. Are you using ROS 2 ([Humble](http://docs.ros.org/en/humble/ "http://docs.ros.org/en/humble/"), [Iron](http://docs.ros.org/en/iron/ "http://docs.ros.org/en/iron/"), or [Rolling](http://docs.ros.org/en/rolling/ "http://docs.ros.org/en/rolling/"))?   
[Check out the ROS 2 Project Documentation](http://docs.ros.org "http://docs.ros.org")  
Package specific documentation can be found on [index.ros.org](https://index.ros.org "https://index.ros.org")

# Wiki

* [Distributions](/Distributions "/Distributions")
* [ROS/Installation](/ROS/Installation "/ROS/Installation")
* [ROS/Tutorials](/ROS/Tutorials "/ROS/Tutorials")
* [RecentChanges](/RecentChanges "/RecentChanges")
* [Packaging y...t as a snap](/ROS/Tutorials/Packaging%20your%20ROS%20project%20as%20a%20snap "/ROS/Tutorials/Packaging%20your%20ROS%20project%20as%20a%20snap")

# Page

* Immutable Page
* [Comments](# "#")
* [Info](/action/info/ROS/Tutorials/Packaging%20your%20ROS%20project%20as%20a%20snap?action=info "/action/info/ROS/Tutorials/Packaging%20your%20ROS%20project%20as%20a%20snap?action=info")
* [Attachments](/action/AttachFile/ROS/Tutorials/Packaging%20your%20ROS%20project%20as%20a%20snap?action=AttachFile "/action/AttachFile/ROS/Tutorials/Packaging%20your%20ROS%20project%20as%20a%20snap?action=AttachFile")
* More Actions:

Raw Text
Print View
Render as Docbook
Delete Cache
------------------------
Check Spelling
Like Pages
Local Site Map
------------------------
Rename Page
Copy Page
Delete Page
------------------------
My Pages
Subscribe User
------------------------
Remove Spam
Revert to this revision
Package Pages
Sync Pages
------------------------
CreatePdfDocument
Load
RawFile
Save
SlideShow

<!--// Init menu
actionsMenuInit('More Actions:');
//-->

# User

* [Login](/action/login/ROS/Tutorials/Packaging%20your%20ROS%20project%20as%20a%20snap?action=login "/action/login/ROS/Tutorials/Packaging%20your%20ROS%20project%20as%20a%20snap?action=login")

 melodic 
 noetic 
  *Show EOL distros:* *EOL distros:*  
 electric 
 fuerte 
 groovy 
 hydro 
 indigo 
 jade 
 kinetic 
 lunar 

|  |
| --- |
| **Note:** This tutorial assumes that you have completed the previous tutorials: [examining the simple publisher and subscriber](/ROS/Tutorials/ExaminingPublisherSubscriber "/ROS/Tutorials/ExaminingPublisherSubscriber").  |

|  |
| --- |
| (!) Please ask about problems and questions regarding this tutorial on [answers.ros.org](http://answers.ros.org "http://answers.ros.org"). Don't forget to include in your question the link to this page, the versions of your OS & ROS, and also add appropriate tags. |

# Packaging your ROS project as a snap

**Description:** This tutorial covers how to package and deploy your ROS project as a snap.  

**Tutorial Level:** INTERMEDIATE   

**Next Tutorial:** [Writing a Tutorial](/WritingTutorials "/WritingTutorials")   

 Contents1. [What are snaps?](#What_are_snaps.3F "#What_are_snaps.3F")
2. [Creating a snap](#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fnoetic.Creating_a_snap "#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fnoetic.Creating_a_snap")
	1. [The snapcraft file](#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fnoetic.The_snapcraft_file "#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fnoetic.The_snapcraft_file")
		1. [Metadata](#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fnoetic.Metadata "#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fnoetic.Metadata")
		2. [Base](#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fnoetic.Base "#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fnoetic.Base")
		3. [Security model](#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fnoetic.Security_model "#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fnoetic.Security_model")
		4. [Parts](#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fnoetic.Parts "#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fnoetic.Parts")
		5. [Apps](#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fnoetic.Apps "#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fnoetic.Apps")
	2. [Building the snap](#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fnoetic.Building_the_snap "#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fnoetic.Building_the_snap")
3. [Testing the snap](#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fnoetic.Testing_the_snap "#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fnoetic.Testing_the_snap")
4. [Creating a snap](#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fmelodic.Creating_a_snap "#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fmelodic.Creating_a_snap")
	1. [The snapcraft file](#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fmelodic.The_snapcraft_file "#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fmelodic.The_snapcraft_file")
		1. [Metadata](#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fmelodic.Metadata "#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fmelodic.Metadata")
		2. [Base](#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fmelodic.Base "#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fmelodic.Base")
		3. [Security model](#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fmelodic.Security_model "#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fmelodic.Security_model")
		4. [Parts](#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fmelodic.Parts "#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fmelodic.Parts")
		5. [Apps](#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fmelodic.Apps "#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fmelodic.Apps")
	2. [Building the snap](#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fmelodic.Building_the_snap "#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fmelodic.Building_the_snap")
5. [Testing the snap](#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fmelodic.Testing_the_snap "#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fmelodic.Testing_the_snap")
6. [Creating a snap](#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fkinetic.Creating_a_snap "#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fkinetic.Creating_a_snap")
	1. [The snapcraft.yaml](#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fkinetic.The_snapcraft.yaml "#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fkinetic.The_snapcraft.yaml")
	2. [The snapcraft.yaml explained](#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fkinetic.The_snapcraft.yaml_explained "#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fkinetic.The_snapcraft.yaml_explained")
	3. [Actually create the snap](#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fkinetic.Actually_create_the_snap "#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fkinetic.Actually_create_the_snap")
7. [Testing the snap](#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fkinetic.Testing_the_snap "#ROS.2FTutorials.2FPackaging_your_ROS_project_as_a_snap.2Fkinetic.Testing_the_snap")
8. [Sharing the snap with the world](#Sharing_the_snap_with_the_world "#Sharing_the_snap_with_the_world")

## What are snaps?

[Snaps](https://snapcraft.io/docs/robotics "https://snapcraft.io/docs/robotics") are containers that bundle an application and all its dependencies. They offer several features that address important concerns as one gets closer to shipping a robotic platform: * **Container solution**: Snaps bundle all your dependencies and assets in one package (including ROS) making your application installable on dozens of Linux distributions and across distro versions.
* **Strict confinement**: Snaps are designed to be [secure and isolated](https://snapcraft.io/docs/snap-confinement "https://snapcraft.io/docs/snap-confinement") from the underlying system and other applications, with [dedicated interfaces](https://snapcraft.io/docs/supported-interfaces "https://snapcraft.io/docs/supported-interfaces") to access the host machine.
* **Managing updates**: Snaps can update [automatically and transactionally](https://snapcraft.io/docs/keeping-snaps-up-to-date "https://snapcraft.io/docs/keeping-snaps-up-to-date"), making sure the device is never broken and always up-to-date.
* **Release management**: Snaps' [multiple release](https://snapcraft.io/docs/channels "https://snapcraft.io/docs/channels") channels allow you to have role-based access controls and application versioning, making A/B testing easy and releasing fixes faster.

## Creating a snap

This tutorial will demonstrate how to use [Snapcraft](https://github.com/snapcore/snapcraft "https://github.com/snapcore/snapcraft") to create a new snap, and then how to use it. First, let us install Snapcraft. 
```
$ sudo snap install --classic snapcraft
```
(Note that the snapcraft Debian package from the apt repositories is largely deprecated. One should use the snap package.) Snapcraft has built-in support for Catkin. In order for it to know which project components to include, you must ensure that your projects have install rules. For our example, we will use roscpp\_tutorials from the [ros\_tutorials](https://github.com/ros/ros_tutorials/tree/noetic-devel/roscpp_tutorials "https://github.com/ros/ros_tutorials/tree/noetic-devel/roscpp_tutorials"). Initialize a new Snapcraft project here: 
```
$ mkdir ~/roscpp_tutorials_snap
$ cd ~/roscpp_tutorials_snap
$ snapcraft init
```
This will create a file in a subdirectory *snap/snapcraft.yaml* 
### The snapcraft file

Open that *snap/snapcraft.yaml* file and make copy over the following: 
```
name: ros-talker-listener
version: '0.1'
summary: ROS Talker/Listener Example
description: |
 This example launches a ROS talker and listener.

confinement: devmode
base: core20

parts:
 ros-tutorials:
   plugin: catkin
   source: https://github.com/ros/ros_tutorials.git
   source-branch: noetic-devel
   source-subdir: roscpp_tutorials
   stage-packages:
       - ros-noetic-roslaunch

apps:
 ros-talker-listener:
   command: opt/ros/noetic/bin/roslaunch roscpp_tutorials talker_listener.launch
   extensions: [ros1-noetic]
```
Don’t worry, we will break it down together. 
#### Metadata

```
name: ros-talker-listener
version: '0.1'
summary: ROS Talker/Listener Example
description: |
 This example launches a ROS talker and listener.
```
This is the basic [metadata](https://snapcraft.io/docs/snapcraft-top-level-metadata "https://snapcraft.io/docs/snapcraft-top-level-metadata") that all snaps require. These fields are fairly self-explanatory but note that the name must be globally unique across all snaps. 
#### Base

```
base: core20
```
The [base](https://snapcraft.io/docs/base-snaps "https://snapcraft.io/docs/base-snaps") keyword defines a special kind of snap that provides a run-time environment with a minimal set of libraries that are common to most applications. [Core20](https://snapcraft.io/core20 "https://snapcraft.io/core20") is the current standard base for snap building and is based on [Ubuntu 20.04 LTS](http://releases.ubuntu.com/20.04/ "http://releases.ubuntu.com/20.04/"). It is, therefore, the base used for Noetic. 
#### Security model

```
confinement: devmode
```
To get started, we won’t confine this application. Unconfined applications, specified with *[devmode](https://snapcraft.io/docs/snap-confinement "https://snapcraft.io/docs/snap-confinement")*, can only be released to the [edge](https://snapcraft.io/docs/channels "https://snapcraft.io/docs/channels") channel of the snapcraft store. 
#### Parts

```
parts:
 ros-tutorials:
   plugin: catkin
   source: https://github.com/ros/ros_tutorials.git
   source-branch: noetic-devel
   source-subdir: roscpp_tutorials
   stage-packages:
       - ros-noetic-roslaunch
```
Parts define how to build your app. In this case, we have one: *ros-tutorials*. Parts can point to local directories, remote git repositories, or tarballs. Here, we specify our source as a [GitHub](/GitHub "/GitHub") repository at a specific branch. We also specifically tell Catkin to build the *roscpp\_tutorials* subdirectory. Furthermore, we tell snapcraft that packages such as make are necessary at build time while the package *ros-noetic-roslaunch* is necessary at build time. For more information about the plugin and it options, please refer to the [online documentation](https://snapcraft.io/docs/catkin-plugin "https://snapcraft.io/docs/catkin-plugin"). The Catkin packages you’re building must have install rules, or the snapcraft CLI won’t know which components to place into the snap. Make sure you install binaries, libraries, header files, launch files, etc. 
#### Apps

```
apps:
 ros-talker-listener:
   command: opt/ros/noetic/bin/roslaunch roscpp_tutorials talker_listener.launch
   extensions: [ros1-noetic]
```
Apps are the commands exposed to end users. Each key under apps is the command name that should be made available on users’ systems. The command keyword specifies the command to be run, as its name suggests. Finally, the extensions *[ros1-noetic](https://snapcraft.io/docs/ros1-extension "https://snapcraft.io/docs/ros1-extension")* essentially sets up the ROS2 apt package repository together with the necessary environment variables. 
### Building the snap

Now that we are all set up, let’s build the snap: 
```
$ cd ~/roscpp_tutorials_snap
$ snapcraft --enable-experimental-extensions
*EXPERIMENTAL* extensions enabled.
Launching a VM.
Launched: snapcraft-ros-talker-listener
[...]
Snapped ros-talker-listener_0.1_amd64.snap
```
That will take a few minutes. From the logs, and among other things, you will see Snapcraft using [rosdep](http://docs.ros.org/independent/api/rosdep/html/ "http://docs.ros.org/independent/api/rosdep/html/") to pull the dependencies of your package but also Catkin building your application. That is because internally, Snapcraft relies on the familiar ROS tool. 
## Testing the snap

This snap is completely standalone: it includes ROS and your application, meaning that you don’t even need to install ROS on your system. Let’s test it out: 
```
$ sudo snap install ros-talker-listener_0.1_amd64.snap --devmode
```
Note that we use --devmode here because the snap is devmode confinement. The moment of truth, will it run? 
```
$ ros-talker-listener
```

```
[ INFO] [1497643945.491444894]: hello world 0
[ INFO] [1497643945.495444894]: I heard: [hello world 0]
[ INFO] [1497643945.591430533]: hello world 1
[ INFO] [1497643945.595430533]: I heard: [hello world 1]
[ INFO] [1497643945.691426519]: hello world 2
[ INFO] [1497643945.695426519]: I heard: [hello world 2]
[ INFO] [1497643945.791444793]: hello world 3
[ INFO] [1497643945.795444793]: I heard: [hello world 3]
```
It does! We see the expected output! You can find more information about snap on the [snapcraft](https://snapcraft.io/docs "https://snapcraft.io/docs") documentation and [ROS snap page](https://snapcraft.io/docs/ros-applications "https://snapcraft.io/docs/ros-applications"). 

## Creating a snap

This tutorial will demonstrate how to use [Snapcraft](https://github.com/snapcore/snapcraft "https://github.com/snapcore/snapcraft") to create a new snap, and how to use it. First, let us install Snapcraft. 
```
$ sudo snap install --classic snapcraft
```
(Note that the snapcraft Debian package from the apt repositories is largely deprecated. One should use the snap package.) Snapcraft has built-in support for Catkin. In order for it to know which project components to include, you must ensure that your projects have install rules. For our example, we will use roscpp\_tutorials from the [ros\_tutorials](https://github.com/ros/ros_tutorials/tree/melodic-devel/roscpp_tutorials "https://github.com/ros/ros_tutorials/tree/melodic-devel/roscpp_tutorials"). Initialize a new Snapcraft project here: 
```
$ mkdir ~/roscpp_tutorials_snap
$ cd ~/roscpp_tutorials_snap
$ snapcraft init
```
This will create a file in a subdirectory *snap/snapcraft.yaml* 
### The snapcraft file

Open that *snap/snapcraft.yaml* file and copy over the following: 
```
name: ros-talker-listener
version: '0.1'
summary: ROS Talker/Listener Example
description: |
 This example launches a ROS talker and listener.
confinement: devmode
base: core18

parts:
 ros-tutorials:
   plugin: catkin
   source: https://github.com/ros/ros_tutorials.git
   source-branch: melodic-devel
   source-space: roscpp_tutorials/

apps:
 ros-talker-listener:
   command: roslaunch roscpp_tutorials talker_listener.launch
```
Don't worry, we will break it down together. 
#### Metadata

```
name: ros-talker-listener
version: '0.1'
summary: ROS Talker/Listener Example
description: |
 This example launches a ROS talker and listener.
```
This is the basic [metadata](https://snapcraft.io/docs/snapcraft-top-level-metadata "https://snapcraft.io/docs/snapcraft-top-level-metadata") that all snaps require. These fields are fairly self-explanatory but note that the name must be globally unique across all snaps. 
#### Base

```
base: core18
```
The [base](https://snapcraft.io/docs/base-snaps "https://snapcraft.io/docs/base-snaps") keyword defines a special kind of snap that provides a run-time environment with a minimal set of libraries that are common to most applications. [Core18](https://snapcraft.io/core18 "https://snapcraft.io/core18") is the current standard base for snap building and is based on [Ubuntu 18.04 LTS](http://releases.ubuntu.com/18.04/ "http://releases.ubuntu.com/18.04/"). It is, therefore, the base used for Melodic. 
#### Security model

```
confinement: devmode
```
To get started, we won’t confine this application. Unconfined applications, specified with *[devmode](https://snapcraft.io/docs/snap-confinement "https://snapcraft.io/docs/snap-confinement")*, can only be released to the [edge](https://snapcraft.io/docs/channels "https://snapcraft.io/docs/channels") channel of the snapcraft store. 
#### Parts

```
parts:
 ros-tutorials:
   plugin: catkin
   source: https://github.com/ros/ros_tutorials.git
   source-branch: melodic-devel
   source-space: roscpp_tutorials/
```
Parts define how to build your app. In this case, we have one: *ros-tutorials*. Parts can point to local directories, remote git repositories, or tarballs. Here, we specify our source as a [GitHub](/GitHub "/GitHub") repository at a specific branch. We also specifically tell Catkin to build the *roscpp\_tutorials* subdirectory. For more information about the plugin and it options, please refer to the [online documentation](https://snapcraft.io/docs/catkin-plugin "https://snapcraft.io/docs/catkin-plugin"). The Catkin packages you’re building must have install rules, or the snapcraft CLI won’t know which components to place into the snap. Make sure you install binaries, libraries, header files, launch files, etc. 
#### Apps

```
apps:
 ros-talker-listener:
   command: roslaunch roscpp_tutorials talker_listener.launch
```
Apps are the commands exposed to end users. Each key under apps is the command name that should be made available on users’ systems. The command keyword specifies the command to be run as its name suggests. 
### Building the snap

Now that we are all set up, let’s build the snap: 
```
$ cd ~/roscpp_tutorials_snap
$ snapcraft
*EXPERIMENTAL* extensions enabled.
Launching a VM.
Launched: snapcraft-ros-talker-listener
[...]
Snapped ros-talker-listener_0.1_amd64.snap
```
That will take a few minutes. From the logs, and among other things, you will see Snapcraft using [rosdep](http://docs.ros.org/independent/api/rosdep/html/ "http://docs.ros.org/independent/api/rosdep/html/") to pull the dependencies of your package but also Catkin building your application. That is because internally, Snapcraft relies on the familiar ROS tool. 
## Testing the snap

This snap is completely standalone: it includes ROS and your application, meaning that you don’t even need to install ROS on your system. Let's test it out: 
```
$ sudo snap install ros-talker-listener_0.1_amd64.snap --devmode
```
Note that we use --devmode here because the snap is devmode confinement. The moment of truth, will it run? 
```
$ ros-talker-listener
```

```
[ INFO] [1497643945.491444894]: hello world 0
[ INFO] [1497643945.495444894]: I heard: [hello world 0]
[ INFO] [1497643945.591430533]: hello world 1
[ INFO] [1497643945.595430533]: I heard: [hello world 1]
[ INFO] [1497643945.691426519]: hello world 2
[ INFO] [1497643945.695426519]: I heard: [hello world 2]
[ INFO] [1497643945.791444793]: hello world 3
[ INFO] [1497643945.795444793]: I heard: [hello world 3]
```
It does! We see the expected output! You can find more information about snap on the [snapcraft](https://snapcraft.io/docs "https://snapcraft.io/docs") documentation and [ROS snap page](https://snapcraft.io/docs/ros-applications "https://snapcraft.io/docs/ros-applications"). 

## Creating a snap

This tutorial will demonstrate how to use [Snapcraft](https://github.com/snapcore/snapcraft "https://github.com/snapcore/snapcraft") to create a new snap, and then the usage. First, install Snapcraft. It’s recommended to install it from the Snap Store: 
```
$ sudo snap install --classic snapcraft
```
(Note that using the apt repositories for snapcraft is not recommended and this tutorial will assume that you installed the snap.) Snapcraft has built-in support for Catkin: you point it at a workspace, and tell it what packages to include in the snap. In order for it to know which project components to include, you must ensure that your projects have good install rules. Let's do that now. Open up your [CMakeLists.txt](/catkin/CMakeLists.txt "/catkin/CMakeLists.txt") with rosed beginner\_tutorials CMakeLists.txt. If you followed the [Python](/ROS/Tutorials/WritingPublisherSubscriber%28python%29 "/ROS/Tutorials/WritingPublisherSubscriber%28python%29") tutorial, add the install target at the end so that it looks like this (unused bits and comments removed): 
```
cmake_minimum_required(VERSION 2.8.3)
project(beginner_tutorials)

## Find catkin and any catkin packages
find_package(catkin REQUIRED COMPONENTS roscpp rospy std_msgs genmsg)

## Declare ROS messages and services
add_message_files(FILES Num.msg)
add_service_files(FILES AddTwoInts.srv)

## Generate added messages and services
generate_messages(DEPENDENCIES std_msgs)

## Declare a catkin package
catkin_package()

include_directories(include ${catkin_INCLUDE_DIRS})

## Install scripts
install(PROGRAMS scripts/talker.py scripts/listener.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```
If you followed the [C++](/ROS/Tutorials/WritingPublisherSubscriber%28c%2B%2B%29 "/ROS/Tutorials/WritingPublisherSubscriber%28c%2B%2B%29") tutorial, add the install target at the end so that the [CMakeLists.txt](/catkin/CMakeLists.txt "/catkin/CMakeLists.txt") looks like this: 
```
cmake_minimum_required(VERSION 2.8.3)
project(beginner_tutorials)

## Find catkin and any catkin packages
find_package(catkin REQUIRED COMPONENTS roscpp rospy std_msgs genmsg)

## Declare ROS messages and services
add_message_files(FILES Num.msg)
add_service_files(FILES AddTwoInts.srv)

## Generate added messages and services
generate_messages(DEPENDENCIES std_msgs)

## Declare a catkin package
catkin_package()

## Build talker and listener
include_directories(include ${catkin_INCLUDE_DIRS})

add_executable(talker src/talker.cpp)
target_link_libraries(talker ${catkin_LIBRARIES})
add_dependencies(talker beginner_tutorials_generate_messages_cpp)

add_executable(listener src/listener.cpp)
target_link_libraries(listener ${catkin_LIBRARIES})
add_dependencies(listener beginner_tutorials_generate_messages_cpp)

## Install talker and listener
install(TARGETS talker listener
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```
Change to the root of the catkin workspace you used in the "writing a simple publisher and subscriber" tutorial: 
```
# This workspace should contain the beginner_tutorials package.
$ cd ~/catkin_ws
```
Initialize a new Snapcraft project here: 
```
$ snapcraft init
Created snap/snapcraft.yaml.
Edit the file to your liking or run `snapcraft` to get started
```

### The snapcraft.yaml

Open that snap/snapcraft.yaml file and make it look like this: 
```
name: publisher-subscriber
base: core
version: '0.1'
summary: ROS Example
description: |
  The ROS publisher/subscriber example packaged as a snap.

grade: stable
confinement: strict

parts:
  workspace:
    plugin: catkin
    source: .
    catkin-packages: [beginner_tutorials]

apps:
  roscore:
    command: roscore
    plugs: [network, network-bind]

  talker:
    # Use talker.py if you followed the Python tutorial
    command: rosrun beginner_tutorials talker
    plugs: [network, network-bind]

  listener:
    # Use listener.py if you followed the Python tutorial
    command: rosrun beginner_tutorials listener
    plugs: [network, network-bind]
```

### The snapcraft.yaml explained

Let's break that down piece by piece. 
```
name: publisher-subscriber
base: core
version: '0.1'
summary: ROS Example
description: |
  The ROS publisher/subscriber example packaged as a snap.
```
This is the basic metadata that all snaps require. These fields are fairly self-explanatory, but note that the name must be globally unique among all snaps. The one that is probably not obvious is base. A base is a special kind of snap that provides a minimal set of libraries common to most applications. A base snap mounts itself as the root filesystem within your snap so that when your application runs, the base's library paths are searched directly after the paths for your specific snap. In our case, we're using base: core which is a rootfs generated from Ubuntu 16.04 (Xenial). As a result, snapcraft understands what you're wanting to use ROS Kinetic. Another option would be to use base: core18, which is a rootfs generated from Ubuntu 18.04 (Bionic), thereby causing snapcraft to use ROS Melodic. 
```
grade: stable
confinement: strict
```
grade can be either stable or devel. If it's devel, the store will prevent you from releasing into one of the two stable channels (stable and candidate, specifically)-- think of it as a safety net to prevent accidental releases. If it's stable, you can release it anywhere. confinement can be strict, devmode, or classic. strict enforces confinement, whereas devmode allows all accesses, even those that would be disallowed under strict confinement (and logs accesses that would otherwise be disallowed for your reference). classic is even less confined than devmode, in that it doesn't even get private namespaces anymore (among other things). There is [more extensive documentation on confinement available](https://snapcraft.io/docs/snap-confinement "https://snapcraft.io/docs/snap-confinement"). 
```
parts:
  workspace:
    plugin: catkin
    source: .
    catkin-packages: [beginner_tutorials]
```
Snapcraft is responsible for taking many disparate parts and orchestrating them all into one cohesive snap. You tell it the parts that make up your snap, and it takes care of the rest. Here, we tell Snapcraft that we have a single part called workspace. We specify that it builds with Catkin, and we specify the packages in this workspace that we want included in the snap. In our case, we only have one: the beginner\_tutorials package we've been working on through the tutorials. Note that this is not required: if you leave catkin-packages off entirely, Snapcraft will build all packages in the workspace. 
```
apps:
  roscore:
    command: roscore
    plugs: [network, network-bind]

  talker:
    # Use talker.py if you followed the Python tutorial
    command: rosrun beginner_tutorials talker
    plugs: [network, network-bind]

  listener:
    # Use listener.py if you followed the Python tutorial
    command: rosrun beginner_tutorials listener
    plugs: [network, network-bind]
```
Now things get a little interesting. When this snap is built, it will include a complete ROS system: roscpp, rospy, roscore, your ROS workspace, etc. It's a standalone unit, and you're in complete control over how the user interacts with it. You exercise that control via the apps keyword, where you expose specific commands to the user. Here we simply expose the three components of the publisher/subscriber tutorial: roscore, the talker, and the listener. We could just as easily written a [launch file](http://wiki.ros.org/roslaunch "http://wiki.ros.org/roslaunch") to bring up the entire system in a single app. We use plugs to specify that each app requires network access ([read more about interfaces](https://snapcraft.io/docs/core/interfaces "https://snapcraft.io/docs/core/interfaces")). Without this, each app would be confined such that they couldn't communicate. 
### Actually create the snap

That's it: time to build the snap. 
```
$ cd ~/catkin_ws
$ snapcraft
```
That will take a few minutes. You may be prompted to install multipass, a tool used by snapcraft to ensure build isolation (so it doesn't dirty up your host when building). You'll see Snapcraft fetch [rosdep](http://docs.ros.org/independent/api/rosdep/html/ "http://docs.ros.org/independent/api/rosdep/html/"), which is then used to determine the dependencies of the ROS packages in the workspace. It then pulls those down and puts them into the snap along with roscore. Finally, it builds the requested packages in the workspace, and installs them into the snap as well. At the end, you'll have your snap. 
## Testing the snap

As we discussed previously, this snap is completely standalone: you could email it to someone and they'd be able to install it and run your ROS system, even if they didn't have ROS installed themselves. Test it out yourself: 
```
# We use --dangerous here because the snap doesn't come from an
# authenticated source
$ sudo snap install --dangerous publisher-subscriber_0.1_amd64.snap
```
Now you can take it for a spin just like you did when [examining the simple publisher and subscriber](/ROS/Tutorials/ExaminingPublisherSubscriber "/ROS/Tutorials/ExaminingPublisherSubscriber"). First, run roscore: 
```
$ publisher-subscriber.roscore
```
Now run the publisher: 
```
$ publisher-subscriber.talker
```
And you'll see the familiar output: 
```
[ INFO] [1497643945.491444894]: hello world 5
[ INFO] [1497643945.591430533]: hello world 6
[ INFO] [1497643945.691426519]: hello world 7
[ INFO] [1497643945.791444793]: hello world 8
[ INFO] [1497643945.891433313]: hello world 9
```
Now let's run the listener: 
```
$ publisher-subscriber.listener
```
And you'll see the this project works exactly the same as before: 
```
[ INFO] [1497643969.443662208]: I heard: [hello world 41]
[ INFO] [1497643969.543668530]: I heard: [hello world 42]
[ INFO] [1497643969.643621679]: I heard: [hello world 43]
[ INFO] [1497643969.743650720]: I heard: [hello world 44]
[ INFO] [1497643969.843650108]: I heard: [hello world 45]
```
When you're done, as usual, press Ctrl-C to terminate roscore, as well as the talker and listener. 

## Sharing the snap with the world

Emailing snaps to people doesn't scale, but more importantly, it gives the snap users no upgrade path. If you make your snap available in the [snap store](https://snapcraft.io/ "https://snapcraft.io/"), whenever you release a new version, your robots (or users) will automatically update. In order to do this, you'll need to create a (free) store account at [snapcraft.io](https://snapcraft.io/ "https://snapcraft.io/"). Then, using Snapcraft, login with that account: 
```
$ snapcraft login
```
Remember our previous discussion about how snap names need to be unique. Before you can release your snap in the store, you need to register the snap name to your store account: 
```
$ snapcraft register <my snap name>
```
Finally, push the snap up to the store and release it into the stable channel: 
```
$ snapcraft push path/to/my.snap --release=stable
```
Once the upload and automated reviews finish successfully, anyone in the world can install your snap as simply as: 
```
$ sudo snap install <my snap name>
```
And they can rest secure knowing that when you release an update, they'll get it, no further work required. 

Wiki: ROS/Tutorials/Packaging your ROS project as a snap (last edited 2022-03-25 11:15:21 by [GuillaumeBeuzeboc](/GuillaumeBeuzeboc "GuillaumeBeuzeboc @ 2a01:e0a:322:7130:cd86:8c7a:f413:222c[2a01:e0a:322:7130:cd86:8c7a:f413:222c]"))

Except where otherwise noted, the ROS wiki is licensed under the   

