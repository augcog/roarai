

# 

Discussion 7: OOP

 * [disc07.pdf](disc07.pdf "disc07.pdf")

Pick someone in your group to [join Discord](https://cs61a.org/articles/discord "https://cs61a.org/articles/discord").
It's fine if multiple people join, but one is enough.

Now switch to Pensieve:

* **Everyone**: Go to [discuss.pensieve.co](http://discuss.pensieve.co "http://discuss.pensieve.co") and log in with your @berkeley.edu email, then enter your group number. (Your group number is the number of your Discord channel.)

Once you're on Pensieve, you don't need to return to this page; Pensieve has all the same content (but more features). If for some reason Penseive doesn't work, return to this page and continue with the discussion.

Post in the `#help` channel on [Discord](https://cs61a.org/articles/discord/ "https://cs61a.org/articles/discord/") if you have trouble.

# Getting Started

Say your name, another class you're taking besides CS 61A, and something you've
practiced for a while, such as playing an instrument, juggling, or martial arts.
Did you discover any common interests among your group members?

### Q1: Draw

The `draw` function takes a list `hand` and a list of unique non-negative
integers `positions` that are all less than the length of `hand`. It removes
`hand[p]` for each `p` in `positions` and returns a list of those elements in
the order they appeared in `hand` (not the order they appeared in `positions`).

Fill in each blank with one of these names: `list`, `map`, `filter`, `reverse`,
`reversed`, `sort`, `sorted`, `append`, `insert`, `index`, `remove`, `pop`,
`zip`, or `sum`. See the [built-in functions](https://docs.python.org/3/library/functions.html "https://docs.python.org/3/library/functions.html") and
[list methods](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists "https://docs.python.org/3/tutorial/datastructures.html#more-on-lists")
documentation for descriptions of what these do.

**Discussion Time:** Before writing anything, talk as a group about what
process you'll implement in order to make sure the right cards are removed and
returned. Try not to guess-and-check! The purpose of discussion is for you to
try to solve problems without the help of an interpreter checking your work.

[Run in 61A Code](javascript:void "javascript:void")

 $(() => activateEditor('def draw(hand, positions):\n &quot;&quot;&quot;Remove and return the items at positions from hand.\n\n &gt;&gt;&gt; hand = [&#x27;A&#x27;, &#x27;K&#x27;, &#x27;Q&#x27;, &#x27;J&#x27;, 10, 9]\n &gt;&gt;&gt; draw(hand, [2, 1, 4])\n [&#x27;K&#x27;, &#x27;Q&#x27;, 10]\n &gt;&gt;&gt; hand\n [&#x27;A&#x27;, &#x27;J&#x27;, 9]\n &quot;&quot;&quot;\n return \_\_\_\_\_(\_\_\_\_\_( [hand.\_\_\_\_\_(i) for i in \_\_\_\_\_(\_\_\_\_\_(positions))] ))\n\n', "python", "draw-input"));

 Hint: Ordering (enable JavaScript)

For a list `s` and integer `i`, `s.pop(i)` returns and removes the `i`th
element, which changes the position (index) of all the later elements but
does not affect the position of prior elements.

 Hint: Reversed (enable JavaScript)

Calling `reversed(s)` on a list `s` returns an iterator. Calling
`list(reversed(s))` returns a list of the elements in `s` in reversed order.

*Aced* it? Give yourselves a *hand*!

# Object-Oriented Programming

A productive approach to defining new classes is to determine what instance
attributes each object should have and what class attributes each class should
have. First, describe the type of each attribute and how it will be used, then
try to implement the class's methods in terms of those attributes.

### Q2: Keyboard

**Overview:** A keyboard has a button for every letter of the alphabet. When a
button is pressed, it outputs its letter by calling an `output` function (such
as `print`). Whether that letter is uppercase or lowercase depends on how many
times the *caps lock* key has been pressed.

**First**, implement the `Button` class, which takes a lowercase `letter` (a
string) and a one-argument `output` function, such as `Button('c', print)`.

The `press` method of a `Button` calls its `output` attribute (a function) on
its `letter` attribute: either uppercase if `caps_lock` has been pressed an odd
number of times or lowercase otherwise. The `press` method also increments
`pressed` and returns the key that was pressed. *Hint*: `'hi'.upper()` evaluates
to `'HI'`.

**Second**, implement the `Keyboard` class. A `Keyboard` has a dictionary called
`keys` containing a `Button` (with its `letter` as its key) for each letter in
`LOWERCASE_LETTERS`. It also has a list of the letters `typed`, which may be
a mix of uppercase and lowercase letters.

The `type` method takes a string `word` containing only lowercase letters. It
invokes the `press` method of the `Button` in `keys` for each letter in `word`,
which adds a letter (either lowercase or uppercase depending on `caps_lock`) to
the `Keyboard`'s `typed` list. **Important:** Do not use `upper` or `letter` in
your implementation of `type`; just call `press` instead.

Read the doctests and talk about:

* Why it's possible to press a button repeatedly with `.press().press().press()`.
* Why pressing a button repeatedly sometimes prints on only one line and sometimes
 prints multiple lines.
* Why `bored.typed` has 10 elements at the end.

**Discussion Time**: Before anyone types anything, have a conversation
describing the type of each attribute and how it will be used. Start with
`Button`: how will `letter` and `output` be used? Then discuss `Keyboard`: how
will `typed` and `keys` be used? How will new letters be added to the list
called `typed` each time a `Button` in `keys` is pressed? Call the staff if
you're not sure! Once everyone understands the answers to these questions, you
can try writing the code together.

[Run in 61A Code](javascript:void "javascript:void")

 $(() => activateEditor('LOWERCASE\_LETTERS = &#x27;abcdefghijklmnopqrstuvwxyz&#x27;\n\nclass CapsLock:\n def \_\_init\_\_(self):\n self.pressed = 0\n\n def press(self):\n self.pressed += 1\n\nclass Button:\n &quot;&quot;&quot;A button on a keyboard.\n\n &gt;&gt;&gt; f = lambda c: print(c, end=&#x27;&#x27;) # The end=&#x27;&#x27; argument avoids going to a new line\n &gt;&gt;&gt; k, e, y = Button(&#x27;k&#x27;, f), Button(&#x27;e&#x27;, f), Button(&#x27;y&#x27;, f)\n &gt;&gt;&gt; s = e.press().press().press()\n eee\n &gt;&gt;&gt; caps = Button.caps\_lock\n &gt;&gt;&gt; t = [x.press() for x in [k, e, y, caps, e, e, k, caps, e, y, e, caps, y, e, e]]\n keyEEKeyeYEE\n &gt;&gt;&gt; u = Button(&#x27;a&#x27;, print).press().press().press()\n A\n A\n A\n &quot;&quot;&quot;\n caps\_lock = CapsLock()\n\n def \_\_init\_\_(self, letter, output):\n assert letter in LOWERCASE\_LETTERS\n self.letter = letter\n self.output = output\n self.pressed = 0\n\n def press(self):\n &quot;Call output on letter (maybe uppercased), then return the button that was pressed.&quot;\n self.pressed += 1\n "\*\*\* YOUR CODE HERE \*\*\*"\n\nclass Keyboard:\n &quot;&quot;&quot;A keyboard.\n\n &gt;&gt;&gt; Button.caps\_lock.pressed = 0 # Reset the caps\_lock key\n &gt;&gt;&gt; bored = Keyboard()\n &gt;&gt;&gt; bored.type(&#x27;hello&#x27;)\n &gt;&gt;&gt; bored.typed\n [&#x27;h&#x27;, &#x27;e&#x27;, &#x27;l&#x27;, &#x27;l&#x27;, &#x27;o&#x27;]\n &gt;&gt;&gt; bored.keys[&#x27;l&#x27;].pressed\n 2\n\n &gt;&gt;&gt; Button.caps\_lock.press()\n &gt;&gt;&gt; bored.type(&#x27;hello&#x27;)\n &gt;&gt;&gt; bored.typed\n [&#x27;h&#x27;, &#x27;e&#x27;, &#x27;l&#x27;, &#x27;l&#x27;, &#x27;o&#x27;, &#x27;H&#x27;, &#x27;E&#x27;, &#x27;L&#x27;, &#x27;L&#x27;, &#x27;O&#x27;]\n &gt;&gt;&gt; bored.keys[&#x27;l&#x27;].pressed\n 4\n &quot;&quot;&quot;\n def \_\_init\_\_(self):\n self.typed = []\n self.keys = ... # Try a dictionary comprehension!\n\n def type(self, word):\n &quot;Press the button for each letter in word.&quot;\n assert all([w in LOWERCASE\_LETTERS for w in word]), &#x27;word must be all lowercase&#x27;\n "\*\*\* YOUR CODE HERE \*\*\*"\n\n', "python", "keyboard-input"));

Please don't look at the hints until you've discussed as a group and agreed that
you need a hint.

 Button Hint: Uppercasing (enable JavaScript)

Since `self.letter` is always lowercase, use `self.letter.upper()` to produce the uppercase version.

 Button Hint: Caps Lock (enable JavaScript)

The number of times `caps_lock` has been pressed is either
`self.caps_lock.pressed` or `Button.caps_lock.pressed`.

 Button Hint: Output (enable JavaScript)

The `output` attribute is a function that can be called:
`self.output(self.letter)` or `self.output(self.letter.upper())`. You do not
need to return the result. Instead return `self` afterward in order to return
the button that was pressed.

 Keyboard Hint: Keys (enable JavaScript)

The keys can be created using a dictionary comprehension: `self.keys = {c: Button(c, ...) for c in LETTERS}`.
The call to `Button` should take `c` and **an output function that appends to `self.typed`**, so that every time
one of these buttons is pressed, it appends a letter to `self.typed`.

 Keyboard Hint: Type (enable JavaScript)

Call the `press` method of `self.key[w]` for each `w` in `word`. It should be
the case that when you call `press`, the `Button` is already set up (in the
`Keyboard.__init__` method) to output to the `typed` list of this `Keyboard`.

**Presentation Time**: Describe how new letters are added to
`typed` each time a `Button` in `keys` is pressed. Instead of just reading
your code, say what it does (e.g., "When the button of a keyboard is pressed ...").
One short sentence is enough to describe how new letters are added to `typed`.
When you're ready, send a message to the `#discuss-queue` channel with the
`@discuss` tag, your discussion group number, and the message "Put it on our
tab!" and a member of the course staff will join your voice channel to hear your
description and give feedback.

### Q3: Bear

Implement the `SleepyBear`, and `WinkingBear` classes so that calling their `print` method
matches the doctests. Use as little code as possible and try not to
repeat any logic from `Eye` or `Bear`. Each blank can be filled with just two
short lines.

**Discussion Time:** Before writing code, talk about what is different about a
`SleepyBear` and a `Bear`. When using inheritance, you only need to implement
the differences between the base class and subclass. Then, talk about what is
different about a `WinkingBear` and a `Bear`. Can you think of a way to make
the bear wink without a new implementation of `print`?

[Run in 61A Code](javascript:void "javascript:void")

 $(() => activateEditor('class Eye:\n &quot;&quot;&quot;An eye.\n\n &gt;&gt;&gt; Eye().draw()\n &#x27;•&#x27;\n &gt;&gt;&gt; print(Eye(False).draw(), Eye(True).draw())\n • &#x2d;\n &quot;&quot;&quot;\n def \_\_init\_\_(self, closed=False):\n self.closed = closed\n\n def draw(self):\n if self.closed:\n return &#x27;&#x2d;&#x27;\n else:\n return &#x27;•&#x27;\n\nclass Bear:\n &quot;&quot;&quot;A bear.\n\n &gt;&gt;&gt; Bear().print()\n ʕ •ᴥ•ʔ\n &quot;&quot;&quot;\n def \_\_init\_\_(self):\n self.nose\_and\_mouth = &#x27;ᴥ&#x27;\n\n def next\_eye(self):\n return Eye()\n\n def print(self):\n left, right = self.next\_eye(), self.next\_eye()\n print(&#x27;ʕ &#x27; + left.draw() + self.nose\_and\_mouth + right.draw() + &#x27;ʔ&#x27;)\n\nclass SleepyBear(Bear):\n &quot;&quot;&quot;A bear with closed eyes.\n\n &gt;&gt;&gt; SleepyBear().print()\n ʕ &#x2d;ᴥ&#x2d;ʔ\n &quot;&quot;&quot;\n "\*\*\* YOUR CODE HERE \*\*\*"\n\nclass WinkingBear(Bear):\n &quot;&quot;&quot;A bear whose left eye is different from its right eye.\n\n &gt;&gt;&gt; WinkingBear().print()\n ʕ &#x2d;ᴥ•ʔ\n &quot;&quot;&quot;\n def \_\_init\_\_(self):\n "\*\*\* YOUR CODE HERE \*\*\*"\n\n def next\_eye(self):\n "\*\*\* YOUR CODE HERE \*\*\*"\n\n', "python", "bear-input"));

 Hint: SleepyBear (enable JavaScript)

Implement a `next_eye` method that returns an Eye instance that is closed.

 Hint: WinkingBear (enable JavaScript)

One way to make the bear wink is to track how may times the `next_eye` method is
invoked using a new instance attribute and return a closed eye if `next_eye` has
been called an even number of times.

# Document the Occasion

Please all fill out the [attendance form](https://docs.google.com/forms/d/e/1FAIpQLSeqlK8l6WkScGr-RHR-kM4p5bnR9cllYrG95fDqPJspSlll7A/viewform "https://docs.google.com/forms/d/e/1FAIpQLSeqlK8l6WkScGr-RHR-kM4p5bnR9cllYrG95fDqPJspSlll7A/viewform") (one submission per person per week).

 $('.alwaystoggle').css('display', 'inline-block');
 $('.alwaystoggle').click(function() {
 var solution\_id = $(this).attr('id');
 $('div.' + solution\_id).slideToggle(600);
 });
