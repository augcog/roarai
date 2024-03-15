

# 

Project 3: Ants Vs. SomeBees

 * [ants.zip](ants.zip "ants.zip")

![Ants vs. Somebees](static/assets/splash.png)

> 
>  The bees are coming!  
> 
>  Create a better soldier  
> 
>  With inherit-ants.
> 

## Introduction

> **For full credit:**
> 
> 
> * Submit with Phase 1 complete by **Thursday, March 7** (worth 1 pt).
> * Submit with Phase 2 complete by **Tuesday, March 12** (worth 1 pt).
> * Submit with all phases complete by **Tuesday, March 19**.
> 
> 
> Solve the problems in order, since some later problems depend on earlier
> problems.
> 
> 
> The entire project can be completed with a partner.
> 
> 
> You can get 1 bonus point by submitting the entire project by
> **Monday, March 18**.
> 
> 

In this project, you will create a [tower defense](https://secure.wikimedia.org/wikipedia/en/wiki/Tower_defense "https://secure.wikimedia.org/wikipedia/en/wiki/Tower_defense") game called Ants Vs.
SomeBees. As the ant queen, you populate your colony with the bravest ants you
can muster. Your ants must protect their queen from the evil bees that invade
your territory. Irritate the bees enough by throwing leaves at them, and they
will be vanquished. Fail to pester the airborne intruders adequately, and your
queen will succumb to the bees' wrath. This game is inspired by PopCap Games'
[Plants Vs. Zombies](https://www.ea.com/studios/popcap/plants-vs-zombies "https://www.ea.com/studios/popcap/plants-vs-zombies").

This project uses an object-oriented programming paradigm,
focusing on material from [Chapter 2.5](https://www.composingprograms.com/pages/25-object-oriented-programming.html "https://www.composingprograms.com/pages/25-object-oriented-programming.html") of Composing Programs. The
project also involves understanding, extending, and testing a large program.

## Download starter files

The [ants.zip](ants.zip "ants.zip") archive contains several files, but all of your
changes will be made to `ants.py`.

* `ants.py`: The game logic of Ants Vs. SomeBees
* `ants_plans.py`: The details of each difficulty level
* `ucb.py`: Utility functions for CS 61A
* `gui.py:` A graphical user interface (GUI) for Ants Vs. SomeBees.
* `ok`: The autograder
* `proj3.ok`: The `ok` configuration file
* `tests`: A directory of tests used by `ok`
* `libs`: A directory of libraries used by `gui.py`
* `static`: A directory of images and files used by `gui.py`
* `templates`: A directory of HTML templates used by `gui.py`

## Logistics

The project is worth 25 points.
23 points are for correctness,
1 point is for submitting Phase 1 by the first checkpoint date and 1 point is for submitting Phase 2 by the second checkpoint date.

You can get 1 EC point for submitting the entire project by
**Monday, March 18**.

You will turn in the following files:

* `ants.py`

You do not need to modify or turn in any other files to complete the
project. To submit the project,  **submit the required files to the appropriate Gradescope assignment.**

For the functions that we ask you to complete, there may be some
initial code that we provide. If you would rather not use that code,
feel free to delete it and start from scratch. You may also add new
function definitions as you see fit.

**However, please do not modify any other functions or edit any files not
listed above**. Doing so may result in your code failing our autograder tests.
Also, please do not change any function signatures (names, argument order, or
number of arguments).

Throughout this project, you should be testing the correctness of your code.
It is good practice to test often, so that it is easy to isolate any problems.
However, you should not be testing *too* often, to allow yourself time to
think through problems.

We have provided an **autograder** called `ok` to help you
with testing your code and tracking your progress. The first time you run the
autograder, you will be asked to **log in with your Ok account using your web
browser**. Please do so. Each time you run `ok`, it will back up
your work and progress on our servers.

The primary purpose of `ok` is to test your implementations.

If you want to test your code interactively, you can run

```
 python3 ok -q [question number] -i 
```

with the appropriate question number (e.g. `01`) inserted.
This will run the tests for that question until the first one you failed,
then give you a chance to test the functions you wrote interactively.

You can also use the debugging print feature in OK by writing

```
 print("DEBUG:", x) 
```

which will produce an output in your terminal without causing OK tests to fail
with extra output.

## The Game

A game of Ants Vs. SomeBees consists of a series of turns. In each turn, new
bees may enter the ant colony. Then, new ants are placed to defend their colony.
Finally, all insects (ants, then bees) take individual actions. Bees either try
to move toward the end of the tunnel or sting ants in their way. Ants perform a
different action depending on their type, such as collecting more food or
throwing leaves at the bees. The game ends either when a bee reaches the end of
the tunnel (ants lose), the bees destroy a `QueenAnt` if it exists (ants lose),
or the entire bee fleet has been vanquished (ants win).

![](static/assets/screenshot.gif)
### Core concepts

**The Colony**. This is where the game takes place. The colony consists of
several `Place`s that are chained together to form tunnels through which the
bees travel. The colony also has some quantity of food which can be expended in
order to place an ant in a tunnel.

**Places**. A place links to another place to form a tunnel. The player can
put a single ant into each place. However, there can be many bees in a single
place.

**The Hive**. This is the place where bees originate. Bees exit the beehive to
enter the ant colony.

**Ants**. The player places an ant into the colony by selecting from the
available ant types at the top of the screen.
Each type of ant takes a different action and requires a different
amount of colony food to place. The two most basic ant types are the `HarvesterAnt`,
which adds one food to the colony during each turn, and the `ThrowerAnt`, which
throws a leaf at a bee each turn. You will be implementing many more!

**Bees**. Each turn, a bee either advances to the next place in the tunnel if no
ant is in its way, or it stings the ant in its way. Bees win when at least one
bee reaches the end of a tunnel. In addition to the orange bees, there are
yellow wasps that do double damage and a green boss bee that is quite difficult
to vanquish.

### Core classes

The concepts described above each have a corresponding class that encapsulates
the logic for that concept. Here is a summary of the main classes involved in
this game:

* **`GameState`**: Represents the colony and some state information about the game,
 including how much food is available, how much time has elapsed, where the
 `AntHomeBase` is, and all the `Place`s in the game.
* **`Place`**: Represents a single place that holds insects. At most one `Ant` can
 be in a single place, but there can be many `Bee`s in a single place. `Place` objects have an
 `exit` to the left and an `entrance` to the right, which are also places.
 Bees travel through a tunnel by moving to a `Place`'s `exit`.
* **`Hive`**: Represents the place where `Bee`s start out (on the right of the tunnel).
* **`AntHomeBase`**: Represents the place `Ant`s are defending (on the left of the tunnel). If `Bee`s get here, they win :(
* **`Insect`**: A base class for `Ant` and `Bee`. Each insect has a `health`
 attribute representing its remaining health and a `place` attribute representing the `Place` where
 it is currently located. Each turn, every active `Insect` in the game
 performs its `action`.
* **`Ant`**: Represents ants. Each `Ant` subclass has special attributes or a
 special `action` that distinguish it from other `Ant` types. For example, a
 `HarvesterAnt` gets food for the colony and a `ThrowerAnt` attacks `Bee`s.
 Each ant type also has a `food_cost` attribute that indicates how much it
 costs to deploy one unit of that type of ant.
* **`Bee`**: Represents bees. Each turn, a bee either moves to the `exit` of
 its current `Place` if the `Place` is not `blocked` by an ant, or stings the
 ant occupying its same `Place`.

### Game Layout

Below is a visualization of a GameState.

![](static/assets/colony-drawing.png)
