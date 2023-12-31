

 var \_gaq = \_gaq || [];
 \_gaq.push(['\_setAccount', 'UA-17821189-2']);
 \_gaq.push(['\_setDomainName', 'wiki.ros.org']);
 \_gaq.push(['\_trackPageview']);

 (function() {
 var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
 ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
 var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
 })();

ROS/Tutorials/UnderstandingNodes - ROS Wiki

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
* [UnderstandingNodes](/action/fullsearch/ROS/Tutorials/UnderstandingNodes?action=fullsearch&context=180&value=linkto%3A%22ROS%2FTutorials%2FUnderstandingNodes%22 "Click to do a full-text search for this title")

#### ROS 2 Documentation

The ROS Wiki is for ROS 1. Are you using ROS 2 ([Humble](http://docs.ros.org/en/humble/ "http://docs.ros.org/en/humble/"), [Iron](http://docs.ros.org/en/iron/ "http://docs.ros.org/en/iron/"), or [Rolling](http://docs.ros.org/en/rolling/ "http://docs.ros.org/en/rolling/"))?   
[Check out the ROS 2 Project Documentation](http://docs.ros.org "http://docs.ros.org")  
Package specific documentation can be found on [index.ros.org](https://index.ros.org "https://index.ros.org")

# Wiki

* [Distributions](/Distributions "/Distributions")
* [ROS/Installation](/ROS/Installation "/ROS/Installation")
* [ROS/Tutorials](/ROS/Tutorials "/ROS/Tutorials")
* [RecentChanges](/RecentChanges "/RecentChanges")
* [UnderstandingNodes](/ROS/Tutorials/UnderstandingNodes "/ROS/Tutorials/UnderstandingNodes")

# Page

* Immutable Page
* [Comments](# "#")
* [Info](/action/info/ROS/Tutorials/UnderstandingNodes?action=info "/action/info/ROS/Tutorials/UnderstandingNodes?action=info")
* [Attachments](/action/AttachFile/ROS/Tutorials/UnderstandingNodes?action=AttachFile "/action/AttachFile/ROS/Tutorials/UnderstandingNodes?action=AttachFile")
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

* [Login](/action/login/ROS/Tutorials/UnderstandingNodes?action=login "/action/login/ROS/Tutorials/UnderstandingNodes?action=login")

|  |
| --- |
| **Note:** This tutorial assumes that you have completed the previous tutorials: [building a ROS package](/ROS/Tutorials/BuildingPackages "/ROS/Tutorials/BuildingPackages").  |

|  |
| --- |
| (!) Please ask about problems and questions regarding this tutorial on [answers.ros.org](http://answers.ros.org "http://answers.ros.org"). Don't forget to include in your question the link to this page, the versions of your OS & ROS, and also add appropriate tags. |

# Understanding ROS Nodes

**Description:** This tutorial introduces ROS graph concepts and discusses the use of [roscore](/roscore "/roscore"), [rosnode](/rosnode "/rosnode"), and [rosrun](/rosrun "/rosrun") commandline tools.  

**Tutorial Level:** BEGINNER  

**Next Tutorial:** [Understanding ROS topics](/ROS/Tutorials/UnderstandingTopics "/ROS/Tutorials/UnderstandingTopics")  

 Contents1. [Prerequisites](#Prerequisites "#Prerequisites")
2. [Quick Overview of Graph Concepts](#Quick_Overview_of_Graph_Concepts "#Quick_Overview_of_Graph_Concepts")
3. [Nodes](#Nodes "#Nodes")
4. [Client Libraries](#Client_Libraries "#Client_Libraries")
5. [roscore](#roscore "#roscore")
6. [Using rosnode](#Using_rosnode "#Using_rosnode")
7. [Using rosrun](#Using_rosrun "#Using_rosrun")
8. [Review](#Review "#Review")
9. [Video Demonstration](#Video_Demonstration "#Video_Demonstration")

## Prerequisites

For this tutorial we'll use a lighweight simulator, to install it run the following command: 
```
$ sudo apt-get install ros-<distro>-ros-tutorials
```
Replace '<distro>' with the name of your ROS distribution (e.g. indigo, jade, kinetic, noetic) 
## Quick Overview of Graph Concepts

* [Nodes](/Nodes "/Nodes"): A node is an executable that uses ROS to communicate with other nodes.
* [Messages](/Messages "/Messages"): ROS data type used when subscribing or publishing to a topic.
* [Topics](/Topics "/Topics"): Nodes can *publish* messages to a topic as well as *subscribe* to a topic to receive messages.
* [Master](/Master "/Master"): Name service for ROS (i.e. helps nodes find each other)
* [rosout](/rosout "/rosout"): ROS equivalent of stdout/stderr
* [roscore](/roscore "/roscore"): Master + rosout + parameter server (parameter server will be introduced later)

## Nodes

A node really isn't much more than an executable file within a ROS package. ROS nodes use a ROS client library to communicate with other nodes. Nodes can publish or subscribe to a Topic. Nodes can also provide or use a Service. 
## Client Libraries

ROS client libraries allow nodes written in different programming languages to communicate: * rospy = python client library
* roscpp = c++ client library

## roscore

roscore is the first thing you should run when using ROS. Please run: 
```
$ roscore
```
You will see something similar to: * ```
... logging to ~/.ros/log/9cf88ce4-b14d-11df-8a75-00251148e8cf/roslaunch-machine_name-13039.log
Checking log directory for disk usage. This may take awhile.
Press Ctrl-C to interrupt
Done checking log file disk usage. Usage is <1GB.

started roslaunch server http://machine_name:33919/
ros_comm version 1.4.7

SUMMARY
======

PARAMETERS
 * /rosversion
 * /rosdistro

NODES

auto-starting new master
process[master]: started with pid [13054]
ROS_MASTER_URI=http://machine_name:11311/

setting /run_id to 9cf88ce4-b14d-11df-8a75-00251148e8cf
process[rosout-1]: started with pid [13067]
started core service [/rosout]
```

If roscore does not initialize, you probably have a network configuration issue. See [Network Setup - Single Machine Configuration](http://www.ros.org/wiki/ROS/NetworkSetup#Single_machine_configuration "http://www.ros.org/wiki/ROS/NetworkSetup#Single_machine_configuration") If roscore does not initialize and sends a message about lack of permissions, probably the ~/.ros folder is owned by root, change recursively the ownership of that folder with: 
```
$ sudo chown -R <your_username> ~/.ros
```

## Using rosnode

Open up a **new terminal**, and let's use **rosnode** to see what running roscore did... Bear in mind to keep the previous terminal open either by opening a new tab or simply minimizing it. **Note:** When opening a new terminal your environment is reset and your ~/.bashrc file is sourced. If you have trouble running commands like rosnode then you might need to add some environment setup files to your ~/.bashrc or manually re-source them. 

rosnode displays information about the ROS nodes that are currently running. The rosnode list command lists these active nodes: 
```
$ rosnode list
```
* You will see:
* ```
/rosout
```

This showed us that there is only one node running: [rosout](/rosout "/rosout"). This is always running as it collects and logs nodes' debugging output. The rosnode info command returns information about a specific node. 
```
$ rosnode info /rosout
```
This gave us some more information about rosout, such as the fact that it publishes /rosout\_agg. * ```
------------------------------------------------------------------------
Node [/rosout]
Publications:
 * /rosout_agg [rosgraph_msgs/Log]

Subscriptions:
 * /rosout [unknown type]

Services:
 * /rosout/get_loggers
 * /rosout/set_logger_level

contacting node http://machine_name:54614/ ...
Pid: 5092
```

Now, let's see some more nodes. For this, we're going to use rosrun to bring up another node. 
## Using rosrun

rosrun allows you to use the package name to directly run a node within a package (without having to know the package path). Usage: 
```
$ rosrun [package_name] [node_name]
```
So now we can run the turtlesim\_node in the turtlesim package. Then, in a **new terminal**: 
```
$ rosrun turtlesim turtlesim_node
```
You will see the turtlesim window: * ![turtlesim.png](/ROS/Tutorials/UnderstandingNodes?action=AttachFile&do=get&target=turtlesim.png "turtlesim.png")

**NOTE:** The turtle may look different in your turtlesim window. Don't worry about it - there are [many types of turtle](/Distributions#Current_Distribution_Releases "/Distributions#Current_Distribution_Releases") and yours is a surprise! In a **new terminal**: 
```
$ rosnode list
```
You will see something similar to: * ```
/rosout
/turtlesim
```

One powerful feature of ROS is that you can reassign Names from the command-line. Close the turtlesim window to stop the node (or go back to the rosrun turtlesim terminal and use ctrl-C). Now let's re-run it, but this time use a [Remapping Argument](/Remapping%20Arguments "/Remapping%20Arguments") to change the node's name: 
```
$ rosrun turtlesim turtlesim_node __name:=my_turtle
```
Now, if we go back and use rosnode list: 
```
$ rosnode list
```
* You will see something similar to:
* ```
/my_turtle
/rosout
```

Note: If you still see /turtlesim in the list, it might mean that you stopped the node in the terminal using ctrl-C instead of closing the window, or that you don't have the $ROS\_HOSTNAME environment variable defined as described in [Network Setup - Single Machine Configuration](http://www.ros.org/wiki/ROS/NetworkSetup#Single_machine_configuration "http://www.ros.org/wiki/ROS/NetworkSetup#Single_machine_configuration"). You can try cleaning the rosnode list with: $ rosnode cleanup 

We see our new /my\_turtle node. Let's use another rosnode command, ping, to test that it's up: 
```
$ rosnode ping my_turtle
```
* ```
rosnode: node is [/my_turtle]
pinging /my_turtle with a timeout of 3.0s
xmlrpc reply from http://aqy:42235/     time=1.152992ms
xmlrpc reply from http://aqy:42235/     time=1.120090ms
xmlrpc reply from http://aqy:42235/     time=1.700878ms
xmlrpc reply from http://aqy:42235/     time=1.127958ms
```

## Review

What was covered: * roscore = ros+core : master (provides name service for ROS) + rosout (stdout/stderr) + parameter server (parameter server will be introduced later)
* rosnode = ros+node : ROS tool to get information about a node.
* rosrun = ros+run : runs a node from a given package.

Now that you understand how ROS nodes work, let's look at [how ROS topics work](/ROS/Tutorials/UnderstandingTopics "/ROS/Tutorials/UnderstandingTopics"). Also, feel free to press Ctrl-C to stop turtlesim\_node. 
## Video Demonstration

Watch the video below to have more explanation on Python Nodes Communication and step by step guide .  

Wiki: ROS/Tutorials/UnderstandingNodes (last edited 2022-10-18 16:16:55 by [Muhammad Luqman](/Muhammad%20Luqman "Muhammad Luqman @ 103.138.11.4[103.138.11.4]"))

Except where otherwise noted, the ROS wiki is licensed under the   

