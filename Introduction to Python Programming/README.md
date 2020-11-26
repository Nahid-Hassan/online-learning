# Welcome To Introduction To Python

In this course, we use Python version 3 (or simply Python 3). If you'd like more details on previous versions of Python and how version 3 differs from previous versions, check out the History of Python on Wikipedia. If you're new to Python or programming in general, this article will make more sense after you've completed a lesson or two, so you may want to hold off for now. All you need to know now is that your solution code for the programming exercises in this course will be graded based on Python 3 code.

- [Welcome To Introduction To Python](#welcome-to-introduction-to-python)
  - [Why Python Programming](#why-python-programming)
    - [Programming In Python](#programming-in-python)
    - [Introduction to Programming](#introduction-to-programming)
  - [Data Types and Operators](#data-types-and-operators)
    - [Introduction](#introduction)
    - [Arithmetic Operators](#arithmetic-operators)
    - [Quiz: Arithmetic Operators](#quiz-arithmetic-operators)
    - [Variables and Assignment Operators](#variables-and-assignment-operators)
    - [Quiz: Variables and Assignment Operators](#quiz-variables-and-assignment-operators)
    - [Integers and Floats](#integers-and-floats)
    - [Quiz: Integer vs Float](#quiz-integer-vs-float)
    - [Booleans, Comparison Operators, and Logical Operators](#booleans-comparison-operators-and-logical-operators)
    - [Quiz: Which is denser, Rio or San Francisco?](#quiz-which-is-denser-rio-or-san-francisco)

## Why Python Programming

In this module we learn why you use Python Language.

### Programming In Python

As you learn Python throughout this course, there are a few things you should keep in mind.

- Python is case sensitive.
- Spacing is important.
- Use error messages to help you learn.

Let’s get started!

### Introduction to Programming

When we go about using technology every single day we don't realize that these programs are build by people who learned how to code and if they can learn so can anyone. I have no background at all in and I wanted to do it but I never believed that I could. But now I'm finishing up now I'm kind of seeing myself professionally in that environment you can work alongside who have tech skills or you can become an engineer yourself honestly the options are endless.  

## Data Types and Operators

### Introduction

**Data Types And Operators**:

Welcome to this lesson on Data Types and Operators! You'll learn about:

- `Data Types`: Integers, Floats, Booleans, Strings
- `Operators`: Arithmetic, Assignment, Comparison, Logical
- Built-In Functions, Type Conversion
- Whitespace and Style Guidelines

```py
print(3 + 5) # print() is a built-in function that displays input value as text in the output.
8
```

### Arithmetic Operators

Arithmetic Operators
Arithmetic operators

- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division
- `%` Mod (the remainder after dividing)
- `**` Exponentiation (note that ^ does not do this operation, as you might have seen in other languages)
- `//` Divides and rounds down to the nearest integer
The usual order of mathematical operations holds in Python, which you can review in this Math Forum page if needed.

[Bitwise operators][1] are special operators in Python that you can learn more about here if you'd like.

### Quiz: Arithmetic Operators

**Quiz: Average Electricity Bill**:

It's time to try a calculation in Python!

My electricity bills for the last three months have been `$23`, `$32` and `$64`. What is the average monthly electricity bill over the three month period? Write an expression to calculate the mean, and use `print()` to view the result.

**Solution**:

```py
# Write an expression that calculates the average of 23, 32 and 64
# Place the expression in this print statement
print((23 + 32 + 64) / 3)
```

**Quiz: Calculate**:

In this quiz you're going to do some calculations for a tiler. Two parts of a floor need tiling. One part is 9 tiles wide by 7 tiles long, the other is 5 tiles wide by 7 tiles long. Tiles come in packages of 6.

How many tiles are needed?
You buy 17 packages of tiles containing 6 tiles each. How many tiles will be left over?

```py
# Fill this in with an expression that calculates how many tiles are needed.
print((9 * 7) + (5 * 7))

# Fill this in with an expression that calculates how many tiles will be left over.
print((17 * 6) - ((9 * 7) + (5 * 7)))
```

### Variables and Assignment Operators

From this page, you will get your first look at variables in Python. There are three videos in this concept to show you some different cases you might run into!

**Variables I**:

Variables are used all the time in Python! Below is the example you saw in the video where we performed the following:

```py
mv_population = 74728
```

Here `mv_population` is a variable, which holds the value of `74728`. This assigns the item on the right to the name on the left, which is actually a little different than mathematical equality, as `74728` does not hold the value of `mv_population`.

In any case, whatever term is on the left side, is now a name for whatever value is on the right side. Once a value has been assigned to a variable name, you can access the value from the variable name.

```py
x = 2
y = x
print(y) # 2
```

**Variables II**:

In this video you saw that the following two are equivalent in terms of assignment:

```py
x = 3
y = 4
z = 5
```

and

```py
x, y, z = 3, 4, 5
```

However, the above isn't a great way to assign variables in most cases, because our variable names should be descriptive of the values they hold.

Besides writing variable names that are descriptive, there are a few things to watch out for when naming variables in Python.

`1.` Only use ordinary letters, numbers and underscores in your variable names. They can’t have spaces, and need to start with a letter or underscore.

`2.` **You can’t use reserved words or built-in identifiers** that have important purposes in Python, which you’ll learn about throughout this course. A list of python reserved words is described here. Creating names that are descriptive of the values often will help you avoid using any of these words. A quick table of these words is also available below.

`3.` The `pythonic way` to name variables is to use all lowercase letters and underscores to separate words.

`YES`

```py
my_height = 58
my_lat = 40
my_long = 105
```

`NO`

```py
my height = 58
MYLONG = 40
MyLat = 105
```

Though the last two of these would work in python, they are not pythonic ways to name variables. The way we name variables is called snake case, because we tend to connect the words with underscores.

```py
mv_population = 74728
mv_population += 4000 - 600 # instead of using mv_population twice we can do like this
print(mv_population) # 78128
```

**Assignment Operators**:

Below are the assignment operators from the video. You can also use *= in a similar way, but this is less common than the operations shown below. You can find some practice with much of what we have already covered [here][2].

### Quiz: Variables and Assignment Operators

**Quiz: Assign and Modify Variables**:

Now it's your turn to work with variables. The comments in this quiz (the lines that begin with #) have instructions for creating and modifying variables. After each comment write a line of code that implements the instruction.

Note that this code uses scientific notation to define large numbers. `4.445e8` is equal to `4.445 * 10 ** 8` which is equal to `444500000.0`.

```py
# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall *= .9

# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall

# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume *= 1.05

# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume *= 0.95

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.5e5

# print the new value of the reservoir_volume variable
print(reservoir_volume) # 447627500.0
```

**Quiz: Changing Variable Values**:

How does changing the value of a variable affect another variable that was defined in terms of it? Let's look at an example.

We're intentionally not providing a place to execute the code here, because we want to help you practice the important skill of walking through lines of code by hand.

Each line of code executes in order, one at a time, with control going from one line to the next.

```py
>>> carrots = 24
>>> rabbits = 8
>>> crs_per_rab = carrots/rabbits
```

Now we add a new 4th line to this code, that assigns a new value to the rabbits variable:

```py
>>> rabbits = 12
```

QUESTION 2 OF 3
If we now add this new 5th line of code to the above, what will the output be?

```py
>>> print(crs_per_rab) #3.0
```

### Integers and Floats

**Integers and Floats**:

There are two Python data types that could be used for numeric values:

`int` - for integer values
`float` - for decimal or floating point values

You can create a value that follows the data type by using the following syntax:

```py
x = int(4.7)   # x is now an integer 4
y = float(4)   # y is now a float of 4.0
```

You can check the type by using the type function:

```py
>>> print(type(x))
int
>>> print(type(y))
float
```

Because the `float`, or `approximation`, for `0.1` is actually `slightly more than 0.1`, when we add several of them together we can see the difference between the mathematically correct answer and the one that Python creates.

```py
>>> print(.1 + .1 + .1 == .3)
False
```

You can see more on this [here][3].

**Python Best Practices**:

For all the best practices, see the [PEP8 Guidelines][4].

You can use the atom package [linter-python-pep8][5] to use pep8 within your own programming environment in the Atom text editor, but more on this later. If you aren't familiar with text editors yet, and you are performing all of your programming in the classroom, no need to worry about this right now.

Follow these guidelines to make other programmers and future you happy!

`Good`

```py
print(4 + 5)
```

`Bad`

```py
print(                       4 + 5)
```

You should limit each line of code to `80` characters, though `99` is okay for certain use cases. [You can thank IBM for this ruling][6].

Why are these conventions important? Although how you format the code doesn’t affect how it runs, following standard style guidelines makes code easier to read and consistent among different developers on a team.

### Quiz: Integer vs Float

**`int` vs. `float`**:

In the fishy situation below, some of the quantities are of type `int` and some are of type `float`. Check all the ones that should be of type `float`.

- Length of fish you caught.
- Length of time it took to catch the fish, in hours.

**Divide By Zero?**:

What happens if you divide by zero in Python? Try it out! Test run this code and see what happens.

Here's what you should have seen when you submitted the Divide by Zero code above:

```log
Traceback (most recent call last):
  File "/tmp/vmuser_tnryxwdmhw/quiz.py", line 1, in <module>
    print(5/0)

ZeroDivisionError: division by zero
```

`Traceback` means `"What was the programming doing when it broke"`! This part is usually less helpful than the very last line of your error. Though you can dig through the rest of the error, looking at just the final line `ZeroDivisionError`, and the message says we `divided by zero`. Python is enforcing the rules of arithmetic!

In general, there are `two` types of errors to look out for

- Exceptions
- Syntax

An Exception is a problem that occurs when the code is running, but a 'Syntax Error' is a problem detected when Python checks the code before it runs it. For more information, see the Python tutorial page on [Errors and Exceptions][7].

### Booleans, Comparison Operators, and Logical Operators

The bool data type holds one of the values `True` or `False`, which are often encoded as `1` or `0`, respectively.

There are 6 comparison operators that are common to see in order to obtain a `bool` value:

**Comparison Operators**:

| Symbol Use Case | Bool  | Operation                |
| :-------------: | :---: | :----------------------- |
|      5 < 3      | False | Less Than                |
|      5 > 3      | True  | Greater Than             |
|     3 <= 3      | True  | Less Than or Equal To    |
|     3 >= 5      | False | Greater Than or Equal To |
|     3 == 5      | False | Equal To                 |
|     3 != 5      | True  | Not Equal To             |

And there are `three` logical operators you need to be familiar with:

| Logical Use        | Bool  | Operation                                                   |
| :----------------- | :---: | :---------------------------------------------------------- |
| 5 < 3 `and` 5 == 5 | False | `and` - Evaluates if all provided statements are True       |
| 5 < 3 `or` 5 == 5  | True  | `or` - Evaluates if at least one of many statements is True |
| `not` 5 < 3        | True  | `not` - Flips the Bool Value                                |

### Quiz: Which is denser, Rio or San Francisco?

Try comparison operators in this quiz! This code calculates the population densities of Rio de Janeiro and San Francisco.

Write code to compare these densities. Is the population of San Francisco more dense than that of Rio de Janeiro? Print `True` if it is and `False` if not.

```py
sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise
print(san_francisco_pop_density > rio_de_janeiro_pop_density)
```

`or`

```py
if(san_francisco_pop_density > rio_de_janeiro_pop_density):
    print(True)
else:
    print(False)
```

<!-- urls / paths -->
[1]: https://wiki.python.org/moin/BitwiseOperators
[2]: https://www.programiz.com/python-programming/operators
[3]: https://docs.python.org/3/tutorial/floatingpoint.html
[4]: https://www.python.org/dev/peps/pep-0008/
[5]: https://atom.io/packages/linter-python-pep8
[6]: https://softwareengineering.stackexchange.com/questions/148677/why-is-80-characters-the-standard-limit-for-code-width
[7]: https://docs.python.org/3/tutorial/errors.html
