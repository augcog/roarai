

# Midterm 1 Walkthrough

## Reverse Environment Diagrams

There were three possible questions, all pretty much the same but with different variable names and some parameter order switching.

You can view the code for each in PythonTutor:

[Flow that Yo-Yo](http://pythontutor.com/composingprograms.html#code=def%20yo_%28n,%20rev%29%3A%0A%20%20%20%20if%20n%20%3C%200%3A%0A%20%20%20%20%20%20%20%20return%20rev%28n,%20-3%29%0A%20%20%20%20elif%20n%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20float%28%22inf%22%29%0A%20%20%20%20return%20n%20*%20-2%0A%0Adef%20_yo%28x,%20y%29%3A%0A%20%20%20%20if%20y%20%3C%200%3A%0A%20%20%20%20%20%20%20%20y%20%2B%3D%201%0A%20%20%20%20if%20x%20%3D%3D%20y%3A%0A%20%20%20%20%20%20%20%20return%20lambda%20a%3A%20lambda%20b%3A%20a%20*%20x%20%2B%20b%20*%20y%0A%20%20%20%20return%20lambda%20a%3A%20lambda%20b%3A%20a%20%2B%20b%0A%0Aflo%20%3D%20yo_%28-2,%20_yo%29%283%29%285%29%0A&cumulative=true&curInstr=19&mode=display&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D "http://pythontutor.com/composingprograms.html#code=def%20yo_%28n,%20rev%29%3A%0A%20%20%20%20if%20n%20%3C%200%3A%0A%20%20%20%20%20%20%20%20return%20rev%28n,%20-3%29%0A%20%20%20%20elif%20n%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20float%28%22inf%22%29%0A%20%20%20%20return%20n%20*%20-2%0A%0Adef%20_yo%28x,%20y%29%3A%0A%20%20%20%20if%20y%20%3C%200%3A%0A%20%20%20%20%20%20%20%20y%20%2B%3D%201%0A%20%20%20%20if%20x%20%3D%3D%20y%3A%0A%20%20%20%20%20%20%20%20return%20lambda%20a%3A%20lambda%20b%3A%20a%20*%20x%20%2B%20b%20*%20y%0A%20%20%20%20return%20lambda%20a%3A%20lambda%20b%3A%20a%20%2B%20b%0A%0Aflo%20%3D%20yo_%28-2,%20_yo%29%283%29%285%29%0A&cumulative=true&curInstr=19&mode=display&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D")

[Radio Ga-Ga](http://pythontutor.com/composingprograms.html#code=def%20ga%28station,%20radio%29%3A%0A%20%20%20%20if%20station%20%3C%200%3A%0A%20%20%20%20%20%20%20%20return%20radio%28station,%20-3%29%0A%20%20%20%20elif%20station%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20float%28%22inf%22%29%0A%20%20%20%20return%20station%20*%20-98%0A%0Adef%20gaa%28cee,%20dee%29%3A%0A%20%20%20%20if%20dee%20%3C%200%3A%0A%20%20%20%20%20%20%20%20dee%20%2B%3D%201%0A%20%20%20%20if%20cee%20%3D%3D%20dee%3A%0A%20%20%20%20%20%20%20%20return%20lambda%20x%3A%20lambda%20y%3A%20x%20*%20cee%20-%20y%20*%20dee%0A%20%20%20%20return%20lambda%20x%3A%20lambda%20y%3A%20x%20*%20y%0A%0Aqueen%20%3D%20ga%28-2,%20gaa%29%283%29%285%29&cumulative=true&curInstr=19&mode=display&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D "http://pythontutor.com/composingprograms.html#code=def%20ga%28station,%20radio%29%3A%0A%20%20%20%20if%20station%20%3C%200%3A%0A%20%20%20%20%20%20%20%20return%20radio%28station,%20-3%29%0A%20%20%20%20elif%20station%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20float%28%22inf%22%29%0A%20%20%20%20return%20station%20*%20-98%0A%0Adef%20gaa%28cee,%20dee%29%3A%0A%20%20%20%20if%20dee%20%3C%200%3A%0A%20%20%20%20%20%20%20%20dee%20%2B%3D%201%0A%20%20%20%20if%20cee%20%3D%3D%20dee%3A%0A%20%20%20%20%20%20%20%20return%20lambda%20x%3A%20lambda%20y%3A%20x%20*%20cee%20-%20y%20*%20dee%0A%20%20%20%20return%20lambda%20x%3A%20lambda%20y%3A%20x%20*%20y%0A%0Aqueen%20%3D%20ga%28-2,%20gaa%29%283%29%285%29&cumulative=true&curInstr=19&mode=display&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D")

[YipYiip Book](http://pythontutor.com/composingprograms.html#code=def%20yiip%28signal,%20bookbook%29%3A%0A%20%20%20%20if%20signal%20%3C%200%3A%0A%20%20%20%20%20%20%20%20return%20bookbook%28-3,%20signal%29%0A%20%20%20%20elif%20signal%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20float%28%22inf%22%29%0A%20%20%20%20return%20signal%20*%20-98%0A%0Adef%20yip%28mup,%20pet%29%3A%0A%20%20%20%20if%20mup%20%3C%200%3A%0A%20%20%20%20%20%20%20%20mup%20%2B%3D%201%0A%20%20%20%20if%20mup%20%3D%3D%20pet%3A%0A%20%20%20%20%20%20%20%20return%20lambda%20al%3A%20lambda%20fal%3A%20mup**al%20%2B%20pet**fal%0A%20%20%20%20return%20lambda%20al%3A%20lambda%20fal%3A%20al%20-%20fal%0A%0Ayuiop%20%3D%20yiip%28-2,%20yip%29%283%29%285%29%0A&cumulative=true&curInstr=19&mode=display&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D "http://pythontutor.com/composingprograms.html#code=def%20yiip%28signal,%20bookbook%29%3A%0A%20%20%20%20if%20signal%20%3C%200%3A%0A%20%20%20%20%20%20%20%20return%20bookbook%28-3,%20signal%29%0A%20%20%20%20elif%20signal%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20float%28%22inf%22%29%0A%20%20%20%20return%20signal%20*%20-98%0A%0Adef%20yip%28mup,%20pet%29%3A%0A%20%20%20%20if%20mup%20%3C%200%3A%0A%20%20%20%20%20%20%20%20mup%20%2B%3D%201%0A%20%20%20%20if%20mup%20%3D%3D%20pet%3A%0A%20%20%20%20%20%20%20%20return%20lambda%20al%3A%20lambda%20fal%3A%20mup**al%20%2B%20pet**fal%0A%20%20%20%20return%20lambda%20al%3A%20lambda%20fal%3A%20al%20-%20fal%0A%0Ayuiop%20%3D%20yiip%28-2,%20yip%29%283%29%285%29%0A&cumulative=true&curInstr=19&mode=display&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D")

Two of the questions had multiple possible answers, and you had to select every possible answer to get full credit. The answer had to be a logical condition that would evaluate to a truthy value, and multiple conditions evaluated to `True` for each diagram. For example, the code above used `y < 0`, but many other conditions also worked: `x < 0`, `y <= 0`, `x <= 0`. If you missed the other conditions, please remember to read a question fully to see if it's a "select all that apply" question, and then consider which conditions would result in the same diagram.

Here's a general strategy for Reverse Environment Diagram questions:

* Load up PythonTutor
* Fill in the blanks with some default values to see full environment diagram (add random numbers/string/lambda)
* Go through code line by line, and see if you can update any of your default values to match what the expected output should be
* For "select all that apply", consider each case with the variables present at that line of code to see how it would change the control flow

## The Case of the Missing Docstring

The correct answer was "Returns the average of positive elements in L or returns zero if no such elements exist."

Here's why the others were incorrect:

* Returns the average of all elements in L or returns zero if no elements exist.

	+ The code had `if item > 0:` inside the loop and only added the value in that case, so it wasn't averaging all the elements, it was only averaging the elements that were greater than 0.
* Returns the average of elements in L with an odd index or returns zero if no such elements exist.

	+ There was no condition checking to see if the elements had an odd index (such a condition would probably look like `if i % 2 == 1`).
* Returns the average of elements in L that are >= 0 or returns zero if no such elements exist.

	+ The code had `if item > 0`, not `if item >= 0`, so this is not quite right.

## Magical Test Weaver

This question was inspired by `interleave_digits` from the 2/8 Function Examples lecture.

The answer required a very careful reading of the docstring:

```
""" Assuming A and B are positive integers with the same number of base-10 digits
and C is a positive integer < 10, return the number whose base-10
representation is the interleaving of digits in A and B (alternating
first one from A then one from B) from all positions where the
two digits in A and B at that position are both >= C.  Return 0 if there
are no such positions. Raises an exception if preconditions are not met."""
```

Plus an understanding of the terms used:

* **Positive**: A number that is greater than 0. We made the clarification during the exam that 0 is not a positive number, as many people asked.
* **Integer**: An integer is a whole number (a number that is not a fraction).
* **Precondition**: A precondition describes the requirements of the input parameters of a function (versus a postcondition that describes the requirements of the output).
* **Exception**: When code raises an exception and that exception is not explicitly handled, the entire program stops running and the exception is displayed. See [Exceptions](https://www.composingprograms.com/pages/33-exceptions.html "https://www.composingprograms.com/pages/33-exceptions.html") in the textbook or the 2/5 Design + Exceptions lecture.

The correct answer was only:

```
>>> magic_weave(456, 567, 5)
5667
```

Here's why the others were incorrect:

```
>>> magic_weave(123, 456, 5)
56
```

^ This test contains two numbers from the second number and none from the first number. That is *not* an interleaving as described by the docstring and evidenced in the passing doctest.

```
>>> magic_weave(234, 456, 5)
3546
```

^ This test interleaves the second and third elements of each number. However, the docstring specifies that a pair of digits can only be interleaved if they are both >= the third parameter. Since 3 and 4 are less than 5, neither pair of digits should have been interleaved.

```
>>> magic_weave(0, 0, 5)
0
```

^ This test passes in 0 for both A and B. However, 0 is not a positive integer, and the docstring specified that an exception would be raised if preconditions are not met. An exception is not the same thing as the answer 0, so this not be a passing doctest. (We gave partial credit if you selected this and the other precondition failure below, however, since we have not shown exception-checking doctests in class).

```
>>> magic_weave(101, 202, 0)
120012
```

^ This test passed in 0 for C. However, 0 is not a positive integer, so once again, this function call should result in a raised exception, not a return value of 0. (We gave partial credit if you selected this and the one above, however.)

```
>>> magic_weave(567, 899, 10)
586979
```

^ This test has two issues. The first issue is that it should only interleave digits in each position that are >= C, and none of the digits are >= 10 (as that'd be impossible for a single digit). The other issue is that the preconditions specify that C should be < 10, so this should actually result in an exception raised.

## Domain on the Range

This question asked you to make higher-order functions to restrict the domain and range of a function. These functions are inspired by functions that are common in production codebases for checking that the input parameters to functions are valid in some way. They're quite handy, especially when combined with Python decorators.

### Restrict domain

This solution checks whether the given `n` is outside the range and returns -Infinity if so, and returns `f(n)` otherwise.

```
def restrict_domain(f, min_d, max_d):
    def helper(n):
        if n < min_d or n > max_d:
            return float("-inf")
        return f(n)
    return helper
```

It's also valid to do the opposite: check if n is within the range, and return `f(n)` if so.

```
def restrict_domain(f, min_d, max_d):
    def helper(n):
        if n >= min_d and n <= max_d:
            return f(n)
        return float("-inf")
    return helper
```

The docstring says that the range is inclusive, which means it contains the start and the end of the range. So it would be incorrect to say `n > min_d and n < max_d`, since a value of `min_d` or `max_d` would be excluded in that case. Pay careful attention to whether you use `>=` or `>` in a problem, and whether you have doctests checking for the edges of a range, since that can be a common source of errors in programming.

### Restrict range

This solution first calculates the result of `f(n)` and stores it in a variable. If that result is outside the range, it returns -Infinity and otherwise returns the result.

```
def restrict_range(f, min_r, max_r):
    def helper(n):
        result = f(n)
        if result < min_r or result > max_r:
            return float("-inf")
        return result
    return helper
```

Another valid approach is to switch the `if`:

```
def restrict_range(f, min_r, max_r):
    def helper(n):
        result = f(n)
        if result >= min_r and result <= max_r:
            return result
        return float("-inf")
    return helper
```

Some solutions opted not to store the result in a temporary variable:

```
def restrict_range(f, min_r, max_r):
    def helper(n):
        if f(n) >= min_r and f(n) <= max_r:
            return f(n)
        return float("-inf")
    return helper
```

That approach requires calling `f(n)` three times, and `f(n)` could be an expensive computation, so it's not the most efficient solution. However, we gave full credit for it, since we did not ask for efficiency and have not discussed that much. Plus, this function could be used in a codebase where the computations were either trivial or cached, so a repeated call to a function would not be a significant waste of computation time.

### Restrict both

This question asked you to write a single higher-order function that called both functions in order to restrict both the domain and the range.

The simplest solution composes the two functions

```
def restrict_both(f, min_d, max_d, min_r, max_r):
    return restrict_range(restrict_domain(f, min_d, max_d), min_r, max_r)
```

Some students came up with longer solutions that still worked and got full credit, such as:

```
def restrict_both3(f, low_d, high_d, low_r, high_r):
    def helper(x):
        a1 = restrict_domain(f, low_d, high_d)(x)
        if a1 != float("-inf"):
            a2 = restrict_range(f, low_r, high_r)(x)
            if a2 != float("-inf"):
                return f(x)
        return float("-inf")
    return helper
```

It's important that a solution like that checks the domain before the range. If the checks aren't ordered that way, the doctests fail, since the test lambda resulted in a `DivisionByZero` error if it was called with 0. If you have time, please always check your solutions in code.cs61a.org and run the doctests there (by clicking the red test tube), since that can reveal errors and edge cases.

If you missed this question, you may want to revisit:

* [Lab 7: Composite Identity function](https://cs61a.org/lab/lab02/#q7 "https://cs61a.org/lab/lab02/#q7")
* [Homework 2: Q1-3](https://cs61a.org/hw/hw02/#q1 "https://cs61a.org/hw/hw02/#q1")

You can erase your work and try those problems again to see if the concepts still make sense.

## Digit replacer

This question required an ability to break down numbers and build them back up again. We've done that in several problems, starting with [Lab 1: Sum Digits](https://cs61a.org/lab/lab01/#q5 "https://cs61a.org/lab/lab01/#q5"). Remember:

* `(n // 10)` shaves off the last digit of a number (`345 // 10` results in 34).
* `(n % 10)` gets the last digit of a number (`345 % 10` results in 5).
* `(n * 10**pow)` creates a number with `n` in that `pow`-er of 10 (`3 * 10**2` results in 300).

We generally process numbers from the right-most digit to the left-most digit since it is easier to get the right-most digit (thanks to `%`) than the left-most digit.

Let's see how we can use those techniques for iterative and recursive solutions.

### Iterative

This solution initializes the new number to 0, the power of ten to 0, and starts processing the right-most digit. If `pred(digit)` is true, it computes `transform(digit)`. It then multiplies that digit by the current power of 10 and adds it to the new number. It increments the power of ten, shaves the last digit off the number, and keeps going in the next iteration of the loop.

```
def digit_replacer(pred, transform):
    def func(n):
            new_number = 0
            power_of_ten = 0

            while n > 0:
                    digit = n % 10
                    if pred(digit):
                        digit = transform(digit)
                    new_number += digit * 10**power_of_ten
                    power_of_ten += 1
                    n = n // 10
            return new_number
    return func
```

So, for `n` of 345, if we ignore digit transformation, the values in each iteration of the loop are:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| START
OF LOOP | n | digit | new\_number | power\_of\_ten | n | END OF
LOOP |
|  | 345 | 5 | 5 (from 0 + 5 \* 10\*\*0) | 1 | 34 |  |
|  | 34 | 4 | 45 (from 5 + 4 \* 10\*\*1) | 2 | 3 |  |
|  | 3 | 3 | 345 (from 45 + 3 \* 10\*\*2) | 3 | 0 |  |

When combined with the digit transformation step, the digit added to the new number can change as needed.

### Recursive

We use similar techniques when solving this recursively. Here's one solution:

```
def digit_replacer(pred, transform):

    def func(n):
            if n == 0:
                return 0
            digit = n % 10
            if pred(digit):
                digit = transform(digit)
            return func(n // 10) * 10 + digit

    return func
```

The base case is when `n == 0`, which is the same as the case when the loop stopped in the iterative approach. Keep that in mind when considering iterative and recursive approaches to the same problem - the loop condition is often related to the base case.

The recursive call breaks down the problem by passing the shaved number (`n // 10`), then multiplying it by 10 and adding it to the digit. That's very similar to `digit * 10**power_of_ten` from the iterative approach. However, it doesn't need to multiply by the power of 10 as the recursion takes care of that (each call will add `* 10` to the next result). You can see why that works in this video about [interleave\_digits](https://www.youtube.com/watch?v=UMZqEXY-e5c&feature=youtu.be "https://www.youtube.com/watch?v=UMZqEXY-e5c&feature=youtu.be"), a similar problem.

There were several variants on this recursive approach which also got full credit. They mostly differed in their length and use of intermediary variables. Here's an example:

```
def digit_replacer(pred, transform):

    def replacer(n):
            if n == 0:
                return 0
            if p(n % 10):
                return replacer(n // 10) * 10 + f(n % 10)
            return replacer(n // 10) * 10 + (n % 10)

    return replacer
```

If you missed this question, try doing the problems in Lecture 9 (Function examples) and revisiting [the Merge numbers problem](https://cs61a.org/disc/disc03/#q2 "https://cs61a.org/disc/disc03/#q2")from discussion.

## Run Checker

This question shows how we can use nested functions to remember previous inputs to a function. We used similar techniques for the `commentary` and `say` functions in the Hog project.

Here's the suggested solution:

```
def run_checker(condition, result):

    def f(two_ago, one_ago):
            def g(input):
                if condition(two_ago, one_ago, input):
                    print(result(two_ago, one_ago, input))
                else:
                    print("No run!")
                return f(one_ago, input)
            return g

    return f(-1, -1)
```

Let's step through the doctest example:

```
>>> f = run_checker(lambda a, b, c: a > b > c and a >= 10,
                lambda a, b, c: a*(b+c))
```

When `run_checker` is first called, it returns `f(-1, -1)`, which returns a reference to the `g` function. That `g` reference was defined in an environment where `two_ago` is -1 and `one_ago` is -1.

```
>>> f = f(15)
```

That call to `f` is really a call to the `g` reference with an input of 15. It checks `condition(-1, -1, 15)`, sees that it is `False`, and prints "No run!". It then returns `f(-1, 15)`, which returns a new reference to a `g` function. This `g` reference was defined in an environment where `two_ago` is -1 and `one_ago` is 15.

```
>>> f = f(10)
```

Once again, this call to `f` is really a call to the recent `g` reference with an input of 10. It checks `condition(-1, 15, 10)`, sees that it's `False`, and prints "No run!". It then returns `f(15, 10)`, which returns a new reference to the `g` function. This `g` reference was defined in an environment where `two_ago` is 15 and `one_ago` is 10.

```
>>> f = f(5)
```

This call to `f` is really a call to the most recent `g` reference with an input of 5. It checks `condition(15, 10, 5)`, sees that it's `True`, and prints `result(15, 10, 5)`, which is 225. It then returns `f(10, 5)`, which returns a new reference to the `g` function. This `g` reference was defined in an environment where `two_ago` is 10 and `one_ago` is 5.

You can keep going with the doctests (and try in PythonTutor), but hopefully that gives you an idea of how this type of function works. It's important to understand how Python looks up the values of names in an environment, and to realize that there's a different environment for each of the `g` functions returned during the program.

Similar questions:

* [Exam Prep: My Last Three Brain Cells](https://cs61a.org/examprep/examprep01/#q4 "https://cs61a.org/examprep/examprep01/#q4") (nearly the same!)
* [Exam Prep: Natural Chains](https://cs61a.org/examprep/examprep02/#q2 "https://cs61a.org/examprep/examprep02/#q2")

## Measure Twice, Cup Once

This is essentially a partition counting problem. If you had never seen this before, this would be a fairly difficult problem to solve (especially on an exam).
However, we have seen this problem in [the textbook](https://www.composingprograms.com/pages/17-recursive-functions.html#example-partitions "https://www.composingprograms.com/pages/17-recursive-functions.html#example-partitions"), [in lecture 7 (Slides 39-45)](https://cs61a.org/assets/slides/07-Tree_Recursion_full.pdf "https://cs61a.org/assets/slides/07-Tree_Recursion_full.pdf"), and [in homework (Count Coins)](https://cs61a.org/hw/hw03/#q4 "https://cs61a.org/hw/hw03/#q4"). One skill you can aim to develop in this class is recognizing classes of problems and considering what algorithms you have learned in the past to tackle that class of problem. Then you can consider the particular problem, how it's different from the solution you learned, and adjust your approach accordingly.

The classic `count_partitions(n, m)` problem counts up how many ways we can make the number `n` using parts up to size `m`. For example, `count_partitions(6, 4)` results in 9, since there are nine ways to make the number 6 using numbers up to 4:

1. 6 = 2 + 4
2. 6 = 1 + 1 + 4
3. 6 = 3 + 3
4. 6 = 1 + 2 + 3
5. 6 = 1 + 1 + 1 + 3
6. 6 = 2 + 2 + 2
7. 6 = 1 + 1 + 2 + 2
8. 6 = 1 + 1 + 1 + 1 + 2
9. 6 = 1 + 1 + 1 + 1 + 1 + 1

The `count_coins(change)` problem counts how many ways we can make `change` using coins. So, `count_change(15)` results in 6, since there are six ways to make 15 cents using US coins:

1. 15 1-cent coins
2. 10 1-cent, 1 5-cent coins
3. 5 1-cent, 2 5-cent coins
4. 5 1-cent, 1 10-cent coins
5. 3 5-cent coins
6. 1 5-cent, 1 10-cent coin

There are some differences between the problems:

* `count_partitions` is using integers for partitions, so it can just increment by 1 to find the next largest partition size. It stops when the partition size is > m. (Or it can decrement by 1, and stop when partition size is 0).
* `count_coins` is using coin sizes, so it must use a function to find the next largest coin size. It stops when the coin size is `None`.

That meant we could use a very similar approach to each problem, but had to change the way that we found the next partition size and our logic for stopping.

Here's the textbook solution for `count_partitions`:

```
def count_partitions(n, m):
    """Count the ways to partition n using parts up to m."""
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        return count_partitions(n-m, m) + count_partitions(n, m-1)
```

Review the solution for `count_coins` by solving the problem again or by checking the official solution.

What's the same?

* They both have the same two bases cases for returning 1 when it's found a successful partition and returning 0 when it's overshot.
* They both return the sum of two recursive calls, one call that counts partitioning with the next largest coin, and the other that counts partitions with the current coin.

What's different?

* The `count_coins` function uses a helper function, which aids us in keeping track of the current coin (since `count_coins` only takes a single parameter, not enough for our tracking purposes).
* Relatedly, it calls a function to figure out the next coin size, instead of simply decrementing.
* They have two different conditions for their third base case, which tells them when they've run out of partition sizes. `count_partitions` checks `m == 0`, while `count_coins` checks for an invalid smallest coin.

That brings us to `measure_methods(grams_needed, available_sizes)`. This variant of the problem passes in a list of cup sizes, and we must select partition sizes from that list.

Here's a solution that's similar to the `count_coins` solution:

```
def measure_methods(grams_needed, available_sizes):

    def measurer(grams_needed, cup_index):
            if grams_needed < 0:
                return 0
            if grams_needed == 0:
                return 1
            if cup_index >= len(available_sizes):
                return 0

            without_cup = measurer(grams_needed, cup_index + 1)
            with_cup = measurer(grams_needed - available_sizes[cup_index], cup_index)
            return without_cup + with_cup

    return measurer(grams_needed, 0)
```

What's the same? The first two bases cases, the summing of the two recursive calls, the use of a helper function to track the current cup size.

What's different?

* The helper method uses a second parameter to track the current list index (instead of the current coin value). It starts with 0, since that's the first index in a list, and then adds 1 in the recursive call which count partitions for the next largest cup.
* In order to get the current size, it indexes into the array: `available_sizes[cup_index]`
* The third base case checks whether the index is beyond the length of the array, using `cup_index >= len(available_sizes)`.

There were quite a few correct approaches to this problem, but they all essentially did the same thing: figured out some way to track where we were in the array and count partitions, either by counting up or counting down.

Here's one that counted down:

```
def measure_methods(total_needed, cup_sizes):

    def helper(total_needed, curr_i):
        if total_needed < 0:
            return 0
        elif curr_i < 0:
            return 0
        elif total_needed == 0:
            return 1
        else:
            with_cup = helper(total_needed - cup_sizes[curr_i], curr_i)
            without_cup = helper(total_needed, curr_i - 1)
            return with_cup + without_cup

    return helper(total_needed, len(cup_sizes) - 1)
```

Try spotting the differences in that approach!

If you missed this problem, please try it again and re-visit the `count_cups`. If you're perplexed by how the two recursive calls manage to count partitions, you could even draw out the whole tree of recursive calls. You'll see that the paths that end in 1 are correct partitions, and the paths that end in 0 are not (due to either resulting in too large of a total or trying to use a size that doesn't exist). Do whatever helps you understand the approach! :)
