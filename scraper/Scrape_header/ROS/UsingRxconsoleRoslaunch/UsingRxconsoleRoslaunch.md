

 var \_gaq = \_gaq || [];
 \_gaq.push(['\_setAccount', 'UA-17821189-2']);
 \_gaq.push(['\_setDomainName', 'wiki.ros.org']);
 \_gaq.push(['\_trackPageview']);

 (function() {
 var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
 ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
 var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
 })();

ROS/Tutorials/UsingRxconsoleRoslaunch - ROS Wiki

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
* [UsingRxconsoleRoslaunch](/action/fullsearch/ROS/Tutorials/UsingRxconsoleRoslaunch?action=fullsearch&context=180&value=linkto%3A%22ROS%2FTutorials%2FUsingRxconsoleRoslaunch%22 "Click to do a full-text search for this title")

#### ROS 2 Documentation

The ROS Wiki is for ROS 1. Are you using ROS 2 ([Humble](http://docs.ros.org/en/humble/ "http://docs.ros.org/en/humble/"), [Iron](http://docs.ros.org/en/iron/ "http://docs.ros.org/en/iron/"), or [Rolling](http://docs.ros.org/en/rolling/ "http://docs.ros.org/en/rolling/"))?   
[Check out the ROS 2 Project Documentation](http://docs.ros.org "http://docs.ros.org")  
Package specific documentation can be found on [index.ros.org](https://index.ros.org "https://index.ros.org")

# Wiki

* [Distributions](/Distributions "/Distributions")
* [ROS/Installation](/ROS/Installation "/ROS/Installation")
* [ROS/Tutorials](/ROS/Tutorials "/ROS/Tutorials")
* [RecentChanges](/RecentChanges "/RecentChanges")
* [UsingRxconsoleRoslaunch](/ROS/Tutorials/UsingRxconsoleRoslaunch "/ROS/Tutorials/UsingRxconsoleRoslaunch")

# Page

* Immutable Page
* [Comments](# "#")
* [Info](/action/info/ROS/Tutorials/UsingRxconsoleRoslaunch?action=info "/action/info/ROS/Tutorials/UsingRxconsoleRoslaunch?action=info")
* [Attachments](/action/AttachFile/ROS/Tutorials/UsingRxconsoleRoslaunch?action=AttachFile "/action/AttachFile/ROS/Tutorials/UsingRxconsoleRoslaunch?action=AttachFile")
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

* [Login](/action/login/ROS/Tutorials/UsingRxconsoleRoslaunch?action=login "/action/login/ROS/Tutorials/UsingRxconsoleRoslaunch?action=login")

|  |
| --- |
| **Note:** This tutorial assumes that you have completed the previous tutorials: [Understanding ROS services and parameters](/ROS/Tutorials/UnderstandingServicesParams "/ROS/Tutorials/UnderstandingServicesParams").  |

|  |
| --- |
| (!) Please ask about problems and questions regarding this tutorial on [answers.ros.org](http://answers.ros.org "http://answers.ros.org"). Don't forget to include in your question the link to this page, the versions of your OS & ROS, and also add appropriate tags. |

# Using rxconsole and roslaunch

**Description:** This tutorial introduces ROS using [rxconsole](/rxconsole "/rxconsole") and rxloggerlevel for debugging and [roslaunch](/roslaunch "/roslaunch") for starting many nodes at once.  

**Tutorial Level:** BEGINNER  

**Next Tutorial:** [Using rosed](/ROS/Tutorials/UsingRosEd "/ROS/Tutorials/UsingRosEd")   

 Contents1. [Prerequisites rxtools and turtlesim package](#Prerequisites_rxtools_and_turtlesim_package "#Prerequisites_rxtools_and_turtlesim_package")
2. [Using rxconsole and rxloggerlevel](#Using_rxconsole_and_rxloggerlevel "#Using_rxconsole_and_rxloggerlevel")
	1. [Quick Note about logger levels](#Quick_Note_about_logger_levels "#Quick_Note_about_logger_levels")
	2. [Using roslaunch](#Using_roslaunch "#Using_roslaunch")
	3. [The Launch File](#The_Launch_File "#The_Launch_File")
	4. [The Launch File Explained](#The_Launch_File_Explained "#The_Launch_File_Explained")
	5. [roslaunching](#roslaunching "#roslaunching")

 ![/!\](/moin_static197/rostheme/img/alert.png "/!\") **This tutorial page is obsolete starting from ROS [groovy](/groovy "/groovy"). Please see [ROS/Tutorials/UsingRqtconsoleRoslaunch](/ROS/Tutorials/UsingRqtconsoleRoslaunch "/ROS/Tutorials/UsingRqtconsoleRoslaunch") and come back if necessary. 
### Prerequisites rxtools and turtlesim package

The tutorial uses both the rxtools and turtlesim packages. To do this tutorial, please install both packages, if you have not yet. 
```
$ sudo apt-get install ros-<distro>-rx ros-<distro>-turtlesim 
```
Replace <distro> with the name of your ROS distribution (e.g. electric, fuerte, groovy).**NOTE: **you may have already built rxtools and turtlesim for one of the previous tutorials. If you are not sure, installing them again will not hurt anything. 
### Using rxconsole and rxloggerlevel

rxconsole attaches to ROS's logging framework to display output from nodes. rxloggerlevel allows us to change the verbosity level (DEBUG, WARN, INFO, and ERROR) of nodes as they run. Now let's look at the turtlesim output in rxconsole and switch logger levels in rxloggerlevel as we use turtlesim. Before we start the turtlesim,**in two new terminals **start rxconsole and rxloggerlevel: 
```
$ rxconsole
```

```
$ rxloggerlevel
```
 You will see two windows popup: ![http://ros.org/images/wiki/UsingRxconsoleRoslaunch/rxconsole(start).png](http://ros.org/images/wiki/UsingRxconsoleRoslaunch/rxconsole(start).png "http://ros.org/images/wiki/UsingRxconsoleRoslaunch/rxconsole(start).png") ![http://ros.org/images/wiki/UsingRxconsoleRoslaunch/rxloggerlevel.png](http://ros.org/images/wiki/UsingRxconsoleRoslaunch/rxloggerlevel.png "http://ros.org/images/wiki/UsingRxconsoleRoslaunch/rxloggerlevel.png") Now let's start turtlesim in a**new terminal**: 
```
$ rosrun turtlesim turtlesim_node
```
Since the default logger level is INFO you will see any info that the turtlesim publishes when it starts up, which should look like: ![http://ros.org/images/wiki/UsingRxconsoleRoslaunch/rxconsole(turtlesimstart).png](http://ros.org/images/wiki/UsingRxconsoleRoslaunch/rxconsole(turtlesimstart).png "http://ros.org/images/wiki/UsingRxconsoleRoslaunch/rxconsole(turtlesimstart).png") Now let's change the logger level to Warn by refreshing the nodes in the rxloggerlevel window and selecting Warn as shown below: ![http://ros.org/images/wiki/UsingRxconsoleRoslaunch/rxloggerlevel(error).png](http://ros.org/images/wiki/UsingRxconsoleRoslaunch/rxloggerlevel(error).png "http://ros.org/images/wiki/UsingRxconsoleRoslaunch/rxloggerlevel(error).png") Now let's run our turtle into the wall and see what is displayed in our rxconsole: 
```
rostopic pub /turtle1/command_velocity turtlesim/Velocity -r 1 -- 2.0  0.0
```
![http://ros.org/images/wiki/UsingRxconsoleRoslaunch/rxconsole(turtlesimerror).png](http://ros.org/images/wiki/UsingRxconsoleRoslaunch/rxconsole(turtlesimerror).png "http://ros.org/images/wiki/UsingRxconsoleRoslaunch/rxconsole(turtlesimerror).png") 
#### Quick Note about logger levels

Logging levels are prioritized in the following order: 
```
Fatal
Error
Warn
Info
Debug
```
Fatal has the highest priority and Debug has the lowest. By setting the logger level, you will get all messages of that priority level or higher. For example, by setting the level to Warn, you will get all Warn, Error, and Fatal logging messages. Let's Ctrl-C our turtlesim and let's use roslaunch to bring up multiple turtlesim nodes and a mimicking node to cause one turtlesim to mimic another: 
#### Using roslaunch

roslaunch starts nodes as defined in a launch file. Usage: 
```
$ roslaunch [package] [filename.launch]
```
First we must make a launch file. In your beginner\_tutorials package let's make a launch directory and create a launch file: 
```
$ roscd beginner_tutorials 
$ mkdir launch
$ cd launch
```
If roscd fails, remember to set the ROS\_PACKAGE\_PATH variable in your terminal. Then the commands will look like this: 
```
$ export ROS_PACKAGE_PATH=~/fuerte_workspace/sandbox:$ROS_PACKAGE_PATH
$ roscd beginner_tutorials 
$ mkdir launch
$ cd launch
```
If you still cannot find the beginner\_tutorials then go back and follow the instructions on creating a package in the second lesson [[http://www.ros.org/wiki/ROS/Tutorials/CreatingPackage](http://www.ros.org/wiki/ROS/Tutorials/CreatingPackage "http://www.ros.org/wiki/ROS/Tutorials/CreatingPackage")] 
#### The Launch File

Now let's create a launch file called turtlemimic.launch and paste the following: 

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

document.write('<a href="#" onclick="return togglenumber(\'CA-81706ca00169a94451b52977d7eb34d6bffe1c2a\', 1, 1);" \
 class="codenumbers">Toggle line numbers<\/a>');

```
 [1](#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_1 "#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_1") <launch>
 [2](#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_2 "#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_2") 
 [3](#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_3 "#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_3")  <group ns="turtlesim1">
 [4](#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_4 "#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_4")  <node pkg="turtlesim" name="sim" type="turtlesim\_node"/>
 [5](#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_5 "#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_5")  </group>
 [6](#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_6 "#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_6") 
 [7](#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_7 "#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_7")  <group ns="turtlesim2">
 [8](#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_8 "#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_8")  <node pkg="turtlesim" name="sim" type="turtlesim\_node"/>
 [9](#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_9 "#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_9")  </group>
 [10](#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_10 "#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_10")  
 [11](#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_11 "#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_11")  <node pkg="turtlesim" name="mimic" type="mimic">
 [12](#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_12 "#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_12")  <remap from="input" to="turtlesim1/turtle1"/>
 [13](#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_13 "#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_13")  <remap from="output" to="turtlesim2/turtle1"/>
 [14](#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_14 "#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_14")  </node>
 [15](#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_15 "#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_15") 
 [16](#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_16 "#CA-81706ca00169a94451b52977d7eb34d6bffe1c2a_16") </launch>

```

#### The Launch File Explained

Now, let's break the launch xml down. 

document.write('<a href="#" onclick="return togglenumber(\'CA-21ef414cf4c910bb1286ff2aedfe349a32a099b9\', 1, 1);" \
 class="codenumbers">Toggle line numbers<\/a>');

```
 [1](#CA-21ef414cf4c910bb1286ff2aedfe349a32a099b9_1 "#CA-21ef414cf4c910bb1286ff2aedfe349a32a099b9_1") <launch>

```
 Here we start the launch file with the launch tag, so that the file is identified as a launch file. 

document.write('<a href="#" onclick="return togglenumber(\'CA-0975bc12bed743bd6d6b7cf5af4a7bc4bf2fdd64\', 3, 1);" \
 class="codenumbers">Toggle line numbers<\/a>');

```
 [3](#CA-0975bc12bed743bd6d6b7cf5af4a7bc4bf2fdd64_3 "#CA-0975bc12bed743bd6d6b7cf5af4a7bc4bf2fdd64_3")  <group ns="turtlesim1">
 [4](#CA-0975bc12bed743bd6d6b7cf5af4a7bc4bf2fdd64_4 "#CA-0975bc12bed743bd6d6b7cf5af4a7bc4bf2fdd64_4")  <node pkg="turtlesim" name="sim" type="turtlesim\_node"/>
 [5](#CA-0975bc12bed743bd6d6b7cf5af4a7bc4bf2fdd64_5 "#CA-0975bc12bed743bd6d6b7cf5af4a7bc4bf2fdd64_5")  </group>
 [6](#CA-0975bc12bed743bd6d6b7cf5af4a7bc4bf2fdd64_6 "#CA-0975bc12bed743bd6d6b7cf5af4a7bc4bf2fdd64_6") 
 [7](#CA-0975bc12bed743bd6d6b7cf5af4a7bc4bf2fdd64_7 "#CA-0975bc12bed743bd6d6b7cf5af4a7bc4bf2fdd64_7")  <group ns="turtlesim2">
 [8](#CA-0975bc12bed743bd6d6b7cf5af4a7bc4bf2fdd64_8 "#CA-0975bc12bed743bd6d6b7cf5af4a7bc4bf2fdd64_8")  <node pkg="turtlesim" name="sim" type="turtlesim\_node"/>
 [9](#CA-0975bc12bed743bd6d6b7cf5af4a7bc4bf2fdd64_9 "#CA-0975bc12bed743bd6d6b7cf5af4a7bc4bf2fdd64_9")  </group>

```
 Here we start two groups with a namespace tag of turtlesim1 and turtlesim2 with a turtlesim node with a name of sim. This allows us to start two simulators without having name conflicts. 

document.write('<a href="#" onclick="return togglenumber(\'CA-78308b822a594630211cae0b2b508b405d07b108\', 11, 1);" \
 class="codenumbers">Toggle line numbers<\/a>');

```
 [11](#CA-78308b822a594630211cae0b2b508b405d07b108_11 "#CA-78308b822a594630211cae0b2b508b405d07b108_11")  <node pkg="turtlesim" name="mimic" type="mimic">
 [12](#CA-78308b822a594630211cae0b2b508b405d07b108_12 "#CA-78308b822a594630211cae0b2b508b405d07b108_12")  <remap from="input" to="turtlesim1/turtle1"/>
 [13](#CA-78308b822a594630211cae0b2b508b405d07b108_13 "#CA-78308b822a594630211cae0b2b508b405d07b108_13")  <remap from="output" to="turtlesim2/turtle1"/>
 [14](#CA-78308b822a594630211cae0b2b508b405d07b108_14 "#CA-78308b822a594630211cae0b2b508b405d07b108_14")  </node>

```
 Here we start the mimic node with the topics input and output renamed to turtlesim1 and turtlesim2. This renaming will cause turtlesim2 to mimic turtlesim1. 

document.write('<a href="#" onclick="return togglenumber(\'CA-e33435967e0cc6e3273fdf1ce957aba2daaf5023\', 16, 1);" \
 class="codenumbers">Toggle line numbers<\/a>');

```
 [16](#CA-e33435967e0cc6e3273fdf1ce957aba2daaf5023_16 "#CA-e33435967e0cc6e3273fdf1ce957aba2daaf5023_16") </launch>

```
 This closes the xml tag for the launch file. 
#### roslaunching

Now let's roslaunch the launch file: 
```
$ roslaunch beginner_tutorials turtlemimic.launch
```
Two turtlesims will start and in a**new terminal **send the rostopic command: 
```
$ rostopic pub /turtlesim1/turtle1/command_velocity turtlesim/Velocity -r 1 -- 2.0  -1.8
```
You will see the two turtlesims start moving even though the publish command is only being sent to turtlesim1. ![http://ros.org/images/wiki/UsingRxconsoleRoslaunch/mimic.png](http://ros.org/images/wiki/UsingRxconsoleRoslaunch/mimic.png "http://ros.org/images/wiki/UsingRxconsoleRoslaunch/mimic.png") We can also use rxgraph to better understand what our launch file did: 
```
$ rxgraph
```
![http://ros.org/images/wiki/UsingRxconsoleRoslaunch/mimiclaunch.png](http://ros.org/images/wiki/UsingRxconsoleRoslaunch/mimiclaunch.png "http://ros.org/images/wiki/UsingRxconsoleRoslaunch/mimiclaunch.png") Now that you have successfully used rxconsole and roslaunch, let's learn about [editor options for ROS](/ROS/Tutorials/UsingRosEd "/ROS/Tutorials/UsingRosEd"). You can Crtl-C all your turtlesims, as you will not need them for the next tutorials.**

Wiki: ROS/Tutorials/UsingRxconsoleRoslaunch (last edited 2013-04-09 20:27:22 by [IsaacSaito](/IsaacSaito "130s @ gw.willowgarage.com[70.35.54.194]"))

Except where otherwise noted, the ROS wiki is licensed under the   

