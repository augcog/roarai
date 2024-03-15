

# 

Homework 3 Solutions

 * [hw03.zip](hw03.zip "hw03.zip")

## Solution Files

You can find the solutions in [hw03.py](hw03.py "hw03.py").

# Required Questions

 Getting Started Videos (enable JavaScript)

## Getting Started Videos

These videos may provide some helpful direction for tackling the coding
problems on this assignment.

> To see these videos, you should be logged into your berkeley.edu email.
> 
> 

 [YouTube link](https://youtu.be/playlist?list=PLx38hZJ5RLZceh9L8HHuBvUjozvwJSC0i "https://youtu.be/playlist?list=PLx38hZJ5RLZceh9L8HHuBvUjozvwJSC0i") 

### Q1: Num Eights

Write a recursive function `num_eights` that takes a positive integer `n` and
returns the number of times the digit 8 appears in `n`.

**Important:**
Use recursion; the tests will fail if you use any assignment statements or loops.
(You can, however, use function definitions if you'd like.)

```
def num_eights(n):
    """Returns the number of times 8 appears as a digit of n.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> num_eights(8782089)
    3
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'For', 'While'])
    True
    """
 if n % 10 == 8:
 return 1 + num\_eights(n // 10)
 elif n < 10:
 return 0
 else:
 return num\_eights(n // 10)
```

Use Ok to test your code:

```
python3 ok -q num_eightsCopy✂️
```

 document.getElementById("copy-code-python3ok-qnum\_eights").onclick = () => copyCode('python3 ok -q num\_eights', "copy-code-python3ok-qnum\_eights");

The equivalent iterative version of this problem might look something like
this:

```
total = 0
while n > 0:
    if n % 10 == 8:
        total = total + 1
    n = n // 10
return total
```

The main idea is that we check each digit for a eight. The recursive solution
is similar, except that you depend on the recursive call to count the
occurences of eight in the rest of the number. Then, you add that to the number
of eights you see in the current digit.

### Q2: Digit Distance

For a given integer, the *digit distance* is the sum of the absolute differences between
consecutive digits. For example:

* The digit distance of `6` is `0`.
* The digit distance of `61` is `5`, as the absolute value of `6 - 1` is `5`.
* The digit distance of `71253` is `12` (`6 + 1 + 3 + 2`).

Write a function that determines the digit distance of a given positive integer.
You must use recursion or the tests will fail.

> **Hint:** There are multiple valid ways of solving this problem!
> If you're stuck, try writing out an iterative solution
> first, and then convert your iterative solution into a recursive one.
> 
> 

```
def digit_distance(n):
    """Determines the digit distance of n.

    >>> digit_distance(3)
    0
    >>> digit_distance(777)
    0
    >>> digit_distance(314)
    5
    >>> digit_distance(31415926535)
    32
    >>> digit_distance(3464660003)
    16
    >>> from construct_check import check
    >>> # ban all loops
    >>> check(HW_SOURCE_FILE, 'digit_distance',
    ...       ['For', 'While'])
    True
    """
 if n < 10:
 return 0
 return abs(n % 10 - (n // 10) % 10) + digit\_distance(n // 10)

# Alternate solution 1
def digit\_distance\_alt(n):
 def helper(prev, n):
 if n == 0:
 return 0
 dist = abs(prev - n % 10)
 return dist + helper(n % 10, n // 10)
 return helper(n % 10, n // 10)

# Alternate solution 2
def digit\_distance\_alt\_2(n):
 def helper(dist, prev, n):
 if n == 0:
 return dist
 dist += abs(prev - n % 10)
 prev = n % 10
 n //= 10
 return helper(dist, prev, n)
 return helper(0, n % 10, n // 10)
```

Use Ok to test your code:

```
python3 ok -q digit_distanceCopy✂️
```

 document.getElementById("copy-code-python3ok-qdigit\_distance").onclick = () => copyCode('python3 ok -q digit\_distance', "copy-code-python3ok-qdigit\_distance");
