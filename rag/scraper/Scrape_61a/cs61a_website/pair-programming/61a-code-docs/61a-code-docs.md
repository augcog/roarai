

# 61A Code Documentation

[code.cs61a.org](https://code.cs61a.org "https://code.cs61a.org") is an online interpreter for all three
of the languages (Python 3.9, 61A Scheme, and the SQLite variant of SQL) taught
in this course. Using this interpreter, you can edit, run, debug, visualize, and
share programs with staff.

## Getting Started

The easiest way to get started with 61A Code is to visit
[code.cs61a.org](https://code.cs61a.org "https://code.cs61a.org") and play around with the interpreters.
Hit `Start Python Interpreter` on the launch screen, and start interacting with
`python`!

Note that the site may take a few seconds to load for the first time, since it's
downloading interpreters for Python, Scheme, and SQL to your browser. In most
modern browsers, these interpreters are cached, so subsequent loads should be a
lot faster! In addition, the interpreters will all run offline after they enter
your cache, so you can work even without an internet connection!

## Creating Files

Rather than running code straight in an interpreter, you may want to edit a
program in a file. To do so, you can

* Click `New` at the top menu bar
* Click `Create new file` on the launch screen
* Call the `editor` function in an interactive interpreter (`editor()` in
 Python, `(editor)` in Scheme, and `.editor` in SQL)

To run code in a file, hit the green `Run` icon at the top-right of the window.
An interactive interpreter will open showing the printed output of your code,
that will allow you to further interact with your program. You can use the red
`Stop` icon to the left of the interactive interpreter to stop a program that is
running for a long time.

To save a file, hit `Ctrl/Cmd + S` or click the `Save` / `Save As` options at
the top menu bar. You will be given the option to either download a copy of your
code as a file, or to save it locally in your browser. If you choose to save it
in your browser, you should give it a meaningful name. If you give two files the
same name, the older file will be silently overridden, so be careful!

Once you open an editor, you can write code in any of the three languages, and
the editor will automatically detect the language. If you want to override the
language detected, add a `lang` comment at the top of the file:

* `#lang python` will force the interpreter to use `python`
* `;lang scheme` will force the interpreter to use `scheme`
* `--lang sql` will force the interpreter to use `sql`

Alternatively, you can save a file with a `.py`, `.scm`, or `.sql` extension to
force it to run with the corresponding language.

## Loading Files

You may want to interact with programs written elsewhere using 61A Code. To do
so, there are a number of options:

* Click `Open` at the top menu bar, and upload a file to 61A code by dragging
 it into the drop target or selecting it manually.
* Click `Open existing file` on the launch screen, and upload a file using the
 previously described dialog.
* Select a file from `Recent Local Files` or `OKPy Backups`.
* Open a file from the course homepage.

When opening files, look in the `cs61a` directory to find your OKPy backups for
the current semester. You will be prompted to log in the first time you try to
perform an action that requires OKPy authentication. You can open, edit, run,
and save backups, and they will be synchronized on OKPy and with your partner.
However, you cannot run OKPy test cases.

Files in the `home` folder are stored in your local browser storage. Some
browsers may clear this storage periodically (Safari is known to do this), so
don't rely on it! Files stored in the `cs61a` folder are saved as an OKPy
backup, and so will be accessible even if you clear your browser data, but will
be inaccessible from 61A Code after the semester ends (though they will remain
on OKPy).

To open a file already saved in 61A Code, you can either use the `Open` dialog
described previously to open a previously saved file, or access a direct link to
the file (such as those on the course homepage). Note that publicly accessible
direct links can only be created by course staff.

## Formatting Code

To make your code more readable, click the blue `Format` icon at the top right
of the window. Especially for Scheme, this can make your code easier to read and
debug, and will also catch simple syntax errors.

## Visualizing Data Structures

To visualize data structures, call the `draw` function (`draw(...)` in Python,
or `(draw ...)` in Scheme) with a data structure passed in as its only argument.
Lists and linked lists will be drawn as box-and-pointer diagrams, while (both
types of) trees will be drawn in the standard manner. The `Link` and `Tree` data
structures, as well as the standard tree ADT functions, are already declared for
use in the Python interpreter.

You can also call the `autodraw` function to draw all data structures that are
returned in the interactive interpreter. Call `disable_autodraw` to stop this
behavior.

## Visualizing Programs

To visualize code written in an editor, click the yellow `Debug` icon at the top
right next to the `Run` icon.

* If you are writing Python, the visualizer will use Python Tutor to draw an
 environment diagram of your code.
* If you are writing Scheme, the visualizer will show the tree-recursive
 execution of your code, along with an environment diagram.
* If you are writing SQL, the visualizer will let you interact with the tables
 generated by your code, and step through the execution of most `SELECT`
 statements.

To visualize code run in an interactive interpreter, call the `visualize`
function (`visualize()` in Python or `(visualize)` in Scheme) to view a similar
visualization of all the code run in the interactive interpreter. In SQL, you
can click the `Step-By-Step` button in the console to view the step-by-step
execution of a particular `SELECT` statement.

Tables from lecture are preloaded in the SQL interpreter, so you don't have to
create them yourself. Run `.tables` or `.schema` to see all the currently
available tables, and run `.open --new` to drop all tables.

Be aware that, while most code is run on your local machine, the Python and
Scheme program visualizers run your code on the server, so there exist
restrictions that prevent you from visualizing very long-running programs.

## Sharing Code

Remember that sharing code related to 61A assignments with any student (even one
not taking CS 61A!) aside from your project partner is a violation of course
policies.

However, you may wish to share code with staff members to help with debugging.
To do so, click the `Share` button at the top menu bar to generate a unique URL
for your code, that can be accessed by members of staff but not students.
Members of staff should log in to share files with students. When a file is
shared from the Share menu, edits will be visible to all collaborators.

## Advanced

To mess with the internals of the interpreter, click `Console` at the top menu
bar. You will be able to interact with a minimal terminal-esque interface. Type
`help` to view the commands enabled. In particular, note that you can delete
files using `rm`.

To save files in a directory, write the full path in the `Save As` dialog,
rather just the file name.

## Troubleshooting / Reporting Bugs

If you experience a bug, try using a different browser. This tool is most
extensively tested in Google Chrome, but should work in most modern browsers.
You should also consider clearing your browser's cache and localStorage. If the
bug persists, make a post on Piazza or contact a member of staff.
