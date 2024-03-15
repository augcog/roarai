

# 

Homework 5 Solutions

 * [hw05.zip](hw05.zip "hw05.zip")

## Solution Files

You can find the solutions in [hw05.py](hw05.py "hw05.py").

# Required Questions

 Getting Started Videos (enable JavaScript)

## Getting Started Videos

These videos may provide some helpful direction for tackling the coding
problems on this assignment.

> To see these videos, you should be logged into your berkeley.edu email.
> 
> 

 [YouTube link](https://youtu.be/playlist?list=PLx38hZJ5RLZcg5Zd4EMdx9fctIYVfJvnd "https://youtu.be/playlist?list=PLx38hZJ5RLZcg5Zd4EMdx9fctIYVfJvnd") 

### Q1: Infinite Hailstone

Write a generator function that yiels the elements of the hailstone sequence starting at number `n`.
After reaching the end of the hailstone sequence, the generator should yield the value 1 indefinitely.

Here's a quick reminder of how the hailstone sequence is defined:

1. Pick a positive integer `n` as the start.
2. If `n` is even, divide it by 2.
3. If `n` is odd, multiply it by 3 and add 1.
4. Continue this process until `n` is 1.

Try to write this generator function recursively. If you're stuck, you can first try writing it iteratively
and then seeing how you can turn that implementation into a recursive one.

> **Hint:** Since `hailstone` returns a generator, you can `yield from` a call to `hailstone`!
> 
> 

```
def hailstone(n):
    """Q1: Yields the elements of the hailstone sequence starting at n.
       At the end of the sequence, yield 1 infinitely.

    >>> hail_gen = hailstone(10)
    >>> [next(hail_gen) for _ in range(10)]
    [10, 5, 16, 8, 4, 2, 1, 1, 1, 1]
    >>> next(hail_gen)
    1
    """
 yield n
 if n == 1:
 yield from hailstone(n)
 elif n % 2 == 0:
 yield from hailstone(n // 2)
 else:
 yield from hailstone(n \* 3 + 1)
```

Use Ok to test your code:

```
python3 ok -q hailstoneCopy✂️
```

 document.getElementById("copy-code-python3ok-qhailstone").onclick = () => copyCode('python3 ok -q hailstone', "copy-code-python3ok-qhailstone");

### Q2: Merge

Write a generator function `merge` that takes in two infinite generators `a` and `b` that are in increasing order without duplicates and returns a generator that has all the elements of both generators, in increasing order, without duplicates.

```
def merge(a, b):
    """Q2:
    >>> def sequence(start, step):
    ...     while True:
    ...         yield start
    ...         start += step
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
 first\_a, first\_b = next(a), next(b)
 while True:
 if first\_a == first\_b:
 yield first\_a
 first\_a, first\_b = next(a), next(b)
 elif first\_a < first\_b:
 yield first\_a
 first\_a = next(a)
 else:
 yield first\_b
 first\_b = next(b)
```

Use Ok to test your code:

```
python3 ok -q mergeCopy✂️
```

 document.getElementById("copy-code-python3ok-qmerge").onclick = () => copyCode('python3 ok -q merge', "copy-code-python3ok-qmerge");
