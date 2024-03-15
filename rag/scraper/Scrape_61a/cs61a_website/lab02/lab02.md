

# 

Lab 2: Higher-Order Functions, Lambda Expressions

 * [lab02.zip](lab02.zip "lab02.zip")

*Due by 11:59pm on Wednesday, January 31.*

## Starter Files

Download [lab02.zip](lab02.zip "lab02.zip").
Inside the archive, you will find starter files for the questions in this lab,
 along with a copy of the [Ok](ok "ok") autograder.

# Topics

Consult this section if you need a refresher on the material for this lab. It's
okay to skip directly to [the questions](#required-questions "#required-questions") and refer back
here should you get stuck.

 Short Circuiting (enable JavaScript)

## Short Circuiting

What do you think will happen if we type the following into Python?

```
1 / 0
```

Try it out in Python! You should see a `ZeroDivisionError`. But what about this expression?

```
True or 1 / 0
```

It evaluates to `True` because Python's `and` and `or` operators *short-circuit*. That is, they don't necessarily evaluate every operand.

| Operator | Checks if: | Evaluates from left to right up to: | Example |
| --- | --- | --- | --- |
| AND | All values are true | The first false value | `False and 1 / 0` evaluates to `False` |
| OR | At least one value is true | The first true value | `True or 1 / 0` evaluates to `True` |

Short-circuiting happens when the operator reaches an operand that allows them to make a conclusion about the expression. For example, `and` will short-circuit as soon as it reaches the first false value because it then knows that not all the values are true.

If `and` and `or` do not *short-circuit*, they just return the last
value; another way to remember this is that `and` and `or` always return the last
thing they evaluate, whether they short circuit or not. Keep in mind that `and` and `or`
don't always return booleans when using values other than `True` and `False`.

 Higher-Order Functions (enable JavaScript)

## Higher-Order Functions

Variables are names bound to values, which can be primitives like `3` or
`'Hello World'`, but they can also be functions. And since functions can take
arguments of any value, other functions can be passed in as arguments. This is
the basis for higher-order functions.

A higher order function is a function that manipulates other functions by
taking in functions as arguments, returning a function, or both. We will
introduce the basics of higher order functions in this lab and will be
exploring many applications of higher order functions in our next lab.

### Functions as arguments

In Python, function objects are values that can be passed around. We know that one
way to create functions is by using a `def` statement:

```
def square(x):
    return x * x
```

The above statement created a function object with the intrinsic name `square` as
well as binded it to the name `square` in the current environment. Now let's try
passing it as an argument.

First, let's write a function that takes in another function as an argument:

```
def scale(f, x, k):
    """ Returns the result of f(x) scaled by k. """
    return k * f(x)
```

We can now call `scale` on `square` and some other arguments:

```
>>> scale(square, 3, 2) # Double square(3)
18
>>> scale(square, 2, 5) # 5 times 2 squared
20
```

Note that in the body of the call to `scale`, the function object with the intrinsic
name `square` is bound to the parameter `f`. Then, we call `square` in the body of
`scale` by calling `f(x)`.

As we saw in the above section on `lambda` expressions, we can also pass
`lambda` expressions into call expressions!

```
>>> scale(lambda x: x + 10, 5, 2)
30
```

In the frame for this call expression, the name `f` is bound to the function
created by the `lambda` expression `lambda x: x + 10`.

### Functions that return functions

Because functions are values, they are valid as return values! Here's an example:

```
def multiply_by(m):
    def multiply(n):
        return n * m
    return multiply
```

In this particular case, we defined the function `multiply` within the body of `multiply_by`
and then returned it. Let's see it in action:

```
>>> multiply_by(3)
<function multiply_by.<locals>.multiply at ...>
>>> multiply(4)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'multiply' is not defined
```

A call to `multiply_by` returns a function, as expected. However, calling
`multiply` errors, even though that's the name we gave the inner function. This
is because the name `multiply` only exists within the frame where we evaluate
the body of `multiply_by`.

So how do we actually use the inner function? Here are two ways:

```
>>> times_three = multiply_by(3) # Assign the result of the call expression to a name
>>> times_three(5) # Call the inner function with its new name
15
>>> multiply_by(3)(10) # Chain together two call expressions
30
```

The point is, because `multiply_by` returns a function, you can use its return
value just like you would use any other function.

 Lambda Expressions (enable JavaScript)

## Lambda Expressions

Lambda expressions are expressions that evaluate to functions by specifying two
things: the parameters and a return expression.

```
lambda <parameters>: <return expression>
```

While both `lambda` expressions and `def` statements create function objects,
there are some notable differences. `lambda` expressions work like other
expressions; much like a mathematical expression just evaluates to a number and
does not alter the current environment, a `lambda` expression
evaluates to a function without changing the current environment. Let's take a
closer look.

|  | lambda | def |
| --- | --- | --- |
| Type | *Expression* that evaluates to a value | *Statement* that alters the environment |
| Result of execution | Creates an anonymous lambda function with no intrinsic name. | Creates a function with an intrinsic name and binds it to that
 name in the current environment. |
| Effect on the environment | Evaluating a `lambda` expression does *not* create or
 modify any variables. | Executing a `def` statement both creates a new function
 object *and* binds it to a name in the current environment. |
| Usage | A `lambda` expression can be used anywhere that
 expects an expression, such as in an assignment statement or as the
 operator or operand to a call expression. | After executing a `def` statement, the created
 function is bound to a name. You should use this name to refer to the
 function anywhere that expects an expression. |
| Example | 
```
# A lambda expression by itself does not alter
# the environment
lambda x: x * x

# We can assign lambda functions to a name
# with an assignment statement
square = lambda x: x * x
square(3)

# Lambda expressions can be used as an operator
# or operand
negate = lambda f, x: -f(x)
negate(lambda x: x * x, 3)
```
 | 
```
def square(x):
    return x * x

# A function created by a def statement
# can be referred to by its intrinsic name
square(3)
```
 |

 [YouTube link](https://youtu.be/vCeNq_P3akI?list=PLx38hZJ5RLZcUPWZ1-3HYsRPgZ8OCrvqz "https://youtu.be/vCeNq_P3akI?list=PLx38hZJ5RLZcUPWZ1-3HYsRPgZ8OCrvqz") 

 Environment Diagrams (enable JavaScript)

## Environment Diagrams

Environment diagrams are one of the best learning tools for understanding
`lambda` expressions and higher order functions because you're able to keep
track of all the different names, function objects, and arguments to functions.
We highly recommend drawing environment diagrams or using [Python
tutor](https://tutor.cs61a.org "https://tutor.cs61a.org") if you get stuck doing the WWPD problems below.
For examples of what environment diagrams should look like, try running some
code in Python tutor. Here are the rules:

### Assignment Statements

1. Evaluate the expression on the right hand side of the `=` sign.
2. If the name found on the left hand side of the `=` doesn't already exist in
 the current frame, write it in. If it does, erase the current binding. Bind the
 *value* obtained in step 1 to this name.

If there is more than one name/expression in the statement, evaluate all the
expressions first from left to right before making any bindings.

### def Statements

1. Draw the function object with its intrinsic name, formal parameters, and
 parent frame. A function's parent frame is the frame in which the function was
 defined.
2. If the intrinsic name of the function doesn't already exist in the current
 frame, write it in. If it does, erase the current binding. Bind the newly
 created function object to this name.

### Call expressions

> Note: you do not have to go through this process for a built-in Python function like `max` or `print`.
> 
> 

1. Evaluate the operator, whose value should be a function.
2. Evaluate the operands left to right.
3. Open a new frame. Label it with the sequential frame number, the intrinsic
 name of the function, and its parent.
4. Bind the formal parameters of the function to the arguments whose values you
 found in step 2.
5. Execute the body of the function in the new environment.

### Lambdas

> *Note:* As we saw in the `lambda` expression section above, `lambda`
> functions have no intrinsic name. When drawing `lambda` functions in
> environment diagrams, they are labeled with the name `lambda` or with the
> lowercase Greek letter λ. This can get confusing when there are
> multiple lambda functions in an environment diagram, so you can distinguish
> them by numbering them or by writing the line number on which they were defined.
> 
> 

1. Draw the lambda function object and label it with λ, its formal
 parameters, and its parent frame. A function's parent frame is the frame in
 which the function was defined.

This is the only step. We are including this section to emphasize the fact that
the difference between `lambda` expressions and `def` statements is that
`lambda` expressions *do not* create any new bindings in the environment.

 [YouTube link](https://youtu.be/IPec2A7j2bY?list=PLx38hZJ5RLZcUPWZ1-3HYsRPgZ8OCrvqz "https://youtu.be/IPec2A7j2bY?list=PLx38hZJ5RLZcUPWZ1-3HYsRPgZ8OCrvqz") 

# Required Questions

 Getting Started Videos (enable JavaScript)

## Getting Started Videos

These videos may provide some helpful direction for tackling the coding
problems on this assignment.

> To see these videos, you should be logged into your berkeley.edu email.
> 
> 

 [YouTube link](https://youtu.be/playlist?list=PLx38hZJ5RLZeufgodzb9XzDT_9Sr-L4sJ "https://youtu.be/playlist?list=PLx38hZJ5RLZeufgodzb9XzDT_9Sr-L4sJ") 

## What Would Python Display?

> **Important:**
> For all WWPD questions, type `Function` if you believe the answer is
> `<function...>`, `Error` if it errors, and `Nothing` if nothing is displayed.
> 
> 

### Q1: WWPD: The Truth Will Prevail

> Use Ok to test your knowledge with the following "What Would Python Display?" questions:
> 
> 
> 
```
> python3 ok -q short-circuit -uCopy✂️
> 
```
> 
> 
>  document.getElementById("copy-code-python3ok-qshort-circuit-u").onclick = () => copyCode('python3 ok -q short-circuit -u', "copy-code-python3ok-qshort-circuit-u");
>  
>   
> 

```
>>> True and 13
\_\_\_\_\_\_13
>>> False or 0
\_\_\_\_\_\_0
>>> not 10
\_\_\_\_\_\_False
>>> not None
\_\_\_\_\_\_True
```

 Toggle Solution (enable JavaScript)

```
>>> True and 1 / 0
\_\_\_\_\_\_Error (ZeroDivisionError)
>>> True or 1 / 0
\_\_\_\_\_\_True
>>> -1 and 1 > 0
\_\_\_\_\_\_True
>>> -1 or 5
\_\_\_\_\_\_-1
>>> (1 + 1) and 1
\_\_\_\_\_\_1
>>> print(3) or ""
\_\_\_\_\_\_3
''
```

 Toggle Solution (enable JavaScript)

```
>>> def f(x):
...     if x == 0:
...         return "zero"
...     elif x > 0:
...         return "positive"
...     else:
...         return ""
>>> 0 or f(1)
\_\_\_\_\_\_'positive'
>>> f(0) or f(-1)
\_\_\_\_\_\_'zero'
>>> f(0) and f(-1)
\_\_\_\_\_\_''
```

 Toggle Solution (enable JavaScript)

### Q2: WWPD: Higher-Order Functions

> Use Ok to test your knowledge with the following "What Would Python Display?" questions:
> 
> 
> 
```
> python3 ok -q hof-wwpd -uCopy✂️
> 
```
> 
> 
>  document.getElementById("copy-code-python3ok-qhof-wwpd-u").onclick = () => copyCode('python3 ok -q hof-wwpd -u', "copy-code-python3ok-qhof-wwpd-u");
>  
>   
> 
> 

```
>>> def cake():
...    print('beets')
...    def pie():
...        print('sweets')
...        return 'cake'
...    return pie
>>> chocolate = cake()
\_\_\_\_\_\_beets
>>> chocolate
\_\_\_\_\_\_Function
>>> chocolate()
\_\_\_\_\_\_sweets
'cake'
>>> more_chocolate, more_cake = chocolate(), cake
\_\_\_\_\_\_sweets
>>> more_chocolate
\_\_\_\_\_\_'cake'
>>> def snake(x, y):
...    if cake == more_cake:
...        return chocolate
...    else:
...        return x + y
>>> snake(10, 20)
\_\_\_\_\_\_Function
>>> snake(10, 20)()
\_\_\_\_\_\_30
>>> cake = 'cake'
>>> snake(10, 20)
\_\_\_\_\_\_30
```

 Toggle Solution (enable JavaScript)

### Q3: WWPD: Lambda

> Use Ok to test your knowledge with the following "What Would Python Display?" questions:
> 
> 
> 
```
> python3 ok -q lambda -uCopy✂️
> 
```
> 
> 
>  document.getElementById("copy-code-python3ok-qlambda-u").onclick = () => copyCode('python3 ok -q lambda -u', "copy-code-python3ok-qlambda-u");
>  
>   
> 
>   
> 
> As a reminder, the following two lines of code will not display any output in the
> interactive Python interpreter when executed:
> 
> 
> 
```
> >>> x = None
> >>> x
> >>>
> 
```
> 

```
>>> lambda x: x  # A lambda expression with one parameter x
\_\_\_\_\_\_<function <lambda> at ...>
>>> a = lambda x: x  # Assigning the lambda function to the name a
>>> a(5)
\_\_\_\_\_\_5
>>> (lambda: 3)()  # Using a lambda expression as an operator in a call exp.
\_\_\_\_\_\_3
>>> b = lambda x, y: lambda: x + y  # Lambdas can return other lambdas!
>>> c = b(8, 4)
>>> c
\_\_\_\_\_\_<function <lambda> at ...
>>> c()
\_\_\_\_\_\_12
>>> d = lambda f: f(4)  # They can have functions as arguments as well.
>>> def square(x):
...     return x * x
>>> d(square)
\_\_\_\_\_\_16
```

 Toggle Solution (enable JavaScript)

```
>>> higher_order_lambda = lambda f: lambda x: f(x)
>>> g = lambda x: x * x
>>> higher_order_lambda(2)(g)  # Which argument belongs to which function call?
\_\_\_\_\_\_Error
>>> higher_order_lambda(g)(2)
\_\_\_\_\_\_4
>>> call_thrice = lambda f: lambda x: f(f(f(x)))
>>> call_thrice(lambda y: y + 1)(0)
\_\_\_\_\_\_3
>>> print_lambda = lambda z: print(z)  # When is the return expression of a lambda expression executed?
>>> print_lambda
\_\_\_\_\_\_Function
>>> one_thousand = print_lambda(1000)
\_\_\_\_\_\_1000
>>> one_thousand # What did the call to print_lambda return?
\_\_\_\_\_\_# print\_lambda returned None, so nothing gets displayed
```

 Toggle Solution (enable JavaScript)

## Coding Practice

### Q4: Composite Identity Function

Write a function that takes in two single-argument functions, `f` and `g`, and
returns another **function** that has a single parameter `x`. The returned
function should return `True` if `f(g(x))` is equal to `g(f(x))` and `False`
otherwise. You can assume the output of `g(x)` is a valid input for `f` and vice
versa.

```
def composite_identity(f, g):
    """
    Return a function with one parameter x that returns True if f(g(x)) is
    equal to g(f(x)). You can assume the result of g(x) is a valid input for f
    and vice versa.

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2          # squares x [returns x^2]
    >>> b1 = composite_identity(square, add_one)
    >>> b1(0)                            # (0 + 1) ** 2 == 0 ** 2 + 1
    True
    >>> b1(4)                            # (4 + 1) ** 2 != 4 ** 2 + 1
    False
    """
    "*** YOUR CODE HERE ***"

```

Use Ok to test your code:

```
python3 ok -q composite_identityCopy✂️
```

 document.getElementById("copy-code-python3ok-qcomposite\_identity").onclick = () => copyCode('python3 ok -q composite\_identity', "copy-code-python3ok-qcomposite\_identity");

### Q5: Count Cond

Consider the following implementations of `count_fives` and `count_primes` which
use the `sum_digits` and `is_prime` functions from earlier assignments:

```
def count_fives(n):
    """Return the number of values i from 1 to n (including n)
    where sum_digits(n * i) is 5.
    >>> count_fives(10)  # Among 10, 20, 30, ..., 100, only 50 (10 * 5) has digit sum 5
    1
    >>> count_fives(50)  # 50 (50 * 1), 500 (50 * 10), 1400 (50 * 28), 2300 (50 * 46)
    4
    """
    i = 1
    count = 0
    while i <= n:
        if sum_digits(n * i) == 5:
            count += 1
        i += 1
    return count

def count_primes(n):
    """Return the number of prime numbers up to and including n.
    >>> count_primes(6)   # 2, 3, 5
    3
    >>> count_primes(13)  # 2, 3, 5, 7, 11, 13
    6
    """
    i = 1
    count = 0
    while i <= n:
        if is_prime(i):
            count += 1
        i += 1
    return count
```

The implementations look quite similar! Generalize this logic by writing a
function `count_cond`, which takes in a two-argument predicate function
`condition(n, i)`. `count_cond` returns a one-argument function that takes
in `n`, which counts all the numbers from 1 to `n` that satisfy `condition`
when called.

> **Note:**
> When we say `condition` is a predicate function, we mean that it is
> a function that will return `True` or `False`.
> 
> 

```
def sum_digits(y):
    """Return the sum of the digits of non-negative integer y."""
    total = 0
    while y > 0:
        total, y = total + y % 10, y // 10
    return total

def is_prime(n):
    """Return whether positive integer n is prime."""
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function Condition, where
    the first argument for Condition is N and the second argument is the
    number from 1 to N.

    >>> count_fives = count_cond(lambda n, i: sum_digits(n * i) == 5)
    >>> count_fives(10)   # 50 (10 * 5)
    1
    >>> count_fives(50)   # 50 (50 * 1), 500 (50 * 10), 1400 (50 * 28), 2300 (50 * 46)
    4

    >>> is_i_prime = lambda n, i: is_prime(i) # need to pass 2-argument function into count_cond
    >>> count_primes = count_cond(is_i_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    "*** YOUR CODE HERE ***"

```

Use Ok to test your code:

```
python3 ok -q count_condCopy✂️
```

 document.getElementById("copy-code-python3ok-qcount\_cond").onclick = () => copyCode('python3 ok -q count\_cond', "copy-code-python3ok-qcount\_cond");
