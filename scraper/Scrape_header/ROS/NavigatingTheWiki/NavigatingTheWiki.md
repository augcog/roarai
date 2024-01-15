

 var \_gaq = \_gaq || [];
 \_gaq.push(['\_setAccount', 'UA-17821189-2']);
 \_gaq.push(['\_setDomainName', 'wiki.ros.org']);
 \_gaq.push(['\_trackPageview']);

 (function() {
 var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
 ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
 var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
 })();

ROS/Tutorials/NavigatingTheWiki - ROS Wiki

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
* [NavigatingTheWiki](/ROS/Tutorials/NavigatingTheWiki "/ROS/Tutorials/NavigatingTheWiki")

#### ROS 2 Documentation

The ROS Wiki is for ROS 1. Are you using ROS 2 ([Humble](http://docs.ros.org/en/humble/ "http://docs.ros.org/en/humble/"), [Iron](http://docs.ros.org/en/iron/ "http://docs.ros.org/en/iron/"), or [Rolling](http://docs.ros.org/en/rolling/ "http://docs.ros.org/en/rolling/"))?   
[Check out the ROS 2 Project Documentation](http://docs.ros.org "http://docs.ros.org")  
Package specific documentation can be found on [index.ros.org](https://index.ros.org "https://index.ros.org")

# Wiki

* [Distributions](/Distributions "/Distributions")
* [ROS/Installation](/ROS/Installation "/ROS/Installation")
* [ROS/Tutorials](/ROS/Tutorials "/ROS/Tutorials")
* [RecentChanges](/RecentChanges "/RecentChanges")
* [NavigatingTheWiki](/ROS/Tutorials/NavigatingTheWiki "/ROS/Tutorials/NavigatingTheWiki")

# Page

* Immutable Page
* [Comments](# "#")
* [Info](/action/info/ROS/Tutorials/NavigatingTheWiki?action=info "/action/info/ROS/Tutorials/NavigatingTheWiki?action=info")
* [Attachments](/action/AttachFile/ROS/Tutorials/NavigatingTheWiki?action=AttachFile "/action/AttachFile/ROS/Tutorials/NavigatingTheWiki?action=AttachFile")
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

* [Login](/action/login/ROS/Tutorials/NavigatingTheWiki?action=login "/action/login/ROS/Tutorials/NavigatingTheWiki?action=login")

|  |
| --- |
| **Note:** This tutorials assumes you have read the [Introduction to ROS](/ROS/Introduction "/ROS/Introduction").  |

|  |
| --- |
| (!) Please ask about problems and questions regarding this tutorial on [answers.ros.org](http://answers.ros.org "http://answers.ros.org"). Don't forget to include in your question the link to this page, the versions of your OS & ROS, and also add appropriate tags. |

# Navigating the ROS wiki

**Description:** This tutorial discusses the layout of the ROS wiki ([wiki.ros.org](/Documentation "/Documentation")) and talks about how to find what you want to know.  

**Keywords:** wiki  

**Tutorial Level:** BEGINNER  

**Next Tutorial:** [Where Next?](/ROS/Tutorials/WhereNext "/ROS/Tutorials/WhereNext")   

 Contents1. [Basics](#Basics "#Basics")
	1. [ROS Wiki Landing Page](#ROS_Wiki_Landing_Page "#ROS_Wiki_Landing_Page")
	2. [ROS Package Pages](#ROS_Package_Pages "#ROS_Package_Pages")
	3. [ROS Stack Pages](#ROS_Stack_Pages "#ROS_Stack_Pages")
2. [Advanced](#Advanced "#Advanced")
	1. [To create tutorial pages under your package](#To_create_tutorial_pages_under_your_package "#To_create_tutorial_pages_under_your_package")
		1. [Sort the tutorial](#Sort_the_tutorial "#Sort_the_tutorial")

 This tutorial will look at the different headers, links, and sidebars through out the wiki to help you understand how the ROS wiki is laid out. 
## Basics

### ROS Wiki Landing Page

The landing page is where you are directed to when you type wiki.ros.org into you browser. Let's look at the ROS wiki header that is displayed at the top of every wiki page.   

![descriptive_ros_header.png](/ROS/Tutorials/NavigatingTheWiki?action=AttachFile&do=get&target=descriptive_ros_header.png "descriptive_ros_header.png") As you can see each package contains tutorials and troubleshooting specific to the package. 
### ROS Package Pages

Let's look at *ros-pkg* package wiki page for [tf (www.ros.org/wiki/tf)](/tf "/tf"). The package header for each package is auto generated from the stack and package manifest.   

![tf_package_detail.png](/ROS/Tutorials/NavigatingTheWiki?action=AttachFile&do=get&target=tf_package_detail.png "tf_package_detail.png") 
### ROS Stack Pages

Let's look at *ros* stack wiki page for [ROS (www.ros.org/wiki/ROS)](/ROS "/ROS"). The stack header for each stack is auto generated from the stack manifest.   

![stack_header_detail.png](/ROS/Tutorials/NavigatingTheWiki?action=AttachFile&do=get&target=stack_header_detail.png "stack_header_detail.png") As you can see each stack contains tutorials and troubleshooting specific to the stack. 
## Advanced

Beginners can skip this section. 
### To create tutorial pages under your package

1. Once you have created your package page, open the URL with /Tutorials at the tail of the URL of your package. For example, suppose your package is located at http://wiki.ros.org/foo\_pkg. You should open http://wiki.ros.org/foo\_pkg/Tutorials. This way the wiki will create a new page.
2. The page will say This page does not exist yet. What type of page are you trying to create?. The wiki is correct, because there's no (hopefully) such page. ROS wiki now shows a list of templates, choose TutorialIndexTemplate.
3. Now you are redirected to the wiki page editor. Add whatever change you think you need, and save it at the end. Using Preview often to check how it looks is a great idea. Notice that, however, there are some ROS wiki macros that do not get activated until you save the page (in that case you just have to pray that your edition works, but it's okay to try and error!).

#### Sort the tutorial

By default, TutorialIndexTemplate uses a macro FullSearchWithDescriptionsCS, which searches all available tutorials under the URL hierarchy you chose (http://wiki.ros.org/foo\_pkg/Tutorials in this case). There the order of tutorials are based on the "links" between tutorials (next.0 attribute in each page's tutorial header). Often, you want to sort the tutorial in your own way, like [ROS' basic tutorial top page](/ROS/Tutorials "/ROS/Tutorials") does. To do so you use TutorialChain macro. See the example in [ROS basic tutorials](http://wiki.ros.org/ROS/Tutorials?action=diff&rev2=153&rev1=152 "http://wiki.ros.org/ROS/Tutorials?action=diff&rev2=153&rev1=152"). 

Wiki: ROS/Tutorials/NavigatingTheWiki (last edited 2022-02-22 09:25:35 by [CyrilJourdan](/CyrilJourdan "CyrilJourdan @ lstlambert-658-1-211-33.w80-13.abo.wanadoo.fr[80.13.230.33]"))

Except where otherwise noted, the ROS wiki is licensed under the   

