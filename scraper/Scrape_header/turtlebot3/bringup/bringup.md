

TurtleBot3

 {
 "@context" : "http://schema.org",
 "@type" : "Person",
 "name" : "ROBOTIS",
 "url" : "https://emanual.robotis.com",
 "sameAs" : null
 }

$(function() {
 return $("h1, h2, h3, h4, h5, h6").each(function(i, el) {
 var $el, icon, id;
 $el = $(el);
 id = $el.attr('id');
 icon = '<i class="fa fa-link"></i>';
 if (id) {
 return $el.append($("<a />").addClass("header-link").attr("href", "#" + decodeURI(id)).attr("onclick", "copyurl(this);").html(icon));
 }
 });
});

$(function(){
 $('h1').each(function(){
 $(this).addClass('class-h1');
 });
 $('h2').each(function(){
 $(this).addClass('class-h2');
 });
 $('h3').each(function(){
 $(this).addClass('class-h3');
 });
 $('h4').each(function(){
 $(this).addClass('class-h4');
 });
 $('h5').each(function(){
 $(this).addClass('class-h5');
 });
 $('h6').each(function(){
 $(this).addClass('class-h6');
 });
});

$(function() {
 $('h1, h2, h3, h4, h5, h6').each(function(i, e) {
 $(e).nextUntil('h1, h2, h3, h4, h5, h6').wrapAll('<div>');
 });

});

 var toggle\_google = 0;
 var toggle\_search\_tool = 0;
 var toggle\_search\_result = 0;
 var mobile\_width = 960;

 function extendgoogletool() {
 if (toggle\_google == 0) {
 google\_tools.classList.add("extend\_googletools");
 switch\_ko\_en.classList.add("show\_switch\_ko\_en");
 toggle\_google = 1;
 }
 else {
 google\_tools.classList.remove("extend\_googletools");
 switch\_ko\_en.classList.remove("show\_switch\_ko\_en");
 toggle\_google = 0;
 }
 }

 function extendsearchtool() {
 if (toggle\_search\_tool == 0) {
 $('.searchbox').css('display', 'block');
 $('#archive').css('margin-top', '40px');
 toggle\_search\_tool = 1;
 }
 else {
 $('.searchbox').css('display', 'none');
 $('#archive').css('margin-top', '0px');
 toggle\_search\_tool = 0;
 }
 }

 $(document).ready(function() {
 $('.blank').attr('target', '\_blank');
 $('.popup').magnificPopup({
 type: 'ajax',
 alignTop: true,
 overflowY: 'scroll' // as we know that popup content is tall we set scroll overflow by default to avoid jump
 });
 $('.popup2').magnificPopup({
 type: 'inline',
 alignTop: true,
 overflowY: 'scroll' // as we know that popup content is tall we set scroll overflow by default to avoid jump
 });
 });

 $(function () {
 var currentHash = $(location).attr('hash');
 var filename = $(location).attr('href').split('/').reverse()[1];
 $(document).scroll(function () {
 $('.header-link').each(function () {
 var top = window.pageYOffset;
 var distance = top - $(this).offset().top;
 var rawHash = $(this).attr('href');
 var contentId = rawHash.replace('#', '');
 var tocId = rawHash.replace('#', filename+'\_toc\_');
 var searchContentId = $('#'+contentId);
 var searchTocId = $('#'+tocId);

 if (distance < 50 && distance > -50 && currentHash != tocId) {
 // window.history.pushState(window.location.href, "title", currentHash); //Update browser URL history with current anchor
 if ((searchContentId.hasClass('class-h1') || searchContentId.hasClass('class-h2') || searchContentId.hasClass('class-h3')) && $('.nav\_\_items').has('#'+tocId).length) {
 // console.log(contentId);
 // console.log(tocId);
 searchTocId.prop("checked", true); //Open folded Toc menu
 $('.current\_contents').removeClass("current\_contents");

 //Check if Buttoned ToC with children
 // console.log(searchTocId);
 if( searchTocId.prop("tagName") == "INPUT" ) {
 // console.log("input detected");
 if( searchTocId.prop("name") == "sublevel" ) {
 searchTocId.closest("li.has-grandchildren").find("label > button").addClass("current\_contents");
 }
 }
 else {
 searchTocId.addClass("current\_contents");
 }

 // Open folded Toc menu
 searchTocId.closest("li.has-grandchildren").find("input").first().prop("checked", true);
 searchTocId.closest("li.has-children").find("input").first().prop("checked", true);

 currentHash = tocId;
 }
 }
 });
 });
 });

 window.onscroll = function () {
 var offset = 64 - $(window).scrollTop();
 if(offset < 0) { offset = 0; }
 $(".sidebar\_\_left").css("top", offset); //sticky sidebar
 $(".extend\_sidebar").css("top", offset);
 $(".local\_navigation").css("top", offset); //sticky local navigation
 $(".searchbox").css("top", offset); //sticky searchbox
 // console.log(offset);
 };

 var toggle = 0;

 function extendnav() {
 if (toggle == 0) {
 sidebar\_\_left.classList.add("extend\_sidebar");
 toggle = 1;
 }
 else {
 sidebar\_\_left.classList.remove("extend\_sidebar");
 toggle = 0;
 }
 }

 function copyurl(item)
 {
 // location.href = item.href;
 var copiedurl = decodeURI(item.href);
 var tempurl = $('<input>').val(copiedurl).appendTo('body').select();
 document.execCommand('copy');
 // console.log(copiedurl);
 // document.getElementById(id).href;
 // document.execCommand('copy');
 }

 function movetopage(targeturl)
 {
 location.href=targeturl;
 }

 function tab\_handler(en){
 console.log(en.textContent);
 var tabs = document.getElementById('tabs').children;
 for(i = 0; i < tabs.length; i++) {
 tabs[i].className = "tab not\_\_selected";
 $(".archive").removeClass(tabs[i].textContent);
 }
 en.className = "tab selected";
 $(".archive").addClass(en.textContent);
 }

 // When a page is reloaded, a previously selected tab and tab\_contents will be recalled to the current page keeping the same status until user's windows is closed.
 $(document).ready(function() {
 //defualt Tab Status. 
 if(sessionStorage.getItem("tabActive") == null){
 console.log("tabActive:" + sessionStorage.getItem("tabActive")); 
 $(".tab:nth-child(1)").addClass("selected");
 $(".tab\_contents:nth-of-type(1)").addClass("active");
 } else if(sessionStorage.getItem("tabActive") !== null) {
 console.log("tabActive: Not Null"); 
 $('[data-id="' + sessionStorage.getItem("tabActive")+'"]').addClass("active");
 $('[data-tab-name="'+ sessionStorage.getItem("tabActive")+'"]').addClass("tab selected");
 }
 })

 // en = enable
 function tab\_handler(en){
 // console.log(en.textContent);
 var tabs = document.getElementById('tabs').children;
 for(i = 0; i < tabs.length; i++) {
 tabs[i].className = "tab not\_\_selected";
 // $(".archive").removeClass(tabs[i].textContent);
 }
 en.className = "tab selected";
 // $(".archive").addClass(en.textContent);
 show\_contents(en.textContent);
 }

 // Controling a clicked tab's contents when a click event occurs. 
 function show\_contents(temp){
 // Seaching active class within .tab\_contents classes in the DOM tree, and remove the "active" class and set the disply as none. 
 $(".tab\_contents.active").removeClass("active");
 // in the "tab\_contents" class, searching for a matched ID to add a new class to the speidic ID. 
 $(".tab\_contents").each(function(){
 // Searching for a ID parameter "temp" and add a class, active, and css style. 
 // $("#" + temp).addClass("active");
 $('[data-id="' + temp +'"]').addClass("active");
 console.log(temp+":"+ $('.tab\_contents').hasClass("active")); 
 // To store user's data in the local storage, collect a class data of the active class.
 sessionStorage.setItem('tabActive', temp); 
 })
 }

![](/assets/images/search_icon.png)

[![](/assets/images/robotis_emanual_logo.png)](http://emanual.robotis.com "http://emanual.robotis.com")

* DYNAMIXEL
	+ P Series
		- [PH54-200-S500-R (H54P)](https://emanual.robotis.com/docs/en/dxl/p/ph54-200-s500-r/ "https://emanual.robotis.com/docs/en/dxl/p/ph54-200-s500-r/")
		- [PH54-100-S500-R (H54P)](https://emanual.robotis.com/docs/en/dxl/p/ph54-100-s500-r/ "https://emanual.robotis.com/docs/en/dxl/p/ph54-100-s500-r/")
		- [PH42-020-S300-R (H42P)](https://emanual.robotis.com/docs/en/dxl/p/ph42-020-s300-r/ "https://emanual.robotis.com/docs/en/dxl/p/ph42-020-s300-r/")
		- [PM54-060-S250-R (M54P)](https://emanual.robotis.com/docs/en/dxl/p/pm54-060-s250-r/ "https://emanual.robotis.com/docs/en/dxl/p/pm54-060-s250-r/")
		- [PM54-040-S250-R (M54P)](https://emanual.robotis.com/docs/en/dxl/p/pm54-040-s250-r/ "https://emanual.robotis.com/docs/en/dxl/p/pm54-040-s250-r/")
		- [PM42-010-S260-R (M42P)](https://emanual.robotis.com/docs/en/dxl/p/pm42-010-s260-r/ "https://emanual.robotis.com/docs/en/dxl/p/pm42-010-s260-r/")
	+ DYNAMIXEL DRIVE (DYD)
		- [DYD-11](https://emanual.robotis.com/docs/en/all-dyd/dyd-11 "https://emanual.robotis.com/docs/en/all-dyd/dyd-11")
		- [DYD-14](https://emanual.robotis.com/docs/en/all-dyd/dyd-14 "https://emanual.robotis.com/docs/en/all-dyd/dyd-14")
		- [DYD-17](https://emanual.robotis.com/docs/en/all-dyd/dyd-17 "https://emanual.robotis.com/docs/en/all-dyd/dyd-17")
	+ [X Series](https://emanual.robotis.com/docs/en/dxl/x/ "https://emanual.robotis.com/docs/en/dxl/x/")
	+ XW Series
		- [XW540-T140](https://emanual.robotis.com/docs/en/dxl/x/xw540-t140/ "https://emanual.robotis.com/docs/en/dxl/x/xw540-t140/")
		- [XW540-T260](https://emanual.robotis.com/docs/en/dxl/x/xw540-t260/ "https://emanual.robotis.com/docs/en/dxl/x/xw540-t260/")
		- [XW430-T200](https://emanual.robotis.com/docs/en/dxl/x/xw430-t200/ "https://emanual.robotis.com/docs/en/dxl/x/xw430-t200/")
		- [XW430-T333](https://emanual.robotis.com/docs/en/dxl/x/xw430-t333/ "https://emanual.robotis.com/docs/en/dxl/x/xw430-t333/")
	+ XD Series
		- [XD540-T150](https://emanual.robotis.com/docs/en/dxl/x/xd540-t150/ "https://emanual.robotis.com/docs/en/dxl/x/xd540-t150/")
		- [XD540-T270](https://emanual.robotis.com/docs/en/dxl/x/xd540-t270/ "https://emanual.robotis.com/docs/en/dxl/x/xd540-t270/")
		- [XD430-T210](https://emanual.robotis.com/docs/en/dxl/x/xd430-t210/ "https://emanual.robotis.com/docs/en/dxl/x/xd430-t210/")
		- [XD430-T350](https://emanual.robotis.com/docs/en/dxl/x/xd430-t350/ "https://emanual.robotis.com/docs/en/dxl/x/xd430-t350/")
	+ XH Series
		- [XH540-W150](https://emanual.robotis.com/docs/en/dxl/x/xh540-w150/ "https://emanual.robotis.com/docs/en/dxl/x/xh540-w150/")
		- [XH540-W270](https://emanual.robotis.com/docs/en/dxl/x/xh540-w270/ "https://emanual.robotis.com/docs/en/dxl/x/xh540-w270/")
		- [XH540-V150](https://emanual.robotis.com/docs/en/dxl/x/xh540-v150/ "https://emanual.robotis.com/docs/en/dxl/x/xh540-v150/")
		- [XH540-V270](https://emanual.robotis.com/docs/en/dxl/x/xh540-v270/ "https://emanual.robotis.com/docs/en/dxl/x/xh540-v270/")
		- [XH430-W210](https://emanual.robotis.com/docs/en/dxl/x/xh430-w210/ "https://emanual.robotis.com/docs/en/dxl/x/xh430-w210/")
		- [XH430-W350](https://emanual.robotis.com/docs/en/dxl/x/xh430-w350/ "https://emanual.robotis.com/docs/en/dxl/x/xh430-w350/")
		- [XH430-V210](https://emanual.robotis.com/docs/en/dxl/x/xh430-v210/ "https://emanual.robotis.com/docs/en/dxl/x/xh430-v210/")
		- [XH430-V350](https://emanual.robotis.com/docs/en/dxl/x/xh430-v350/ "https://emanual.robotis.com/docs/en/dxl/x/xh430-v350/")
	+ XM Series
		- [XM540-W150](https://emanual.robotis.com/docs/en/dxl/x/xm540-w150/ "https://emanual.robotis.com/docs/en/dxl/x/xm540-w150/")
		- [XM540-W270](https://emanual.robotis.com/docs/en/dxl/x/xm540-w270/ "https://emanual.robotis.com/docs/en/dxl/x/xm540-w270/")
		- [XM430-W210](https://emanual.robotis.com/docs/en/dxl/x/xm430-w210/ "https://emanual.robotis.com/docs/en/dxl/x/xm430-w210/")
		- [XM430-W350](https://emanual.robotis.com/docs/en/dxl/x/xm430-w350/ "https://emanual.robotis.com/docs/en/dxl/x/xm430-w350/")
	+ XC Series
		- [2XC430-W250](https://emanual.robotis.com/docs/en/dxl/x/2xc430-w250/ "https://emanual.robotis.com/docs/en/dxl/x/2xc430-w250/")
		- [XC430-W150](https://emanual.robotis.com/docs/en/dxl/x/xc430-w150/ "https://emanual.robotis.com/docs/en/dxl/x/xc430-w150/")
		- [XC430-W240](https://emanual.robotis.com/docs/en/dxl/x/xc430-w240/ "https://emanual.robotis.com/docs/en/dxl/x/xc430-w240/")
		- [XC430-T150BB](https://emanual.robotis.com/docs/en/dxl/x/xc430-t150bb/ "https://emanual.robotis.com/docs/en/dxl/x/xc430-t150bb/")
		- [XC430-T240BB](https://emanual.robotis.com/docs/en/dxl/x/xc430-t240bb/ "https://emanual.robotis.com/docs/en/dxl/x/xc430-t240bb/")
		- [XC330-T288](https://emanual.robotis.com/docs/en/dxl/x/xc330-t288/ "https://emanual.robotis.com/docs/en/dxl/x/xc330-t288/")
		- [XC330-T181](https://emanual.robotis.com/docs/en/dxl/x/xc330-t181/ "https://emanual.robotis.com/docs/en/dxl/x/xc330-t181/")
		- [XC330-M181](https://emanual.robotis.com/docs/en/dxl/x/xc330-m181/ "https://emanual.robotis.com/docs/en/dxl/x/xc330-m181/")
		- [XC330-M288](https://emanual.robotis.com/docs/en/dxl/x/xc330-m288/ "https://emanual.robotis.com/docs/en/dxl/x/xc330-m288/")
	+ XL Series
		- [2XL430-W250](https://emanual.robotis.com/docs/en/dxl/x/2xl430-w250/ "https://emanual.robotis.com/docs/en/dxl/x/2xl430-w250/")
		- [XL430-W250](https://emanual.robotis.com/docs/en/dxl/x/xl430-w250/ "https://emanual.robotis.com/docs/en/dxl/x/xl430-w250/")
		- [XL330-M077](https://emanual.robotis.com/docs/en/dxl/x/xl330-m077/ "https://emanual.robotis.com/docs/en/dxl/x/xl330-m077/")
		- [XL330-M288](https://emanual.robotis.com/docs/en/dxl/x/xl330-m288/ "https://emanual.robotis.com/docs/en/dxl/x/xl330-m288/")
		- [XL-320](https://emanual.robotis.com/docs/en/dxl/x/xl320/ "https://emanual.robotis.com/docs/en/dxl/x/xl320/")
	+ MX Series
		- [MX-106T/R(2.0)](https://emanual.robotis.com/docs/en/dxl/mx/mx-106-2/ "https://emanual.robotis.com/docs/en/dxl/mx/mx-106-2/")
		- [MX-64T/R/AT/AR(2.0)](https://emanual.robotis.com/docs/en/dxl/mx/mx-64-2/ "https://emanual.robotis.com/docs/en/dxl/mx/mx-64-2/")
		- [MX-28T/R/AT/AR(2.0)](https://emanual.robotis.com/docs/en/dxl/mx/mx-28-2/ "https://emanual.robotis.com/docs/en/dxl/mx/mx-28-2/")
		- [MX-106T/R](https://emanual.robotis.com/docs/en/dxl/mx/mx-106/ "https://emanual.robotis.com/docs/en/dxl/mx/mx-106/")
		- [MX-64T/R/AT/AR](https://emanual.robotis.com/docs/en/dxl/mx/mx-64/ "https://emanual.robotis.com/docs/en/dxl/mx/mx-64/")
		- [MX-28T/R/AT/AR](https://emanual.robotis.com/docs/en/dxl/mx/mx-28/ "https://emanual.robotis.com/docs/en/dxl/mx/mx-28/")
		- [MX-12W](https://emanual.robotis.com/docs/en/dxl/mx/mx-12w/ "https://emanual.robotis.com/docs/en/dxl/mx/mx-12w/")
	+ AX Series
		- [AX-18F/18A](https://emanual.robotis.com/docs/en/dxl/ax/ax-18a/ "https://emanual.robotis.com/docs/en/dxl/ax/ax-18a/")
		- [AX-12/12+/12A](https://emanual.robotis.com/docs/en/dxl/ax/ax-12a/ "https://emanual.robotis.com/docs/en/dxl/ax/ax-12a/")
		- [AX-12W](https://emanual.robotis.com/docs/en/dxl/ax/ax-12w/ "https://emanual.robotis.com/docs/en/dxl/ax/ax-12w/")
	+ [DYNAMIXEL Protocol 1.0](https://emanual.robotis.com/docs/en/dxl/protocol1/ "https://emanual.robotis.com/docs/en/dxl/protocol1/")
	+ [DYNAMIXEL Protocol 2.0](https://emanual.robotis.com/docs/en/dxl/protocol2/ "https://emanual.robotis.com/docs/en/dxl/protocol2/")
	+ EX Series 
		- [EX-106+](https://emanual.robotis.com/docs/en/dxl/ex/ex-106+/ "https://emanual.robotis.com/docs/en/dxl/ex/ex-106+/")
	+ DX Series 
		- [DX-113](https://emanual.robotis.com/docs/en/dxl/dx/dx-113/ "https://emanual.robotis.com/docs/en/dxl/dx/dx-113/")
		- [DX-116](https://emanual.robotis.com/docs/en/dxl/dx/dx-116/ "https://emanual.robotis.com/docs/en/dxl/dx/dx-116/")
		- [DX-117](https://emanual.robotis.com/docs/en/dxl/dx/dx-117/ "https://emanual.robotis.com/docs/en/dxl/dx/dx-117/")
	+ RX Series 
		- [RX-10](https://emanual.robotis.com/docs/en/dxl/rx/rx-10/ "https://emanual.robotis.com/docs/en/dxl/rx/rx-10/")
		- [RX-24F](https://emanual.robotis.com/docs/en/dxl/rx/rx-24f/ "https://emanual.robotis.com/docs/en/dxl/rx/rx-24f/")
		- [RX-28](https://emanual.robotis.com/docs/en/dxl/rx/rx-28/ "https://emanual.robotis.com/docs/en/dxl/rx/rx-28/")
		- [RX-64](https://emanual.robotis.com/docs/en/dxl/rx/rx-64/ "https://emanual.robotis.com/docs/en/dxl/rx/rx-64/")
	+ PRO Series 
		- [H54-200-S500-R(A)](https://emanual.robotis.com/docs/en/dxl/pro/h54-200-s500-ra/ "https://emanual.robotis.com/docs/en/dxl/pro/h54-200-s500-ra/")
		- [H54-100-S500-R(A)](https://emanual.robotis.com/docs/en/dxl/pro/h54-100-s500-ra/ "https://emanual.robotis.com/docs/en/dxl/pro/h54-100-s500-ra/")
		- [H42-20-S300-R(A)](https://emanual.robotis.com/docs/en/dxl/pro/h42-20-s300-ra/ "https://emanual.robotis.com/docs/en/dxl/pro/h42-20-s300-ra/")
		- [M54-60-S250-R(A)](https://emanual.robotis.com/docs/en/dxl/pro/m54-60-s250-ra/ "https://emanual.robotis.com/docs/en/dxl/pro/m54-60-s250-ra/")
		- [M54-40-S250-R(A)](https://emanual.robotis.com/docs/en/dxl/pro/m54-40-s250-ra/ "https://emanual.robotis.com/docs/en/dxl/pro/m54-40-s250-ra/")
		- [M42-10-S260-R(A)](https://emanual.robotis.com/docs/en/dxl/pro/m42-10-s260-ra/ "https://emanual.robotis.com/docs/en/dxl/pro/m42-10-s260-ra/")
		- [H54-200-S500-R](https://emanual.robotis.com/docs/en/dxl/pro/h54-200-s500-r/ "https://emanual.robotis.com/docs/en/dxl/pro/h54-200-s500-r/")
		- [H54-100-S500-R](https://emanual.robotis.com/docs/en/dxl/pro/h54-100-s500-r/ "https://emanual.robotis.com/docs/en/dxl/pro/h54-100-s500-r/")
		- [H42-20-S300-R](https://emanual.robotis.com/docs/en/dxl/pro/h42-20-s300-r/ "https://emanual.robotis.com/docs/en/dxl/pro/h42-20-s300-r/")
		- [M54-60-S250-R](https://emanual.robotis.com/docs/en/dxl/pro/m54-60-s250-r/ "https://emanual.robotis.com/docs/en/dxl/pro/m54-60-s250-r/")
		- [M54-40-S250-R](https://emanual.robotis.com/docs/en/dxl/pro/m54-40-s250-r/ "https://emanual.robotis.com/docs/en/dxl/pro/m54-40-s250-r/")
		- [M42-10-S260-R](https://emanual.robotis.com/docs/en/dxl/pro/m42-10-s260-r/ "https://emanual.robotis.com/docs/en/dxl/pro/m42-10-s260-r/")
		- [L54-50-S500-R](https://emanual.robotis.com/docs/en/dxl/pro/l54-50-s500-r/ "https://emanual.robotis.com/docs/en/dxl/pro/l54-50-s500-r/")
		- [L54-50-S290-R](https://emanual.robotis.com/docs/en/dxl/pro/l54-50-s290-r/ "https://emanual.robotis.com/docs/en/dxl/pro/l54-50-s290-r/")
		- [L54-30-S500-R](https://emanual.robotis.com/docs/en/dxl/pro/l54-30-s500-r/ "https://emanual.robotis.com/docs/en/dxl/pro/l54-30-s500-r/")
		- [L54-30-S400-R](https://emanual.robotis.com/docs/en/dxl/pro/l54-30-s400-r/ "https://emanual.robotis.com/docs/en/dxl/pro/l54-30-s400-r/")
		- [L42-10-S300-R](https://emanual.robotis.com/docs/en/dxl/pro/l42-10-s300-r/ "https://emanual.robotis.com/docs/en/dxl/pro/l42-10-s300-r/")
* DYNAMIXEL  SYSTEM
	+ [TurtleBot3](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/ "https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/")
	+ OpenMANIPULATOR
		- [OpenMANIPULATOR-P](https://emanual.robotis.com/docs/en/platform/openmanipulator_p/overview/ "https://emanual.robotis.com/docs/en/platform/openmanipulator_p/overview/")
		- [OpenMANIPULATOR-X](https://emanual.robotis.com/docs/en/platform/openmanipulator_x/overview/ "https://emanual.robotis.com/docs/en/platform/openmanipulator_x/overview/")
		- [Manipulator-H](https://emanual.robotis.com/docs/en/platform/manipulator_h/introduction/ "https://emanual.robotis.com/docs/en/platform/manipulator_h/introduction/")
	+ Robot Hands
		- [RH-P12-RN(A)](https://emanual.robotis.com/docs/en/platform/rh_p12_rna/ "https://emanual.robotis.com/docs/en/platform/rh_p12_rna/")
		- [RH-P12-RN-UR](https://emanual.robotis.com/docs/en/platform/rh_p12_rn_ur/ "https://emanual.robotis.com/docs/en/platform/rh_p12_rn_ur/")
	+ ROBOTIS OP
		- [ROBOTIS OP3](https://emanual.robotis.com/docs/en/platform/op3/introduction/ "https://emanual.robotis.com/docs/en/platform/op3/introduction/")
		- [ROBOTIS OP](https://emanual.robotis.com/docs/en/platform/op/getting_started/ "https://emanual.robotis.com/docs/en/platform/op/getting_started/")
		- [ROBOTIS OP2](https://emanual.robotis.com/docs/en/platform/op2/getting_started/ "https://emanual.robotis.com/docs/en/platform/op2/getting_started/")
	+ [THORMANG3](https://emanual.robotis.com/docs/en/platform/thormang3/introduction/ "https://emanual.robotis.com/docs/en/platform/thormang3/introduction/")
* EDUCATIONAL  KITS
	+ PLAY
		- [PLAY 300](https://emanual.robotis.com/docs/en/edu/play/play-300/ "https://emanual.robotis.com/docs/en/edu/play/play-300/")
		- [PLAY 600](https://emanual.robotis.com/docs/en/edu/play/play-600/ "https://emanual.robotis.com/docs/en/edu/play/play-600/")
		- [PLAY 700](https://emanual.robotis.com/docs/en/edu/play/play-700/ "https://emanual.robotis.com/docs/en/edu/play/play-700/")
	+ ROBOTIS DREAM II
		- [LEVEL 1](https://emanual.robotis.com/docs/en/edu/dream/dream2-1/ "https://emanual.robotis.com/docs/en/edu/dream/dream2-1/")
		- [LEVEL 2](https://emanual.robotis.com/docs/en/edu/dream/dream2-2/ "https://emanual.robotis.com/docs/en/edu/dream/dream2-2/")
		- [LEVEL 3](https://emanual.robotis.com/docs/en/edu/dream/dream2-3/ "https://emanual.robotis.com/docs/en/edu/dream/dream2-3/")
		- [LEVEL 4](https://emanual.robotis.com/docs/en/edu/dream/dream2-4/ "https://emanual.robotis.com/docs/en/edu/dream/dream2-4/")
		- [LEVEL 5](https://emanual.robotis.com/docs/en/edu/dream/dream2-5/ "https://emanual.robotis.com/docs/en/edu/dream/dream2-5/")
		- [School Set](https://emanual.robotis.com/docs/en/edu/dream/dream2-schoolset/ "https://emanual.robotis.com/docs/en/edu/dream/dream2-schoolset/")
	+ ROBOTIS BIOLOID
		- [ROBOTIS STEM](https://emanual.robotis.com/docs/en/edu/bioloid/stem/ "https://emanual.robotis.com/docs/en/edu/bioloid/stem/")
		- [ROBOTIS PREMIUM](https://emanual.robotis.com/docs/en/edu/bioloid/premium/ "https://emanual.robotis.com/docs/en/edu/bioloid/premium/")
		- [ROBOTIS GP](https://emanual.robotis.com/docs/en/edu/bioloid/gp/ "https://emanual.robotis.com/docs/en/edu/bioloid/gp/")
		- [Beginner Level](https://emanual.robotis.com/docs/en/edu/bioloid/beginner/ "https://emanual.robotis.com/docs/en/edu/bioloid/beginner/")
		- [Comprehensive Level](https://emanual.robotis.com/docs/en/edu/bioloid/comprehensive/ "https://emanual.robotis.com/docs/en/edu/bioloid/comprehensive/")
	+ ROBOTIS ENGINEER
		- [Kit 1](https://emanual.robotis.com/docs/en/edu/engineer/kit1/ "https://emanual.robotis.com/docs/en/edu/engineer/kit1/")
		- [Kit 2](https://emanual.robotis.com/docs/en/edu/engineer/kit2_introduction/ "https://emanual.robotis.com/docs/en/edu/engineer/kit2_introduction/")
	+ [ROBOTIS MINI](https://emanual.robotis.com/docs/en/edu/mini/ "https://emanual.robotis.com/docs/en/edu/mini/")
	+ OLLO 
		- [BUG KIT](https://emanual.robotis.com/docs/en/edu/ollo/bugkit/ "https://emanual.robotis.com/docs/en/edu/ollo/bugkit/")
		- [EXPLORER](https://emanual.robotis.com/docs/en/edu/ollo/explorer/ "https://emanual.robotis.com/docs/en/edu/ollo/explorer/")
		- [INVENTOR](https://emanual.robotis.com/docs/en/edu/ollo/inventor/ "https://emanual.robotis.com/docs/en/edu/ollo/inventor/")
	+ DREAM 
		- [LEVEL 2](https://emanual.robotis.com/docs/en/edu/dream/dream1-2/ "https://emanual.robotis.com/docs/en/edu/dream/dream1-2/")
		- [LEVEL 3](https://emanual.robotis.com/docs/en/edu/dream/dream1-3/ "https://emanual.robotis.com/docs/en/edu/dream/dream1-3/")
		- [LEVEL 4](https://emanual.robotis.com/docs/en/edu/dream/dream1-4/ "https://emanual.robotis.com/docs/en/edu/dream/dream1-4/")
		- [SET A](https://emanual.robotis.com/docs/en/edu/dream/dream-a/ "https://emanual.robotis.com/docs/en/edu/dream/dream-a/")
		- [SET B](https://emanual.robotis.com/docs/en/edu/dream/dream-b/ "https://emanual.robotis.com/docs/en/edu/dream/dream-b/")
* SOFTWARE
	+ DYNAMIXEL
		- [DYNAMIXEL SDK](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/overview/ "https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/overview/")
		- [DYNAMIXEL Workbench](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_workbench/ "https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_workbench/")
		- [DYNAMIXEL Wizard 2.0](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_wizard2/ "https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_wizard2/")
	+ Mobile Apps
		- [ROBOTIS MINI](https://emanual.robotis.com/docs/en/software/mobile_app/mini_app/ "https://emanual.robotis.com/docs/en/software/mobile_app/mini_app/")
		- [R+ Block](https://emanual.robotis.com/docs/en/software/rplus2/rplus2_block/ "https://emanual.robotis.com/docs/en/software/rplus2/rplus2_block/")
	+ R+ 1.0
		- [R+ Task](https://emanual.robotis.com/docs/en/software/rplus1/task/getting_started/ "https://emanual.robotis.com/docs/en/software/rplus1/task/getting_started/")
		- [R+ Manager](https://emanual.robotis.com/docs/en/software/rplus1/manager/ "https://emanual.robotis.com/docs/en/software/rplus1/manager/")
		- [R+ Motion](https://emanual.robotis.com/docs/en/software/rplus1/motion/ "https://emanual.robotis.com/docs/en/software/rplus1/motion/")
		- [Dynamixel Wizard](https://emanual.robotis.com/docs/en/software/rplus1/dynamixel_wizard/ "https://emanual.robotis.com/docs/en/software/rplus1/dynamixel_wizard/")
	+ R+ 2.0
		- [R+ Task 2.0](https://emanual.robotis.com/docs/en/software/rplus2/task/ "https://emanual.robotis.com/docs/en/software/rplus2/task/")
		- [R+ Manager 2.0](https://emanual.robotis.com/docs/en/software/rplus2/manager/ "https://emanual.robotis.com/docs/en/software/rplus2/manager/")
		- [R+ Motion 2.0](https://emanual.robotis.com/docs/en/software/rplus2/motion/ "https://emanual.robotis.com/docs/en/software/rplus2/motion/")
		- [R+ Design 2.0](https://emanual.robotis.com/docs/en/software/rplus2/design/ "https://emanual.robotis.com/docs/en/software/rplus2/design/")
		- [R+ Scratch](https://emanual.robotis.com/docs/en/software/rplus2/scratch/ "https://emanual.robotis.com/docs/en/software/rplus2/scratch/")
	+ [R+ Task 3.0](https://emanual.robotis.com/docs/en/software/rplustask3/ "https://emanual.robotis.com/docs/en/software/rplustask3/")
	+ R+ Mobile
		- [R+ m.Task 2.0](https://emanual.robotis.com/docs/en/software/rplus_mobile/mtask20/ "https://emanual.robotis.com/docs/en/software/rplus_mobile/mtask20/")
		- [R+ m.Motion 2.0](https://emanual.robotis.com/docs/en/software/rplus_mobile/mmotion/ "https://emanual.robotis.com/docs/en/software/rplus_mobile/mmotion/")
		- [R+ m.Design](https://emanual.robotis.com/docs/en/software/rplus_mobile/mdesign/ "https://emanual.robotis.com/docs/en/software/rplus_mobile/mdesign/")
	+ EMBEDDED SDK
		- [Embedded C(CM-510/700)](https://emanual.robotis.com/docs/en/software/embedded_sdk/embedded_c_cm510/ "https://emanual.robotis.com/docs/en/software/embedded_sdk/embedded_c_cm510/")
		- [Embedded C(CM-530)](https://emanual.robotis.com/docs/en/software/embedded_sdk/embedded_c_cm530/ "https://emanual.robotis.com/docs/en/software/embedded_sdk/embedded_c_cm530/")
		- [ZIGBEE SDK](https://emanual.robotis.com/docs/en/software/embedded_sdk/zigbee_sdk/ "https://emanual.robotis.com/docs/en/software/embedded_sdk/zigbee_sdk/")
	+ [Arduino IDE](https://emanual.robotis.com/docs/en/software/arduino_ide/ "https://emanual.robotis.com/docs/en/software/arduino_ide/")
	+ [ROBOTIS Framework Packages](https://emanual.robotis.com/docs/en/software/robotis_framework_packages/ "https://emanual.robotis.com/docs/en/software/robotis_framework_packages/")
	+ [ROBOTIS Manipulator library](https://emanual.robotis.com/docs/en/software/robotis_manipulator_libs/ "https://emanual.robotis.com/docs/en/software/robotis_manipulator_libs/")
	+ [\*OpenCM IDE](https://emanual.robotis.com/docs/en/software/opencm_ide/getting_started/ "https://emanual.robotis.com/docs/en/software/opencm_ide/getting_started/")
* PARTS
	+ Controller
		- [CM-50](https://emanual.robotis.com/docs/en/parts/controller/cm-50/ "https://emanual.robotis.com/docs/en/parts/controller/cm-50/")
		- [CM-150](https://emanual.robotis.com/docs/en/parts/controller/cm-150/ "https://emanual.robotis.com/docs/en/parts/controller/cm-150/")
		- [CM-151](https://emanual.robotis.com/docs/en/parts/controller/cm-151/ "https://emanual.robotis.com/docs/en/parts/controller/cm-151/")
		- [CM-200](https://emanual.robotis.com/docs/en/parts/controller/cm-200/ "https://emanual.robotis.com/docs/en/parts/controller/cm-200/")
		- [CM-530](https://emanual.robotis.com/docs/en/parts/controller/cm-530/ "https://emanual.robotis.com/docs/en/parts/controller/cm-530/")
		- [CM-550](https://emanual.robotis.com/docs/en/parts/controller/cm-550/ "https://emanual.robotis.com/docs/en/parts/controller/cm-550/")
		- [CM-700](https://emanual.robotis.com/docs/en/parts/controller/cm-700/ "https://emanual.robotis.com/docs/en/parts/controller/cm-700/")
		- [OpenRB-150](https://emanual.robotis.com/docs/en/parts/controller/openrb-150/ "https://emanual.robotis.com/docs/en/parts/controller/openrb-150/")
		- [OpenCM9.04](https://emanual.robotis.com/docs/en/parts/controller/opencm904/ "https://emanual.robotis.com/docs/en/parts/controller/opencm904/")
		- [OpenCM 485 EXP](https://emanual.robotis.com/docs/en/parts/controller/opencm485exp/ "https://emanual.robotis.com/docs/en/parts/controller/opencm485exp/")
		- [OpenCR1.0](https://emanual.robotis.com/docs/en/parts/controller/opencr10/ "https://emanual.robotis.com/docs/en/parts/controller/opencr10/")
		- [CM-100A](https://emanual.robotis.com/docs/en/parts/controller/cm-100/ "https://emanual.robotis.com/docs/en/parts/controller/cm-100/")
		- [CM-5](https://emanual.robotis.com/docs/en/parts/controller/cm-5/ "https://emanual.robotis.com/docs/en/parts/controller/cm-5/")
		- [CM-510](https://emanual.robotis.com/docs/en/parts/controller/cm-510/ "https://emanual.robotis.com/docs/en/parts/controller/cm-510/")
		- [CM-900](https://emanual.robotis.com/docs/en/parts/controller/cm-900/ "https://emanual.robotis.com/docs/en/parts/controller/cm-900/")
	+ Communication
		- [RC-100A/100B](https://emanual.robotis.com/docs/en/parts/communication/rc-100/ "https://emanual.robotis.com/docs/en/parts/communication/rc-100/")
		- [RC-200](https://emanual.robotis.com/docs/en/parts/communication/rc-200/ "https://emanual.robotis.com/docs/en/parts/communication/rc-200/")
		- [BT-210](https://emanual.robotis.com/docs/en/parts/communication/bt-210/ "https://emanual.robotis.com/docs/en/parts/communication/bt-210/")
		- [BT-410](https://emanual.robotis.com/docs/en/parts/communication/bt-410/ "https://emanual.robotis.com/docs/en/parts/communication/bt-410/")
		- [BT-410 Dongle](https://emanual.robotis.com/docs/en/parts/communication/bt-410-dongle/ "https://emanual.robotis.com/docs/en/parts/communication/bt-410-dongle/")
		- [ZIG-100/110A](https://emanual.robotis.com/docs/en/parts/communication/zig-110/ "https://emanual.robotis.com/docs/en/parts/communication/zig-110/")
		- [BT-100/110A](https://emanual.robotis.com/docs/en/parts/communication/bt-110/ "https://emanual.robotis.com/docs/en/parts/communication/bt-110/")
		- [ZIG2Serial](https://emanual.robotis.com/docs/en/parts/communication/zig2serial/ "https://emanual.robotis.com/docs/en/parts/communication/zig2serial/")
	+ Motors
		- [Geared Motor](https://emanual.robotis.com/docs/en/parts/motor/gm-10a/ "https://emanual.robotis.com/docs/en/parts/motor/gm-10a/")
		- [Servo Motor](https://emanual.robotis.com/docs/en/parts/motor/servo_motor/ "https://emanual.robotis.com/docs/en/parts/motor/servo_motor/")
		- [High Speed Geared Motor](https://emanual.robotis.com/docs/en/parts/motor/h_speed_geared_motor/ "https://emanual.robotis.com/docs/en/parts/motor/h_speed_geared_motor/")
		- [Low Speed Geared Motor](https://emanual.robotis.com/docs/en/parts/motor/l_speed_geared_motor/ "https://emanual.robotis.com/docs/en/parts/motor/l_speed_geared_motor/")
	+ Interface
		- [DYNAMIXEL Communication Bridge](https://emanual.robotis.com/docs/en/parts/interface/dxl_bridge/ "https://emanual.robotis.com/docs/en/parts/interface/dxl_bridge/")
		- [LN-101](https://emanual.robotis.com/docs/en/parts/interface/ln-101/ "https://emanual.robotis.com/docs/en/parts/interface/ln-101/")
		- [U2D2](https://emanual.robotis.com/docs/en/parts/interface/u2d2/ "https://emanual.robotis.com/docs/en/parts/interface/u2d2/")
		- [U2D2 Power Hub](https://emanual.robotis.com/docs/en/parts/interface/u2d2_power_hub/ "https://emanual.robotis.com/docs/en/parts/interface/u2d2_power_hub/")
		- [DYNAMIXEL Shield](https://emanual.robotis.com/docs/en/parts/interface/dynamixel_shield/ "https://emanual.robotis.com/docs/en/parts/interface/dynamixel_shield/")
		- [DYNAMIXEL Shield MKR](https://emanual.robotis.com/docs/en/parts/interface/mkr_shield/ "https://emanual.robotis.com/docs/en/parts/interface/mkr_shield/")
		- [USB2DYNAMIXEL](https://emanual.robotis.com/docs/en/parts/interface/usb2dynamixel/ "https://emanual.robotis.com/docs/en/parts/interface/usb2dynamixel/")
	+ Sensors
		- [IR Sensor](https://emanual.robotis.com/docs/en/parts/sensor/irss-10/ "https://emanual.robotis.com/docs/en/parts/sensor/irss-10/")
		- [Distance Sensor](https://emanual.robotis.com/docs/en/parts/sensor/dms-80/ "https://emanual.robotis.com/docs/en/parts/sensor/dms-80/")
		- [Touch Sensor](https://emanual.robotis.com/docs/en/parts/sensor/ts-10/ "https://emanual.robotis.com/docs/en/parts/sensor/ts-10/")
		- [Gyro Sensor](https://emanual.robotis.com/docs/en/parts/sensor/gs-12/ "https://emanual.robotis.com/docs/en/parts/sensor/gs-12/")
		- [IR Array Sensor](https://emanual.robotis.com/docs/en/parts/sensor/ir-array/ "https://emanual.robotis.com/docs/en/parts/sensor/ir-array/")
		- [Color Sensor](https://emanual.robotis.com/docs/en/parts/sensor/cs-10/ "https://emanual.robotis.com/docs/en/parts/sensor/cs-10/")
		- [Magnetic Sensor](https://emanual.robotis.com/docs/en/parts/sensor/mgss-10/ "https://emanual.robotis.com/docs/en/parts/sensor/mgss-10/")
		- [Temperature Sensor](https://emanual.robotis.com/docs/en/parts/sensor/tps-10/ "https://emanual.robotis.com/docs/en/parts/sensor/tps-10/")
		- [Motion Sensor](https://emanual.robotis.com/docs/en/parts/sensor/pir-10/ "https://emanual.robotis.com/docs/en/parts/sensor/pir-10/")
		- [Integrated Sensor](https://emanual.robotis.com/docs/en/parts/sensor/ax-s1/ "https://emanual.robotis.com/docs/en/parts/sensor/ax-s1/")
	+ Display
		- [LED Module](https://emanual.robotis.com/docs/en/parts/display/lm-10/ "https://emanual.robotis.com/docs/en/parts/display/lm-10/")
* FAQ
	+ [DYNAMIXEL Selection Guide](https://emanual.robotis.com/docs/en/reference/dxl-selection-guide/ "https://emanual.robotis.com/docs/en/reference/dxl-selection-guide/")
	+ [DYNAMIXEL Quick Start Guide](https://emanual.robotis.com/docs/en/dxl/dxl-quick-start-guide/ "https://emanual.robotis.com/docs/en/dxl/dxl-quick-start-guide/")
	+ [DYNAMIXEL](https://emanual.robotis.com/docs/en/faq/faq_dynamixel/ "https://emanual.robotis.com/docs/en/faq/faq_dynamixel/")
	+ [DYNAMIXEL SYSTEM](https://emanual.robotis.com/docs/en/faq/faq_platform/ "https://emanual.robotis.com/docs/en/faq/faq_platform/")
	+ [EDUCATION KITS](https://emanual.robotis.com/docs/en/faq/faq_steam/ "https://emanual.robotis.com/docs/en/faq/faq_steam/")
	+ [SOFTWARE](https://emanual.robotis.com/docs/en/faq/faq_software/ "https://emanual.robotis.com/docs/en/faq/faq_software/")
	+ [PARTS](https://emanual.robotis.com/docs/en/faq/faq_parts/ "https://emanual.robotis.com/docs/en/faq/faq_parts/")
	+ [GENERAL](https://emanual.robotis.com/docs/en/faq/general "https://emanual.robotis.com/docs/en/faq/general")

 DYNAMIXEL

[P Series](https://emanual.robotis.com/docs/en/dxl/p/ "https://emanual.robotis.com/docs/en/dxl/p/")

[PH54-200-S500-R (H54P)](https://emanual.robotis.com/docs/en/dxl/p/ph54-200-s500-r/ "https://emanual.robotis.com/docs/en/dxl/p/ph54-200-s500-r/")
[PH54-100-S500-R (H54P)](https://emanual.robotis.com/docs/en/dxl/p/ph54-100-s500-r/ "https://emanual.robotis.com/docs/en/dxl/p/ph54-100-s500-r/")
[PH42-020-S300-R (H42P)](https://emanual.robotis.com/docs/en/dxl/p/ph42-020-s300-r/ "https://emanual.robotis.com/docs/en/dxl/p/ph42-020-s300-r/")
[PM54-060-S250-R (M54P)](https://emanual.robotis.com/docs/en/dxl/p/pm54-060-s250-r/ "https://emanual.robotis.com/docs/en/dxl/p/pm54-060-s250-r/")
[PM54-040-S250-R (M54P)](https://emanual.robotis.com/docs/en/dxl/p/pm54-040-s250-r/ "https://emanual.robotis.com/docs/en/dxl/p/pm54-040-s250-r/")
[PM42-010-S260-R (M42P)](https://emanual.robotis.com/docs/en/dxl/p/pm42-010-s260-r/ "https://emanual.robotis.com/docs/en/dxl/p/pm42-010-s260-r/")

[DYNAMIXEL DRIVE (DYD)](https://emanual.robotis.com/docs/en/all-dyd/ "https://emanual.robotis.com/docs/en/all-dyd/")

[DYD-11](https://emanual.robotis.com/docs/en/all-dyd/dyd-11 "https://emanual.robotis.com/docs/en/all-dyd/dyd-11")
[DYD-14](https://emanual.robotis.com/docs/en/all-dyd/dyd-14 "https://emanual.robotis.com/docs/en/all-dyd/dyd-14")
[DYD-17](https://emanual.robotis.com/docs/en/all-dyd/dyd-17 "https://emanual.robotis.com/docs/en/all-dyd/dyd-17")

[X Series](https://emanual.robotis.com/docs/en/dxl/x/ "https://emanual.robotis.com/docs/en/dxl/x/")

XW Series

[XW540-T140](https://emanual.robotis.com/docs/en/dxl/x/xw540-t140/ "https://emanual.robotis.com/docs/en/dxl/x/xw540-t140/")
[XW540-T260](https://emanual.robotis.com/docs/en/dxl/x/xw540-t260/ "https://emanual.robotis.com/docs/en/dxl/x/xw540-t260/")
[XW430-T200](https://emanual.robotis.com/docs/en/dxl/x/xw430-t200/ "https://emanual.robotis.com/docs/en/dxl/x/xw430-t200/")
[XW430-T333](https://emanual.robotis.com/docs/en/dxl/x/xw430-t333/ "https://emanual.robotis.com/docs/en/dxl/x/xw430-t333/")

XD Series

[XD540-T150](https://emanual.robotis.com/docs/en/dxl/x/xd540-t150/ "https://emanual.robotis.com/docs/en/dxl/x/xd540-t150/")
[XD540-T270](https://emanual.robotis.com/docs/en/dxl/x/xd540-t270/ "https://emanual.robotis.com/docs/en/dxl/x/xd540-t270/")
[XD430-T210](https://emanual.robotis.com/docs/en/dxl/x/xd430-t210/ "https://emanual.robotis.com/docs/en/dxl/x/xd430-t210/")
[XD430-T350](https://emanual.robotis.com/docs/en/dxl/x/xd430-t350/ "https://emanual.robotis.com/docs/en/dxl/x/xd430-t350/")

XH Series

[XH540-W150](https://emanual.robotis.com/docs/en/dxl/x/xh540-w150/ "https://emanual.robotis.com/docs/en/dxl/x/xh540-w150/")
[XH540-W270](https://emanual.robotis.com/docs/en/dxl/x/xh540-w270/ "https://emanual.robotis.com/docs/en/dxl/x/xh540-w270/")
[XH540-V150](https://emanual.robotis.com/docs/en/dxl/x/xh540-v150/ "https://emanual.robotis.com/docs/en/dxl/x/xh540-v150/")
[XH540-V270](https://emanual.robotis.com/docs/en/dxl/x/xh540-v270/ "https://emanual.robotis.com/docs/en/dxl/x/xh540-v270/")
[XH430-W210](https://emanual.robotis.com/docs/en/dxl/x/xh430-w210/ "https://emanual.robotis.com/docs/en/dxl/x/xh430-w210/")
[XH430-W350](https://emanual.robotis.com/docs/en/dxl/x/xh430-w350/ "https://emanual.robotis.com/docs/en/dxl/x/xh430-w350/")
[XH430-V210](https://emanual.robotis.com/docs/en/dxl/x/xh430-v210/ "https://emanual.robotis.com/docs/en/dxl/x/xh430-v210/")
[XH430-V350](https://emanual.robotis.com/docs/en/dxl/x/xh430-v350/ "https://emanual.robotis.com/docs/en/dxl/x/xh430-v350/")

XM Series

[XM540-W150](https://emanual.robotis.com/docs/en/dxl/x/xm540-w150/ "https://emanual.robotis.com/docs/en/dxl/x/xm540-w150/")
[XM540-W270](https://emanual.robotis.com/docs/en/dxl/x/xm540-w270/ "https://emanual.robotis.com/docs/en/dxl/x/xm540-w270/")
[XM430-W210](https://emanual.robotis.com/docs/en/dxl/x/xm430-w210/ "https://emanual.robotis.com/docs/en/dxl/x/xm430-w210/")
[XM430-W350](https://emanual.robotis.com/docs/en/dxl/x/xm430-w350/ "https://emanual.robotis.com/docs/en/dxl/x/xm430-w350/")

XC Series

[2XC430-W250](https://emanual.robotis.com/docs/en/dxl/x/2xc430-w250/ "https://emanual.robotis.com/docs/en/dxl/x/2xc430-w250/")
[XC430-W150](https://emanual.robotis.com/docs/en/dxl/x/xc430-w150/ "https://emanual.robotis.com/docs/en/dxl/x/xc430-w150/")
[XC430-W240](https://emanual.robotis.com/docs/en/dxl/x/xc430-w240/ "https://emanual.robotis.com/docs/en/dxl/x/xc430-w240/")
[XC430-T150BB](https://emanual.robotis.com/docs/en/dxl/x/xc430-t150bb/ "https://emanual.robotis.com/docs/en/dxl/x/xc430-t150bb/")
[XC430-T240BB](https://emanual.robotis.com/docs/en/dxl/x/xc430-t240bb/ "https://emanual.robotis.com/docs/en/dxl/x/xc430-t240bb/")
[XC330-T288](https://emanual.robotis.com/docs/en/dxl/x/xc330-t288/ "https://emanual.robotis.com/docs/en/dxl/x/xc330-t288/")
[XC330-T181](https://emanual.robotis.com/docs/en/dxl/x/xc330-t181/ "https://emanual.robotis.com/docs/en/dxl/x/xc330-t181/")
[XC330-M181](https://emanual.robotis.com/docs/en/dxl/x/xc330-m181/ "https://emanual.robotis.com/docs/en/dxl/x/xc330-m181/")
[XC330-M288](https://emanual.robotis.com/docs/en/dxl/x/xc330-m288/ "https://emanual.robotis.com/docs/en/dxl/x/xc330-m288/")

XL Series

[2XL430-W250](https://emanual.robotis.com/docs/en/dxl/x/2xl430-w250/ "https://emanual.robotis.com/docs/en/dxl/x/2xl430-w250/")
[XL430-W250](https://emanual.robotis.com/docs/en/dxl/x/xl430-w250/ "https://emanual.robotis.com/docs/en/dxl/x/xl430-w250/")
[XL330-M077](https://emanual.robotis.com/docs/en/dxl/x/xl330-m077/ "https://emanual.robotis.com/docs/en/dxl/x/xl330-m077/")
[XL330-M288](https://emanual.robotis.com/docs/en/dxl/x/xl330-m288/ "https://emanual.robotis.com/docs/en/dxl/x/xl330-m288/")
[XL-320](https://emanual.robotis.com/docs/en/dxl/x/xl320/ "https://emanual.robotis.com/docs/en/dxl/x/xl320/")

[MX Series](https://emanual.robotis.com/docs/en/dxl/mx/ "https://emanual.robotis.com/docs/en/dxl/mx/")

[MX-106T/R(2.0)](https://emanual.robotis.com/docs/en/dxl/mx/mx-106-2/ "https://emanual.robotis.com/docs/en/dxl/mx/mx-106-2/")
[MX-64T/R/AT/AR(2.0)](https://emanual.robotis.com/docs/en/dxl/mx/mx-64-2/ "https://emanual.robotis.com/docs/en/dxl/mx/mx-64-2/")
[MX-28T/R/AT/AR(2.0)](https://emanual.robotis.com/docs/en/dxl/mx/mx-28-2/ "https://emanual.robotis.com/docs/en/dxl/mx/mx-28-2/")
[MX-106T/R](https://emanual.robotis.com/docs/en/dxl/mx/mx-106/ "https://emanual.robotis.com/docs/en/dxl/mx/mx-106/")
[MX-64T/R/AT/AR](https://emanual.robotis.com/docs/en/dxl/mx/mx-64/ "https://emanual.robotis.com/docs/en/dxl/mx/mx-64/")
[MX-28T/R/AT/AR](https://emanual.robotis.com/docs/en/dxl/mx/mx-28/ "https://emanual.robotis.com/docs/en/dxl/mx/mx-28/")
[MX-12W](https://emanual.robotis.com/docs/en/dxl/mx/mx-12w/ "https://emanual.robotis.com/docs/en/dxl/mx/mx-12w/")

AX Series

[AX-18F/18A](https://emanual.robotis.com/docs/en/dxl/ax/ax-18a/ "https://emanual.robotis.com/docs/en/dxl/ax/ax-18a/")
[AX-12/12+/12A](https://emanual.robotis.com/docs/en/dxl/ax/ax-12a/ "https://emanual.robotis.com/docs/en/dxl/ax/ax-12a/")
[AX-12W](https://emanual.robotis.com/docs/en/dxl/ax/ax-12w/ "https://emanual.robotis.com/docs/en/dxl/ax/ax-12w/")

[DYNAMIXEL Protocol 1.0](https://emanual.robotis.com/docs/en/dxl/protocol1/ "https://emanual.robotis.com/docs/en/dxl/protocol1/")

[DYNAMIXEL Protocol 2.0](https://emanual.robotis.com/docs/en/dxl/protocol2/ "https://emanual.robotis.com/docs/en/dxl/protocol2/")

EX Series

[EX-106+](https://emanual.robotis.com/docs/en/dxl/ex/ex-106+/ "https://emanual.robotis.com/docs/en/dxl/ex/ex-106+/") 

DX Series

[DX-113](https://emanual.robotis.com/docs/en/dxl/dx/dx-113/ "https://emanual.robotis.com/docs/en/dxl/dx/dx-113/") 
[DX-116](https://emanual.robotis.com/docs/en/dxl/dx/dx-116/ "https://emanual.robotis.com/docs/en/dxl/dx/dx-116/") 
[DX-117](https://emanual.robotis.com/docs/en/dxl/dx/dx-117/ "https://emanual.robotis.com/docs/en/dxl/dx/dx-117/") 

RX Series

[RX-10](https://emanual.robotis.com/docs/en/dxl/rx/rx-10/ "https://emanual.robotis.com/docs/en/dxl/rx/rx-10/") 
[RX-24F](https://emanual.robotis.com/docs/en/dxl/rx/rx-24f/ "https://emanual.robotis.com/docs/en/dxl/rx/rx-24f/") 
[RX-28](https://emanual.robotis.com/docs/en/dxl/rx/rx-28/ "https://emanual.robotis.com/docs/en/dxl/rx/rx-28/") 
[RX-64](https://emanual.robotis.com/docs/en/dxl/rx/rx-64/ "https://emanual.robotis.com/docs/en/dxl/rx/rx-64/") 

[PRO Series](https://emanual.robotis.com/docs/en/dxl/pro/ "https://emanual.robotis.com/docs/en/dxl/pro/") 

[H54-200-S500-R(A)](https://emanual.robotis.com/docs/en/dxl/pro/h54-200-s500-ra/ "https://emanual.robotis.com/docs/en/dxl/pro/h54-200-s500-ra/") 
[H54-100-S500-R(A)](https://emanual.robotis.com/docs/en/dxl/pro/h54-100-s500-ra/ "https://emanual.robotis.com/docs/en/dxl/pro/h54-100-s500-ra/") 
[H42-20-S300-R(A)](https://emanual.robotis.com/docs/en/dxl/pro/h42-20-s300-ra/ "https://emanual.robotis.com/docs/en/dxl/pro/h42-20-s300-ra/") 
[M54-60-S250-R(A)](https://emanual.robotis.com/docs/en/dxl/pro/m54-60-s250-ra/ "https://emanual.robotis.com/docs/en/dxl/pro/m54-60-s250-ra/") 
[M54-40-S250-R(A)](https://emanual.robotis.com/docs/en/dxl/pro/m54-40-s250-ra/ "https://emanual.robotis.com/docs/en/dxl/pro/m54-40-s250-ra/") 
[M42-10-S260-R(A)](https://emanual.robotis.com/docs/en/dxl/pro/m42-10-s260-ra/ "https://emanual.robotis.com/docs/en/dxl/pro/m42-10-s260-ra/") 
[H54-200-S500-R](https://emanual.robotis.com/docs/en/dxl/pro/h54-200-s500-r/ "https://emanual.robotis.com/docs/en/dxl/pro/h54-200-s500-r/") 
[H54-100-S500-R](https://emanual.robotis.com/docs/en/dxl/pro/h54-100-s500-r/ "https://emanual.robotis.com/docs/en/dxl/pro/h54-100-s500-r/") 
[H42-20-S300-R](https://emanual.robotis.com/docs/en/dxl/pro/h42-20-s300-r/ "https://emanual.robotis.com/docs/en/dxl/pro/h42-20-s300-r/") 
[M54-60-S250-R](https://emanual.robotis.com/docs/en/dxl/pro/m54-60-s250-r/ "https://emanual.robotis.com/docs/en/dxl/pro/m54-60-s250-r/") 
[M54-40-S250-R](https://emanual.robotis.com/docs/en/dxl/pro/m54-40-s250-r/ "https://emanual.robotis.com/docs/en/dxl/pro/m54-40-s250-r/") 
[M42-10-S260-R](https://emanual.robotis.com/docs/en/dxl/pro/m42-10-s260-r/ "https://emanual.robotis.com/docs/en/dxl/pro/m42-10-s260-r/") 
[L54-50-S500-R](https://emanual.robotis.com/docs/en/dxl/pro/l54-50-s500-r/ "https://emanual.robotis.com/docs/en/dxl/pro/l54-50-s500-r/") 
[L54-50-S290-R](https://emanual.robotis.com/docs/en/dxl/pro/l54-50-s290-r/ "https://emanual.robotis.com/docs/en/dxl/pro/l54-50-s290-r/") 
[L54-30-S500-R](https://emanual.robotis.com/docs/en/dxl/pro/l54-30-s500-r/ "https://emanual.robotis.com/docs/en/dxl/pro/l54-30-s500-r/") 
[L54-30-S400-R](https://emanual.robotis.com/docs/en/dxl/pro/l54-30-s400-r/ "https://emanual.robotis.com/docs/en/dxl/pro/l54-30-s400-r/") 
[L42-10-S300-R](https://emanual.robotis.com/docs/en/dxl/pro/l42-10-s300-r/ "https://emanual.robotis.com/docs/en/dxl/pro/l42-10-s300-r/") 

 DYNAMIXEL  SYSTEM

[TurtleBot3](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/ "https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/")

[OpenMANIPULATOR](https://emanual.robotis.com/docs/en/platform/openmanipulator_main "https://emanual.robotis.com/docs/en/platform/openmanipulator_main")

[OpenMANIPULATOR-P](https://emanual.robotis.com/docs/en/platform/openmanipulator_p/overview/ "https://emanual.robotis.com/docs/en/platform/openmanipulator_p/overview/")
[OpenMANIPULATOR-X](https://emanual.robotis.com/docs/en/platform/openmanipulator_x/overview/ "https://emanual.robotis.com/docs/en/platform/openmanipulator_x/overview/")
[Manipulator-H](https://emanual.robotis.com/docs/en/platform/manipulator_h/introduction/ "https://emanual.robotis.com/docs/en/platform/manipulator_h/introduction/") 

Robot Hands

[RH-P12-RN(A)](https://emanual.robotis.com/docs/en/platform/rh_p12_rna/ "https://emanual.robotis.com/docs/en/platform/rh_p12_rna/")
[RH-P12-RN-UR](https://emanual.robotis.com/docs/en/platform/rh_p12_rn_ur/ "https://emanual.robotis.com/docs/en/platform/rh_p12_rn_ur/")

[ROBOTIS OP](https://emanual.robotis.com/docs/en/platform/op/getting_started/ "https://emanual.robotis.com/docs/en/platform/op/getting_started/")

[ROBOTIS OP3](https://emanual.robotis.com/docs/en/platform/op3/introduction/ "https://emanual.robotis.com/docs/en/platform/op3/introduction/")
[ROBOTIS OP](https://emanual.robotis.com/docs/en/platform/op/getting_started/ "https://emanual.robotis.com/docs/en/platform/op/getting_started/") 
[ROBOTIS OP2](https://emanual.robotis.com/docs/en/platform/op2/getting_started/ "https://emanual.robotis.com/docs/en/platform/op2/getting_started/") 

[THORMANG3](https://emanual.robotis.com/docs/en/platform/thormang3/introduction/ "https://emanual.robotis.com/docs/en/platform/thormang3/introduction/")

 EDUCATIONAL  KITS

PLAY

[PLAY 300](https://emanual.robotis.com/docs/en/edu/play/play-300/ "https://emanual.robotis.com/docs/en/edu/play/play-300/")
[PLAY 600](https://emanual.robotis.com/docs/en/edu/play/play-600/ "https://emanual.robotis.com/docs/en/edu/play/play-600/")
[PLAY 700](https://emanual.robotis.com/docs/en/edu/play/play-700/ "https://emanual.robotis.com/docs/en/edu/play/play-700/")

ROBOTIS DREAM II

[LEVEL 1](https://emanual.robotis.com/docs/en/edu/dream/dream2-1/ "https://emanual.robotis.com/docs/en/edu/dream/dream2-1/")
[LEVEL 2](https://emanual.robotis.com/docs/en/edu/dream/dream2-2/ "https://emanual.robotis.com/docs/en/edu/dream/dream2-2/")
[LEVEL 3](https://emanual.robotis.com/docs/en/edu/dream/dream2-3/ "https://emanual.robotis.com/docs/en/edu/dream/dream2-3/")
[LEVEL 4](https://emanual.robotis.com/docs/en/edu/dream/dream2-4/ "https://emanual.robotis.com/docs/en/edu/dream/dream2-4/")
[LEVEL 5](https://emanual.robotis.com/docs/en/edu/dream/dream2-5/ "https://emanual.robotis.com/docs/en/edu/dream/dream2-5/")
[School Set](https://emanual.robotis.com/docs/en/edu/dream/dream2-schoolset/ "https://emanual.robotis.com/docs/en/edu/dream/dream2-schoolset/")

[ROBOTIS BIOLOID](https://emanual.robotis.com/docs/en/edu/bioloid/ "https://emanual.robotis.com/docs/en/edu/bioloid/")

[ROBOTIS STEM](https://emanual.robotis.com/docs/en/edu/bioloid/stem/ "https://emanual.robotis.com/docs/en/edu/bioloid/stem/")
[ROBOTIS PREMIUM](https://emanual.robotis.com/docs/en/edu/bioloid/premium/ "https://emanual.robotis.com/docs/en/edu/bioloid/premium/")
[ROBOTIS GP](https://emanual.robotis.com/docs/en/edu/bioloid/gp/ "https://emanual.robotis.com/docs/en/edu/bioloid/gp/")
[Beginner Level](https://emanual.robotis.com/docs/en/edu/bioloid/beginner/ "https://emanual.robotis.com/docs/en/edu/bioloid/beginner/") 
[Comprehensive Level](https://emanual.robotis.com/docs/en/edu/bioloid/comprehensive/ "https://emanual.robotis.com/docs/en/edu/bioloid/comprehensive/") 

ROBOTIS ENGINEER

[Kit 1](https://emanual.robotis.com/docs/en/edu/engineer/kit1/ "https://emanual.robotis.com/docs/en/edu/engineer/kit1/")
[Kit 2](https://emanual.robotis.com/docs/en/edu/engineer/kit2_introduction/ "https://emanual.robotis.com/docs/en/edu/engineer/kit2_introduction/")

[ROBOTIS MINI](https://emanual.robotis.com/docs/en/edu/mini/ "https://emanual.robotis.com/docs/en/edu/mini/")

[OLLO](https://emanual.robotis.com/docs/en/edu/ollo/ollo-4/ "https://emanual.robotis.com/docs/en/edu/ollo/ollo-4/") 

[BUG KIT](https://emanual.robotis.com/docs/en/edu/ollo/bugkit/ "https://emanual.robotis.com/docs/en/edu/ollo/bugkit/") 
[EXPLORER](https://emanual.robotis.com/docs/en/edu/ollo/explorer/ "https://emanual.robotis.com/docs/en/edu/ollo/explorer/") 
[INVENTOR](https://emanual.robotis.com/docs/en/edu/ollo/inventor/ "https://emanual.robotis.com/docs/en/edu/ollo/inventor/") 

DREAM

[LEVEL 2](https://emanual.robotis.com/docs/en/edu/dream/dream1-2/ "https://emanual.robotis.com/docs/en/edu/dream/dream1-2/") 
[LEVEL 3](https://emanual.robotis.com/docs/en/edu/dream/dream1-3/ "https://emanual.robotis.com/docs/en/edu/dream/dream1-3/") 
[LEVEL 4](https://emanual.robotis.com/docs/en/edu/dream/dream1-4/ "https://emanual.robotis.com/docs/en/edu/dream/dream1-4/") 
[SET A](https://emanual.robotis.com/docs/en/edu/dream/dream-a/ "https://emanual.robotis.com/docs/en/edu/dream/dream-a/") 
[SET B](https://emanual.robotis.com/docs/en/edu/dream/dream-b/ "https://emanual.robotis.com/docs/en/edu/dream/dream-b/") 

 SOFTWARE

DYNAMIXEL

[DYNAMIXEL SDK](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/overview/ "https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/overview/")
[DYNAMIXEL Workbench](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_workbench/ "https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_workbench/")
[DYNAMIXEL Wizard 2.0](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_wizard2/ "https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_wizard2/")

Mobile Apps

[ROBOTIS MINI](https://emanual.robotis.com/docs/en/software/mobile_app/mini_app/ "https://emanual.robotis.com/docs/en/software/mobile_app/mini_app/")
[R+ Block](https://emanual.robotis.com/docs/en/software/rplus2/rplus2_block/ "https://emanual.robotis.com/docs/en/software/rplus2/rplus2_block/")

R+ 1.0

[R+ Task](https://emanual.robotis.com/docs/en/software/rplus1/task/getting_started/ "https://emanual.robotis.com/docs/en/software/rplus1/task/getting_started/")
[R+ Manager](https://emanual.robotis.com/docs/en/software/rplus1/manager/ "https://emanual.robotis.com/docs/en/software/rplus1/manager/")
[R+ Motion](https://emanual.robotis.com/docs/en/software/rplus1/motion/ "https://emanual.robotis.com/docs/en/software/rplus1/motion/")
[Dynamixel Wizard](https://emanual.robotis.com/docs/en/software/rplus1/dynamixel_wizard/ "https://emanual.robotis.com/docs/en/software/rplus1/dynamixel_wizard/")

R+ 2.0

[R+ Task 2.0](https://emanual.robotis.com/docs/en/software/rplus2/task/ "https://emanual.robotis.com/docs/en/software/rplus2/task/")
[R+ Manager 2.0](https://emanual.robotis.com/docs/en/software/rplus2/manager/ "https://emanual.robotis.com/docs/en/software/rplus2/manager/")
[R+ Motion 2.0](https://emanual.robotis.com/docs/en/software/rplus2/motion/ "https://emanual.robotis.com/docs/en/software/rplus2/motion/")
[R+ Design 2.0](https://emanual.robotis.com/docs/en/software/rplus2/design/ "https://emanual.robotis.com/docs/en/software/rplus2/design/")
[R+ Scratch](https://emanual.robotis.com/docs/en/software/rplus2/scratch/ "https://emanual.robotis.com/docs/en/software/rplus2/scratch/")

[R+ Task 3.0](https://emanual.robotis.com/docs/en/software/rplustask3/ "https://emanual.robotis.com/docs/en/software/rplustask3/")

R+ Mobile

[R+ m.Task 2.0](https://emanual.robotis.com/docs/en/software/rplus_mobile/mtask20/ "https://emanual.robotis.com/docs/en/software/rplus_mobile/mtask20/")
[R+ m.Motion 2.0](https://emanual.robotis.com/docs/en/software/rplus_mobile/mmotion/ "https://emanual.robotis.com/docs/en/software/rplus_mobile/mmotion/")
[R+ m.Design](https://emanual.robotis.com/docs/en/software/rplus_mobile/mdesign/ "https://emanual.robotis.com/docs/en/software/rplus_mobile/mdesign/")

[EMBEDDED SDK](https://emanual.robotis.com/docs/en/software/embedded_sdk/ "https://emanual.robotis.com/docs/en/software/embedded_sdk/")

[Embedded C(CM-510/700)](https://emanual.robotis.com/docs/en/software/embedded_sdk/embedded_c_cm510/ "https://emanual.robotis.com/docs/en/software/embedded_sdk/embedded_c_cm510/")
[Embedded C(CM-530)](https://emanual.robotis.com/docs/en/software/embedded_sdk/embedded_c_cm530/ "https://emanual.robotis.com/docs/en/software/embedded_sdk/embedded_c_cm530/")
[ZIGBEE SDK](https://emanual.robotis.com/docs/en/software/embedded_sdk/zigbee_sdk/ "https://emanual.robotis.com/docs/en/software/embedded_sdk/zigbee_sdk/")

[Arduino IDE](https://emanual.robotis.com/docs/en/software/arduino_ide/ "https://emanual.robotis.com/docs/en/software/arduino_ide/")

[ROBOTIS Framework Packages](https://emanual.robotis.com/docs/en/software/robotis_framework_packages/ "https://emanual.robotis.com/docs/en/software/robotis_framework_packages/")

[ROBOTIS Manipulator library](https://emanual.robotis.com/docs/en/software/robotis_manipulator_libs/ "https://emanual.robotis.com/docs/en/software/robotis_manipulator_libs/")

[OpenCM IDE](https://emanual.robotis.com/docs/en/software/opencm_ide/getting_started/ "https://emanual.robotis.com/docs/en/software/opencm_ide/getting_started/") 

 PARTS

[Controller](https://emanual.robotis.com/docs/en/parts/controller/controller_compatibility/ "https://emanual.robotis.com/docs/en/parts/controller/controller_compatibility/")

[CM-50](https://emanual.robotis.com/docs/en/parts/controller/cm-50/ "https://emanual.robotis.com/docs/en/parts/controller/cm-50/")
[CM-150](https://emanual.robotis.com/docs/en/parts/controller/cm-150/ "https://emanual.robotis.com/docs/en/parts/controller/cm-150/")
[CM-151](https://emanual.robotis.com/docs/en/parts/controller/cm-151/ "https://emanual.robotis.com/docs/en/parts/controller/cm-151/")
[CM-200](https://emanual.robotis.com/docs/en/parts/controller/cm-200/ "https://emanual.robotis.com/docs/en/parts/controller/cm-200/")
[CM-530](https://emanual.robotis.com/docs/en/parts/controller/cm-530/ "https://emanual.robotis.com/docs/en/parts/controller/cm-530/")
[CM-550](https://emanual.robotis.com/docs/en/parts/controller/cm-550/ "https://emanual.robotis.com/docs/en/parts/controller/cm-550/")
[CM-700](https://emanual.robotis.com/docs/en/parts/controller/cm-700/ "https://emanual.robotis.com/docs/en/parts/controller/cm-700/")
[OpenRB-150](https://emanual.robotis.com/docs/en/parts/controller/openrb-150/ "https://emanual.robotis.com/docs/en/parts/controller/openrb-150/")
[OpenCM9.04](https://emanual.robotis.com/docs/en/parts/controller/opencm904/ "https://emanual.robotis.com/docs/en/parts/controller/opencm904/")
[OpenCM 485 EXP](https://emanual.robotis.com/docs/en/parts/controller/opencm485exp/ "https://emanual.robotis.com/docs/en/parts/controller/opencm485exp/")
[OpenCR1.0](https://emanual.robotis.com/docs/en/parts/controller/opencr10/ "https://emanual.robotis.com/docs/en/parts/controller/opencr10/")
[CM-100A](https://emanual.robotis.com/docs/en/parts/controller/cm-100/ "https://emanual.robotis.com/docs/en/parts/controller/cm-100/") 
[CM-5](https://emanual.robotis.com/docs/en/parts/controller/cm-5/ "https://emanual.robotis.com/docs/en/parts/controller/cm-5/") 
[CM-510](https://emanual.robotis.com/docs/en/parts/controller/cm-510/ "https://emanual.robotis.com/docs/en/parts/controller/cm-510/") 
[CM-900](https://emanual.robotis.com/docs/en/parts/controller/cm-900/ "https://emanual.robotis.com/docs/en/parts/controller/cm-900/") 

Communication

[RC-100A/100B](https://emanual.robotis.com/docs/en/parts/communication/rc-100/ "https://emanual.robotis.com/docs/en/parts/communication/rc-100/")
[RC-200](https://emanual.robotis.com/docs/en/parts/communication/rc-200/ "https://emanual.robotis.com/docs/en/parts/communication/rc-200/")
[BT-210](https://emanual.robotis.com/docs/en/parts/communication/bt-210/ "https://emanual.robotis.com/docs/en/parts/communication/bt-210/")
[BT-410](https://emanual.robotis.com/docs/en/parts/communication/bt-410/ "https://emanual.robotis.com/docs/en/parts/communication/bt-410/")
[BT-410 Dongle](https://emanual.robotis.com/docs/en/parts/communication/bt-410-dongle/ "https://emanual.robotis.com/docs/en/parts/communication/bt-410-dongle/")
[ZIG-100/110A](https://emanual.robotis.com/docs/en/parts/communication/zig-110/ "https://emanual.robotis.com/docs/en/parts/communication/zig-110/") 
[BT-100/110A](https://emanual.robotis.com/docs/en/parts/communication/bt-110/ "https://emanual.robotis.com/docs/en/parts/communication/bt-110/") 
[ZIG2Serial](https://emanual.robotis.com/docs/en/parts/communication/zig2serial/ "https://emanual.robotis.com/docs/en/parts/communication/zig2serial/") 

Motors

[Geared Motor](https://emanual.robotis.com/docs/en/parts/motor/gm-10a/ "https://emanual.robotis.com/docs/en/parts/motor/gm-10a/")
[Servo Motor](https://emanual.robotis.com/docs/en/parts/motor/servo_motor/ "https://emanual.robotis.com/docs/en/parts/motor/servo_motor/")
[High Speed Geared Motor](https://emanual.robotis.com/docs/en/parts/motor/h_speed_geared_motor/ "https://emanual.robotis.com/docs/en/parts/motor/h_speed_geared_motor/") 
[Low Speed Geared Motor](https://emanual.robotis.com/docs/en/parts/motor/l_speed_geared_motor/ "https://emanual.robotis.com/docs/en/parts/motor/l_speed_geared_motor/") 

Interface

[DYNAMIXEL Communication Bridge](https://emanual.robotis.com/docs/en/parts/interface/dxl_bridge/ "https://emanual.robotis.com/docs/en/parts/interface/dxl_bridge/")
[LN-101](https://emanual.robotis.com/docs/en/parts/interface/ln-101/ "https://emanual.robotis.com/docs/en/parts/interface/ln-101/")
[U2D2](https://emanual.robotis.com/docs/en/parts/interface/u2d2/ "https://emanual.robotis.com/docs/en/parts/interface/u2d2/")
[U2D2 Power Hub](https://emanual.robotis.com/docs/en/parts/interface/u2d2_power_hub/ "https://emanual.robotis.com/docs/en/parts/interface/u2d2_power_hub/")
[DYNAMIXEL Shield](https://emanual.robotis.com/docs/en/parts/interface/dynamixel_shield/ "https://emanual.robotis.com/docs/en/parts/interface/dynamixel_shield/")
[DYNAMIXEL Shield MKR](https://emanual.robotis.com/docs/en/parts/interface/mkr_shield/ "https://emanual.robotis.com/docs/en/parts/interface/mkr_shield/")
[USB2DYNAMIXEL](https://emanual.robotis.com/docs/en/parts/interface/usb2dynamixel/ "https://emanual.robotis.com/docs/en/parts/interface/usb2dynamixel/") 

Sensors

[IR Sensor](https://emanual.robotis.com/docs/en/parts/sensor/irss-10/ "https://emanual.robotis.com/docs/en/parts/sensor/irss-10/")
[Distance Sensor](https://emanual.robotis.com/docs/en/parts/sensor/dms-80/ "https://emanual.robotis.com/docs/en/parts/sensor/dms-80/")
[Touch Sensor](https://emanual.robotis.com/docs/en/parts/sensor/ts-10/ "https://emanual.robotis.com/docs/en/parts/sensor/ts-10/")
[Gyro Sensor](https://emanual.robotis.com/docs/en/parts/sensor/gs-12/ "https://emanual.robotis.com/docs/en/parts/sensor/gs-12/")
[IR Array Sensor](https://emanual.robotis.com/docs/en/parts/sensor/ir-array/ "https://emanual.robotis.com/docs/en/parts/sensor/ir-array/")
[Color Sensor](https://emanual.robotis.com/docs/en/parts/sensor/cs-10/ "https://emanual.robotis.com/docs/en/parts/sensor/cs-10/")
[Magnetic Sensor](https://emanual.robotis.com/docs/en/parts/sensor/mgss-10/ "https://emanual.robotis.com/docs/en/parts/sensor/mgss-10/")
[Temperature Sensor](https://emanual.robotis.com/docs/en/parts/sensor/tps-10/ "https://emanual.robotis.com/docs/en/parts/sensor/tps-10/")
[Motion Sensor](https://emanual.robotis.com/docs/en/parts/sensor/pir-10/ "https://emanual.robotis.com/docs/en/parts/sensor/pir-10/")
[Integrated Sensor](https://emanual.robotis.com/docs/en/parts/sensor/ax-s1/ "https://emanual.robotis.com/docs/en/parts/sensor/ax-s1/") 

Display

[LED Module](https://emanual.robotis.com/docs/en/parts/display/lm-10/ "https://emanual.robotis.com/docs/en/parts/display/lm-10/")

 FAQ

[DYNAMIXEL Selection Guide](https://emanual.robotis.com/docs/en/reference/dxl-selection-guide/ "https://emanual.robotis.com/docs/en/reference/dxl-selection-guide/")

[DYNAMIXEL Quick Start Guide](https://emanual.robotis.com/docs/en/dxl/dxl-quick-start-guide/ "https://emanual.robotis.com/docs/en/dxl/dxl-quick-start-guide/")

[DYNAMIXEL](https://emanual.robotis.com/docs/en/faq/faq_dynamixel/ "https://emanual.robotis.com/docs/en/faq/faq_dynamixel/")

[DYNAMIXEL SYSTEM](https://emanual.robotis.com/docs/en/faq/faq_platform/ "https://emanual.robotis.com/docs/en/faq/faq_platform/")

[EDUCATION KITS](https://emanual.robotis.com/docs/en/faq/faq_steam/ "https://emanual.robotis.com/docs/en/faq/faq_steam/")

[SOFTWARE](https://emanual.robotis.com/docs/en/faq/faq_software/ "https://emanual.robotis.com/docs/en/faq/faq_software/")

[PARTS](https://emanual.robotis.com/docs/en/faq/faq_parts/ "https://emanual.robotis.com/docs/en/faq/faq_parts/")

[GENERAL](https://emanual.robotis.com/docs/en/faq/general "https://emanual.robotis.com/docs/en/faq/general")

![](https://www.google.com/images/cleardot.gif)

 function googleTranslateElementInit() {
 new google.translate.TranslateElement({pageLanguage: 'en', includedLanguages: 'ar,de,es,fr,hi,ja,ko,pt,ru,sv,th,tr,vi,zh-CN', layout: google.translate.TranslateElement.InlineLayout.SIMPLE, multilanguagePage: true, gaTrack: true, gaId: 'UA-83196341'}, 'google\_translate\_element');
 }

N/A

[![](/assets/images/youtube_logo.png)Youtube](https://www.youtube.com/channel/UCDCsF6xgpeb5dAmTK9Usn_g?view_as=subscriber "https://www.youtube.com/channel/UCDCsF6xgpeb5dAmTK9Usn_g?view_as=subscriber")
[![](/assets/images/shop_icon_36.png)  ROBOTIS](http://en.robotis.com "http://en.robotis.com") 
[![](/assets/images/community.jpeg)  Community](https://community.robotis.us/ "https://community.robotis.us/") 
[![](/assets/images/github_logo.png)  GitHub](https://github.com/ROBOTIS-GIT "https://github.com/ROBOTIS-GIT")

[![](/assets/images/youtube_logo.png)](https://www.youtube.com/channel/UCDCsF6xgpeb5dAmTK9Usn_g?view_as=subscriber "https://www.youtube.com/channel/UCDCsF6xgpeb5dAmTK9Usn_g?view_as=subscriber")
[![](/assets/images/shop_icon_28.png)](http://en.robotis.com "http://en.robotis.com")
[![](/assets/images/community.jpeg)](https://community.robotis.us/ "https://community.robotis.us/")
[![](/assets/images/github_logo.png)](https://github.com/ROBOTIS-GIT "https://github.com/ROBOTIS-GIT")

![](/assets/images/search_icon.png)

ToC
[▲  
TOP](# "#")

* [TurtleBot3](https://emanual.robotis.com/docs/en/platform/turtlebot3/bringup/ "https://emanual.robotis.com/docs/en/platform/turtlebot3/bringup/")
* 1. Overview
	+ [1. 1. Notices](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/#notices "https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/#notices")
	+ 1. 2. Events
		- [- Online Competition on RDS](https://emanual.robotis.com/docs/en/platform/turtlebot3/challenges/#online-competition-on-rds "https://emanual.robotis.com/docs/en/platform/turtlebot3/challenges/#online-competition-on-rds")
		- [- Offline Competition](https://emanual.robotis.com/docs/en/platform/turtlebot3/challenges/#offline-competition "https://emanual.robotis.com/docs/en/platform/turtlebot3/challenges/#offline-competition")
		- [- AutoRace RBIZ Challenge](https://emanual.robotis.com/docs/en/platform/turtlebot3/challenges/#autorace-rbiz-challenge "https://emanual.robotis.com/docs/en/platform/turtlebot3/challenges/#autorace-rbiz-challenge")
* 2. Features
	+ [2. 1. Specifications](https://emanual.robotis.com/docs/en/platform/turtlebot3/features/#specifications "https://emanual.robotis.com/docs/en/platform/turtlebot3/features/#specifications")
	+ [2. 2. Components](https://emanual.robotis.com/docs/en/platform/turtlebot3/features/#components "https://emanual.robotis.com/docs/en/platform/turtlebot3/features/#components")
* 3. Quick Start Guide
	+ [3. 1. PC Setup](https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/#pc-setup "https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/#pc-setup")
	+ [3. 2. SBC Setup](https://emanual.robotis.com/docs/en/platform/turtlebot3/sbc_setup/#sbc-setup "https://emanual.robotis.com/docs/en/platform/turtlebot3/sbc_setup/#sbc-setup")
	+ [3. 3. OpenCR Setup](https://emanual.robotis.com/docs/en/platform/turtlebot3/opencr_setup/#opencr-setup "https://emanual.robotis.com/docs/en/platform/turtlebot3/opencr_setup/#opencr-setup")
	+ [3. 4. Hardware Assembly](https://emanual.robotis.com/docs/en/platform/turtlebot3/hardware_setup/#hardware-assembly "https://emanual.robotis.com/docs/en/platform/turtlebot3/hardware_setup/#hardware-assembly")
	+ [3. 5. Bringup](https://emanual.robotis.com/docs/en/platform/turtlebot3/bringup/#bringup "https://emanual.robotis.com/docs/en/platform/turtlebot3/bringup/#bringup")
	+ 3. 6. Basic Operation
		- [- Teleoperation](https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_operation/#teleoperation "https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_operation/#teleoperation")
		- [- Topic Monitor](https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_operation/#topic-monitor "https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_operation/#topic-monitor")
* 4. SLAM
	+ [4. 1. Run SLAM Node](https://emanual.robotis.com/docs/en/platform/turtlebot3/slam/#run-slam-node "https://emanual.robotis.com/docs/en/platform/turtlebot3/slam/#run-slam-node")
	+ [4. 2. Run Teleoperation Node](https://emanual.robotis.com/docs/en/platform/turtlebot3/slam/#run-teleoperation-node "https://emanual.robotis.com/docs/en/platform/turtlebot3/slam/#run-teleoperation-node")
	+ [4. 3. Tuning Guide](https://emanual.robotis.com/docs/en/platform/turtlebot3/slam/#tuning-guide "https://emanual.robotis.com/docs/en/platform/turtlebot3/slam/#tuning-guide")
	+ [4. 4. Save Map](https://emanual.robotis.com/docs/en/platform/turtlebot3/slam/#save-map "https://emanual.robotis.com/docs/en/platform/turtlebot3/slam/#save-map")
	+ [4. 5. Map](https://emanual.robotis.com/docs/en/platform/turtlebot3/slam/#map "https://emanual.robotis.com/docs/en/platform/turtlebot3/slam/#map")
* 5. Navigation
	+ [5. 1. Run Navigation Nodes](https://emanual.robotis.com/docs/en/platform/turtlebot3/navigation/#run-navigation-nodes "https://emanual.robotis.com/docs/en/platform/turtlebot3/navigation/#run-navigation-nodes")
	+ [5. 2. Estimate Initial Pose](https://emanual.robotis.com/docs/en/platform/turtlebot3/navigation/#estimate-initial-pose "https://emanual.robotis.com/docs/en/platform/turtlebot3/navigation/#estimate-initial-pose")
	+ [5. 3. Set Navigation Goal](https://emanual.robotis.com/docs/en/platform/turtlebot3/navigation/#set-navigation-goal "https://emanual.robotis.com/docs/en/platform/turtlebot3/navigation/#set-navigation-goal")
	+ [5. 4. Tuning Guide](https://emanual.robotis.com/docs/en/platform/turtlebot3/navigation/#tuning-guide "https://emanual.robotis.com/docs/en/platform/turtlebot3/navigation/#tuning-guide")
* 6. Simulation
	+ [6. 1. Gazebo Simulation](https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/#gazebo-simulation "https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/#gazebo-simulation")
	+ [6. 2. SLAM Simulation](https://emanual.robotis.com/docs/en/platform/turtlebot3/slam_simulation/ "https://emanual.robotis.com/docs/en/platform/turtlebot3/slam_simulation/")
	+ [6. 3. Navigation Simulation](https://emanual.robotis.com/docs/en/platform/turtlebot3/nav_simulation/ "https://emanual.robotis.com/docs/en/platform/turtlebot3/nav_simulation/")
	+ [6. 4. Fake Node Simulation](https://emanual.robotis.com/docs/en/platform/turtlebot3/fakenode_simulation/ "https://emanual.robotis.com/docs/en/platform/turtlebot3/fakenode_simulation/")
	+ [6. 5. Standalone Gazebo Simulation](https://emanual.robotis.com/docs/en/platform/turtlebot3/standalone_gazebo_simulation/ "https://emanual.robotis.com/docs/en/platform/turtlebot3/standalone_gazebo_simulation/")
* 7. Manipulation
	+ [7. 1. TB3 & OpenMANIPULATOR-X](https://emanual.robotis.com/docs/en/platform/turtlebot3/manipulation/#turtlebot3-with-openmanipulator "https://emanual.robotis.com/docs/en/platform/turtlebot3/manipulation/#turtlebot3-with-openmanipulator")
	+ [7. 2. Software Setup](https://emanual.robotis.com/docs/en/platform/turtlebot3/manipulation/#software-setup "https://emanual.robotis.com/docs/en/platform/turtlebot3/manipulation/#software-setup")
	+ [7. 3. Hardware Assembly](https://emanual.robotis.com/docs/en/platform/turtlebot3/manipulation/#hardware-assembly "https://emanual.robotis.com/docs/en/platform/turtlebot3/manipulation/#hardware-assembly")
	+ [7. 4. OpenCR Setup](https://emanual.robotis.com/docs/en/platform/turtlebot3/manipulation/#opencr-setup "https://emanual.robotis.com/docs/en/platform/turtlebot3/manipulation/#opencr-setup")
	+ [7. 5. Bringup](https://emanual.robotis.com/docs/en/platform/turtlebot3/manipulation/#bringup "https://emanual.robotis.com/docs/en/platform/turtlebot3/manipulation/#bringup")
	+ [7. 6. Simulation](https://emanual.robotis.com/docs/en/platform/turtlebot3/manipulation/#simulation "https://emanual.robotis.com/docs/en/platform/turtlebot3/manipulation/#simulation")
	+ [7. 7. Operate the Actual OpenMANIPULATOR](https://emanual.robotis.com/docs/en/platform/turtlebot3/manipulation/#operate-the-actual-openmanipulator "https://emanual.robotis.com/docs/en/platform/turtlebot3/manipulation/#operate-the-actual-openmanipulator")
	+ [7. 8. SLAM](https://emanual.robotis.com/docs/en/platform/turtlebot3/manipulation/#slam "https://emanual.robotis.com/docs/en/platform/turtlebot3/manipulation/#slam")
	+ [7. 9. Navigation](https://emanual.robotis.com/docs/en/platform/turtlebot3/manipulation/#navigation "https://emanual.robotis.com/docs/en/platform/turtlebot3/manipulation/#navigation")
	+ 7. 10. Home Service Challenge
		- [- Getting Started](https://emanual.robotis.com/docs/en/platform/turtlebot3/home_service_challenge/#getting-started "https://emanual.robotis.com/docs/en/platform/turtlebot3/home_service_challenge/#getting-started")
		- [- Camera Calibration](https://emanual.robotis.com/docs/en/platform/turtlebot3/home_service_challenge/#camera-calibration "https://emanual.robotis.com/docs/en/platform/turtlebot3/home_service_challenge/#camera-calibration")
		- [- SLAM](https://emanual.robotis.com/docs/en/platform/turtlebot3/home_service_challenge/#slam "https://emanual.robotis.com/docs/en/platform/turtlebot3/home_service_challenge/#slam")
		- [- Missions](https://emanual.robotis.com/docs/en/platform/turtlebot3/home_service_challenge/#missions "https://emanual.robotis.com/docs/en/platform/turtlebot3/home_service_challenge/#missions")
		- [- Simulation](https://emanual.robotis.com/docs/en/platform/turtlebot3/home_service_challenge/#simulation "https://emanual.robotis.com/docs/en/platform/turtlebot3/home_service_challenge/#simulation")
* 8. Autonomous Driving
	+ [8. 1. Getting Started](https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#getting-started "https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#getting-started")
	+ 8. 2. Camera Calibration
		- [- Camera Imaging Calibration](https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#camera-imaging-calibration "https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#camera-imaging-calibration")
		- [- Intrinsic Camera Calibration](https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#intrinsic-camera-calibration "https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#intrinsic-camera-calibration")
		- [- Extrinsic Camera Calibration](https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#extrinsic-camera-calibration "https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#extrinsic-camera-calibration")
		- [- Check Calibration Result](https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#check-calibration-result "https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#check-calibration-result")
	+ [8. 3. Lane Detection](https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#lane-detection "https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#lane-detection")
	+ [8. 4. Traffic Sign Detection](https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#traffic-sign-detection "https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#traffic-sign-detection")
	+ 8. 5. Missions
		- [- Traffic Lights](https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#traffic-lights "https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#traffic-lights")
		- [- Intersection](https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#intersection "https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#intersection")
		- [- Construction](https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#construction "https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#construction")
		- [- Parking](https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#parking "https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#parking")
		- [- Level Crossing](https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#level-crossing "https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#level-crossing")
		- [- Tunnel](https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#tunnel "https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/#tunnel")
	+ [8. 6. TurtleBot3 AutoRace 2019](https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving_autorace/ "https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving_autorace/")
* 9. Machine Learning
	+ [9. 1. Software Setup](https://emanual.robotis.com/docs/en/platform/turtlebot3/machine_learning/#software-setup "https://emanual.robotis.com/docs/en/platform/turtlebot3/machine_learning/#software-setup")
	+ [9. 2. Set parameters](https://emanual.robotis.com/docs/en/platform/turtlebot3/machine_learning/#set-parameters "https://emanual.robotis.com/docs/en/platform/turtlebot3/machine_learning/#set-parameters")
	+ [9. 3. Run Machine Learning](https://emanual.robotis.com/docs/en/platform/turtlebot3/machine_learning/#run-machine-learning "https://emanual.robotis.com/docs/en/platform/turtlebot3/machine_learning/#run-machine-learning")
* 10. Examples
	+ [10. 1. Interactive Markers](https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_examples/#move-using-interactive-markers "https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_examples/#move-using-interactive-markers")
	+ [10. 2. Obstacle Detection](https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_examples/#obstacle-detection "https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_examples/#obstacle-detection")
	+ [10. 3. Position Control](https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_examples/#position-control "https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_examples/#position-control")
	+ [10. 4. Point Operation](https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_examples/#point-operation "https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_examples/#point-operation")
	+ [10. 5. Patrol](https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_examples/#patrol "https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_examples/#patrol")
	+ [10. 6. TurtleBot Follower Demo](https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_examples/#turtlebot-follower-demo "https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_examples/#turtlebot-follower-demo")
	+ [10. 7. TurtleBot Panorama Demo](https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_examples/#turtlebot-panorama-demo "https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_examples/#turtlebot-panorama-demo")
	+ [10. 8. Automatic Parking](https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_examples/#automatic-parking "https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_examples/#automatic-parking")
	+ [10. 9. Automatic Parking Vision](https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_examples/#automatic-parking-vision "https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_examples/#automatic-parking-vision")
	+ [10. 10. Load Multiple TurtleBot3s](https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_examples/#load-multiple-turtlebot3s "https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_examples/#load-multiple-turtlebot3s")
* 11. Friends(Locomotion)
	+ [11. 1. TurtleBot3 Friends: Car](https://emanual.robotis.com/docs/en/platform/turtlebot3/locomotion/#turtlebot3-friends-car "https://emanual.robotis.com/docs/en/platform/turtlebot3/locomotion/#turtlebot3-friends-car")
	+ [11. 2. TurtleBot3 Friends: OpenMANIPULATOR](https://emanual.robotis.com/docs/en/platform/turtlebot3/locomotion/#turtlebot3-friends-openmanipulator "https://emanual.robotis.com/docs/en/platform/turtlebot3/locomotion/#turtlebot3-friends-openmanipulator")
	+ [11. 3. TurtleBot3 Friends: Segway](https://emanual.robotis.com/docs/en/platform/turtlebot3/locomotion/#turtlebot3-friends-segway "https://emanual.robotis.com/docs/en/platform/turtlebot3/locomotion/#turtlebot3-friends-segway")
	+ [11. 4. TurtleBot3 Friends: Conveyor](https://emanual.robotis.com/docs/en/platform/turtlebot3/locomotion/#turtlebot3-friends-conveyor "https://emanual.robotis.com/docs/en/platform/turtlebot3/locomotion/#turtlebot3-friends-conveyor")
	+ [11. 5. TurtleBot3 Friends: Monster](https://emanual.robotis.com/docs/en/platform/turtlebot3/locomotion/#turtlebot3-friends-monster "https://emanual.robotis.com/docs/en/platform/turtlebot3/locomotion/#turtlebot3-friends-monster")
	+ [11. 6. TurtleBot3 Friends: Tank](https://emanual.robotis.com/docs/en/platform/turtlebot3/locomotion/#turtlebot3-friends-tank "https://emanual.robotis.com/docs/en/platform/turtlebot3/locomotion/#turtlebot3-friends-tank")
	+ [11. 7. TurtleBot3 Friends: Omni](https://emanual.robotis.com/docs/en/platform/turtlebot3/locomotion/#turtlebot3-friends-omni "https://emanual.robotis.com/docs/en/platform/turtlebot3/locomotion/#turtlebot3-friends-omni")
	+ [11. 8. TurtleBot3 Friends: Mecanum](https://emanual.robotis.com/docs/en/platform/turtlebot3/locomotion/#turtlebot3-friends-mecanum "https://emanual.robotis.com/docs/en/platform/turtlebot3/locomotion/#turtlebot3-friends-mecanum")
	+ [11. 9. TurtleBot3 Friends: Bike](https://emanual.robotis.com/docs/en/platform/turtlebot3/locomotion/#turtlebot3-friends-bike "https://emanual.robotis.com/docs/en/platform/turtlebot3/locomotion/#turtlebot3-friends-bike")
	+ [11. 10. TurtleBot3 Friends: Road Train](https://emanual.robotis.com/docs/en/platform/turtlebot3/locomotion/#turtlebot3-friends-road-train "https://emanual.robotis.com/docs/en/platform/turtlebot3/locomotion/#turtlebot3-friends-road-train")
	+ [11. 11. TurtleBot3 Friends: Real TurtleBot](https://emanual.robotis.com/docs/en/platform/turtlebot3/locomotion/#turtlebot3-friends-real-turtlebot "https://emanual.robotis.com/docs/en/platform/turtlebot3/locomotion/#turtlebot3-friends-real-turtlebot")
	+ [11. 12. TurtleBot3 Friends: Carrier](https://emanual.robotis.com/docs/en/platform/turtlebot3/locomotion/#turtlebot3-friends-carrier "https://emanual.robotis.com/docs/en/platform/turtlebot3/locomotion/#turtlebot3-friends-carrier")
* 12. Learn
	+ [12. 1. AWS RoboMaker with TurtleBot3](https://emanual.robotis.com/docs/en/platform/turtlebot3/learn/#aws-robomaker-with-turtlebot3 "https://emanual.robotis.com/docs/en/platform/turtlebot3/learn/#aws-robomaker-with-turtlebot3")
	+ [12. 2. Data Collection via Matlab](https://emanual.robotis.com/docs/en/platform/turtlebot3/learn/#data-collection-via-matlab "https://emanual.robotis.com/docs/en/platform/turtlebot3/learn/#data-collection-via-matlab")
	+ [12. 3. TurtleBot3 Blockly](https://emanual.robotis.com/docs/en/platform/turtlebot3/learn/#turtlebot3-blockly "https://emanual.robotis.com/docs/en/platform/turtlebot3/learn/#turtlebot3-blockly")
	+ [12. 4. TurtleBot3 Simulation on ROS Indigo](https://emanual.robotis.com/docs/en/platform/turtlebot3/learn/#turtlebot3-simulation-on-ros-indigo "https://emanual.robotis.com/docs/en/platform/turtlebot3/learn/#turtlebot3-simulation-on-ros-indigo")
	+ [12. 5. Youtube Course](https://emanual.robotis.com/docs/en/platform/turtlebot3/learn/#youtube-course "https://emanual.robotis.com/docs/en/platform/turtlebot3/learn/#youtube-course")
	+ [12. 6. Books](https://emanual.robotis.com/docs/en/platform/turtlebot3/learn/#books "https://emanual.robotis.com/docs/en/platform/turtlebot3/learn/#books")
	+ 12. 7. Videos
		- [- Open Source Team](https://emanual.robotis.com/docs/en/platform/turtlebot3/videos/#videos-from-open-source-team "https://emanual.robotis.com/docs/en/platform/turtlebot3/videos/#videos-from-open-source-team")
		- [- ROBOTIS Channel](https://emanual.robotis.com/docs/en/platform/turtlebot3/videos/#videos-from-robotis-channel "https://emanual.robotis.com/docs/en/platform/turtlebot3/videos/#videos-from-robotis-channel")
		- [- Projects](https://emanual.robotis.com/docs/en/platform/turtlebot3/projects/ "https://emanual.robotis.com/docs/en/platform/turtlebot3/projects/")
* 13. More Info
	+ 13. 1. Appendixes
		- [- DYNAMIXEL](https://emanual.robotis.com/docs/en/platform/turtlebot3/appendixes/#dynamixel "https://emanual.robotis.com/docs/en/platform/turtlebot3/appendixes/#dynamixel")
		- [- OpenCR1.0](https://emanual.robotis.com/docs/en/platform/turtlebot3/appendix_opencr1_0/ "https://emanual.robotis.com/docs/en/platform/turtlebot3/appendix_opencr1_0/")
		- [- LDS-01](https://emanual.robotis.com/docs/en/platform/turtlebot3/appendix_lds_01/ "https://emanual.robotis.com/docs/en/platform/turtlebot3/appendix_lds_01/")
		- [- LDS-02](https://emanual.robotis.com/docs/en/platform/turtlebot3/appendix_lds_02/ "https://emanual.robotis.com/docs/en/platform/turtlebot3/appendix_lds_02/")
		- [- RealSense™](https://emanual.robotis.com/docs/en/platform/turtlebot3/appendix_realsense/ "https://emanual.robotis.com/docs/en/platform/turtlebot3/appendix_realsense/")
		- [- Raspberry Pi Camera](https://emanual.robotis.com/docs/en/platform/turtlebot3/appendix_raspi_cam/ "https://emanual.robotis.com/docs/en/platform/turtlebot3/appendix_raspi_cam/")
	+ [13. 2. Compatible Devices](https://emanual.robotis.com/docs/en/platform/turtlebot3/compatible_devices/ "https://emanual.robotis.com/docs/en/platform/turtlebot3/compatible_devices/")
	+ [13. 3. Additional Sensors](https://emanual.robotis.com/docs/en/platform/turtlebot3/additional_sensors/ "https://emanual.robotis.com/docs/en/platform/turtlebot3/additional_sensors/")
	+ 13. 4. OpenSource and Licenses
		- [- OpenSource Software](https://emanual.robotis.com/docs/en/platform/turtlebot3/opensource/#opensource-software "https://emanual.robotis.com/docs/en/platform/turtlebot3/opensource/#opensource-software")
		- [- OpenSource Hardware](https://emanual.robotis.com/docs/en/platform/turtlebot3/opensource/#opensource-hardware "https://emanual.robotis.com/docs/en/platform/turtlebot3/opensource/#opensource-hardware")
		- [- Software License](https://emanual.robotis.com/docs/en/platform/turtlebot3/opensource/#software-license "https://emanual.robotis.com/docs/en/platform/turtlebot3/opensource/#software-license")
		- [- Hardware License](https://emanual.robotis.com/docs/en/platform/turtlebot3/opensource/#hardware-license "https://emanual.robotis.com/docs/en/platform/turtlebot3/opensource/#hardware-license")
		- [- Documents License](https://emanual.robotis.com/docs/en/platform/turtlebot3/opensource/#documents-license "https://emanual.robotis.com/docs/en/platform/turtlebot3/opensource/#documents-license")
	+ 13. 5. Contact US
		- [- About Open Robotics](https://emanual.robotis.com/docs/en/platform/turtlebot3/contact_us/#about-open-robotics "https://emanual.robotis.com/docs/en/platform/turtlebot3/contact_us/#about-open-robotics")
		- [- About ROBOTIS](https://emanual.robotis.com/docs/en/platform/turtlebot3/contact_us/#about-robotis "https://emanual.robotis.com/docs/en/platform/turtlebot3/contact_us/#about-robotis")
		- [- About OST (Open Source Team)](https://emanual.robotis.com/docs/en/platform/turtlebot3/contact_us/#about-ost-open-source-team "https://emanual.robotis.com/docs/en/platform/turtlebot3/contact_us/#about-ost-open-source-team")
* [14. FAQ](https://emanual.robotis.com/docs/en/platform/turtlebot3/faq/#faq "https://emanual.robotis.com/docs/en/platform/turtlebot3/faq/#faq")

[Edit on GitHub](https://github.com/ROBOTIS-GIT/emanual/blob/master/docs/en/platform/turtlebot3/quick_start/bringup.md "https://github.com/ROBOTIS-GIT/emanual/blob/master/docs/en/platform/turtlebot3/quick_start/bringup.md") 

Kinetic 
Melodic
Noetic
Dashing
Foxy
Humble
Windows

## [Bringup](#bringup "#bringup")

### [Run roscore](#run-roscore "#run-roscore")

Run roscore from PC.

```
$ roscore

```

### [Bringup TurtleBot3](#bringup-turtlebot3 "#bringup-turtlebot3")

1. Open a new terminal from PC with `Ctrl` + `Alt` + `T` and connect to Raspberry Pi with its IP address.  

 The default password is **turtlebot**.

```
$ ssh pi@{IP_ADDRESS_OF_RASPBERRY_PI}

```
2. Bring up basic packages to start TurtleBot3 applications.

```
$ roslaunch turtlebot3_bringup turtlebot3_robot.launch

```
3. If the TurtleBot3 model is `burger`, the terminal will print below messages.

```
 SUMMARY
 ========

 PARAMETERS
 \* /rosdistro: kinetic
 \* /rosversion: 1.12.13
 \* /turtlebot3_core/baud: 115200
 \* /turtlebot3_core/port: /dev/ttyACM0
 \* /turtlebot3_core/tf_prefix:
 \* /turtlebot3_lds/frame_id: base_scan
 \* /turtlebot3_lds/port: /dev/ttyUSB0

 NODES
 /
     turtlebot3_core (rosserial_python/serial_node.py)
     turtlebot3_diagnostics (turtlebot3_bringup/turtlebot3_diagnostics)
     turtlebot3_lds (hls_lfcd_lds_driver/hlds_laser_publisher)

 ROS\_MASTER\_URI=http://192.168.1.2:11311

 process[turtlebot3_core-1]: started with pid [14198]
 process[turtlebot3_lds-2]: started with pid [14199]
 process[turtlebot3_diagnostics-3]: started with pid [14200]
 [INFO] [1531306690.947198]: ROS Serial Python Node
 [INFO] [1531306691.000143]: Connecting to /dev/ttyACM0 at 115200 baud
 [INFO] [1531306693.522019]: Note: publish buffer size is 1024 bytes
 [INFO] [1531306693.525615]: Setup publisher on sensor_state [turtlebot3_msgs/SensorState]
 [INFO] [1531306693.544159]: Setup publisher on version_info [turtlebot3_msgs/VersionInfo]
 [INFO] [1531306693.620722]: Setup publisher on imu [sensor_msgs/Imu]
 [INFO] [1531306693.642319]: Setup publisher on cmd_vel_rc100 [geometry_msgs/Twist]
 [INFO] [1531306693.687786]: Setup publisher on odom [nav_msgs/Odometry]
 [INFO] [1531306693.706260]: Setup publisher on joint_states [sensor_msgs/JointState]
 [INFO] [1531306693.722754]: Setup publisher on battery_state [sensor_msgs/BatteryState]
 [INFO] [1531306693.759059]: Setup publisher on magnetic_field [sensor_msgs/MagneticField]
 [INFO] [1531306695.979057]: Setup publisher on /tf [tf/tfMessage]
 [INFO] [1531306696.007135]: Note: subscribe buffer size is 1024 bytes
 [INFO] [1531306696.009083]: Setup subscriber on cmd_vel [geometry_msgs/Twist]
 [INFO] [1531306696.040047]: Setup subscriber on sound [turtlebot3_msgs/Sound]
 [INFO] [1531306696.069571]: Setup subscriber on motor_power [std_msgs/Bool]
 [INFO] [1531306696.096364]: Setup subscriber on reset [std_msgs/Empty]
 [INFO] [1531306696.390979]: Setup TF on Odometry [odom]
 [INFO] [1531306696.394314]: Setup TF on IMU [imu_link]
 [INFO] [1531306696.397498]: Setup TF on MagneticField [mag_link]
 [INFO] [1531306696.400537]: Setup TF on JointState [base_link]
 [INFO] [1531306696.407813]: --------------------------
 [INFO] [1531306696.411412]: Connected to OpenCR board!
 [INFO] [1531306696.415140]: This core(v1.2.1) is compatible with TB3 Burger
 [INFO] [1531306696.418398]: --------------------------
 [INFO] [1531306696.421749]: Start Calibration of Gyro
 [INFO] [1531306698.953226]: Calibration End

```

![](/assets/images/icon_unfold.png)

### [Load TurtleBot3 on Rviz](#load-turtlebot3-on-rviz "#load-turtlebot3-on-rviz")

1. Open a new terminal and launch the robot state publisher.

```
$ roslaunch turtlebot3_bringup turtlebot3_remote.launch

```
2. Open a new terminal and enter the below command to run RViz.

```
$ rosrun rviz rviz -d `rospack find turtlebot3_description`/rviz/model.rviz

```

![](/assets/images/platform/turtlebot3/bringup/run_rviz.jpg)

## [Bringup](#bringup "#bringup")

### [Run roscore](#run-roscore "#run-roscore")

Run roscore from PC.

```
$ roscore

```

### [Bringup TurtleBot3](#bringup-turtlebot3 "#bringup-turtlebot3")

1. Open a new terminal from PC with `Ctrl` + `Alt` + `T` and connect to Raspberry Pi with its IP address.  

 The default password is **turtlebot**.

```
$ ssh ubuntu@{IP_ADDRESS_OF_RASPBERRY_PI}

```
2. Bring up basic packages to start TurtleBot3 applications.

```
$ roslaunch turtlebot3_bringup turtlebot3_robot.launch

```
3. If the TurtleBot3 model is `burger`, the terminal will print below messages.

```
 SUMMARY
 ========

 PARAMETERS
 \* /rosdistro: melodic
 \* /rosversion: 1.14.3
 \* /turtlebot3_core/baud: 115200
 \* /turtlebot3_core/port: /dev/ttyACM0
 \* /turtlebot3_core/tf_prefix:
 \* /turtlebot3_lds/frame_id: base_scan
 \* /turtlebot3_lds/port: /dev/ttyUSB0

 NODES
 /
     turtlebot3_core (rosserial_python/serial_node.py)
     turtlebot3_diagnostics (turtlebot3_bringup/turtlebot3_diagnostics)
     turtlebot3_lds (hls_lfcd_lds_driver/hlds_laser_publisher)

 ROS\_MASTER\_URI=http://192.168.1.2:11311

 process[turtlebot3_core-1]: started with pid [14198]
 process[turtlebot3_lds-2]: started with pid [14199]
 process[turtlebot3_diagnostics-3]: started with pid [14200]
 [INFO] [1531306690.947198]: ROS Serial Python Node
 [INFO] [1531306691.000143]: Connecting to /dev/ttyACM0 at 115200 baud
 [INFO] [1531306693.522019]: Note: publish buffer size is 1024 bytes
 [INFO] [1531306693.525615]: Setup publisher on sensor_state [turtlebot3_msgs/SensorState]
 [INFO] [1531306693.544159]: Setup publisher on version_info [turtlebot3_msgs/VersionInfo]
 [INFO] [1531306693.620722]: Setup publisher on imu [sensor_msgs/Imu]
 [INFO] [1531306693.642319]: Setup publisher on cmd_vel_rc100 [geometry_msgs/Twist]
 [INFO] [1531306693.687786]: Setup publisher on odom [nav_msgs/Odometry]
 [INFO] [1531306693.706260]: Setup publisher on joint_states [sensor_msgs/JointState]
 [INFO] [1531306693.722754]: Setup publisher on battery_state [sensor_msgs/BatteryState]
 [INFO] [1531306693.759059]: Setup publisher on magnetic_field [sensor_msgs/MagneticField]
 [INFO] [1531306695.979057]: Setup publisher on /tf [tf/tfMessage]
 [INFO] [1531306696.007135]: Note: subscribe buffer size is 1024 bytes
 [INFO] [1531306696.009083]: Setup subscriber on cmd_vel [geometry_msgs/Twist]
 [INFO] [1531306696.040047]: Setup subscriber on sound [turtlebot3_msgs/Sound]
 [INFO] [1531306696.069571]: Setup subscriber on motor_power [std_msgs/Bool]
 [INFO] [1531306696.096364]: Setup subscriber on reset [std_msgs/Empty]
 [INFO] [1531306696.390979]: Setup TF on Odometry [odom]
 [INFO] [1531306696.394314]: Setup TF on IMU [imu_link]
 [INFO] [1531306696.397498]: Setup TF on MagneticField [mag_link]
 [INFO] [1531306696.400537]: Setup TF on JointState [base_link]
 [INFO] [1531306696.407813]: --------------------------
 [INFO] [1531306696.411412]: Connected to OpenCR board!
 [INFO] [1531306696.415140]: This core(v1.2.1) is compatible with TB3 Burger
 [INFO] [1531306696.418398]: --------------------------
 [INFO] [1531306696.421749]: Start Calibration of Gyro
 [INFO] [1531306698.953226]: Calibration End

```

![](/assets/images/icon_unfold.png)

### [Load TurtleBot3 on Rviz](#load-turtlebot3-on-rviz "#load-turtlebot3-on-rviz")

1. Open a new terminal and launch the robot state publisher.

```
$ roslaunch turtlebot3_bringup turtlebot3_remote.launch

```
2. Open a new terminal and enter the below command to run RViz.

```
$ rosrun rviz rviz -d `rospack find turtlebot3_description`/rviz/model.rviz

```

![](/assets/images/platform/turtlebot3/bringup/run_rviz.jpg)

## [Bringup](#bringup "#bringup")

### [Run roscore](#run-roscore "#run-roscore")

Run roscore from PC.

```
$ roscore

```

### [Bringup TurtleBot3](#bringup-turtlebot3 "#bringup-turtlebot3")

**TIP**: Before executing this command, you have to specify the model name of TurtleBot3. The `${TB3_MODEL}` is the name of the model you are using in `burger`, `waffle`, `waffle_pi`.

1. Open a new terminal from PC with `Ctrl` + `Alt` + `T` and connect to Raspberry Pi with its IP address.  

 The default password is **turtlebot**.

```
$ ssh ubuntu@{IP_ADDRESS_OF_RASPBERRY_PI}

```
2. Bring up basic packages to start TurtleBot3 applications.

```
$ export TURTLEBOT3\_MODEL=${TB3\_MODEL}
$ roslaunch turtlebot3_bringup turtlebot3_robot.launch

```
3. If the TurtleBot3 model is `burger`, the terminal will print below messages.

```
 SUMMARY
 ========

 PARAMETERS
 \* /rosdistro: noetic
 \* /rosversion: 1.15.8
 \* /turtlebot3_core/baud: 115200
 \* /turtlebot3_core/port: /dev/ttyACM0
 \* /turtlebot3_core/tf_prefix:
 \* /turtlebot3_lds/frame_id: base_scan
 \* /turtlebot3_lds/port: /dev/ttyUSB0

 NODES
 /
     turtlebot3_core (rosserial_python/serial_node.py)
     turtlebot3_diagnostics (turtlebot3_bringup/turtlebot3_diagnostics)
     turtlebot3_lds (hls_lfcd_lds_driver/hlds_laser_publisher)

 ROS\_MASTER\_URI=http://192.168.1.2:11311

 process[turtlebot3_core-1]: started with pid [14198]
 process[turtlebot3_lds-2]: started with pid [14199]
 process[turtlebot3_diagnostics-3]: started with pid [14200]
 [INFO] [1531306690.947198]: ROS Serial Python Node
 [INFO] [1531306691.000143]: Connecting to /dev/ttyACM0 at 115200 baud
 [INFO] [1531306693.522019]: Note: publish buffer size is 1024 bytes
 [INFO] [1531306693.525615]: Setup publisher on sensor_state [turtlebot3_msgs/SensorState]
 [INFO] [1531306693.544159]: Setup publisher on version_info [turtlebot3_msgs/VersionInfo]
 [INFO] [1531306693.620722]: Setup publisher on imu [sensor_msgs/Imu]
 [INFO] [1531306693.642319]: Setup publisher on cmd_vel_rc100 [geometry_msgs/Twist]
 [INFO] [1531306693.687786]: Setup publisher on odom [nav_msgs/Odometry]
 [INFO] [1531306693.706260]: Setup publisher on joint_states [sensor_msgs/JointState]
 [INFO] [1531306693.722754]: Setup publisher on battery_state [sensor_msgs/BatteryState]
 [INFO] [1531306693.759059]: Setup publisher on magnetic_field [sensor_msgs/MagneticField]
 [INFO] [1531306695.979057]: Setup publisher on /tf [tf/tfMessage]
 [INFO] [1531306696.007135]: Note: subscribe buffer size is 1024 bytes
 [INFO] [1531306696.009083]: Setup subscriber on cmd_vel [geometry_msgs/Twist]
 [INFO] [1531306696.040047]: Setup subscriber on sound [turtlebot3_msgs/Sound]
 [INFO] [1531306696.069571]: Setup subscriber on motor_power [std_msgs/Bool]
 [INFO] [1531306696.096364]: Setup subscriber on reset [std_msgs/Empty]
 [INFO] [1531306696.390979]: Setup TF on Odometry [odom]
 [INFO] [1531306696.394314]: Setup TF on IMU [imu_link]
 [INFO] [1531306696.397498]: Setup TF on MagneticField [mag_link]
 [INFO] [1531306696.400537]: Setup TF on JointState [base_link]
 [INFO] [1531306696.407813]: --------------------------
 [INFO] [1531306696.411412]: Connected to OpenCR board!
 [INFO] [1531306696.415140]: This core(v1.2.1) is compatible with TB3 Burger
 [INFO] [1531306696.418398]: --------------------------
 [INFO] [1531306696.421749]: Start Calibration of Gyro
 [INFO] [1531306698.953226]: Calibration End

```

![](/assets/images/icon_unfold.png)

### [Load TurtleBot3 on Rviz](#load-turtlebot3-on-rviz "#load-turtlebot3-on-rviz")

1. Open a new terminal and launch the robot state publisher.

```
$ roslaunch turtlebot3_bringup turtlebot3_remote.launch

```
2. Open a new terminal and enter the below command to run RViz. To run rviz, you need to specify the model name of TurtleBot3.

```
$ rosrun rviz rviz -d `rospack find turtlebot3_description`/rviz/{burger, waffle_pi}.rviz

```

![](/assets/images/platform/turtlebot3/bringup/2022_run_rviz.png)

## [Bringup](#bringup "#bringup")

### [Bringup TurtleBot3](#bringup-turtlebot3 "#bringup-turtlebot3")

1. Open a new terminal from PC with `Ctrl` + `Alt` + `T` and connect to Raspberry Pi with its IP address.  

 Use the password when setting up the SBC.

```
$ ssh ubuntu@{IP_ADDRESS_OF_RASPBERRY_PI}

```
2. Bring up basic packages to start TurtleBot3 applications. Replace the `${TB3_MODEL}` parameter with your model name such as `burger`, `waffle`, `waffle_pi`.

```
$ export TURTLEBOT3\_MODEL=${TB3\_MODEL}
$ ros2 launch turtlebot3_bringup robot.launch.py

```
3. If the TurtleBot3 model is `burger` as below, the terminal will print below messages.

```
$ export TURTLEBOT3\_MODEL=burger
$ ros2 launch turtlebot3_bringup robot.launch.py
[INFO] [launch]: All log files can be found below /home/ubuntu/.ros/log/2019-08-19-01-24-19-009803-ubuntu-15310
[INFO] [launch]: Default logging verbosity is set to INFO
urdf_file_name : turtlebot3_burger.urdf
[INFO] [robot_state_publisher-1]: process started with pid [15320]
[INFO] [hlds_laser_publisher-2]: process started with pid [15321]
[INFO] [turtlebot3_ros-3]: process started with pid [15322]
[robot_state_publisher-1] Initialize urdf model from file: /home/ubuntu/turtlebot_ws/install/turtlebot3_description/share/turtlebot3_description/urdf/turtlebot3_burger.urdf
[robot_state_publisher-1] Parsing robot urdf xml string.
[robot_state_publisher-1] Link base_link had 5 children
[robot_state_publisher-1] Link caster_back_link had 0 children
[robot_state_publisher-1] Link imu_link had 0 children
[robot_state_publisher-1] Link base_scan had 0 children
[robot_state_publisher-1] Link wheel_left_link had 0 children
[robot_state_publisher-1] Link wheel_right_link had 0 children
[robot_state_publisher-1] got segment base_footprint
[robot_state_publisher-1] got segment base_link
[robot_state_publisher-1] got segment base_scan
[robot_state_publisher-1] got segment caster_back_link
[robot_state_publisher-1] got segment imu_link
[robot_state_publisher-1] got segment wheel_left_link
[robot_state_publisher-1] got segment wheel_right_link
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Init TurtleBot3 Node Main
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Init DynamixelSDKWrapper
[turtlebot3_ros-3] [INFO] [DynamixelSDKWrapper]: Succeeded to open the port(/dev/ttyACM0)!
[turtlebot3_ros-3] [INFO] [DynamixelSDKWrapper]: Succeeded to change the baudrate!
[robot_state_publisher-1] Adding fixed segment from base_footprint to base_link
[robot_state_publisher-1] Adding fixed segment from base_link to caster_back_link
[robot_state_publisher-1] Adding fixed segment from base_link to imu_link
[robot_state_publisher-1] Adding fixed segment from base_link to base_scan
[robot_state_publisher-1] Adding moving segment from base_link to wheel_left_link
[robot_state_publisher-1] Adding moving segment from base_link to wheel_right_link
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Start Calibration of Gyro
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Calibration End
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Add Motors
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Add Wheels
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Add Sensors
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create battery state publisher
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create imu publisher
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create sensor state publisher
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create joint state publisher
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Add Devices
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create motor power server
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create reset server
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create sound server
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Run!
[turtlebot3_ros-3] [INFO] [diff_drive_controller]: Init Odometry
[turtlebot3_ros-3] [INFO] [diff_drive_controller]: Run!

```
4. Topics and services can be listed with commands below.

* **Topic list**

```
$ ros2 topic list
/battery_state
/cmd_vel
/imu
/joint_states
/magnetic_field
/odom
/parameter_events
/robot_description
/rosout
/scan
/sensor_state
/tf
/tf_static

```
* **Service list**

```
$ ros2 service list
/diff_drive_controller/describe_parameters
/diff_drive_controller/get_parameter_types
/diff_drive_controller/get_parameters
/diff_drive_controller/list_parameters
/diff_drive_controller/set_parameters
/diff_drive_controller/set_parameters_atomically
/hlds_laser_publisher/describe_parameters
/hlds_laser_publisher/get_parameter_types
/hlds_laser_publisher/get_parameters
/hlds_laser_publisher/list_parameters
/hlds_laser_publisher/set_parameters
/hlds_laser_publisher/set_parameters_atomically
/launch_ros/describe_parameters
/launch_ros/get_parameter_types
/launch_ros/get_parameters
/launch_ros/list_parameters
/launch_ros/set_parameters
/launch_ros/set_parameters_atomically
/motor_power
/reset
/sound
/turtlebot3_node/describe_parameters
/turtlebot3_node/get_parameter_types
/turtlebot3_node/get_parameters
/turtlebot3_node/list_parameters
/turtlebot3_node/set_parameters
/turtlebot3_node/set_parameters_atomically

```

![](/assets/images/icon_unfold.png)

### [Load TurtleBot3 on Rviz](#load-turtlebot3-on-rviz "#load-turtlebot3-on-rviz")

1. Make sure to bring up the TurtleBot3
2. Open a new terminal and enter the below command to launch RViz.

```
$ ros2 launch turtlebot3_bringup rviz2.launch.py

```

![](/assets/images/platform/turtlebot3/bringup/run_rviz.jpg)

## [Bringup](#bringup "#bringup")

### [Bringup TurtleBot3](#bringup-turtlebot3 "#bringup-turtlebot3")

1. Open a new terminal from PC with `Ctrl` + `Alt` + `T` and connect to Raspberry Pi with its IP address.  

 The default password is **turtlebot**.

```
$ ssh ubuntu@{IP_ADDRESS_OF_RASPBERRY_PI}

```
2. Bring up basic packages to start TurtleBot3 applications. Please use the proper keyword among `burger`, `waffle`, `waffle_pi` for the `TURTLEBOT3_MODEL` parameter.

```
$ export TURTLEBOT3\_MODEL=burger
$ ros2 launch turtlebot3_bringup robot.launch.py

```
3. If the TurtleBot3 model is `burger` as below, the terminal will print below messages.

```
$ export TURTLEBOT3\_MODEL=burger
$ ros2 launch turtlebot3_bringup robot.launch.py
[INFO] [launch]: All log files can be found below /home/ubuntu/.ros/log/2019-08-19-01-24-19-009803-ubuntu-15310
[INFO] [launch]: Default logging verbosity is set to INFO
urdf_file_name : turtlebot3_burger.urdf
[INFO] [robot_state_publisher-1]: process started with pid [15320]
[INFO] [hlds_laser_publisher-2]: process started with pid [15321]
[INFO] [turtlebot3_ros-3]: process started with pid [15322]
[robot_state_publisher-1] Initialize urdf model from file: /home/ubuntu/turtlebot_ws/install/turtlebot3_description/share/turtlebot3_description/urdf/turtlebot3_burger.urdf
[robot_state_publisher-1] Parsing robot urdf xml string.
[robot_state_publisher-1] Link base_link had 5 children
[robot_state_publisher-1] Link caster_back_link had 0 children
[robot_state_publisher-1] Link imu_link had 0 children
[robot_state_publisher-1] Link base_scan had 0 children
[robot_state_publisher-1] Link wheel_left_link had 0 children
[robot_state_publisher-1] Link wheel_right_link had 0 children
[robot_state_publisher-1] got segment base_footprint
[robot_state_publisher-1] got segment base_link
[robot_state_publisher-1] got segment base_scan
[robot_state_publisher-1] got segment caster_back_link
[robot_state_publisher-1] got segment imu_link
[robot_state_publisher-1] got segment wheel_left_link
[robot_state_publisher-1] got segment wheel_right_link
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Init TurtleBot3 Node Main
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Init DynamixelSDKWrapper
[turtlebot3_ros-3] [INFO] [DynamixelSDKWrapper]: Succeeded to open the port(/dev/ttyACM0)!
[turtlebot3_ros-3] [INFO] [DynamixelSDKWrapper]: Succeeded to change the baudrate!
[robot_state_publisher-1] Adding fixed segment from base_footprint to base_link
[robot_state_publisher-1] Adding fixed segment from base_link to caster_back_link
[robot_state_publisher-1] Adding fixed segment from base_link to imu_link
[robot_state_publisher-1] Adding fixed segment from base_link to base_scan
[robot_state_publisher-1] Adding moving segment from base_link to wheel_left_link
[robot_state_publisher-1] Adding moving segment from base_link to wheel_right_link
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Start Calibration of Gyro
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Calibration End
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Add Motors
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Add Wheels
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Add Sensors
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create battery state publisher
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create imu publisher
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create sensor state publisher
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create joint state publisher
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Add Devices
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create motor power server
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create reset server
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create sound server
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Run!
[turtlebot3_ros-3] [INFO] [diff_drive_controller]: Init Odometry
[turtlebot3_ros-3] [INFO] [diff_drive_controller]: Run!

```
4. Topics and services can be listed with commands below.

* **Topic list**

```
$ ros2 topic list
/battery_state
/cmd_vel
/imu
/joint_states
/magnetic_field
/odom
/parameter_events
/robot_description
/rosout
/scan
/sensor_state
/tf
/tf_static

```
* **Service list**

```
$ ros2 service list
/diff_drive_controller/describe_parameters
/diff_drive_controller/get_parameter_types
/diff_drive_controller/get_parameters
/diff_drive_controller/list_parameters
/diff_drive_controller/set_parameters
/diff_drive_controller/set_parameters_atomically
/hlds_laser_publisher/describe_parameters
/hlds_laser_publisher/get_parameter_types
/hlds_laser_publisher/get_parameters
/hlds_laser_publisher/list_parameters
/hlds_laser_publisher/set_parameters
/hlds_laser_publisher/set_parameters_atomically
/launch_ros/describe_parameters
/launch_ros/get_parameter_types
/launch_ros/get_parameters
/launch_ros/list_parameters
/launch_ros/set_parameters
/launch_ros/set_parameters_atomically
/motor_power
/reset
/sound
/turtlebot3_node/describe_parameters
/turtlebot3_node/get_parameter_types
/turtlebot3_node/get_parameters
/turtlebot3_node/list_parameters
/turtlebot3_node/set_parameters
/turtlebot3_node/set_parameters_atomically

```

![](/assets/images/icon_unfold.png)

### [Load TurtleBot3 on Rviz](#load-turtlebot3-on-rviz "#load-turtlebot3-on-rviz")

1. Make sure to bring up the TurtleBot3
2. Open a new terminal and enter the below command to launch RViz.

```
$ ros2 launch turtlebot3_bringup rviz2.launch.py

```

![](/assets/images/platform/turtlebot3/bringup/run_rviz.jpg)

## [Bringup](#bringup "#bringup")

### [Bringup TurtleBot3](#bringup-turtlebot3 "#bringup-turtlebot3")

1. Open a new terminal from PC with `Ctrl` + `Alt` + `T` and connect to Raspberry Pi with its IP address.  

 The default password is **turtlebot**.

```
$ ssh ubuntu@{IP_ADDRESS_OF_RASPBERRY_PI}

```
2. Bring up basic packages to start TurtleBot3 applications. Please use the proper keyword among `burger`, `waffle_pi` for the `TURTLEBOT3_MODEL` parameter.

```
$ export TURTLEBOT3\_MODEL=burger
$ ros2 launch turtlebot3_bringup robot.launch.py

```
3. When the TURTLEBOT3\_MODEL is set to `burger`, the terminal output will look like below.

```
$ export TURTLEBOT3\_MODEL=burger
$ ros2 launch turtlebot3_bringup robot.launch.py
[INFO] [launch]: All log files can be found below /home/ubuntu/.ros/log/2019-08-19-01-24-19-009803-ubuntu-15310
[INFO] [launch]: Default logging verbosity is set to INFO
urdf_file_name : turtlebot3_burger.urdf
[INFO] [robot_state_publisher-1]: process started with pid [15320]
[INFO] [hlds_laser_publisher-2]: process started with pid [15321]
[INFO] [turtlebot3_ros-3]: process started with pid [15322]
[robot_state_publisher-1] Initialize urdf model from file: /home/ubuntu/turtlebot_ws/install/turtlebot3_description/share/turtlebot3_description/urdf/turtlebot3_burger.urdf
[robot_state_publisher-1] Parsing robot urdf xml string.
[robot_state_publisher-1] Link base_link had 5 children
[robot_state_publisher-1] Link caster_back_link had 0 children
[robot_state_publisher-1] Link imu_link had 0 children
[robot_state_publisher-1] Link base_scan had 0 children
[robot_state_publisher-1] Link wheel_left_link had 0 children
[robot_state_publisher-1] Link wheel_right_link had 0 children
[robot_state_publisher-1] got segment base_footprint
[robot_state_publisher-1] got segment base_link
[robot_state_publisher-1] got segment base_scan
[robot_state_publisher-1] got segment caster_back_link
[robot_state_publisher-1] got segment imu_link
[robot_state_publisher-1] got segment wheel_left_link
[robot_state_publisher-1] got segment wheel_right_link
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Init TurtleBot3 Node Main
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Init DynamixelSDKWrapper
[turtlebot3_ros-3] [INFO] [DynamixelSDKWrapper]: Succeeded to open the port(/dev/ttyACM0)!
[turtlebot3_ros-3] [INFO] [DynamixelSDKWrapper]: Succeeded to change the baudrate!
[robot_state_publisher-1] Adding fixed segment from base_footprint to base_link
[robot_state_publisher-1] Adding fixed segment from base_link to caster_back_link
[robot_state_publisher-1] Adding fixed segment from base_link to imu_link
[robot_state_publisher-1] Adding fixed segment from base_link to base_scan
[robot_state_publisher-1] Adding moving segment from base_link to wheel_left_link
[robot_state_publisher-1] Adding moving segment from base_link to wheel_right_link
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Start Calibration of Gyro
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Calibration End
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Add Motors
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Add Wheels
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Add Sensors
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create battery state publisher
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create imu publisher
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create sensor state publisher
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create joint state publisher
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Add Devices
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create motor power server
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create reset server
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create sound server
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Run!
[turtlebot3_ros-3] [INFO] [diff_drive_controller]: Init Odometry
[turtlebot3_ros-3] [INFO] [diff_drive_controller]: Run!

```
4. Topics and services can be listed with commands below.  

List of topics and services may vary depend on ROS pacakage version.

* **Topic list**

```
$ ros2 topic list
/battery_state
/cmd_vel
/imu
/joint_states
/magnetic_field
/odom
/parameter_events
/robot_description
/rosout
/scan
/sensor_state
/tf
/tf_static

```
* **Service list**

```
$ ros2 service list
/diff_drive_controller/describe_parameters
/diff_drive_controller/get_parameter_types
/diff_drive_controller/get_parameters
/diff_drive_controller/list_parameters
/diff_drive_controller/set_parameters
/diff_drive_controller/set_parameters_atomically
/hlds_laser_publisher/describe_parameters
/hlds_laser_publisher/get_parameter_types
/hlds_laser_publisher/get_parameters
/hlds_laser_publisher/list_parameters
/hlds_laser_publisher/set_parameters
/hlds_laser_publisher/set_parameters_atomically
/launch_ros/describe_parameters
/launch_ros/get_parameter_types
/launch_ros/get_parameters
/launch_ros/list_parameters
/launch_ros/set_parameters
/launch_ros/set_parameters_atomically
/motor_power
/reset
/sound
/turtlebot3_node/describe_parameters
/turtlebot3_node/get_parameter_types
/turtlebot3_node/get_parameters
/turtlebot3_node/list_parameters
/turtlebot3_node/set_parameters
/turtlebot3_node/set_parameters_atomically

```

![](/assets/images/icon_unfold.png)

### [Load TurtleBot3 on Rviz](#load-turtlebot3-on-rviz "#load-turtlebot3-on-rviz")

1. Make sure to bring up the TurtleBot3
2. Open a new terminal and enter the below command to launch RViz.

```
$ ros2 launch turtlebot3_bringup rviz2.launch.py

```

![](/assets/images/platform/turtlebot3/bringup/run_rviz.jpg)

## [Bringup](#bringup "#bringup")

### [Bringup TurtleBot3](#bringup-turtlebot3 "#bringup-turtlebot3")

Bring up basic packages from TurtleBot3 to start TurtleBot3 applications.

```
> roslaunch turtlebot3_bringup turtlebot3_robot.launch

```

![](/assets/images/icon_unfold.png) **Read more about loading TurtleBot3 on RViz**

1. Bring up basic packages to start TurtleBot3 applications.  

 Please use the proper keyword among `burger`, `waffle`, `waffle_pi` for the `TURTLEBOT3_MODEL` parameter.

```
> set TURTLEBOT3\_MODEL=waffle
> roslaunch turtlebot3_bringup turtlebot3_remote.launch

```
2. Open a new ROS command window and enter the below command.

```
> rosrun rviz rviz -d "<full path to turtlebot3\_description>/rviz/model.rviz"

```

![](/assets/images/platform/turtlebot3/bringup/run_rviz.jpg)

 Previous Page
Next Page 

$reference = $(".archive");
$(window).resize(function() {
 var newWidth = $reference.width() \* 0.90;
 if (newWidth > 640) { newWidth = 640; }

 // Resize all videos according to aspect ratio
 $("iframe").each(
 function(index, elem) {
 elem.setAttribute("width", (newWidth).toFixed());
 elem.setAttribute("height", (newWidth\*0.56).toFixed());
 }
 );
// Kick off one resize to fix all videos on page load
}).resize();

© 2023 ROBOTIS. Powered by [Jekyll](http://jekyllrb.com "http://jekyllrb.com") & [Minimal Mistakes](https://mademistakes.com/work/minimal-mistakes-jekyll-theme/ "https://mademistakes.com/work/minimal-mistakes-jekyll-theme/").

 var \_gaq = \_gaq || [];
 \_gaq.push(['\_setAccount', 'UA-83196341-13']);
 \_gaq.push(['\_trackPageview']);

 (function() {
 var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
 ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
 var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
 })();

 window.dataLayer = window.dataLayer || [];
 function gtag(){dataLayer.push(arguments);}
 gtag('js', new Date());

 gtag('config', 'G-155KHSC07K');
