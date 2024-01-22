

 var \_gaq = \_gaq || [];
 \_gaq.push(['\_setAccount', 'UA-17821189-2']);
 \_gaq.push(['\_setDomainName', 'wiki.ros.org']);
 \_gaq.push(['\_trackPageview']);

 (function() {
 var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
 ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
 var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
 })();

ROS/Tutorials/CreatingMsgAndSrv(plain cmake) - ROS Wiki

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
* [CreatingMsgAndSrv(plain cmake)](/ROS/Tutorials/CreatingMsgAndSrv%28plain%20cmake%29 "/ROS/Tutorials/CreatingMsgAndSrv%28plain%20cmake%29")

#### ROS 2 Documentation

The ROS Wiki is for ROS 1. Are you using ROS 2 ([Humble](http://docs.ros.org/en/humble/ "http://docs.ros.org/en/humble/"), [Iron](http://docs.ros.org/en/iron/ "http://docs.ros.org/en/iron/"), or [Rolling](http://docs.ros.org/en/rolling/ "http://docs.ros.org/en/rolling/"))?   
[Check out the ROS 2 Project Documentation](http://docs.ros.org "http://docs.ros.org")  
Package specific documentation can be found on [index.ros.org](https://index.ros.org "https://index.ros.org")

# Wiki

* [Distributions](/Distributions "/Distributions")
* [ROS/Installation](/ROS/Installation "/ROS/Installation")
* [ROS/Tutorials](/ROS/Tutorials "/ROS/Tutorials")
* [RecentChanges](/RecentChanges "/RecentChanges")
* [CreatingMsg...lain cmake)](/ROS/Tutorials/CreatingMsgAndSrv%28plain%20cmake%29 "/ROS/Tutorials/CreatingMsgAndSrv%28plain%20cmake%29")

# Page

* Immutable Page
* [Comments](# "#")
* [Info](/action/info/ROS/Tutorials/CreatingMsgAndSrv%28plain%20cmake%29?action=info "/action/info/ROS/Tutorials/CreatingMsgAndSrv%28plain%20cmake%29?action=info")
* [Attachments](/action/AttachFile/ROS/Tutorials/CreatingMsgAndSrv%28plain%20cmake%29?action=AttachFile "/action/AttachFile/ROS/Tutorials/CreatingMsgAndSrv%28plain%20cmake%29?action=AttachFile")
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

* [Login](/action/login/ROS/Tutorials/CreatingMsgAndSrv%28plain%20cmake%29?action=login "/action/login/ROS/Tutorials/CreatingMsgAndSrv%28plain%20cmake%29?action=login")

|  |
| --- |
| **Note:** This tutorial assumes that you have completed the previous tutorials: [installing ROS](/ROS/Tutorials/InstallingandConfiguringROSEnvironment "/ROS/Tutorials/InstallingandConfiguringROSEnvironment").  |

|  |
| --- |
| (!) Please ask about problems and questions regarding this tutorial on [answers.ros.org](http://answers.ros.org "http://answers.ros.org"). Don't forget to include in your question the link to this page, the versions of your OS & ROS, and also add appropriate tags. |

# Creating a ROS msg and srv (plain cmake)

**Description:** This tutorial covers how to create and build msg and srv files using plain cmake (i.e., not [catkin](/catkin "/catkin")).  

**Tutorial Level:** BEGINNER  

 Contents1. [Making a directory in which to work](#Making_a_directory_in_which_to_work "#Making_a_directory_in_which_to_work")
2. [Introduction to msg and srv](#ROS.2FTutorials.2FCreatingMsgAndSrv.Introduction_to_msg_and_srv "#ROS.2FTutorials.2FCreatingMsgAndSrv.Introduction_to_msg_and_srv")
3. [Using msg](#Using_msg "#Using_msg")
	1. [Creating a msg](#Creating_a_msg "#Creating_a_msg")
	2. [Using an existing msg (C++)](#Using_an_existing_msg_.28C.2B-.2B-.29 "#Using_an_existing_msg_.28C.2B-.2B-.29")
	3. [Using the new message in code (C++)](#Using_the_new_message_in_code_.28C.2B-.2B-.29 "#Using_the_new_message_in_code_.28C.2B-.2B-.29")
	4. [Using existing and new messages in code (Python)](#Using_existing_and_new_messages_in_code_.28Python.29 "#Using_existing_and_new_messages_in_code_.28Python.29")
	5. [Building messages and code](#Building_messages_and_code "#Building_messages_and_code")
	6. [Running the code](#Running_the_code "#Running_the_code")
4. [Using srv](#Using_srv "#Using_srv")

 **Note:** Be sure that you have already [installed ROS](/ROS/Installation "/ROS/Installation") and remember that you must [source the appropriate setup file](/ROS/Tutorials/InstallingandConfiguringROSEnvironment#Managing_Your_Environment "/ROS/Tutorials/InstallingandConfiguringROSEnvironment#Managing_Your_Environment") in every shell you create. 

## Making a directory in which to work

To help keep yourself organized, make a directory in which to work. You can use any name; we'll just call it msgsrv: 
```
mkdir -p msgsrv
cd msgsrv
```

## Introduction to msg and srv

* [msg](/msg "/msg"): msg files are simple text files that describe the fields of a ROS message. They are used to generate source code for messages in different languages.
* [srv](/srv "/srv"): an srv file describes a service. It is composed of two parts: a request and a response.

msgs are just simple text files with a field type and field name per line. The field types you can use are: * int8, int16, int32, int64 (plus uint\*)
* float32, float64
* string
* time, duration
* other msg files
* variable-length array[] and fixed-length array[C]

There is also a special type in ROS: Header, the header contains a timestamp and coordinate frame information that are commonly used in ROS. You will frequently see the first line in a msg file have Header header. Here is an example of a msg that uses a Header, a string primitive, and two other msgs : 
```
  Header header
  string child_frame_id
  geometry_msgs/PoseWithCovariance pose
  geometry_msgs/TwistWithCovariance twist
```
srv files are just like msg files, except they contain two parts: a request and a response. The two parts are separated by a '---' line. Here is an example of a srv file: 
```
int64 A
int64 B
---
int64 Sum
```
In the above example, A and B are the request, and Sum is the response. 

## Using msg

### Creating a msg

Let's define a couple of new messages. Create a file named Foo.msg and put the following in it: *[https://raw.githubusercontent.com/gerkey/ros1\_external\_use/master/ros1\_msgs/Foo.msg](https://raw.githubusercontent.com/gerkey/ros1_external_use/master/ros1_msgs/Foo.msg "https://raw.githubusercontent.com/gerkey/ros1_external_use/master/ros1_msgs/Foo.msg")* 

function isnumbered(obj) {
 return obj.childNodes.length && obj.firstChild.childNodes.length && obj.firstChild.firstChild.className == 'LineNumber';
}
function nformat(num,chrs,add) {
 var nlen = Math.max(0,chrs-(''+num).length), res = '';
 while (nlen>0) { res += ' '; nlen-- }
 return res+num+add;
}
function addnumber(did, nstart, nstep) {
 var c = document.getElementById(did), l = c.firstChild, n = 1;
 if (!isnumbered(c)) {
 if (typeof nstart == 'undefined') nstart = 1;
 if (typeof nstep == 'undefined') nstep = 1;
 var n = nstart;
 while (l != null) {
 if (l.tagName == 'SPAN') {
 var s = document.createElement('SPAN');
 var a = document.createElement('A');
 s.className = 'LineNumber';
 a.appendChild(document.createTextNode(nformat(n,4,'')));
 a.href = '#' + did + '\_' + n;
 s.appendChild(a);
 s.appendChild(document.createTextNode(' '));
 n += nstep;
 if (l.childNodes.length) {
 l.insertBefore(s, l.firstChild);
 }
 else {
 l.appendChild(s);
 }
 }
 l = l.nextSibling;
 }
 }
 return false;
}
function remnumber(did) {
 var c = document.getElementById(did), l = c.firstChild;
 if (isnumbered(c)) {
 while (l != null) {
 if (l.tagName == 'SPAN' && l.firstChild.className == 'LineNumber') l.removeChild(l.firstChild);
 l = l.nextSibling;
 }
 }
 return false;
}
function togglenumber(did, nstart, nstep) {
 var c = document.getElementById(did);
 if (isnumbered(c)) {
 remnumber(did);
 } else {
 addnumber(did,nstart,nstep);
 }
 return false;
}

document.write('<a href="#" onclick="return togglenumber(\'CA-9dea6aec6f28a7cb07ab3a24127a1364ddb5b10c\', 1, 1);" \
 class="codenumbers">Toggle line numbers<\/a>');

```
 [1](#CA-9dea6aec6f28a7cb07ab3a24127a1364ddb5b10c_1 "#CA-9dea6aec6f28a7cb07ab3a24127a1364ddb5b10c_1") int16 foo

```
 Create a file named Bar.msg and put the following in it: *[https://raw.githubusercontent.com/gerkey/ros1\_external\_use/master/ros1\_msgs/Bar.msg](https://raw.githubusercontent.com/gerkey/ros1_external_use/master/ros1_msgs/Bar.msg "https://raw.githubusercontent.com/gerkey/ros1_external_use/master/ros1_msgs/Bar.msg")* 

document.write('<a href="#" onclick="return togglenumber(\'CA-42a810b9c34eda5f0725a49521ee8c237ded5d6b\', 1, 1);" \
 class="codenumbers">Toggle line numbers<\/a>');

```
 [1](#CA-42a810b9c34eda5f0725a49521ee8c237ded5d6b_1 "#CA-42a810b9c34eda5f0725a49521ee8c237ded5d6b_1") uint16 bar
 [2](#CA-42a810b9c34eda5f0725a49521ee8c237ded5d6b_2 "#CA-42a810b9c34eda5f0725a49521ee8c237ded5d6b_2") # Use messages from other packages
 [3](#CA-42a810b9c34eda5f0725a49521ee8c237ded5d6b_3 "#CA-42a810b9c34eda5f0725a49521ee8c237ded5d6b_3") geometry\_msgs/Pose pose
 [4](#CA-42a810b9c34eda5f0725a49521ee8c237ded5d6b_4 "#CA-42a810b9c34eda5f0725a49521ee8c237ded5d6b_4") map\_msgs/ProjectedMap map

```

### Using an existing msg (C++)

To have a simple C++ example of using an existing ROS message in code, create a file named use\_existing\_msg.cpp and put the following in it: *[https://raw.githubusercontent.com/gerkey/ros1\_external\_use/master/ros1\_msgs/use\_existing\_msg.cpp](https://raw.githubusercontent.com/gerkey/ros1_external_use/master/ros1_msgs/use_existing_msg.cpp "https://raw.githubusercontent.com/gerkey/ros1_external_use/master/ros1_msgs/use_existing_msg.cpp")* 
```
#include <sensor_msgs/LaserScan.h>
#include <stdio.h>
int
main(void)
{
  sensor_msgs::LaserScan scan;
  for(int i=0; i<100; i++)
    scan.ranges.push_back(42.0*i);

  for(std::vector<float>::const_iterator it = scan.ranges.begin();
      it != scan.ranges.end();
      ++it)
    printf("%f\n", *it);
}
```

### Using the new message in code (C++)

To have a simple C++ example of how to use custom messages from code, create a file named use\_custom\_msg.cpp and put the following in it: *[https://raw.githubusercontent.com/gerkey/ros1\_external\_use/master/ros1\_msgs/use\_custom\_msg.cpp](https://raw.githubusercontent.com/gerkey/ros1_external_use/master/ros1_msgs/use_custom_msg.cpp "https://raw.githubusercontent.com/gerkey/ros1_external_use/master/ros1_msgs/use_custom_msg.cpp")* 
```
#include <myproject/Foo.h>
#include <myproject/Bar.h>
#include <stdio.h>
int
main(void)
{
  myproject::Foo foo;
  foo.foo = 42;
  printf("%d\n", foo.foo);

  myproject::Bar bar;
}
```

### Using existing and new messages in code (Python)

To have a simple Python example of using both existing and new messages in code, create a file named use\_msgs.py and put the following in it: *[https://raw.githubusercontent.com/gerkey/ros1\_external\_use/master/ros1\_msgs/use\_msgs.py](https://raw.githubusercontent.com/gerkey/ros1_external_use/master/ros1_msgs/use_msgs.py "https://raw.githubusercontent.com/gerkey/ros1_external_use/master/ros1_msgs/use_msgs.py")* 
```
#!/usr/bin/env python

from sensor_msgs.msg import LaserScan
from myproject.msg import Foo

f = Foo(42)
print(f.foo)

s = LaserScan()
```

### Building messages and code

To use custom messages, we need to run the code generators provided by ROS to process .msg files into code for use in C++, Python, and other languages. Create a file named CMakeLists.txt and put the following in it: *[https://raw.githubusercontent.com/gerkey/ros1\_external\_use/master/ros1\_msgs/CMakeLists.txt](https://raw.githubusercontent.com/gerkey/ros1_external_use/master/ros1_msgs/CMakeLists.txt "https://raw.githubusercontent.com/gerkey/ros1_external_use/master/ros1_msgs/CMakeLists.txt")* 

document.write('<a href="#" onclick="return togglenumber(\'CA-38677fe1b379e35c281776fe1d450fc1ceb7130b\', 1, 1);" \
 class="codenumbers">Toggle line numbers<\/a>');

```
 [1](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_1 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_1") cmake\_minimum\_required(VERSION 2.8.3)
 [2](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_2 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_2") project(myproject)
 [3](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_3 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_3") 
 [4](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_4 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_4") # Build an executable that uses an existing ROS msg: find\_package() the ROS
 [5](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_5 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_5") # package that contains the message, then use its reported include directories.
 [6](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_6 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_6") find\_package(sensor\_msgs REQUIRED)
 [7](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_7 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_7") include\_directories(${sensor\_msgs\_INCLUDE\_DIRS})
 [8](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_8 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_8") add\_executable(use\_existing\_msg use\_existing\_msg.cpp)
 [9](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_9 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_9") 
 [10](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_10 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_10") # Generate code from our own custom messages
 [11](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_11 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_11") # find\_package catkin and genmsg, required for message generation macros
 [12](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_12 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_12") find\_package(catkin REQUIRED)
 [13](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_13 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_13") find\_package(genmsg REQUIRED)
 [14](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_14 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_14") # find\_package the other message packages that our custom messages use
 [15](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_15 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_15") find\_package(geometry\_msgs REQUIRED)
 [16](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_16 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_16") find\_package(map\_msgs REQUIRED)
 [17](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_17 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_17") # Enumerate our custom messages files
 [18](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_18 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_18") add\_message\_files(DIRECTORY ${CMAKE\_CURRENT\_SOURCE\_DIR} FILES Foo.msg Bar.msg)
 [19](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_19 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_19") # Do code generation, specifying which other message packages we depend on.
 [20](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_20 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_20") generate\_messages(DEPENDENCIES geometry\_msgs map\_msgs)
 [21](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_21 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_21") 
 [22](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_22 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_22") # Build an executable that uses our messages, making it depend on the
 [23](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_23 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_23") # message-generation step.
 [24](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_24 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_24") add\_executable(use\_custom\_msg use\_custom\_msg.cpp)
 [25](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_25 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_25") add\_dependencies(use\_custom\_msg ${PROJECT\_NAME}\_generate\_messages)
 [26](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_26 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_26") 
 [27](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_27 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_27") # (optional) Install the executables. The generated code will also
 [28](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_28 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_28") # automatically be installed.
 [29](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_29 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_29") install(TARGETS use\_existing\_msg use\_custom\_msg
 [30](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_30 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_30")  DESTINATION bin)
 [31](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_31 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_31") install(PROGRAMS use\_msgs.py
 [32](#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_32 "#CA-38677fe1b379e35c281776fe1d450fc1ceb7130b_32")  DESTINATION bin)

```
 Process your messages and build your (C++) code in a subdirectory of msgsrv named build using the standard cmake sequence: 
```
mkdir -p build
cd build
cmake ..
make
```

### Running the code

To confirm that everything is working properly, run each of the programs (they won't do anything terribly interesting): 
```
./build/use_existing_msg
```

```
./build/use_custom_msg
```

```
python use_msgs.py
```

## Using srv

**TODO: fill out this section with analogous examples** 

Wiki: ROS/Tutorials/CreatingMsgAndSrv(plain cmake) (last edited 2020-01-10 21:46:19 by [BrianGerkey](/BrianGerkey "gerkey @ 38.98.37.134[38.98.37.134]"))

Except where otherwise noted, the ROS wiki is licensed under the   
