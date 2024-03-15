

# 

Lab 7: Inheritance, Linked Lists

 * [lab07.zip](lab07.zip "lab07.zip")

*Due by 11:59pm on Wednesday, March 13.*

## Starter Files

Download [lab07.zip](lab07.zip "lab07.zip").
Inside the archive, you will find starter files for the questions in this lab,
 along with a copy of the [Ok](ok "ok") autograder.

# Required Questions

 Getting Started Videos (enable JavaScript)

## Getting Started Videos

These videos may provide some helpful direction for tackling the coding
problems on this assignment.

> To see these videos, you should be logged into your berkeley.edu email.
> 
> 

 [YouTube link](https://youtu.be/playlist?list=PLx38hZJ5RLZf149ILKTCfQ11eVDRm8KS1 "https://youtu.be/playlist?list=PLx38hZJ5RLZf149ILKTCfQ11eVDRm8KS1") 

## Inheritance

Consult the drop-down if you need a refresher on Inheritance. It's
okay to skip directly to the questions and refer back
here should you get stuck.

 Inheritance (enable JavaScript)

To avoid redefining attributes and methods for similar classes, we can write a
single **base class** from which more specialized classes **inherit**. For
example, we can write a class called `Pet` and define `Dog` as a **subclass** of
`Pet`:

```
class Pet:

    def __init__(self, name, owner):
        self.is_alive = True    # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)

class Dog(Pet):

    def talk(self):
        super().talk()
        print('This Dog says woof!')
```

Inheritance represents a hierarchical relationship between two or more
classes where one class **is a** more specific version of the other:
a dog **is a** pet
(We use **is a** to describe this sort of relationship in OOP languages,
and not to refer to the Python `is` operator).

Since `Dog` inherits from `Pet`, the `Dog` class will also inherit the
`Pet` class's methods, so we don't have to redefine `__init__` or `eat`.
We do want each `Dog` to `talk` in a `Dog`-specific way,
so we can **override** the `talk` method.

We can use `super()` to refer to the superclass of `self`,
and access any superclass methods as if we were an instance of the superclass.
For example, `super().talk()` in the `Dog` class will call the `talk`
method from the `Pet` class, but passing the `Dog` instance as the `self`.
