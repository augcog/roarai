

OpenCV: How OpenCV-Python Bindings Works?

 MathJax.Hub.Config({
 extensions: ["tex2jax.js", "TeX/AMSmath.js", "TeX/AMSsymbols.js"],
 jax: ["input/TeX","output/HTML-CSS"],
});
//<![CDATA[
MathJax.Hub.Config(
{
 TeX: {
 Macros: {
 matTT: [ "\\[ \\left|\\begin{array}{ccc} #1 & #2 & #3\\\\ #4 & #5 & #6\\\\ #7 & #8 & #9 \\end{array}\\right| \\]", 9],
 fork: ["\\left\\{ \\begin{array}{l l} #1 & \\mbox{#2}\\\\ #3 & \\mbox{#4}\\\\ \\end{array} \\right.", 4],
 forkthree: ["\\left\\{ \\begin{array}{l l} #1 & \\mbox{#2}\\\\ #3 & \\mbox{#4}\\\\ #5 & \\mbox{#6}\\\\ \\end{array} \\right.", 6],
 forkfour: ["\\left\\{ \\begin{array}{l l} #1 & \\mbox{#2}\\\\ #3 & \\mbox{#4}\\\\ #5 & \\mbox{#6}\\\\ #7 & \\mbox{#8}\\\\ \\end{array} \\right.", 8],
 vecthree: ["\\begin{bmatrix} #1\\\\ #2\\\\ #3 \\end{bmatrix}", 3],
 vecthreethree: ["\\begin{bmatrix} #1 & #2 & #3\\\\ #4 & #5 & #6\\\\ #7 & #8 & #9 \\end{bmatrix}", 9],
 cameramatrix: ["#1 = \\begin{bmatrix} f\_x & 0 & c\_x\\\\ 0 & f\_y & c\_y\\\\ 0 & 0 & 1 \\end{bmatrix}", 1],
 distcoeffs: ["(k\_1, k\_2, p\_1, p\_2[, k\_3[, k\_4, k\_5, k\_6 [, s\_1, s\_2, s\_3, s\_4[, \\tau\_x, \\tau\_y]]]]) \\text{ of 4, 5, 8, 12 or 14 elements}"],
 distcoeffsfisheye: ["(k\_1, k\_2, k\_3, k\_4)"],
 hdotsfor: ["\\dots", 1],
 mathbbm: ["\\mathbb{#1}", 1],
 bordermatrix: ["\\matrix{#1}", 1]
 }
 }
}
);
//]]>

 (function() {
 var cx = '002541620211387084530:kaexgxg7oxu';
 var gcse = document.createElement('script');
 gcse.type = 'text/javascript';
 gcse.async = true;
 gcse.src = 'https://cse.google.com/cse.js?cx=' + cx;
 var s = document.getElementsByTagName('script')[0];
 s.parentNode.insertBefore(gcse, s);
 })();

|  |  |
| --- | --- |
| Logo | OpenCV
 4.8.0-dev

Open Source Computer Vision |

var searchBox = new SearchBox("searchBox", "../../search",false,'Search');

$(function() {
 initMenu('../../',true,false,'search.php','Search');
 $(document).ready(function() { init\_search(); });
});

* [OpenCV-Python Tutorials](../../d6/d00/tutorial_py_root.html "../../d6/d00/tutorial_py_root.html")
* [OpenCV-Python Bindings](../../df/da2/tutorial_py_table_of_contents_bindings.html "../../df/da2/tutorial_py_table_of_contents_bindings.html")

How OpenCV-Python Bindings Works?  

## Goal

Learn:

* How OpenCV-Python bindings are generated?
* How to extend new OpenCV modules to Python?

## How OpenCV-Python bindings are generated?

In OpenCV, all algorithms are implemented in C++. But these algorithms can be used from different languages like Python, Java etc. This is made possible by the bindings generators. These generators create a bridge between C++ and Python which enables users to call C++ functions from Python. To get a complete picture of what is happening in background, a good knowledge of Python/C API is required. A simple example on extending C++ functions to Python can be found in official Python documentation[1]. So extending all functions in OpenCV to Python by writing their wrapper functions manually is a time-consuming task. So OpenCV does it in a more intelligent way. OpenCV generates these wrapper functions automatically from the C++ headers using some Python scripts which are located in `modules/python/src2`. We will look into what they do.

First, `modules/python/CMakeFiles.txt` is a CMake script which checks the modules to be extended to Python. It will automatically check all the modules to be extended and grab their header files. These header files contain list of all classes, functions, constants etc. for that particular modules.

Second, these header files are passed to a Python script, `modules/python/src2/gen2.py`. This is the Python bindings generator script. It calls another Python script `modules/python/src2/hdr_parser.py`. This is the header parser script. This header parser splits the complete header file into small Python lists. So these lists contain all details about a particular function, class etc. For example, a function will be parsed to get a list containing function name, return type, input arguments, argument types etc. Final list contains details of all the functions, enums, structs, classes etc. in that header file.

But header parser doesn't parse all the functions/classes in the header file. The developer has to specify which functions should be exported to Python. For that, there are certain macros added to the beginning of these declarations which enables the header parser to identify functions to be parsed. These macros are added by the developer who programs the particular function. In short, the developer decides which functions should be extended to Python and which are not. Details of those macros will be given in next session.

So header parser returns a final big list of parsed functions. Our generator script (gen2.py) will create wrapper functions for all the functions/classes/enums/structs parsed by header parser (You can find these header files during compilation in the `build/modules/python/` folder as pyopencv\_generated\_\*.h files). But there may be some basic OpenCV datatypes like Mat, Vec4i, Size. They need to be extended manually. For example, a Mat type should be extended to Numpy array, Size should be extended to a tuple of two integers etc. Similarly, there may be some complex structs/classes/functions etc. which need to be extended manually. All such manual wrapper functions are placed in `modules/python/src2/cv2.cpp`.

So now only thing left is the compilation of these wrapper files which gives us **cv2** module. So when you call a function, say `res = equalizeHist(img1,img2)` in Python, you pass two numpy arrays and you expect another numpy array as the output. So these numpy arrays are converted to [cv::Mat](../../d3/d63/classcv_1_1Mat.html "n-dimensional dense array class ") and then calls the [equalizeHist()](../../d6/dc7/group__imgproc__hist.html#ga7e54091f0c937d49bf84152a16f76d6e "Equalizes the histogram of a grayscale image. ") function in C++. Final result, res will be converted back into a Numpy array. So in short, almost all operations are done in C++ which gives us almost same speed as that of C++.

So this is the basic version of how OpenCV-Python bindings are generated.

NoteThere is no 1:1 mapping of numpy.ndarray on [cv::Mat](../../d3/d63/classcv_1_1Mat.html "n-dimensional dense array class "). For example, [cv::Mat](../../d3/d63/classcv_1_1Mat.html "n-dimensional dense array class ") has channels field, which is emulated as last dimension of numpy.ndarray and implicitly converted. However, such implicit conversion has problem with passing of 3D numpy arrays into C++ code (the last dimension is implicitly reinterpreted as number of channels). Refer to the [issue](https://github.com/opencv/opencv/issues/19091 "https://github.com/opencv/opencv/issues/19091") for workarounds if you need to process 3D arrays or ND-arrays with channels. OpenCV 4.5.4+ has `[cv.Mat](../../d3/d63/classcv_1_1Mat.html "n-dimensional dense array class ")` wrapper derived from `numpy.ndarray` to explicitly handle the channels behavior.
## How to extend new modules to Python?

Header parser parse the header files based on some wrapper macros added to function declaration. Enumeration constants don't need any wrapper macros. They are automatically wrapped. But remaining functions, classes etc. need wrapper macros.

Functions are extended using `CV_EXPORTS_W` macro. An example is shown below. 

[CV\_EXPORTS\_W](../../db/de0/group__core__utils.html#ga67ea671a3582ce612ac3c281e067f480 "../../db/de0/group__core__utils.html#ga67ea671a3582ce612ac3c281e067f480") void [equalizeHist](../../d6/dc7/group__imgproc__hist.html#ga7e54091f0c937d49bf84152a16f76d6e "../../d6/dc7/group__imgproc__hist.html#ga7e54091f0c937d49bf84152a16f76d6e")( [InputArray](../../dc/d84/group__core__basic.html#ga353a9de602fe76c709e12074a6f362ba "../../dc/d84/group__core__basic.html#ga353a9de602fe76c709e12074a6f362ba") src, [OutputArray](../../dc/d84/group__core__basic.html#gaad17fda1d0f0d1ee069aebb1df2913c0 "../../dc/d84/group__core__basic.html#gaad17fda1d0f0d1ee069aebb1df2913c0") dst ); Header parser can understand the input and output arguments from keywords like InputArray, OutputArray etc. But sometimes, we may need to hardcode inputs and outputs. For that, macros like `CV_OUT`, `CV_IN_OUT` etc. are used. 

[CV\_EXPORTS\_W](../../db/de0/group__core__utils.html#ga67ea671a3582ce612ac3c281e067f480 "../../db/de0/group__core__utils.html#ga67ea671a3582ce612ac3c281e067f480") void [minEnclosingCircle](../../d3/dc0/group__imgproc__shape.html#ga8ce13c24081bbc7151e9326f412190f1 "../../d3/dc0/group__imgproc__shape.html#ga8ce13c24081bbc7151e9326f412190f1")( [InputArray](../../dc/d84/group__core__basic.html#ga353a9de602fe76c709e12074a6f362ba "../../dc/d84/group__core__basic.html#ga353a9de602fe76c709e12074a6f362ba") points, [CV\_OUT](../../db/de0/group__core__utils.html#ga4e999bc21cb894d3ed789f3f0bc26778 "../../db/de0/group__core__utils.html#ga4e999bc21cb894d3ed789f3f0bc26778") [Point2f](../../dc/d84/group__core__basic.html#ga7d080aa40de011e4410bca63385ffe2a "../../dc/d84/group__core__basic.html#ga7d080aa40de011e4410bca63385ffe2a")& center, [CV\_OUT](../../db/de0/group__core__utils.html#ga4e999bc21cb894d3ed789f3f0bc26778 "../../db/de0/group__core__utils.html#ga4e999bc21cb894d3ed789f3f0bc26778") float& radius ); For large classes also, `CV_EXPORTS_W` is used. To extend class methods, `CV_WRAP` is used. Similarly, `CV_PROP` is used for class fields. 

class [CV\_EXPORTS\_W](../../db/de0/group__core__utils.html#ga67ea671a3582ce612ac3c281e067f480 "../../db/de0/group__core__utils.html#ga67ea671a3582ce612ac3c281e067f480") CLAHE : public Algorithm{public: [CV\_WRAP](../../db/de0/group__core__utils.html#gae435babf3ce7cca990524b23adf6b4a3 "../../db/de0/group__core__utils.html#gae435babf3ce7cca990524b23adf6b4a3") virtual void apply([InputArray](../../dc/d84/group__core__basic.html#ga353a9de602fe76c709e12074a6f362ba "../../dc/d84/group__core__basic.html#ga353a9de602fe76c709e12074a6f362ba") src, [OutputArray](../../dc/d84/group__core__basic.html#gaad17fda1d0f0d1ee069aebb1df2913c0 "../../dc/d84/group__core__basic.html#gaad17fda1d0f0d1ee069aebb1df2913c0") dst) = 0; [CV\_WRAP](../../db/de0/group__core__utils.html#gae435babf3ce7cca990524b23adf6b4a3 "../../db/de0/group__core__utils.html#gae435babf3ce7cca990524b23adf6b4a3") virtual void setClipLimit(double clipLimit) = 0; [CV\_WRAP](../../db/de0/group__core__utils.html#gae435babf3ce7cca990524b23adf6b4a3 "../../db/de0/group__core__utils.html#gae435babf3ce7cca990524b23adf6b4a3") virtual double getClipLimit() const = 0;} Overloaded functions can be extended using `CV_EXPORTS_AS`. But we need to pass a new name so that each function will be called by that name in Python. Take the case of integral function below. Three functions are available, so each one is named with a suffix in Python. Similarly `CV_WRAP_AS` can be used to wrap overloaded methods. 

[CV\_EXPORTS\_W](../../db/de0/group__core__utils.html#ga67ea671a3582ce612ac3c281e067f480 "../../db/de0/group__core__utils.html#ga67ea671a3582ce612ac3c281e067f480") void [integral](../../d5/df1/group__imgproc__hal__functions.html#ga78d53bcbe1710d0f7034e89fd0d43259 "../../d5/df1/group__imgproc__hal__functions.html#ga78d53bcbe1710d0f7034e89fd0d43259")( [InputArray](../../dc/d84/group__core__basic.html#ga353a9de602fe76c709e12074a6f362ba "../../dc/d84/group__core__basic.html#ga353a9de602fe76c709e12074a6f362ba") src, [OutputArray](../../dc/d84/group__core__basic.html#gaad17fda1d0f0d1ee069aebb1df2913c0 "../../dc/d84/group__core__basic.html#gaad17fda1d0f0d1ee069aebb1df2913c0") sum, int sdepth = -1 );[CV\_EXPORTS\_AS](../../db/de0/group__core__utils.html#ga288d5d11e4d8675aab962ec2b2066855 "../../db/de0/group__core__utils.html#ga288d5d11e4d8675aab962ec2b2066855")(integral2) void [integral](../../d5/df1/group__imgproc__hal__functions.html#ga78d53bcbe1710d0f7034e89fd0d43259 "../../d5/df1/group__imgproc__hal__functions.html#ga78d53bcbe1710d0f7034e89fd0d43259")( [InputArray](../../dc/d84/group__core__basic.html#ga353a9de602fe76c709e12074a6f362ba "../../dc/d84/group__core__basic.html#ga353a9de602fe76c709e12074a6f362ba") src, [OutputArray](../../dc/d84/group__core__basic.html#gaad17fda1d0f0d1ee069aebb1df2913c0 "../../dc/d84/group__core__basic.html#gaad17fda1d0f0d1ee069aebb1df2913c0") sum, [OutputArray](../../dc/d84/group__core__basic.html#gaad17fda1d0f0d1ee069aebb1df2913c0 "../../dc/d84/group__core__basic.html#gaad17fda1d0f0d1ee069aebb1df2913c0") sqsum, int sdepth = -1, int sqdepth = -1 );[CV\_EXPORTS\_AS](../../db/de0/group__core__utils.html#ga288d5d11e4d8675aab962ec2b2066855 "../../db/de0/group__core__utils.html#ga288d5d11e4d8675aab962ec2b2066855")(integral3) void [integral](../../d5/df1/group__imgproc__hal__functions.html#ga78d53bcbe1710d0f7034e89fd0d43259 "../../d5/df1/group__imgproc__hal__functions.html#ga78d53bcbe1710d0f7034e89fd0d43259")( [InputArray](../../dc/d84/group__core__basic.html#ga353a9de602fe76c709e12074a6f362ba "../../dc/d84/group__core__basic.html#ga353a9de602fe76c709e12074a6f362ba") src, [OutputArray](../../dc/d84/group__core__basic.html#gaad17fda1d0f0d1ee069aebb1df2913c0 "../../dc/d84/group__core__basic.html#gaad17fda1d0f0d1ee069aebb1df2913c0") sum, [OutputArray](../../dc/d84/group__core__basic.html#gaad17fda1d0f0d1ee069aebb1df2913c0 "../../dc/d84/group__core__basic.html#gaad17fda1d0f0d1ee069aebb1df2913c0") sqsum, [OutputArray](../../dc/d84/group__core__basic.html#gaad17fda1d0f0d1ee069aebb1df2913c0 "../../dc/d84/group__core__basic.html#gaad17fda1d0f0d1ee069aebb1df2913c0") tilted, int sdepth = -1, int sqdepth = -1 ); Small classes/structs are extended using `CV_EXPORTS_W_SIMPLE`. These structs are passed by value to C++ functions. Examples are `KeyPoint`, `Match` etc. Their methods are extended by `CV_WRAP` and fields are extended by `CV_PROP_RW`. 

class [CV\_EXPORTS\_W\_SIMPLE](../../db/de0/group__core__utils.html#ga13d649e3f5582a106caaa98f187dd34b "../../db/de0/group__core__utils.html#ga13d649e3f5582a106caaa98f187dd34b") DMatch{public: [CV\_WRAP](../../db/de0/group__core__utils.html#gae435babf3ce7cca990524b23adf6b4a3 "../../db/de0/group__core__utils.html#gae435babf3ce7cca990524b23adf6b4a3") DMatch(); [CV\_WRAP](../../db/de0/group__core__utils.html#gae435babf3ce7cca990524b23adf6b4a3 "../../db/de0/group__core__utils.html#gae435babf3ce7cca990524b23adf6b4a3") DMatch(int \_queryIdx, int \_trainIdx, float \_distance); [CV\_WRAP](../../db/de0/group__core__utils.html#gae435babf3ce7cca990524b23adf6b4a3 "../../db/de0/group__core__utils.html#gae435babf3ce7cca990524b23adf6b4a3") DMatch(int \_queryIdx, int \_trainIdx, int \_imgIdx, float \_distance); [CV\_PROP\_RW](../../db/de0/group__core__utils.html#ga9e800d960e0fc30e7f83c67c98e69ed2 "../../db/de0/group__core__utils.html#ga9e800d960e0fc30e7f83c67c98e69ed2") int queryIdx; // query descriptor index [CV\_PROP\_RW](../../db/de0/group__core__utils.html#ga9e800d960e0fc30e7f83c67c98e69ed2 "../../db/de0/group__core__utils.html#ga9e800d960e0fc30e7f83c67c98e69ed2") int trainIdx; // train descriptor index [CV\_PROP\_RW](../../db/de0/group__core__utils.html#ga9e800d960e0fc30e7f83c67c98e69ed2 "../../db/de0/group__core__utils.html#ga9e800d960e0fc30e7f83c67c98e69ed2") int imgIdx; // train image index [CV\_PROP\_RW](../../db/de0/group__core__utils.html#ga9e800d960e0fc30e7f83c67c98e69ed2 "../../db/de0/group__core__utils.html#ga9e800d960e0fc30e7f83c67c98e69ed2") float distance;}; Some other small classes/structs can be exported using `CV_EXPORTS_W_MAP` where it is exported to a Python native dictionary. `Moments()` is an example of it. 

class [CV\_EXPORTS\_W\_MAP](../../db/de0/group__core__utils.html#gaff7195942cab00fc5eafdd8ed777fac5 "../../db/de0/group__core__utils.html#gaff7195942cab00fc5eafdd8ed777fac5") Moments{public: [CV\_PROP\_RW](../../db/de0/group__core__utils.html#ga9e800d960e0fc30e7f83c67c98e69ed2 "../../db/de0/group__core__utils.html#ga9e800d960e0fc30e7f83c67c98e69ed2") double m00, m10, m01, m20, m11, m02, m30, m21, m12, m03; [CV\_PROP\_RW](../../db/de0/group__core__utils.html#ga9e800d960e0fc30e7f83c67c98e69ed2 "../../db/de0/group__core__utils.html#ga9e800d960e0fc30e7f83c67c98e69ed2") double mu20, mu11, mu02, mu30, mu21, mu12, mu03; [CV\_PROP\_RW](../../db/de0/group__core__utils.html#ga9e800d960e0fc30e7f83c67c98e69ed2 "../../db/de0/group__core__utils.html#ga9e800d960e0fc30e7f83c67c98e69ed2") double nu20, nu11, nu02, nu30, nu21, nu12, nu03;}; So these are the major extension macros available in OpenCV. Typically, a developer has to put proper macros in their appropriate positions. Rest is done by generator scripts. Sometimes, there may be an exceptional cases where generator scripts cannot create the wrappers. Such functions need to be handled manually, to do this write your own `pyopencv_*.hpp` extending headers and put them into misc/python subdirectory of your module. But most of the time, a code written according to OpenCV coding guidelines will be automatically wrapped by generator scripts.

More advanced cases involves providing Python with additional features that does not exist in the C++ interface such as extra methods, type mappings, or to provide default arguments. We will take `UMat` datatype as an example of such cases later on. First, to provide Python-specific methods, `CV_WRAP_PHANTOM` is utilized in a similar manner to `CV_WRAP`, except that it takes the method header as its argument, and you would need to provide the method body in your own `pyopencv_*.hpp` extension. `UMat::queue()` and `UMat::context()` are an example of such phantom methods that does not exist in C++ interface, but are needed to handle OpenCL functionalities at the Python side. Second, if an already-existing datatype(s) is mappable to your class, it is highly preferable to indicate such capacity using `CV_WRAP_MAPPABLE` with the source type as its argument, rather than crafting your own binding function(s). This is the case of `UMat` which maps from `Mat`. Finally, if a default argument is needed, but it is not provided in the native C++ interface, you can provide it for Python side as the argument of `CV_WRAP_DEFAULT`. As per the `UMat::getMat` example below: 

class [CV\_EXPORTS\_W](../../db/de0/group__core__utils.html#ga67ea671a3582ce612ac3c281e067f480 "../../db/de0/group__core__utils.html#ga67ea671a3582ce612ac3c281e067f480") UMat{public: // You would need to provide `static bool cv\_mappable\_to(const Ptr<Mat>& src, Ptr<UMat>& dst)` [CV\_WRAP\_MAPPABLE](../../db/de0/group__core__utils.html#gacbb88034b7de34a8b35aa42f3216a94e "../../db/de0/group__core__utils.html#gacbb88034b7de34a8b35aa42f3216a94e")(Ptr<Mat>); /! returns the OpenCL queue used by OpenCV UMat. // You would need to provide the method body in the binder code [CV\_WRAP\_PHANTOM](../../db/de0/group__core__utils.html#ga6c6ee613d3eebd87f9f391fcde4a6cde "../../db/de0/group__core__utils.html#ga6c6ee613d3eebd87f9f391fcde4a6cde")(static void\* queue()); // You would need to provide the method body in the binder code [CV\_WRAP\_PHANTOM](../../db/de0/group__core__utils.html#ga6c6ee613d3eebd87f9f391fcde4a6cde "../../db/de0/group__core__utils.html#ga6c6ee613d3eebd87f9f391fcde4a6cde")(static void\* context()); [CV\_WRAP\_AS](../../db/de0/group__core__utils.html#ga6a1f29cf8d55c0ee1b4687f6006da0b9 "../../db/de0/group__core__utils.html#ga6a1f29cf8d55c0ee1b4687f6006da0b9")(get) Mat getMat(int flags [CV\_WRAP\_DEFAULT](../../db/de0/group__core__utils.html#ga92152159130797a2713a0992dd5239d2 "../../db/de0/group__core__utils.html#ga92152159130797a2713a0992dd5239d2")([ACCESS\_RW](../../dc/d84/group__core__basic.html#gga6226c29c7b0e7bda7aff72e96ba8e1dfaf44732c797cd59f5940e426ecd62f45f "../../dc/d84/group__core__basic.html#gga6226c29c7b0e7bda7aff72e96ba8e1dfaf44732c797cd59f5940e426ecd62f45f"))) const;}; 

---

Generated on Wed Oct 4 2023 23:37:11 for OpenCV by  [![doxygen](../../doxygen.png)](http://www.doxygen.org/index.html "http://www.doxygen.org/index.html") 1.8.13

//<![CDATA[
addTutorialsButtons();
//]]>

